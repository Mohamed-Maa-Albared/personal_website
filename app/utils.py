"""
Shared utilities — sanitisation, validation, safe type conversion, email, and locale helpers.

Centralises security helpers so routes.py and admin.py share a single
implementation, reducing duplication and the risk of divergent logic.
"""

import logging
import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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


# ---------------------------------------------------------------------------
# Email notification
# ---------------------------------------------------------------------------


def send_notification_email(name: str, email: str, subject: str, message: str) -> None:
    """Send an email notification when a contact form is submitted.

    Requires environment variables:
        MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, NOTIFICATION_EMAIL
    Silently returns if not configured.
    """
    mail_server = os.environ.get("MAIL_SERVER")
    mail_port = int(os.environ.get("MAIL_PORT", "587"))
    mail_username = os.environ.get("MAIL_USERNAME")
    mail_password = os.environ.get("MAIL_PASSWORD")
    notification_email = os.environ.get("NOTIFICATION_EMAIL")

    if not all([mail_server, mail_username, mail_password, notification_email]):
        logger.debug("Email notification skipped — MAIL_* env vars not configured")
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"[Portfolio Contact] {subject}"
    msg["From"] = mail_username
    msg["To"] = notification_email

    text_body = (
        f"New contact form submission:\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}"
    )

    html_body = f"""
    <div style="font-family: 'Inter', Arial, sans-serif; max-width: 600px; margin: 0 auto;
                background: #0a0e17; color: #e2e8f0; padding: 2rem; border-radius: 12px;">
        <h2 style="color: #7c5cfc; margin-top: 0;">New Contact Message</h2>
        <table style="width: 100%; border-collapse: collapse; margin-bottom: 1rem;">
            <tr>
                <td style="padding: .5rem; color: #94a3b8; font-size: .85rem; width: 80px;">From</td>
                <td style="padding: .5rem; color: #e2e8f0;"><strong>{name}</strong></td>
            </tr>
            <tr>
                <td style="padding: .5rem; color: #94a3b8; font-size: .85rem;">Email</td>
                <td style="padding: .5rem;"><a href="mailto:{email}" style="color: #00e5ff;">{email}</a></td>
            </tr>
            <tr>
                <td style="padding: .5rem; color: #94a3b8; font-size: .85rem;">Subject</td>
                <td style="padding: .5rem; color: #e2e8f0;">{subject}</td>
            </tr>
        </table>
        <div style="background: #111827; padding: 1rem; border-radius: 8px; border-left: 3px solid #7c5cfc;">
            <p style="margin: 0; line-height: 1.7; white-space: pre-wrap;">{message}</p>
        </div>
        <p style="color: #94a3b8; font-size: .75rem; margin-top: 1.5rem;">
            Sent from your portfolio contact form
        </p>
    </div>
    """

    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP(mail_server, mail_port, timeout=10) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(mail_username, mail_password)
            server.send_message(msg)
        logger.info("Email notification sent for contact from %s", email)
    except Exception:
        logger.exception("Failed to send email notification")
        raise


# ---------------------------------------------------------------------------
# Locale / Accept-Language parsing
# ---------------------------------------------------------------------------

# Common language code → readable name mapping
_LANG_NAMES = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "ca": "Catalan",
    "cs": "Czech",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "es": "Spanish",
    "et": "Estonian",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "ms": "Malay",
    "nb": "Norwegian",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sr": "Serbian",
    "sv": "Swedish",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "zh": "Chinese",
}

# Region code → country name mapping
_REGION_NAMES = {
    "AD": "Andorra",
    "AE": "UAE",
    "AF": "Afghanistan",
    "AG": "Antigua",
    "AL": "Albania",
    "AM": "Armenia",
    "AR": "Argentina",
    "AT": "Austria",
    "AU": "Australia",
    "AZ": "Azerbaijan",
    "BA": "Bosnia",
    "BD": "Bangladesh",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "BH": "Bahrain",
    "BR": "Brazil",
    "BY": "Belarus",
    "CA": "Canada",
    "CH": "Switzerland",
    "CL": "Chile",
    "CN": "China",
    "CO": "Colombia",
    "CR": "Costa Rica",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DK": "Denmark",
    "DO": "Dominican Rep.",
    "DZ": "Algeria",
    "EC": "Ecuador",
    "EE": "Estonia",
    "EG": "Egypt",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "GB": "UK",
    "GE": "Georgia",
    "GR": "Greece",
    "GT": "Guatemala",
    "HK": "Hong Kong",
    "HR": "Croatia",
    "HU": "Hungary",
    "ID": "Indonesia",
    "IE": "Ireland",
    "IL": "Israel",
    "IN": "India",
    "IQ": "Iraq",
    "IR": "Iran",
    "IS": "Iceland",
    "IT": "Italy",
    "JO": "Jordan",
    "JP": "Japan",
    "KE": "Kenya",
    "KR": "South Korea",
    "KW": "Kuwait",
    "KZ": "Kazakhstan",
    "LB": "Lebanon",
    "LK": "Sri Lanka",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "MA": "Morocco",
    "MX": "Mexico",
    "MY": "Malaysia",
    "NG": "Nigeria",
    "NL": "Netherlands",
    "NO": "Norway",
    "NZ": "New Zealand",
    "OM": "Oman",
    "PA": "Panama",
    "PE": "Peru",
    "PH": "Philippines",
    "PK": "Pakistan",
    "PL": "Poland",
    "PR": "Puerto Rico",
    "PT": "Portugal",
    "QA": "Qatar",
    "RO": "Romania",
    "RS": "Serbia",
    "RU": "Russia",
    "SA": "Saudi Arabia",
    "SE": "Sweden",
    "SG": "Singapore",
    "SI": "Slovenia",
    "SK": "Slovakia",
    "SY": "Syria",
    "TH": "Thailand",
    "TN": "Tunisia",
    "TR": "Turkey",
    "TW": "Taiwan",
    "UA": "Ukraine",
    "US": "USA",
    "UY": "Uruguay",
    "VE": "Venezuela",
    "VN": "Vietnam",
    "ZA": "South Africa",
}


def parse_locale(raw: str) -> str:
    """Convert a raw Accept-Language tag like 'en-US' into 'English (USA)'.

    Falls back to the raw string if no mapping is found.
    """
    if not raw:
        return "(unknown)"
    tag = raw.strip()
    parts = re.split(r"[-_]", tag, maxsplit=1)
    lang_code = parts[0].lower()
    region_code = parts[1].upper() if len(parts) > 1 else ""

    lang_name = _LANG_NAMES.get(lang_code, lang_code)
    if region_code:
        region_name = _REGION_NAMES.get(region_code, region_code)
        return f"{lang_name} ({region_name})"
    return lang_name


def parse_user_agent_short(ua: str) -> dict:
    """Extract browser and OS from a user-agent string (lightweight, no deps)."""
    if not ua:
        return {"browser": "Unknown", "os": "Unknown"}

    # Browser detection
    browser = "Other"
    if "Edg/" in ua or "Edge/" in ua:
        browser = "Edge"
    elif "OPR/" in ua or "Opera" in ua:
        browser = "Opera"
    elif "Chrome/" in ua and "Safari/" in ua:
        browser = "Chrome"
    elif "Firefox/" in ua:
        browser = "Firefox"
    elif "Safari/" in ua:
        browser = "Safari"
    elif "MSIE" in ua or "Trident/" in ua:
        browser = "IE"

    # OS detection (order matters: iPhone UA contains "Mac OS" — check mobile first)
    os_name = "Other"
    if "iPhone" in ua or "iPad" in ua:
        os_name = "iOS"
    elif "Android" in ua:
        os_name = "Android"
    elif "Windows" in ua:
        os_name = "Windows"
    elif "Macintosh" in ua or "Mac OS" in ua:
        os_name = "macOS"
    elif "Linux" in ua:
        os_name = "Linux"
    elif "CrOS" in ua:
        os_name = "ChromeOS"

    # Device type
    is_mobile = any(kw in ua for kw in ("Mobile", "Android", "iPhone", "iPad"))
    device = "Mobile" if is_mobile else "Desktop"

    return {"browser": browser, "os": os_name, "device": device}
