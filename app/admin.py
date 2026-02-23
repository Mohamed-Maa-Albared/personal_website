"""
Admin blueprint — password-protected dashboard for managing content.
Uses a simple session-based login (no user model needed).
"""

import hmac
import json
import logging
import os
import uuid
from datetime import datetime, timedelta, timezone
from functools import wraps

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.utils import secure_filename

from app import db, limiter
from app.models import (
    BlogPost,
    Experience,
    ImpactCard,
    LanguageItem,
    Message,
    PageVisit,
    Project,
    SiteConfig,
    SkillCluster,
)
from app.utils import (
    generate_slug,
    parse_locale,
    parse_user_agent_short,
    safe_int,
    sanitize_html,
    sanitize_input,
)

logger = logging.getLogger(__name__)

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme123")

# ── Login lockout state ──────────────────────────
# In-memory tracker — resets on process restart, which is acceptable for a
# single-admin personal site.  A persistent store (Redis / DB) would be
# needed for multi-process deployments.
_login_failures: dict[str, list] = {}  # ip → [timestamps of recent failures]
_LOGIN_LOCKOUT_THRESHOLD = 5  # failures before lockout
_LOGIN_LOCKOUT_WINDOW = 300  # 5 minutes — only count failures within this window
_LOGIN_LOCKOUT_DURATION = 600  # 10 minutes total lockout after too many failures


def _is_locked_out(ip: str) -> bool:
    """Return True if *ip* has exceeded the failure threshold within the window."""
    attempts = _login_failures.get(ip, [])
    now = datetime.now(timezone.utc).timestamp()
    # Prune stale entries
    recent = [t for t in attempts if now - t < _LOGIN_LOCKOUT_DURATION]
    _login_failures[ip] = recent
    return len(recent) >= _LOGIN_LOCKOUT_THRESHOLD


def _record_login_failure(ip: str) -> None:
    """Record a failed login attempt timestamp for *ip*."""
    _login_failures.setdefault(ip, []).append(datetime.now(timezone.utc).timestamp())


def _clear_login_failures(ip: str) -> None:
    """Clear failure history after a successful login."""
    _login_failures.pop(ip, None)


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
    """Admin login with rate limiting + exponential lockout."""
    client_ip = request.remote_addr or "unknown"
    if request.method == "POST":
        # Check lockout before even comparing password
        if _is_locked_out(client_ip):
            logger.warning("Login attempt during lockout from %s", client_ip)
            flash("Too many failed attempts. Please try again later.", "error")
            return render_template("admin/login.html"), 429

        submitted = request.form.get("password", "")
        if hmac.compare_digest(submitted, ADMIN_PASSWORD):
            session.permanent = True  # Honour PERMANENT_SESSION_LIFETIME
            session["admin_logged_in"] = True
            _clear_login_failures(client_ip)
            logger.info("Admin login successful from %s", client_ip)
            flash("Welcome back!", "success")
            return redirect(url_for("admin.dashboard"))

        _record_login_failure(client_ip)
        logger.warning("Failed admin login attempt from %s", client_ip)
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
    impact_cards = ImpactCard.query.order_by(ImpactCard.sort_order).all()
    skill_clusters = SkillCluster.query.order_by(SkillCluster.sort_order).all()
    language_items = LanguageItem.query.order_by(LanguageItem.sort_order).all()

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

    # Parse locale tags into readable names
    raw_countries = (
        db.session.query(PageVisit.country, func.count(PageVisit.id).label("count"))
        .filter(PageVisit.country.isnot(None), PageVisit.country != "")
        .group_by(PageVisit.country)
        .order_by(func.count(PageVisit.id).desc())
        .limit(20)
        .all()
    )
    top_countries = [(parse_locale(c.country), c.count) for c in raw_countries]

    recent_visits = (
        PageVisit.query.order_by(PageVisit.visited_at.desc()).limit(20).all()
    )

    # ── Enhanced Analytics ──

    # Visits per day (last 30 days)
    thirty_days_ago = datetime.now(timezone.utc) - timedelta(days=30)
    daily_visits_raw = (
        db.session.query(
            func.date(PageVisit.visited_at).label("day"),
            func.count(PageVisit.id).label("count"),
        )
        .filter(PageVisit.visited_at >= thirty_days_ago)
        .group_by(func.date(PageVisit.visited_at))
        .order_by(func.date(PageVisit.visited_at))
        .all()
    )
    # Build full 30-day series (fill gaps with 0)
    daily_labels = []
    daily_counts = []
    visits_by_day = {str(row.day): row.count for row in daily_visits_raw}
    for i in range(30):
        d = (datetime.now(timezone.utc) - timedelta(days=29 - i)).strftime("%Y-%m-%d")
        daily_labels.append(d)
        daily_counts.append(visits_by_day.get(d, 0))

    # Browser stats
    all_uas = (
        db.session.query(PageVisit.user_agent)
        .filter(PageVisit.user_agent.isnot(None), PageVisit.user_agent != "")
        .all()
    )
    browser_counts = {}
    os_counts = {}
    device_counts = {}
    for (ua_str,) in all_uas:
        parsed = parse_user_agent_short(ua_str)
        browser_counts[parsed["browser"]] = browser_counts.get(parsed["browser"], 0) + 1
        os_counts[parsed["os"]] = os_counts.get(parsed["os"], 0) + 1
        device_counts[parsed["device"]] = device_counts.get(parsed["device"], 0) + 1

    # Sort by count, take top 6
    top_browsers = sorted(browser_counts.items(), key=lambda x: -x[1])[:6]
    top_os = sorted(os_counts.items(), key=lambda x: -x[1])[:6]
    device_breakdown = sorted(device_counts.items(), key=lambda x: -x[1])

    # Avg pages per unique visitor
    avg_pages = round(total_visits / unique_visitors, 1) if unique_visitors else 0

    # Bounce rate (visitors who only viewed 1 page)
    visitor_page_counts = (
        db.session.query(PageVisit.ip_hash, func.count(PageVisit.id).label("pages"))
        .group_by(PageVisit.ip_hash)
        .all()
    )
    single_page_visitors = sum(1 for _, pages in visitor_page_counts if pages == 1)
    bounce_rate = (
        round(single_page_visitors / len(visitor_page_counts) * 100, 1)
        if visitor_page_counts
        else 0
    )

    return render_template(
        "admin/dashboard.html",
        projects=projects,
        experiences=experiences,
        messages=messages,
        unread=unread,
        blog_posts=blog_posts,
        site_configs=site_configs,
        impact_cards=impact_cards,
        skill_clusters=skill_clusters,
        language_items=language_items,
        total_visits=total_visits,
        today_visits=today_visits,
        unique_visitors=unique_visitors,
        top_pages=top_pages,
        top_referrers=top_referrers,
        top_countries=top_countries,
        recent_visits=recent_visits,
        daily_labels=json.dumps(daily_labels),
        daily_counts=json.dumps(daily_counts),
        top_browsers=top_browsers,
        top_os=top_os,
        device_breakdown=device_breakdown,
        avg_pages=avg_pages,
        bounce_rate=bounce_rate,
    )


# ── Site Config ──────────────────────────────────
@admin_bp.route("/site-config", methods=["POST"])
@login_required
def site_config_update():
    # Keys that contain rich HTML content — use sanitize_html to preserve formatting
    HTML_CONFIG_KEYS = {"about_bio1", "about_bio2", "about_bio3"}
    count = 0
    for key, value in request.form.items():
        if key.startswith("cfg_"):
            config_key = key[4:]  # strip 'cfg_' prefix
            if config_key in HTML_CONFIG_KEYS:
                SiteConfig.set(config_key, sanitize_html(value, 5000))
            else:
                SiteConfig.set(config_key, sanitize_input(value, 5000))
            count += 1
    db.session.commit()
    logger.info("Site config updated — %d fields", count)
    flash(f"Site configuration updated ({count} fields).", "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


# ── Data Retention ───────────────────────────────
@admin_bp.route("/purge-analytics", methods=["POST"])
@login_required
def purge_analytics():
    """Delete PageVisit records older than 90 days for GDPR-style data retention."""
    retention_days = safe_int(request.form.get("retention_days", 90), 90)
    cutoff = datetime.now(timezone.utc) - timedelta(days=retention_days)
    deleted = PageVisit.query.filter(PageVisit.visited_at < cutoff).delete()
    db.session.commit()
    logger.info(
        "Analytics purge: %d records older than %d days deleted",
        deleted,
        retention_days,
    )
    flash(
        f"Purged {deleted} analytics records older than {retention_days} days.",
        "success",
    )
    return redirect(url_for("admin.dashboard") + "#tab-analytics")


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
    logger.info("Project deleted: %s (id=%d)", title, project_id)
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
        logger.info("Experience updated: %s at %s", experience.role, experience.company)
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
    logger.info("Experience deleted: %s (id=%d)", role, exp_id)
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
    logger.info("Message deleted: id=%d", msg_id)
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
        logger.info("Blog post created: %s (slug=%s)", post.title, post.slug)
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
        logger.info("Blog post updated: %s (slug=%s)", post.title, post.slug)
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
    logger.info("Blog post deleted: %s (id=%d)", title, post_id)
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


# ── Impact Cards CRUD ────────────────────────────
@admin_bp.route("/impact-card/new", methods=["POST"])
@login_required
def impact_card_new():
    card = ImpactCard(
        icon=sanitize_input(request.form.get("icon", "&#9733;"), 50),
        value=sanitize_input(request.form.get("value", "0"), 50),
        prefix=sanitize_input(request.form.get("prefix", ""), 20),
        suffix=sanitize_input(request.form.get("suffix", ""), 20),
        description=sanitize_input(request.form.get("description", ""), 300),
        sort_order=safe_int(request.form.get("sort_order", 0)),
    )
    db.session.add(card)
    db.session.commit()
    logger.info("Impact card added: %s%s%s", card.prefix, card.value, card.suffix)
    flash("Impact card added!", "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


@admin_bp.route("/impact-card/<int:card_id>/edit", methods=["POST"])
@login_required
def impact_card_edit(card_id):
    card = ImpactCard.query.get_or_404(card_id)
    card.icon = sanitize_input(request.form.get("icon", "&#9733;"), 50)
    card.value = sanitize_input(request.form.get("value", "0"), 50)
    card.prefix = sanitize_input(request.form.get("prefix", ""), 20)
    card.suffix = sanitize_input(request.form.get("suffix", ""), 20)
    card.description = sanitize_input(request.form.get("description", ""), 300)
    card.sort_order = safe_int(request.form.get("sort_order", 0))
    db.session.commit()
    logger.info("Impact card updated: id=%d", card_id)
    flash("Impact card updated!", "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


@admin_bp.route("/impact-card/<int:card_id>/delete", methods=["POST"])
@login_required
def impact_card_delete(card_id):
    card = ImpactCard.query.get_or_404(card_id)
    db.session.delete(card)
    db.session.commit()
    logger.info("Impact card deleted: id=%d", card_id)
    flash("Impact card deleted.", "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


# ── Skill Clusters CRUD ─────────────────────────
@admin_bp.route("/skill-cluster/new", methods=["POST"])
@login_required
def skill_cluster_new():
    cluster = SkillCluster(
        icon=sanitize_input(request.form.get("icon", "&#9881;"), 50),
        title=sanitize_input(request.form.get("title", ""), 200),
        tags=sanitize_input(request.form.get("tags", ""), 2000),
        sort_order=safe_int(request.form.get("sort_order", 0)),
    )
    db.session.add(cluster)
    db.session.commit()
    logger.info("Skill cluster added: %s", cluster.title)
    flash(f'Skill cluster "{cluster.title}" added!', "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


@admin_bp.route("/skill-cluster/<int:cluster_id>/edit", methods=["POST"])
@login_required
def skill_cluster_edit(cluster_id):
    cluster = SkillCluster.query.get_or_404(cluster_id)
    cluster.icon = sanitize_input(request.form.get("icon", "&#9881;"), 50)
    cluster.title = sanitize_input(request.form.get("title", ""), 200)
    cluster.tags = sanitize_input(request.form.get("tags", ""), 2000)
    cluster.sort_order = safe_int(request.form.get("sort_order", 0))
    db.session.commit()
    logger.info("Skill cluster updated: %s (id=%d)", cluster.title, cluster_id)
    flash(f'Skill cluster "{cluster.title}" updated!', "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


@admin_bp.route("/skill-cluster/<int:cluster_id>/delete", methods=["POST"])
@login_required
def skill_cluster_delete(cluster_id):
    cluster = SkillCluster.query.get_or_404(cluster_id)
    db.session.delete(cluster)
    db.session.commit()
    logger.info("Skill cluster deleted: id=%d", cluster_id)
    flash("Skill cluster deleted.", "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


# ── Language Items CRUD ──────────────────────────
@admin_bp.route("/language/new", methods=["POST"])
@login_required
def language_new():
    lang = LanguageItem(
        name=sanitize_input(request.form.get("name", ""), 100),
        level=sanitize_input(request.form.get("level", ""), 50),
        sort_order=safe_int(request.form.get("sort_order", 0)),
    )
    db.session.add(lang)
    db.session.commit()
    logger.info("Language added: %s (%s)", lang.name, lang.level)
    flash(f'Language "{lang.name}" added!', "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


@admin_bp.route("/language/<int:lang_id>/edit", methods=["POST"])
@login_required
def language_edit(lang_id):
    lang = LanguageItem.query.get_or_404(lang_id)
    lang.name = sanitize_input(request.form.get("name", ""), 100)
    lang.level = sanitize_input(request.form.get("level", ""), 50)
    lang.sort_order = safe_int(request.form.get("sort_order", 0))
    db.session.commit()
    logger.info("Language updated: %s (id=%d)", lang.name, lang_id)
    flash(f'Language "{lang.name}" updated!', "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


@admin_bp.route("/language/<int:lang_id>/delete", methods=["POST"])
@login_required
def language_delete(lang_id):
    lang = LanguageItem.query.get_or_404(lang_id)
    db.session.delete(lang)
    db.session.commit()
    logger.info("Language deleted: id=%d", lang_id)
    flash("Language deleted.", "success")
    return redirect(url_for("admin.dashboard") + "#tab-site-config")


# ── Image Upload ─────────────────────────────────
# SVG intentionally excluded — it can contain arbitrary JavaScript / XSS.
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
ALLOWED_MIME_TYPES = {
    "image/png",
    "image/jpeg",
    "image/gif",
    "image/webp",
}
MAX_UPLOAD_BYTES = 5 * 1024 * 1024  # 5 MB (matches MAX_CONTENT_LENGTH)


def _allowed_file(filename: str) -> bool:
    """Check extension against allowlist."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def _validate_image_bytes(stream) -> bool:
    """Use Pillow to verify the file contains valid image data (magic-byte check).

    Returns True if valid, False otherwise. Resets stream position after check.
    """
    try:
        from PIL import Image

        img = Image.open(stream)
        img.verify()  # Checks headers / magic bytes without fully decoding
        return True
    except Exception:
        return False
    finally:
        stream.seek(0)


@admin_bp.route("/upload-image", methods=["POST"])
@login_required
@limiter.limit("10 per minute")
def upload_image():
    """Handle image upload with multi-layer validation, return JSON with the URL.

    Security layers:
    1. Extension allowlist (no SVG — XSS vector)
    2. MIME type check (Content-Type header)
    3. File-size guard
    4. Pillow magic-byte verification (prevents disguised executables)
    5. UUID filename (prevents path traversal / name collision)
    """
    if "image" not in request.files:
        return jsonify({"success": False, "message": "No file selected."}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"success": False, "message": "No file selected."}), 400

    # 1. Extension check
    if not _allowed_file(file.filename):
        return jsonify({"success": False, "message": "File type not allowed."}), 400

    # 2. MIME type check
    if file.content_type not in ALLOWED_MIME_TYPES:
        logger.warning(
            "Upload rejected — MIME mismatch: %s for %s",
            file.content_type,
            file.filename,
        )
        return jsonify({"success": False, "message": "File type not allowed."}), 400

    # 3. File-size guard (belt-and-braces alongside MAX_CONTENT_LENGTH)
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    if size > MAX_UPLOAD_BYTES:
        return jsonify({"success": False, "message": "File too large (max 5 MB)."}), 400
    if size == 0:
        return jsonify({"success": False, "message": "Empty file."}), 400

    # 4. Magic-byte validation via Pillow
    if not _validate_image_bytes(file.stream):
        logger.warning("Upload rejected — invalid image data: %s", file.filename)
        return jsonify({"success": False, "message": "File is not a valid image."}), 400

    upload_dir = current_app.config.get(
        "UPLOAD_FOLDER",
        os.path.join(current_app.static_folder, "uploads"),
    )
    os.makedirs(upload_dir, exist_ok=True)

    # 5. UUID filename — prevents path traversal and name collisions
    ext = file.filename.rsplit(".", 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex[:12]}.{ext}"
    safe_name = secure_filename(unique_name)
    file_path = os.path.join(upload_dir, safe_name)
    file.save(file_path)

    # Return relative URL
    image_url = url_for("static", filename=f"uploads/{safe_name}")
    logger.info("Image uploaded: %s (%d bytes, %s)", safe_name, size, file.content_type)
    return jsonify({"success": True, "url": image_url})
