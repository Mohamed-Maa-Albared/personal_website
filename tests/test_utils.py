"""
Tests for utility functions.
"""

from app.utils import (
    generate_slug,
    parse_locale,
    parse_user_agent_short,
    safe_int,
    sanitize_html,
    sanitize_input,
    validate_email,
)


class TestSanitizeInput:
    """Tests for the plain-text sanitizer."""

    def test_strips_html(self):
        assert sanitize_input("<b>bold</b>") == "bold"

    def test_truncates(self):
        result = sanitize_input("a" * 100, max_length=10)
        assert len(result) == 10

    def test_empty_input(self):
        assert sanitize_input("") == ""
        assert sanitize_input(None) == ""

    def test_strips_script_tags(self):
        assert "<script>" not in sanitize_input("<script>alert(1)</script>")


class TestSanitizeHtml:
    """Tests for the rich-text HTML sanitizer."""

    def test_allows_safe_tags(self):
        result = sanitize_html("<p><strong>Hello</strong></p>")
        assert "<p>" in result
        assert "<strong>" in result

    def test_strips_script(self):
        result = sanitize_html("<script>alert('xss')</script><p>Safe</p>")
        assert "<script>" not in result
        assert "<p>Safe</p>" in result

    def test_strips_event_handlers(self):
        result = sanitize_html('<img src="x" onerror="alert(1)">')
        assert "onerror" not in result

    def test_strips_javascript_protocol(self):
        result = sanitize_html('<a href="javascript:alert(1)">Click</a>')
        assert "javascript:" not in result

    def test_allows_safe_links(self):
        result = sanitize_html('<a href="https://example.com">Link</a>')
        assert 'href="https://example.com"' in result

    def test_strips_iframe(self):
        result = sanitize_html('<iframe src="https://evil.com"></iframe>')
        assert "<iframe" not in result

    def test_strips_style_tag(self):
        result = sanitize_html("<style>body{display:none}</style><p>Ok</p>")
        assert "<style>" not in result

    def test_max_length(self):
        long_html = "<p>" + "x" * 100_000 + "</p>"
        result = sanitize_html(long_html, max_length=100)
        assert len(result) <= 100


class TestValidateEmail:
    """Tests for email validation."""

    def test_valid_emails(self):
        assert validate_email("user@example.com") is True
        assert validate_email("first.last@company.co.uk") is True

    def test_invalid_emails(self):
        assert validate_email("not-an-email") is False
        assert validate_email("@missing.com") is False
        assert validate_email("no-domain@") is False
        assert validate_email("") is False


class TestSafeInt:
    """Tests for safe_int conversion."""

    def test_valid_int(self):
        assert safe_int("42") == 42
        assert safe_int(0) == 0

    def test_invalid_returns_default(self):
        assert safe_int("abc") == 0
        assert safe_int("abc", 5) == 5
        assert safe_int(None) == 0

    def test_float_string(self):
        assert safe_int("3.14") == 0  # Not a valid int string


class TestGenerateSlug:
    """Tests for slug generation."""

    def test_basic_slug(self):
        assert generate_slug("Hello World") == "hello-world"

    def test_special_chars(self):
        assert generate_slug("AI & ML: A Guide!") == "ai-ml-a-guide"

    def test_empty(self):
        assert generate_slug("") == ""


class TestParseLocale:
    """Tests for Accept-Language tag parsing."""

    def test_english_us(self):
        assert parse_locale("en-US") == "English (USA)"

    def test_german(self):
        assert parse_locale("de") == "German"

    def test_empty(self):
        assert parse_locale("") == "(unknown)"

    def test_unknown_code(self):
        result = parse_locale("xx-YY")
        assert result  # Should not crash


class TestParseUserAgent:
    """Tests for user-agent string parsing."""

    def test_chrome(self):
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
        result = parse_user_agent_short(ua)
        assert result["browser"] == "Chrome"
        assert result["os"] == "Windows"
        assert result["device"] == "Desktop"

    def test_mobile_safari(self):
        ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) Safari/604.1"
        result = parse_user_agent_short(ua)
        assert result["browser"] == "Safari"
        assert result["os"] == "iOS"
        assert result["device"] == "Mobile"

    def test_empty(self):
        result = parse_user_agent_short("")
        assert result["browser"] == "Unknown"
        assert result["os"] == "Unknown"
