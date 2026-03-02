import hashlib
import hmac as _hmac
import json
import logging

from flask import Flask, g, render_template
from flask import request as flask_request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from app.i18n import (
    DEFAULT_LOCALE,
    build_switch_locale_url,
    get_alternate_locale,
    get_locale_meta,
    get_supported_locale_codes,
    load_translations,
    resolve_locale,
    translate,
)
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

    @app.before_request
    def set_request_locale_defaults():
        raw_locale = (
            flask_request.view_args.get("locale") if flask_request.view_args else None
        )
        g.locale = resolve_locale(raw_locale)

    @app.context_processor
    def inject_i18n_context():
        locale = resolve_locale(getattr(g, "locale", DEFAULT_LOCALE))
        meta = get_locale_meta(locale)
        alternate_locale = get_alternate_locale(locale)
        return {
            "current_locale": locale,
            "locale_dir": meta["dir"],
            "locale_label": meta["label"],
            "og_locale": meta["og_locale"],
            "alternate_locale": alternate_locale,
            "alternate_locale_label": get_locale_meta(alternate_locale)["label"],
            "switch_locale_url": build_switch_locale_url(alternate_locale),
            "supported_locales": get_supported_locale_codes(),
        }

    app.jinja_env.globals["t"] = translate
    app.jinja_env.globals["load_locale_translations"] = load_translations

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
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self';"
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
        path = flask_request.path
        normalized_path = path
        segments = [segment for segment in path.split("/") if segment]
        if segments and segments[0] in get_supported_locale_codes():
            normalized_path = "/" + "/".join(segments[1:])
            if normalized_path == "/":
                normalized_path = "/"

        if (
            flask_request.method != "GET"
            or path.startswith(("/static", "/admin", "/api"))
            or normalized_path in ("/robots.txt", "/sitemap.xml", "/feed.xml")
        ):
            return
        try:
            from app.models import PageVisit

            ip_raw = flask_request.remote_addr or "unknown"
            # Salted HMAC — not rainbow-tableable unlike plain sha256
            secret = app.config["SECRET_KEY"].encode()
            ip_hash = _hmac.new(secret, ip_raw.encode(), hashlib.sha256).hexdigest()
            # Infer rough locale from Accept-Language header
            accept_lang = flask_request.headers.get("Accept-Language", "")
            country = (
                accept_lang.split(",")[0].split(";")[0].strip() if accept_lang else ""
            )
            visit = PageVisit(
                path=normalized_path[:500],
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
