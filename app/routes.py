import logging
from datetime import datetime, timezone

from flask import (
    Blueprint,
    Response,
    abort,
    g,
    jsonify,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)

from app import csrf, db, limiter
from app.i18n import (
    DEFAULT_LOCALE,
    get_supported_locale_codes,
    is_supported_locale,
    resolve_locale,
)
from app.models import (
    BlogPost,
    Experience,
    ImpactCard,
    LanguageItem,
    Message,
    Project,
    SiteConfig,
    SkillCluster,
)
from app.utils import sanitize_input, send_notification_email, validate_email

logger = logging.getLogger(__name__)

main_bp = Blueprint("main", __name__)


@main_bp.url_value_preprocessor
def pull_locale_from_url(endpoint, values):
    if not endpoint or not endpoint.startswith("main."):
        return

    locale = values.get("locale") if values else None
    if locale is None:
        g.locale = DEFAULT_LOCALE
        return

    if not is_supported_locale(locale):
        abort(404)

    normalized = resolve_locale(locale)
    values["locale"] = normalized
    g.locale = normalized


@main_bp.url_defaults
def add_locale_to_main_urls(endpoint, values):
    if not endpoint or not endpoint.startswith("main."):
        return
    if values is None:
        return
    if endpoint.endswith("_legacy"):
        return
    if endpoint in {
        "main.sitemap",
        "main.robots",
        "main.rss_feed",
    }:
        return
    if "locale" in values:
        return
    values["locale"] = resolve_locale(getattr(g, "locale", DEFAULT_LOCALE))


# ── Public pages ─────────────────────────────────────────────────────────────


@main_bp.route("/", endpoint="index_legacy")
def index_legacy():
    return redirect(url_for("main.index", locale=DEFAULT_LOCALE), code=301)


@main_bp.route("/<locale>/")
def index(locale):
    """Homepage — single-page layout with all portfolio sections.

    Loads featured projects, experiences, latest blog posts, editable
    site config values, impact cards, skill clusters, and languages.
    """
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

    # Dynamic sections
    impact_cards = ImpactCard.query.order_by(ImpactCard.sort_order).all()
    skill_clusters = SkillCluster.query.order_by(SkillCluster.sort_order).all()
    language_items = LanguageItem.query.order_by(LanguageItem.sort_order).all()

    return render_template(
        "index.html",
        featured_projects=projects,
        all_projects=all_projects,
        experiences=experiences,
        latest_posts=latest_posts,
        cfg=cfg,
        impact_cards=impact_cards,
        skill_clusters=skill_clusters,
        language_items=language_items,
    )


@main_bp.route("/project/<int:project_id>", endpoint="project_detail_legacy")
def project_detail_legacy(project_id):
    return redirect(
        url_for("main.project_detail", locale=DEFAULT_LOCALE, project_id=project_id),
        code=301,
    )


@main_bp.route("/<locale>/project/<int:project_id>")
def project_detail(locale, project_id):
    """Individual project detail page.

    Returns 404 if the project does not exist.
    """
    project = Project.query.get_or_404(project_id)
    return render_template("project_detail.html", project=project)


@main_bp.route("/case-study/<int:project_id>", endpoint="case_study_legacy")
def case_study_legacy(project_id):
    return redirect(
        url_for("main.case_study", locale=DEFAULT_LOCALE, project_id=project_id),
        code=301,
    )


@main_bp.route("/<locale>/case-study/<int:project_id>")
def case_study(locale, project_id):
    """Deep-dive case study page for a project.

    Returns 404 if the project doesn't exist or has no case study.
    """
    project = Project.query.get_or_404(project_id)
    if not project.has_case_study:
        abort(404)
    return render_template("case_study.html", project=project)


# --- Blog routes ---
# ── Blog ─────────────────────────────────────────────────────────────────────


@main_bp.route("/blog", endpoint="blog_legacy")
def blog_legacy():
    return redirect(url_for("main.blog", locale=DEFAULT_LOCALE), code=301)


@main_bp.route("/<locale>/blog")
def blog(locale):
    """Blog listing page with optional ``?category=`` filter."""
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


@main_bp.route("/blog/<slug>", endpoint="blog_detail_legacy")
def blog_detail_legacy(slug):
    return redirect(
        url_for("main.blog_detail", locale=DEFAULT_LOCALE, slug=slug),
        code=301,
    )


@main_bp.route("/<locale>/blog/<slug>")
def blog_detail(locale, slug):
    """Individual blog post page with related articles sidebar."""
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


# ── Contact ──────────────────────────────────────────────────────────────────


@main_bp.route("/contact", methods=["POST"])
@main_bp.route("/<locale>/contact", methods=["POST"])
@csrf.exempt  # AJAX JSON endpoint — uses honeypot + server validation instead
@limiter.limit("3 per minute")
def contact(locale=None):
    """Process a contact form submission (JSON only).

    Validates all fields, checks for honeypot spam, saves to DB,
    and sends an optional email notification.
    """
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

        # Send email notification (non-blocking: failure doesn't affect response)
        email_sent, _detail = send_notification_email(name, email, subject, msg_text)
        if not email_sent:
            logger.warning(
                "Email notification was not sent for message from %s: %s",
                email,
                _detail,
            )

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


# ── API ──────────────────────────────────────────────────────────────────────


@main_bp.route("/api/projects")
@main_bp.route("/<locale>/api/projects")
def api_projects(locale=None):
    """JSON API returning all projects ordered by sort_order.

    Use the ``?locale=ar`` query parameter (or the ``/<locale>/`` URL prefix)
    to receive Arabic-translated fields where available.  Untranslated fields
    fall back to English transparently.
    """
    # Prefer locale from URL segment; fall back to query-string; then default
    effective_locale = locale or request.args.get("locale", "en")
    projects = Project.query.order_by(Project.sort_order).all()
    return jsonify(
        [
            {
                "id": p.id,
                "title": p.get_field("title", effective_locale),
                "short_description": p.get_field("short_description", effective_locale),
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


# ── SEO ──────────────────────────────────────────────────────────────────────


@main_bp.route("/privacy", endpoint="privacy_legacy")
def privacy_legacy():
    return redirect(url_for("main.privacy", locale=DEFAULT_LOCALE), code=301)


@main_bp.route("/<locale>/privacy")
def privacy(locale):
    """Privacy policy page — describes data collection and retention."""
    now = datetime.now(timezone.utc).strftime("%B %Y")
    return render_template("privacy.html", now=now)


@main_bp.route("/sitemap.xml")
def sitemap():
    """Auto-generated XML sitemap covering all public pages."""
    pages = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Static pages
    for locale in get_supported_locale_codes():
        pages.append(
            {
                "loc": url_for("main.index", locale=locale, _external=True),
                "lastmod": now,
                "changefreq": "weekly",
                "priority": "1.0",
            }
        )
        pages.append(
            {
                "loc": url_for("main.blog", locale=locale, _external=True),
                "lastmod": now,
                "changefreq": "weekly",
                "priority": "0.8",
            }
        )
        pages.append(
            {
                "loc": url_for("main.privacy", locale=locale, _external=True),
                "lastmod": now,
                "changefreq": "yearly",
                "priority": "0.3",
            }
        )

    # Blog posts
    posts = BlogPost.query.filter_by(published=True).all()
    for locale in get_supported_locale_codes():
        for post in posts:
            pages.append(
                {
                    "loc": url_for(
                        "main.blog_detail",
                        locale=locale,
                        slug=post.slug,
                        _external=True,
                    ),
                    "lastmod": (
                        post.updated_at.strftime("%Y-%m-%d") if post.updated_at else now
                    ),
                    "changefreq": "monthly",
                    "priority": "0.7",
                }
            )

    # Projects
    projects = Project.query.all()
    for locale in get_supported_locale_codes():
        for project in projects:
            pages.append(
                {
                    "loc": url_for(
                        "main.project_detail",
                        locale=locale,
                        project_id=project.id,
                        _external=True,
                    ),
                    "lastmod": (
                        project.updated_at.strftime("%Y-%m-%d")
                        if project.updated_at
                        else now
                    ),
                    "changefreq": "monthly",
                    "priority": "0.6",
                }
            )

    # Case studies
    case_studies = Project.query.filter_by(has_case_study=True).all()
    for locale in get_supported_locale_codes():
        for cs in case_studies:
            pages.append(
                {
                    "loc": url_for(
                        "main.case_study",
                        locale=locale,
                        project_id=cs.id,
                        _external=True,
                    ),
                    "lastmod": (
                        cs.updated_at.strftime("%Y-%m-%d") if cs.updated_at else now
                    ),
                    "changefreq": "monthly",
                    "priority": "0.7",
                }
            )

    xml = render_template("sitemap.xml", pages=pages)
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml"
    return response


@main_bp.route("/robots.txt")
def robots():
    """Serve robots.txt — disallows /admin/ for crawlers."""
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        f"Sitemap: {url_for('main.sitemap', _external=True)}\n"
    )
    return Response(content, mimetype="text/plain")


@main_bp.route("/feed.xml")
def rss_feed():
    """RSS 2.0 feed of the latest 20 published blog posts."""
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
