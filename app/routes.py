import logging
from datetime import datetime, timezone

from flask import (
    Blueprint,
    Response,
    abort,
    jsonify,
    make_response,
    render_template,
    request,
    url_for,
)

from app import csrf, db, limiter
from app.models import BlogPost, Experience, Message, Project, SiteConfig
from app.utils import sanitize_input, validate_email

logger = logging.getLogger(__name__)

main_bp = Blueprint("main", __name__)


# --- Public routes ---
@main_bp.route("/")
def index():
    """Homepage — the main immersive experience"""
    projects = Project.query.filter_by(featured=True).order_by(Project.sort_order).all()
    experiences = Experience.query.order_by(Experience.sort_order).all()
    all_projects = Project.query.order_by(Project.sort_order).all()
    latest_posts = (
        BlogPost.query.filter_by(published=True)
        .order_by(BlogPost.created_at.desc())
        .limit(3)
        .all()
    )

    # Editable site content
    cfg = {}
    for sc in SiteConfig.query.all():
        cfg[sc.key] = sc.value

    return render_template(
        "index.html",
        featured_projects=projects,
        all_projects=all_projects,
        experiences=experiences,
        latest_posts=latest_posts,
        cfg=cfg,
    )


@main_bp.route("/project/<int:project_id>")
def project_detail(project_id):
    """Individual project detail page"""
    project = Project.query.get_or_404(project_id)
    return render_template("project_detail.html", project=project)


@main_bp.route("/case-study/<int:project_id>")
def case_study(project_id):
    """Deep-dive case study page for a project"""
    project = Project.query.get_or_404(project_id)
    if not project.has_case_study:
        abort(404)
    return render_template("case_study.html", project=project)


# --- Blog routes ---
@main_bp.route("/blog")
def blog():
    """Blog listing page"""
    category = request.args.get("category", "all")
    if category and category != "all":
        posts = (
            BlogPost.query.filter_by(published=True, category=category)
            .order_by(BlogPost.created_at.desc())
            .all()
        )
    else:
        posts = (
            BlogPost.query.filter_by(published=True)
            .order_by(BlogPost.created_at.desc())
            .all()
        )
    categories = (
        db.session.query(BlogPost.category)
        .filter(BlogPost.published == True)
        .distinct()
        .all()
    )
    categories = [c[0] for c in categories if c[0]]
    return render_template(
        "blog.html", posts=posts, categories=categories, active_category=category
    )


@main_bp.route("/blog/<slug>")
def blog_detail(slug):
    """Individual blog post page"""
    post = BlogPost.query.filter_by(slug=slug, published=True).first_or_404()
    # Get related posts (same category, excluding current)
    related = (
        BlogPost.query.filter(
            BlogPost.category == post.category,
            BlogPost.id != post.id,
            BlogPost.published == True,
        )
        .limit(2)
        .all()
    )
    return render_template("blog_detail.html", post=post, related=related)


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
        logger.info("Contact message received from %s <%s>", name, email)
        return (
            jsonify({"success": True, "message": "Message sent successfully!"}),
            200,
        )
    except Exception:
        db.session.rollback()
        logger.exception("Failed to save contact message")
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


# --- SEO routes ---
@main_bp.route("/sitemap.xml")
def sitemap():
    """Generate sitemap.xml"""
    pages = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Static pages
    pages.append(
        {
            "loc": url_for("main.index", _external=True),
            "lastmod": now,
            "priority": "1.0",
        }
    )
    pages.append(
        {"loc": url_for("main.blog", _external=True), "lastmod": now, "priority": "0.8"}
    )

    # Blog posts
    posts = BlogPost.query.filter_by(published=True).all()
    for post in posts:
        pages.append(
            {
                "loc": url_for("main.blog_detail", slug=post.slug, _external=True),
                "lastmod": (
                    post.updated_at.strftime("%Y-%m-%d") if post.updated_at else now
                ),
                "priority": "0.7",
            }
        )

    # Projects
    projects = Project.query.all()
    for project in projects:
        pages.append(
            {
                "loc": url_for(
                    "main.project_detail", project_id=project.id, _external=True
                ),
                "lastmod": (
                    project.updated_at.strftime("%Y-%m-%d")
                    if project.updated_at
                    else now
                ),
                "priority": "0.6",
            }
        )

    # Case studies
    case_studies = Project.query.filter_by(has_case_study=True).all()
    for cs in case_studies:
        pages.append(
            {
                "loc": url_for("main.case_study", project_id=cs.id, _external=True),
                "lastmod": cs.updated_at.strftime("%Y-%m-%d") if cs.updated_at else now,
                "priority": "0.7",
            }
        )

    xml = render_template("sitemap.xml", pages=pages)
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml"
    return response


@main_bp.route("/robots.txt")
def robots():
    """Serve robots.txt"""
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        f"Sitemap: {url_for('main.sitemap', _external=True)}\n"
    )
    return Response(content, mimetype="text/plain")


@main_bp.route("/feed.xml")
def rss_feed():
    """Generate RSS feed for blog posts"""
    posts = (
        BlogPost.query.filter_by(published=True)
        .order_by(BlogPost.created_at.desc())
        .limit(20)
        .all()
    )
    xml = render_template("feed.xml", posts=posts)
    response = make_response(xml)
    response.headers["Content-Type"] = "application/rss+xml"
    return response
