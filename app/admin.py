"""
Admin blueprint — password-protected dashboard for managing content.
Uses a simple session-based login (no user model needed).
"""

import hmac
import json
import os
from functools import wraps

import bleach
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
from app.models import Experience, Message, Project

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme123")


def _sanitize(text, max_len=500):
    """Strip HTML and limit length for admin inputs."""
    if not text:
        return ""
    return bleach.clean(str(text).strip(), tags=[], strip=True)[:max_len]


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
            session["admin_logged_in"] = True
            flash("Welcome back!", "success")
            return redirect(url_for("admin.dashboard"))
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
    projects = Project.query.order_by(Project.sort_order).all()
    experiences = Experience.query.order_by(Experience.sort_order).all()
    messages = Message.query.order_by(Message.created_at.desc()).all()
    unread = Message.query.filter_by(is_read=False).count()
    return render_template(
        "admin/dashboard.html",
        projects=projects,
        experiences=experiences,
        messages=messages,
        unread=unread,
    )


# ── Projects CRUD ────────────────────────────────
@admin_bp.route("/project/new", methods=["GET", "POST"])
@login_required
def project_new():
    if request.method == "POST":
        project = Project(
            title=_sanitize(request.form["title"], 200),
            short_description=_sanitize(request.form.get("short_description", ""), 300),
            description=_sanitize(request.form["description"], 5000),
            technologies=_sanitize(request.form.get("technologies", ""), 500),
            category=_sanitize(request.form.get("category", ""), 100),
            year=_sanitize(request.form.get("year", ""), 20),
            client=_sanitize(request.form.get("client", ""), 200),
            image_url=_sanitize(request.form.get("image_url", ""), 500),
            demo_url=_sanitize(request.form.get("demo_url", ""), 500),
            github_url=_sanitize(request.form.get("github_url", ""), 500),
            featured="featured" in request.form,
            sort_order=int(request.form.get("sort_order", 0)),
        )
        db.session.add(project)
        db.session.commit()
        flash(f'Project "{project.title}" created!', "success")
        return redirect(url_for("admin.dashboard"))
    return render_template("admin/project_form.html", project=None)


@admin_bp.route("/project/<int:project_id>/edit", methods=["GET", "POST"])
@login_required
def project_edit(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.title = _sanitize(request.form["title"], 200)
        project.short_description = _sanitize(
            request.form.get("short_description", ""), 300
        )
        project.description = _sanitize(request.form["description"], 5000)
        project.technologies = _sanitize(request.form.get("technologies", ""), 500)
        project.category = _sanitize(request.form.get("category", ""), 100)
        project.year = _sanitize(request.form.get("year", ""), 20)
        project.client = _sanitize(request.form.get("client", ""), 200)
        project.image_url = _sanitize(request.form.get("image_url", ""), 500)
        project.demo_url = _sanitize(request.form.get("demo_url", ""), 500)
        project.github_url = _sanitize(request.form.get("github_url", ""), 500)
        project.featured = "featured" in request.form
        project.sort_order = int(request.form.get("sort_order", 0))
        db.session.commit()
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
            [_sanitize(h, 500) for h in highlights_raw.split("\n") if h.strip()]
        )
        experience = Experience(
            role=_sanitize(request.form["role"], 200),
            company=_sanitize(request.form["company"], 200),
            location=_sanitize(request.form.get("location", ""), 200),
            date_range=_sanitize(request.form["date_range"], 100),
            description=_sanitize(request.form.get("description", ""), 2000),
            highlights=highlights,
            sort_order=int(request.form.get("sort_order", 0)),
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
            [_sanitize(h, 500) for h in highlights_raw.split("\n") if h.strip()]
        )
        experience.role = _sanitize(request.form["role"], 200)
        experience.company = _sanitize(request.form["company"], 200)
        experience.location = _sanitize(request.form.get("location", ""), 200)
        experience.date_range = _sanitize(request.form["date_range"], 100)
        experience.description = _sanitize(request.form.get("description", ""), 2000)
        experience.highlights = highlights
        experience.sort_order = int(request.form.get("sort_order", 0))
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
