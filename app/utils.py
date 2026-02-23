"""
Shared utilities — sanitisation, validation, safe type conversion, email, and locale helpers.

Centralises security helpers so routes.py and admin.py share a single
implementation, reducing duplication and the risk of divergent logic.
"""

import json
import logging
import os
import re
import smtplib
import ssl
import urllib.error
import urllib.request
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


def _send_via_resend(
    api_key: str, to_email: str, subject: str, html_body: str, text_body: str
) -> tuple[bool, str]:
    """Send email via Resend HTTP API (no SMTP, no extra packages).

    Uses only Python stdlib (urllib.request). Works on Render free tier
    where outbound SMTP ports are blocked.

    Docs: https://resend.com/docs/api-reference/emails/send-email
    """
    from_email = os.environ.get(
        "RESEND_FROM", "Portfolio <onboarding@resend.dev>"
    ).strip()

    payload = json.dumps(
        {
            "from": from_email,
            "to": [to_email],
            "subject": subject,
            "html": html_body,
            "text": text_body,
        }
    ).encode()

    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            logger.info("Email sent via Resend (id=%s)", data.get("id"))
            return True, "Email sent successfully via Resend"
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        try:
            err = json.loads(body)
            msg = err.get("message", body)
        except (json.JSONDecodeError, ValueError):
            msg = body

        # Provide actionable guidance for common Resend errors
        if "1010" in str(msg) or exc.code == 403:
            detail = (
                f"Resend API error {exc.code}: {msg}. "
                "With the free test sender (onboarding@resend.dev) you can only send "
                "to the SAME email you signed up for Resend with. Fix: set NOTIFICATION_EMAIL "
                "to your Resend signup email, OR verify your own domain at resend.com/domains "
                "and set RESEND_FROM to an address on that domain."
            )
        else:
            detail = f"Resend API error {exc.code}: {msg}"

        logger.error(detail)
        return False, detail
    except urllib.error.URLError as exc:
        detail = f"Could not reach Resend API: {exc.reason}"
        logger.error(detail)
        return False, detail
    except Exception as exc:
        detail = f"Resend error: {type(exc).__name__}: {exc}"
        logger.exception("Failed to send via Resend")
        return False, detail


def get_email_config_status() -> dict:
    """Return a dict describing which email env vars are set.

    Supports two providers:
    - **Resend** (HTTP API, recommended for Render free tier): needs RESEND_API_KEY + NOTIFICATION_EMAIL
    - **SMTP** (legacy): needs MAIL_SERVER, MAIL_USERNAME, MAIL_PASSWORD, NOTIFICATION_EMAIL
    """
    resend_key = bool(os.environ.get("RESEND_API_KEY", "").strip())
    notification = bool(os.environ.get("NOTIFICATION_EMAIL", "").strip())

    smtp_keys = ["MAIL_SERVER", "MAIL_PORT", "MAIL_USERNAME", "MAIL_PASSWORD"]
    smtp_status = {k: bool(os.environ.get(k)) for k in smtp_keys}

    resend_configured = resend_key and notification
    smtp_configured = (
        all(
            os.environ.get(k) for k in ["MAIL_SERVER", "MAIL_USERNAME", "MAIL_PASSWORD"]
        )
        and notification
    )

    return {
        "configured": resend_configured or smtp_configured,
        "provider": (
            "resend" if resend_configured else ("smtp" if smtp_configured else None)
        ),
        "RESEND_API_KEY": resend_key,
        "NOTIFICATION_EMAIL": notification,
        **smtp_status,
    }


def send_notification_email(
    name: str, email: str, subject: str, message: str
) -> tuple[bool, str]:
    """Send an email notification when a contact form is submitted.

    Tries providers in order:
    1. **Resend** (HTTP API) — if RESEND_API_KEY is set
    2. **SMTP** — if MAIL_SERVER / MAIL_USERNAME / MAIL_PASSWORD are set

    Returns (success: bool, detail: str) — detail contains a human-readable
    diagnostic message for admin display.
    """
    notification_email = os.environ.get("NOTIFICATION_EMAIL", "").strip()
    if not notification_email:
        return False, "Missing env var: NOTIFICATION_EMAIL"

    # ── Build email body ──────────────────────────────────────────────
    full_subject = f"[Portfolio Contact] {subject}"

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

    # ── Try Resend first (HTTP API — works on Render free tier) ───────
    resend_api_key = os.environ.get("RESEND_API_KEY", "").strip()
    if resend_api_key:
        return _send_via_resend(
            resend_api_key, notification_email, full_subject, html_body, text_body
        )

    # ── Fall back to SMTP ─────────────────────────────────────────────
    mail_server = os.environ.get("MAIL_SERVER", "").strip()
    mail_username = os.environ.get("MAIL_USERNAME", "").strip()
    mail_password = os.environ.get("MAIL_PASSWORD", "").strip()

    if not all([mail_server, mail_username, mail_password]):
        missing = [
            k
            for k in ["MAIL_SERVER", "MAIL_USERNAME", "MAIL_PASSWORD"]
            if not os.environ.get(k, "").strip()
        ]
        detail = f"No email provider configured. Set RESEND_API_KEY (recommended) or SMTP vars. Missing: {', '.join(missing)}"
        logger.warning("Email notification skipped — %s", detail)
        return False, detail

    # Safe port parsing
    try:
        mail_port = int(os.environ.get("MAIL_PORT", "587"))
    except (ValueError, TypeError):
        mail_port = 587

    msg = MIMEMultipart("alternative")
    msg["Subject"] = full_subject
    msg["From"] = mail_username
    msg["To"] = notification_email
    msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    try:
        if mail_port == 465:
            # Port 465 uses implicit SSL
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(
                mail_server, mail_port, timeout=15, context=context
            )
        else:
            # Port 587 (or other) uses STARTTLS
            server = smtplib.SMTP(mail_server, mail_port, timeout=15)
            server.ehlo()
            server.starttls(context=ssl.create_default_context())
            server.ehlo()

        with server:
            server.login(mail_username, mail_password)
            server.send_message(msg)

        logger.info("Email notification sent for contact from %s", email)
        return True, "Email sent successfully"

    except smtplib.SMTPAuthenticationError as exc:
        detail = (
            f"SMTP authentication failed (server said: {exc.smtp_code} {exc.smtp_error!r}). "
            f"For Gmail: 1) Enable 2-Step Verification at myaccount.google.com/security, "
            f"2) Generate an App Password at myaccount.google.com/apppasswords, "
            f"3) Use that 16-character App Password as MAIL_PASSWORD (not your Gmail login password)."
        )
        logger.error(detail)
        return False, detail
    except smtplib.SMTPRecipientsRefused as exc:
        detail = f"Recipient rejected: {notification_email} — check NOTIFICATION_EMAIL."
        logger.error(detail)
        return False, detail
    except (smtplib.SMTPConnectError, ConnectionRefusedError, OSError) as exc:
        detail = f"Could not connect to {mail_server}:{mail_port} — {type(exc).__name__}: {exc}"
        logger.error(detail)
        return False, detail
    except smtplib.SMTPException as exc:
        detail = f"SMTP error: {type(exc).__name__}: {exc}"
        logger.error(detail)
        return False, detail
    except Exception as exc:
        detail = f"Unexpected error: {type(exc).__name__}: {exc}"
        logger.exception("Failed to send email notification")
        return False, detail


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
