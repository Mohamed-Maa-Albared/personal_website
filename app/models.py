from datetime import datetime, timezone

from app import db


def _utcnow():
    """Timezone-aware UTC timestamp (replaces deprecated datetime.utcnow)."""
    return datetime.now(timezone.utc)


class Project(db.Model):
    """Model for portfolio projects"""

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(300))
    image_url = db.Column(db.String(500))
    demo_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    technologies = db.Column(db.String(500))  # Comma-separated
    category = db.Column(db.String(100))  # e.g. "NLP", "Computer Vision", "GenAI"
    year = db.Column(db.String(20))
    client = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, nullable=False, default=_utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=_utcnow, onupdate=_utcnow
    )
    featured = db.Column(db.Boolean, default=False)
    sort_order = db.Column(db.Integer, default=0)
    # Case study fields (optional — only populated for deep-dive projects)
    case_study = db.Column(db.Text)  # Full HTML/markdown case study content
    metrics = db.Column(db.Text)  # JSON: key metrics for the case study
    challenge = db.Column(db.Text)  # The problem / challenge
    approach = db.Column(db.Text)  # Technical approach
    results = db.Column(db.Text)  # Results & impact
    has_case_study = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Project {self.title}>"


class Experience(db.Model):
    """Model for work experience timeline"""

    __tablename__ = "experiences"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    date_range = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    highlights = db.Column(db.Text)  # JSON array of highlight strings
    sort_order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Experience {self.role} at {self.company}>"


class Message(db.Model):
    """Model for contact form messages"""

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


class BlogPost(db.Model):
    """Model for blog articles"""

    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    slug = db.Column(db.String(300), nullable=False, unique=True)
    excerpt = db.Column(db.String(500))  # Short preview text
    content = db.Column(db.Text, nullable=False)  # Full article HTML
    cover_image = db.Column(db.String(500))  # Cover image URL
    category = db.Column(db.String(100))  # e.g. "AI", "Neuroscience", "Art"
    tags = db.Column(db.String(500))  # Comma-separated tags
    read_time = db.Column(db.Integer, default=5)  # Minutes
    published = db.Column(db.Boolean, default=True)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=_utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=_utcnow, onupdate=_utcnow
    )
    sort_order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<BlogPost {self.title}>"


class SiteConfig(db.Model):
    """Key-value store for editable homepage content (about, impact, hero, etc.)."""

    __tablename__ = "site_config"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), nullable=False, unique=True, index=True)
    value = db.Column(db.Text, nullable=False, default="")
    label = db.Column(db.String(200))  # Human-readable label for admin UI
    group = db.Column(db.String(50))  # Grouping: "hero", "about", "impact", "skills"

    def __repr__(self):
        return f"<SiteConfig {self.key}>"

    @staticmethod
    def get(key, default=""):
        """Retrieve a config value by key."""
        row = SiteConfig.query.filter_by(key=key).first()
        return row.value if row else default

    @staticmethod
    def get_group(group):
        """Return all config rows in a group as a dict."""
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


class PageVisit(db.Model):
    """Lightweight page-view tracker for admin analytics."""

    __tablename__ = "page_visits"

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(500), nullable=False)
    referrer = db.Column(db.String(500))
    user_agent = db.Column(db.String(500))
    ip_hash = db.Column(db.String(64))  # SHA-256 hash — no raw IPs stored
    country = db.Column(db.String(100))  # From Accept-Language or future GeoIP
    visited_at = db.Column(db.DateTime, nullable=False, default=_utcnow, index=True)

    def __repr__(self):
        return f"<PageVisit {self.path} @ {self.visited_at}>"
