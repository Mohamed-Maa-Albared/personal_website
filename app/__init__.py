import hashlib
import json
import logging

from flask import Flask, render_template
from flask import request as flask_request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import config

db = SQLAlchemy()
csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per minute"])


def _configure_logging(app: Flask) -> None:
    """Set up structured logging with appropriate level per environment."""
    log_level = logging.DEBUG if app.debug else logging.INFO
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    app.logger.handlers.clear()
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)
    # Propagate to root so library loggers (app.utils, etc.) also emit
    logging.getLogger().handlers = [handler]
    logging.getLogger().setLevel(log_level)


def create_app(config_name="development"):
    """Application factory function"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    # Logging
    _configure_logging(app)

    # Custom Jinja filters
    @app.template_filter("from_json")
    def from_json_filter(value):
        try:
            return json.loads(value) if value else []
        except (json.JSONDecodeError, TypeError):
            return []

    # ── Security headers ─────────────────────────────────────────────
    @app.after_request
    def set_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-XSS-Protection"] = "0"  # Modern best-practice: rely on CSP
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=()"
        )
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' https://cdnjs.cloudflare.com https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data: https:; "
            "connect-src 'self'; "
            "frame-ancestors 'none';"
        )
        if not app.debug:
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains"
            )
        return response

    # ── Error handlers ───────────────────────────────────────────────
    @app.errorhandler(400)
    def bad_request(e):
        return render_template("errors/400.html"), 400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(429)
    def too_many_requests(e):
        return render_template("errors/429.html"), 429

    @app.errorhandler(500)
    def internal_error(e):
        app.logger.error("Internal server error: %s", e)
        db.session.rollback()
        return render_template("errors/500.html"), 500

    # ── Visitor tracking ────────────────────────────────────────────
    @app.before_request
    def track_page_visit():
        """Record page visits for analytics (public GET pages only)."""
        if (
            flask_request.method != "GET"
            or flask_request.path.startswith(("/static", "/admin", "/api"))
            or flask_request.path in ("/robots.txt", "/sitemap.xml", "/feed.xml")
        ):
            return
        try:
            from app.models import PageVisit

            ip_raw = flask_request.remote_addr or "unknown"
            ip_hash = hashlib.sha256(ip_raw.encode()).hexdigest()
            # Infer rough locale from Accept-Language header
            accept_lang = flask_request.headers.get("Accept-Language", "")
            country = (
                accept_lang.split(",")[0].split(";")[0].strip() if accept_lang else ""
            )
            visit = PageVisit(
                path=flask_request.path[:500],
                referrer=(flask_request.referrer or "")[:500],
                user_agent=(flask_request.user_agent.string or "")[:500],
                ip_hash=ip_hash,
                country=country,
            )
            db.session.add(visit)
            db.session.commit()
        except Exception:
            db.session.rollback()

    # Register blueprints
    from app.admin import admin_bp
    from app.routes import main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
    return app
    return app
    return app
