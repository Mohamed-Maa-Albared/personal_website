"""
Database models for the personal portfolio website.

Nine models covering portfolio content, blog, contact messages,
site configuration, and lightweight analytics.  All timestamps
use timezone-aware UTC via the ``_utcnow`` helper.

Multilingual content
--------------------
Arabic translations are stored as nullable ``_ar`` sibling columns on
content models (Project, Experience, BlogPost, ImpactCard, SkillCluster).
The ``LocalizedMixin.get_field()`` helper retrieves the correct value for
the requested locale, falling back transparently to English when the Arabic
field is empty or absent.

Usage in templates::

    {{ project.get_field('title', current_locale) }}
    {{ project.get_field('challenge', current_locale) | safe }}
    {{ exp.get_highlights(current_locale) | from_json }}
"""

from datetime import datetime, timezone

from app import db


def _utcnow():
    """Timezone-aware UTC timestamp (replaces deprecated datetime.utcnow)."""
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# Mixin — shared ``sort_order`` column used by most content models
# ---------------------------------------------------------------------------


class SortableMixin:
    """Mixin that adds a ``sort_order`` integer column defaulting to 0.

    Used by Project, Experience, BlogPost, ImpactCard, SkillCluster,
    and LanguageItem to allow manual ordering in the admin dashboard.
    """

    sort_order = db.Column(db.Integer, default=0)


# ---------------------------------------------------------------------------
# Mixin — per-locale field accessor used by all translatable models
# ---------------------------------------------------------------------------


class LocalizedMixin:
    """Mixin that provides locale-aware field retrieval with English fallback.

    Arabic translations are stored as nullable ``<field>_ar`` columns.
    Call ``get_field('title', locale)`` instead of accessing ``title``
    directly whenever displaying user-facing content.

    The fallback chain is:
        1. ``<field>_ar`` (when locale == 'ar' and the value is non-empty)
        2. ``<field>``    (English — always present)
    """

    def get_field(self, field: str, locale: str = "en") -> str:
        """Return the localized value of *field* or fall back to English.

        Parameters
        ----------
        field:
            The base field name, e.g. ``'title'``.
        locale:
            The current display locale (``'en'`` or ``'ar'``).

        Returns
        -------
        str
            The translated string, or the English value if no translation
            exists, or ``''`` if neither is set.
        """
        if locale != "en":
            ar_val = getattr(self, f"{field}_ar", None)
            if ar_val and ar_val.strip():
                return ar_val
        return getattr(self, field, "") or ""

    def get_highlights(self, locale: str = "en") -> str:
        """Return the JSON highlights string for the given locale.

        Falls back to English ``highlights`` when ``highlights_ar`` is empty.
        """
        if locale != "en":
            ar_val = getattr(self, "highlights_ar", None)
            if ar_val and ar_val.strip():
                return ar_val
        return getattr(self, "highlights", "") or "[]"


# ---------------------------------------------------------------------------
# Content models
# ---------------------------------------------------------------------------


class Project(LocalizedMixin, SortableMixin, db.Model):
    """Portfolio project with optional deep-dive case study.

    Fields:
        title           – Project display name (unique).
        title_ar        – Arabic translation of title (optional).
        description     – Full project description (plain text).
        description_ar  – Arabic translation of description (optional).
        short_description – Card-level summary (≤ 300 chars).
        short_description_ar – Arabic card-level summary (optional).
        image_url       – Cover image URL.
        demo_url        – Live demo link (optional).
        github_url      – Source repository link (optional).
        technologies    – Comma-separated tech stack tags.
        category        – Grouping label (e.g. "NLP", "GenAI").
        year            – Year / range string.
        client          – Client or internal team.
        featured        – Show on the homepage hero section.
        case_study      – Full HTML case study content (optional).
        case_study_ar   – Arabic case study content (optional).
        metrics         – JSON string of key metric pairs.
        challenge       – Problem statement (HTML).
        challenge_ar    – Arabic challenge HTML (optional).
        approach        – Technical approach (HTML).
        approach_ar     – Arabic approach HTML (optional).
        results         – Results & impact (HTML).
        results_ar      – Arabic results HTML (optional).
        has_case_study  – Whether `case_study` fields are populated.
    """

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    title_ar = db.Column(db.String(200))
    description = db.Column(db.Text, nullable=False)
    description_ar = db.Column(db.Text)
    short_description = db.Column(db.String(300))
    short_description_ar = db.Column(db.String(300))
    image_url = db.Column(db.String(500))
    demo_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    technologies = db.Column(db.String(500))
    category = db.Column(db.String(100))
    year = db.Column(db.String(20))
    client = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, nullable=False, default=_utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=_utcnow, onupdate=_utcnow
    )
    featured = db.Column(db.Boolean, default=False)
    # Case study fields
    case_study = db.Column(db.Text)
    case_study_ar = db.Column(db.Text)
    metrics = db.Column(db.Text)
    challenge = db.Column(db.Text)
    challenge_ar = db.Column(db.Text)
    approach = db.Column(db.Text)
    approach_ar = db.Column(db.Text)
    results = db.Column(db.Text)
    results_ar = db.Column(db.Text)
    has_case_study = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Project {self.title}>"


class Experience(LocalizedMixin, SortableMixin, db.Model):
    """Work experience entry for the timeline section.

    Fields:
        role         – Job title.
        role_ar      – Arabic job title (optional).
        company      – Employer name.
        location     – City / region.
        date_range   – Display string (e.g. "Jan 2023 – Present").
        description  – Paragraph describing the role.
        description_ar – Arabic description (optional).
        highlights   – JSON array of bullet-point strings.
        highlights_ar – JSON array of Arabic bullet-point strings (optional).
    """

    __tablename__ = "experiences"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(200), nullable=False)
    role_ar = db.Column(db.String(200))
    company = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    date_range = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    description_ar = db.Column(db.Text)
    highlights = db.Column(db.Text)
    highlights_ar = db.Column(db.Text)

    def __repr__(self):
        return f"<Experience {self.role} at {self.company}>"


class Message(db.Model):
    """Contact form submission.

    Fields:
        name       – Sender's name.
        email      – Sender's email address.
        subject    – Message subject line.
        message    – Full message body.
        is_read    – Admin has viewed the message.
        created_at – When the message was received.
    """

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=_utcnow)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Message from {self.name}>"


class BlogPost(LocalizedMixin, SortableMixin, db.Model):
    """Blog article with rich-text HTML content.

    Fields:
        title       – Article headline.
        title_ar    – Arabic headline (optional).
        slug        – URL-safe unique identifier.
        excerpt     – Short preview text (≤ 500 chars).
        excerpt_ar  – Arabic excerpt (optional).
        content     – Full article body (sanitised HTML).
        content_ar  – Arabic article body (sanitised HTML, optional).
        cover_image – Cover image URL or path.
        category    – Article category (e.g. "AI", "Neuroscience").
        tags        – Comma-separated tag strings.
        read_time   – Estimated read time in minutes.
        published   – Visible on the public blog.
        featured    – Highlighted on homepage / listings.
    """

    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    title_ar = db.Column(db.String(300))
    slug = db.Column(db.String(300), nullable=False, unique=True)
    excerpt = db.Column(db.String(500))
    excerpt_ar = db.Column(db.String(500))
    content = db.Column(db.Text, nullable=False)
    content_ar = db.Column(db.Text)
    cover_image = db.Column(db.String(500))
    category = db.Column(db.String(100))
    tags = db.Column(db.String(500))
    read_time = db.Column(db.Integer, default=5)
    published = db.Column(db.Boolean, default=True)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=_utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=_utcnow, onupdate=_utcnow
    )

    def __repr__(self):
        return f"<BlogPost {self.title}>"


# ---------------------------------------------------------------------------
# Site configuration & dynamic content
# ---------------------------------------------------------------------------


class SiteConfig(db.Model):
    """Key-value store for editable homepage content (hero, about, etc.).

    Use the static helpers ``get()``, ``set()``, ``get_group()`` instead
    of querying directly — they handle defaults and upsert logic.
    """

    __tablename__ = "site_config"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), nullable=False, unique=True, index=True)
    value = db.Column(db.Text, nullable=False, default="")
    label = db.Column(db.String(200))
    group = db.Column(db.String(50))

    def __repr__(self):
        return f"<SiteConfig {self.key}>"

    @staticmethod
    def get(key, default=""):
        """Retrieve a config value by key."""
        row = SiteConfig.query.filter_by(key=key).first()
        return row.value if row else default

    @staticmethod
    def get_group(group):
        """Return all config rows in a group as a ``{key: value}`` dict."""
        rows = SiteConfig.query.filter_by(group=group).all()
        return {r.key: r.value for r in rows}

    @staticmethod
    def set(key, value):
        """Upsert a config value."""
        row = SiteConfig.query.filter_by(key=key).first()
        if row:
            row.value = str(value)
        else:
            row = SiteConfig(key=key, value=str(value))
            db.session.add(row)


class ImpactCard(LocalizedMixin, SortableMixin, db.Model):
    """Dynamic impact / stat card shown on the homepage.

    Fields:
        icon           – HTML entity or emoji (e.g. ``&#9733;``).
        value          – Numeric display value (e.g. ``"15"``).
        prefix         – Text before the value (e.g. ``"0."`` for ``0.82``).
        suffix         – Text after the value (e.g. ``"%"`` or ``"x"``).
        description    – One-line description below the number.
        description_ar – Arabic description (optional).
    """

    __tablename__ = "impact_cards"

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=False, default="&#9733;")
    value = db.Column(db.String(50), nullable=False)
    prefix = db.Column(db.String(20), default="")
    suffix = db.Column(db.String(20), default="")
    description = db.Column(db.String(300), nullable=False)
    description_ar = db.Column(db.String(300))

    def __repr__(self):
        return f"<ImpactCard {self.prefix}{self.value}{self.suffix}>"


class SkillCluster(LocalizedMixin, SortableMixin, db.Model):
    """Skill category cluster for the capabilities section.

    Fields:
        icon     – HTML entity or emoji for the card header.
        title    – Cluster name (e.g. "Machine Learning").
        title_ar – Arabic cluster name (optional).
        tags     – Comma-separated individual skill names.
        tags_ar  – Arabic comma-separated skill names (optional).
    """

    __tablename__ = "skill_clusters"

    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(50), nullable=False, default="&#9881;")
    title = db.Column(db.String(200), nullable=False)
    title_ar = db.Column(db.String(200))
    tags = db.Column(db.Text, nullable=False)
    tags_ar = db.Column(db.Text)

    def __repr__(self):
        return f"<SkillCluster {self.title}>"


class LanguageItem(SortableMixin, db.Model):
    """Spoken language entry for the skills section.

    Fields:
        name  – Language name (e.g. "Arabic").
        level – Proficiency label (e.g. "Native", "C1-C2", "A2").
    """

    __tablename__ = "language_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<LanguageItem {self.name} ({self.level})>"


# ---------------------------------------------------------------------------
# Analytics
# ---------------------------------------------------------------------------


class PageVisit(db.Model):
    """Lightweight page-view tracker for the admin analytics dashboard.

    Privacy: IP addresses are never stored raw — only HMAC-hashed digests
    (salted with SECRET_KEY) are persisted in ``ip_hash``.

    Fields:
        path       – URL path of the visited page (truncated to 500 chars).
        referrer   – HTTP Referer header (truncated to 500 chars).
        user_agent – Full UA string (truncated to 500 chars).
        ip_hash    – HMAC-SHA256 digest of visitor IP (privacy-safe).
        country    – Rough locale inferred from Accept-Language header.
        visited_at – UTC timestamp (indexed for efficient range queries).
    """

    __tablename__ = "page_visits"

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(500), nullable=False)
    referrer = db.Column(db.String(500))
    user_agent = db.Column(db.String(500))
    ip_hash = db.Column(db.String(64))
    country = db.Column(db.String(100))
    visited_at = db.Column(db.DateTime, nullable=False, default=_utcnow, index=True)

    def __repr__(self):
        return f"<PageVisit {self.path} @ {self.visited_at}>"
