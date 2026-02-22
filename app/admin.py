"""
Admin blueprint — password-protected dashboard for managing content.
Uses a simple session-based login (no user model needed).
"""

import hmac
import json
import logging
import os
from datetime import datetime, timezone
from functools import wraps

from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app import db, limiter
from app.models import BlogPost, Experience, Message, PageVisit, Project, SiteConfig
from app.utils import generate_slug, safe_int, sanitize_html, sanitize_input

logger = logging.getLogger(__name__)

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme123")


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("admin.login"))
        return f(*args, **kwargs)

    return decorated


# ── Auth ─────────────────────────────────────────
@admin_bp.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def login():
    if request.method == "POST":
        submitted = request.form.get("password", "")
        if hmac.compare_digest(submitted, ADMIN_PASSWORD):
            session.permanent = True  # Honour PERMANENT_SESSION_LIFETIME
            session["admin_logged_in"] = True
            logger.info("Admin login successful from %s", request.remote_addr)
            flash("Welcome back!", "success")
            return redirect(url_for("admin.dashboard"))
        logger.warning("Failed admin login attempt from %s", request.remote_addr)
        flash("Invalid password.", "error")
    return render_template("admin/login.html")


@admin_bp.route("/logout")
@login_required
def logout():
    session.pop("admin_logged_in", None)
    flash("Logged out.", "success")
    return redirect(url_for("admin.login"))


# ── Dashboard ────────────────────────────────────
@admin_bp.route("/")
@login_required
def dashboard():
    from sqlalchemy import func

    projects = Project.query.order_by(Project.sort_order).all()
    experiences = Experience.query.order_by(Experience.sort_order).all()
    messages = Message.query.order_by(Message.created_at.desc()).all()
    unread = Message.query.filter_by(is_read=False).count()
    blog_posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    site_configs = SiteConfig.query.order_by(SiteConfig.group, SiteConfig.key).all()

    # ── Analytics ──
    total_visits = PageVisit.query.count()

    today_start = datetime.now(timezone.utc).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    today_visits = PageVisit.query.filter(PageVisit.visited_at >= today_start).count()

    unique_visitors = (
        db.session.query(func.count(func.distinct(PageVisit.ip_hash))).scalar() or 0
    )

    top_pages = (
        db.session.query(PageVisit.path, func.count(PageVisit.id).label("count"))
        .group_by(PageVisit.path)
        .order_by(func.count(PageVisit.id).desc())
        .limit(10)
        .all()
    )

    top_referrers = (
        db.session.query(PageVisit.referrer, func.count(PageVisit.id).label("count"))
        .filter(PageVisit.referrer.isnot(None), PageVisit.referrer != "")
        .group_by(PageVisit.referrer)
        .order_by(func.count(PageVisit.id).desc())
        .limit(10)
        .all()
    )

    top_countries = (
        db.session.query(PageVisit.country, func.count(PageVisit.id).label("count"))
        .filter(PageVisit.country.isnot(None), PageVisit.country != "")
        .group_by(PageVisit.country)
        .order_by(func.count(PageVisit.id).desc())
        .limit(10)
        .all()
    )

    recent_visits = (
        PageVisit.query.order_by(PageVisit.visited_at.desc()).limit(20).all()
    )

    return render_template(
        "admin/dashboard.html",
        projects=projects,
        experiences=experiences,
        messages=messages,
        unread=unread,
        blog_posts=blog_posts,
        site_configs=site_configs,
        total_visits=total_visits,
        today_visits=today_visits,
        unique_visitors=unique_visitors,
        top_pages=top_pages,
        top_referrers=top_referrers,
        top_countries=top_countries,
        recent_visits=recent_visits,
    )


# ── Site Config ──────────────────────────────────
@admin_bp.route("/site-config", methods=["POST"])
@login_required
def site_config_update():
    count = 0
    for key, value in request.form.items():
        if key.startswith("cfg_"):
            config_key = key[4:]  # strip 'cfg_' prefix
            SiteConfig.set(config_key, sanitize_input(value, 5000))
            count += 1
    db.session.commit()
    logger.info("Site config updated — %d fields", count)
    flash(f"Site configuration updated ({count} fields).", "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


# ── Projects CRUD ────────────────────────────────
@admin_bp.route("/project/new", methods=["GET", "POST"])
@login_required
def project_new():
    if request.method == "POST":
        project = Project(
            title=sanitize_input(request.form["title"], 200),
            short_description=sanitize_input(
                request.form.get("short_description", ""), 300
            ),
            description=sanitize_input(request.form["description"], 5000),
            technologies=sanitize_input(request.form.get("technologies", ""), 500),
            category=sanitize_input(request.form.get("category", ""), 100),
            year=sanitize_input(request.form.get("year", ""), 20),
            client=sanitize_input(request.form.get("client", ""), 200),
            image_url=sanitize_input(request.form.get("image_url", ""), 500),
            demo_url=sanitize_input(request.form.get("demo_url", ""), 500),
            github_url=sanitize_input(request.form.get("github_url", ""), 500),
            featured="featured" in request.form,
            sort_order=safe_int(request.form.get("sort_order", 0)),
        )
        db.session.add(project)
        db.session.commit()
        logger.info("Project created: %s", project.title)
        flash(f'Project "{project.title}" created!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/project_form.html", project=None)


@admin_bp.route("/project/<int:project_id>/edit", methods=["GET", "POST"])
@login_required
def project_edit(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.title = sanitize_input(request.form["title"], 200)
        project.short_description = sanitize_input(
            request.form.get("short_description", ""), 300
        )
        project.description = sanitize_input(request.form["description"], 5000)
        project.technologies = sanitize_input(request.form.get("technologies", ""), 500)
        project.category = sanitize_input(request.form.get("category", ""), 100)
        project.year = sanitize_input(request.form.get("year", ""), 20)
        project.client = sanitize_input(request.form.get("client", ""), 200)
        project.image_url = sanitize_input(request.form.get("image_url", ""), 500)
        project.demo_url = sanitize_input(request.form.get("demo_url", ""), 500)
        project.github_url = sanitize_input(request.form.get("github_url", ""), 500)
        project.featured = "featured" in request.form
        project.sort_order = safe_int(request.form.get("sort_order", 0))
        db.session.commit()
        logger.info("Project updated: %s", project.title)
        flash(f'Project "{project.title}" updated!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/project_form.html", project=project)


@admin_bp.route("/project/<int:project_id>/delete", methods=["POST"])
@login_required
def project_delete(project_id):
    project = Project.query.get_or_404(project_id)
    title = project.title
    db.session.delete(project)
    db.session.commit()
    flash(f'Project "{title}" deleted.', "success")
    return redirect(url_for("admin.dashboard"))


# ── Experience CRUD ──────────────────────────────
@admin_bp.route("/experience/new", methods=["GET", "POST"])
@login_required
def experience_new():
    if request.method == "POST":
        highlights_raw = request.form.get("highlights", "")
        highlights = json.dumps(
            [sanitize_input(h, 500) for h in highlights_raw.split("\n") if h.strip()]
        )
        experience = Experience(
            role=sanitize_input(request.form["role"], 200),
            company=sanitize_input(request.form["company"], 200),
            location=sanitize_input(request.form.get("location", ""), 200),
            date_range=sanitize_input(request.form["date_range"], 100),
            description=sanitize_input(request.form.get("description", ""), 2000),
            highlights=highlights,
            sort_order=safe_int(request.form.get("sort_order", 0)),
        )
        db.session.add(experience)
        db.session.commit()
        flash(f'Experience "{experience.role}" created!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/experience_form.html", experience=None)


@admin_bp.route("/experience/<int:exp_id>/edit", methods=["GET", "POST"])
@login_required
def experience_edit(exp_id):
    experience = Experience.query.get_or_404(exp_id)
    if request.method == "POST":
        highlights_raw = request.form.get("highlights", "")
        highlights = json.dumps(
            [sanitize_input(h, 500) for h in highlights_raw.split("\n") if h.strip()]
        )
        experience.role = sanitize_input(request.form["role"], 200)
        experience.company = sanitize_input(request.form["company"], 200)
        experience.location = sanitize_input(request.form.get("location", ""), 200)
        experience.date_range = sanitize_input(request.form["date_range"], 100)
        experience.description = sanitize_input(
            request.form.get("description", ""), 2000
        )
        experience.highlights = highlights
        experience.sort_order = safe_int(request.form.get("sort_order", 0))
        db.session.commit()
        flash(f'Experience "{experience.role}" updated!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/experience_form.html", experience=experience)


@admin_bp.route("/experience/<int:exp_id>/delete", methods=["POST"])
@login_required
def experience_delete(exp_id):
    experience = Experience.query.get_or_404(exp_id)
    role = experience.role
    db.session.delete(experience)
    db.session.commit()
    flash(f'Experience "{role}" deleted.', "success")
    return redirect(url_for("admin.dashboard"))


# ── Messages ─────────────────────────────────────
@admin_bp.route("/message/<int:msg_id>")
@login_required
def message_detail(msg_id):
    message = Message.query.get_or_404(msg_id)
    if not message.is_read:
        message.is_read = True
        db.session.commit()
    return render_template("admin/message_detail.html", message=message)


@admin_bp.route("/message/<int:msg_id>/delete", methods=["POST"])
@login_required
def message_delete(msg_id):
    message = Message.query.get_or_404(msg_id)
    db.session.delete(message)
    db.session.commit()
    flash("Message deleted.", "success")
    return redirect(url_for("admin.dashboard"))


# ── Blog CRUD ────────────────────────────────────
@admin_bp.route("/blog/new", methods=["GET", "POST"])
@login_required
def blog_new():
    if request.method == "POST":
        title = sanitize_input(request.form["title"], 300)
        slug = request.form.get("slug", "").strip()
        if not slug:
            slug = generate_slug(title)
        post = BlogPost(
            title=title,
            slug=sanitize_input(slug, 300),
            excerpt=sanitize_input(request.form.get("excerpt", ""), 500),
            content=sanitize_html(request.form.get("content", "")),
            cover_image=sanitize_input(request.form.get("cover_image", ""), 500),
            category=sanitize_input(request.form.get("category", ""), 100),
            tags=sanitize_input(request.form.get("tags", ""), 500),
            read_time=safe_int(request.form.get("read_time", 5), 5),
            published="published" in request.form,
            featured="featured" in request.form,
            sort_order=safe_int(request.form.get("sort_order", 0)),
        )
        db.session.add(post)
        db.session.commit()
        flash(f'Blog post "{post.title}" created!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/blog_form.html", post=None)


@admin_bp.route("/blog/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def blog_edit(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if request.method == "POST":
        post.title = sanitize_input(request.form["title"], 300)
        slug = request.form.get("slug", "").strip()
        if not slug:
            slug = generate_slug(post.title)
        post.slug = sanitize_input(slug, 300)
        post.excerpt = sanitize_input(request.form.get("excerpt", ""), 500)
        post.content = sanitize_html(request.form.get("content", ""))
        post.cover_image = sanitize_input(request.form.get("cover_image", ""), 500)
        post.category = sanitize_input(request.form.get("category", ""), 100)
        post.tags = sanitize_input(request.form.get("tags", ""), 500)
        post.read_time = safe_int(request.form.get("read_time", 5), 5)
        post.published = "published" in request.form
        post.featured = "featured" in request.form
        post.sort_order = safe_int(request.form.get("sort_order", 0))
        db.session.commit()
        flash(f'Blog post "{post.title}" updated!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/blog_form.html", post=post)


@admin_bp.route("/blog/<int:post_id>/delete", methods=["POST"])
@login_required
def blog_delete(post_id):
    post = BlogPost.query.get_or_404(post_id)
    title = post.title
    db.session.delete(post)
    db.session.commit()
    flash(f'Blog post "{title}" deleted.', "success")
    return redirect(url_for("admin.dashboard"))


# ── Case Study (edit on project) ─────────────────
@admin_bp.route("/project/<int:project_id>/case-study", methods=["GET", "POST"])
@login_required
def case_study_edit(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.challenge = sanitize_html(request.form.get("challenge", ""))
        project.approach = sanitize_html(request.form.get("approach", ""))
        project.results = sanitize_html(request.form.get("results", ""))
        project.metrics = sanitize_input(request.form.get("metrics", ""), 5000)
        project.case_study = sanitize_html(request.form.get("case_study", ""))
        project.has_case_study = "has_case_study" in request.form
        db.session.commit()
        flash(f'Case study for "{project.title}" updated!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/case_study_form.html", project=project)
