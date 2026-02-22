"""
Shared utilities — sanitisation, validation, and safe type conversion.

Centralises security helpers so routes.py and admin.py share a single
implementation, reducing duplication and the risk of divergent logic.
"""

import logging
import re

import bleach

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Allowed HTML tags/attributes for rich-text fields (blog content, case study)
# Deliberately restrictive — only structural/semantic markup, no scripts.
# ---------------------------------------------------------------------------
ALLOWED_TAGS = [
    "p",
    "br",
    "strong",
    "em",
    "b",
    "i",
    "u",
    "s",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "ul",
    "ol",
    "li",
    "a",
    "img",
    "blockquote",
    "pre",
    "code",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
    "hr",
    "span",
    "div",
    "figure",
    "figcaption",
    "sup",
    "sub",
    "mark",
]

ALLOWED_ATTRIBUTES = {
    "a": ["href", "title", "target", "rel"],
    "img": ["src", "alt", "title", "width", "height", "loading"],
    "td": ["colspan", "rowspan"],
    "th": ["colspan", "rowspan"],
    "span": ["class"],
    "div": ["class"],
    "code": ["class"],
    "pre": ["class"],
}

ALLOWED_PROTOCOLS = ["http", "https", "mailto"]


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------


def sanitize_input(text: str, max_length: int = 500) -> str:
    """Strip ALL HTML tags and limit length — for plain-text fields."""
    if not text:
        return ""
    text = bleach.clean(str(text).strip(), tags=[], strip=True)
    return text[:max_length]


def sanitize_html(text: str, max_length: int = 50_000) -> str:
    """Clean HTML to an allowed subset — for rich-text fields (blog, case study).

    Removes dangerous elements (script, iframe, style, event handlers)
    while preserving safe structural markup.
    """
    if not text:
        return ""
    cleaned = bleach.clean(
        str(text).strip(),
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=ALLOWED_PROTOCOLS,
        strip=True,
    )
    return cleaned[:max_length]


def validate_email(email: str) -> bool:
    """Basic email format validation."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def safe_int(value, default: int = 0) -> int:
    """Convert *value* to int, returning *default* on failure.

    Prevents ``ValueError`` / ``TypeError`` crashes when form fields
    contain non-numeric input.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        logger.warning(
            "safe_int: could not convert %r, using default %s", value, default
        )
        return default


def generate_slug(title: str) -> str:
    """Derive a URL-safe slug from a title string."""
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
