import json
import re

import bleach
from flask import Blueprint, abort, jsonify, render_template, request

from app import csrf, db, limiter
from app.models import Experience, Message, Project

main_bp = Blueprint("main", __name__)


# --- Security helpers ---
def sanitize_input(text, max_length=500):
    """Sanitize user input to prevent XSS and injection attacks"""
    if not text:
        return ""
    text = bleach.clean(str(text).strip(), tags=[], strip=True)
    return text[:max_length]


def validate_email(email):
    """Basic email validation"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


# --- Public routes ---
@main_bp.route("/")
def index():
    """Homepage — the main immersive experience"""
    projects = Project.query.filter_by(featured=True).order_by(Project.sort_order).all()
    experiences = Experience.query.order_by(Experience.sort_order).all()
    all_projects = Project.query.order_by(Project.sort_order).all()
    return render_template(
        "index.html",
        featured_projects=projects,
        all_projects=all_projects,
        experiences=experiences,
    )


@main_bp.route("/project/<int:project_id>")
def project_detail(project_id):
    """Individual project detail page"""
    project = Project.query.get_or_404(project_id)
    return render_template("project_detail.html", project=project)


@main_bp.route("/contact", methods=["POST"])
@csrf.exempt  # AJAX JSON endpoint — uses honeypot + server validation instead
@limiter.limit("3 per minute")
def contact():
    """Contact form submission (AJAX only)"""
    if not request.is_json:
        abort(400)

    data = request.get_json()
    name = sanitize_input(data.get("name"), 100)
    email = sanitize_input(data.get("email"), 120)
    subject = sanitize_input(data.get("subject"), 200)
    msg_text = sanitize_input(data.get("message"), 2000)

    # Validation
    if not all([name, email, subject, msg_text]):
        return jsonify({"success": False, "message": "All fields are required."}), 400

    if not validate_email(email):
        return jsonify({"success": False, "message": "Invalid email address."}), 400

    if len(msg_text) < 10:
        return (
            jsonify({"success": False, "message": "Message is too short."}),
            400,
        )

    # Honeypot check
    if data.get("website"):
        return jsonify({"success": True, "message": "Message sent successfully!"}), 200

    try:
        message = Message(name=name, email=email, subject=subject, message=msg_text)
        db.session.add(message)
        db.session.commit()
        return (
            jsonify({"success": True, "message": "Message sent successfully!"}),
            200,
        )
    except Exception:
        db.session.rollback()
        return (
            jsonify({"success": False, "message": "Server error. Please try again."}),
            500,
        )


@main_bp.route("/api/projects")
def api_projects():
    """API endpoint for projects data"""
    projects = Project.query.order_by(Project.sort_order).all()
    return jsonify(
        [
            {
                "id": p.id,
                "title": p.title,
                "short_description": p.short_description,
                "category": p.category,
                "technologies": (
                    [t.strip() for t in p.technologies.split(",")]
                    if p.technologies
                    else []
                ),
                "year": p.year,
                "featured": p.featured,
            }
            for p in projects
        ]
    )
