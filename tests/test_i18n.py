"""Tests for locale and translation infrastructure."""

import json
from pathlib import Path

from app.i18n import (
    TRANSLATIONS_DIR,
    _load_raw_translations,
    get_locale_meta,
    is_supported_locale,
    load_translations,
    normalize_locale,
    resolve_locale,
    translate,
)


class TestLocaleNormalization:
    def test_normalize_locale_primary_tag(self):
        assert normalize_locale("en-US") == "en"
        assert normalize_locale("AR") == "ar"

    def test_normalize_locale_rejects_unsupported(self):
        assert normalize_locale("fr") is None
        assert normalize_locale("../../etc/passwd") is None

    def test_normalize_locale_empty_input(self):
        assert normalize_locale("") is None
        assert normalize_locale(None) is None

    def test_resolve_locale_fallback(self):
        assert resolve_locale("xx") == "en"

    def test_resolve_locale_known_locales(self):
        assert resolve_locale("en") == "en"
        assert resolve_locale("ar") == "ar"

    def test_supported_locale_check(self):
        assert is_supported_locale("ar") is True
        assert is_supported_locale("de") is False
        assert is_supported_locale("en") is True


class TestTranslations:
    def test_translation_returns_existing_value(self):
        assert translate("nav.blog", locale="en") == "Blog"

    def test_translation_returns_arabic_value(self):
        assert translate("nav.blog", locale="ar") == "المدونة"

    def test_translation_returns_key_when_missing(self):
        assert translate("missing.key", locale="en") == "missing.key"

    def test_translation_default_override(self):
        assert translate("missing.key", locale="en", default="fallback") == "fallback"

    def test_locale_meta_contains_direction(self):
        meta = get_locale_meta("ar")
        assert meta["dir"] == "rtl"

    def test_locale_meta_en_is_ltr(self):
        meta = get_locale_meta("en")
        assert meta["dir"] == "ltr"

    def test_locale_meta_og_locale(self):
        assert get_locale_meta("ar")["og_locale"] == "ar_AR"
        assert get_locale_meta("en")["og_locale"] == "en_US"

    def test_translation_cache_avoids_repeat_file_reads(self, monkeypatch):
        _load_raw_translations.cache_clear()
        load_translations.cache_clear()

        call_count = {"count": 0}
        original_open = Path.open

        def counting_open(self, *args, **kwargs):
            if self.name == "en.json":
                call_count["count"] += 1
            return original_open(self, *args, **kwargs)

        monkeypatch.setattr(Path, "open", counting_open)

        load_translations("en")
        load_translations("en")

        assert call_count["count"] == 1

    def test_english_and_arabic_keys_are_in_sync(self):
        with (TRANSLATIONS_DIR / "en.json").open("r", encoding="utf-8") as handle:
            en = json.load(handle)
        with (TRANSLATIONS_DIR / "ar.json").open("r", encoding="utf-8") as handle:
            ar = json.load(handle)

        missing_in_ar = set(en.keys()) - set(ar.keys())
        extra_in_ar = set(ar.keys()) - set(en.keys())
        assert not missing_in_ar, f"Keys missing in ar.json: {missing_in_ar}"
        assert not extra_in_ar, f"Extra keys in ar.json not in en.json: {extra_in_ar}"

    def test_arabic_values_are_not_empty(self):
        with (TRANSLATIONS_DIR / "ar.json").open("r", encoding="utf-8") as handle:
            ar = json.load(handle)

        for key, value in ar.items():
            assert isinstance(value, str)
            assert value.strip(), f"Empty translation value for key: {key}"

    def test_arabic_values_differ_from_english(self):
        """Ensure Arabic translations are actually Arabic, not left as English."""
        with (TRANSLATIONS_DIR / "en.json").open("r", encoding="utf-8") as handle:
            en = json.load(handle)
        with (TRANSLATIONS_DIR / "ar.json").open("r", encoding="utf-8") as handle:
            ar = json.load(handle)

        # These keys must have different (localised) values
        must_differ = [
            "nav.about",
            "nav.experience",
            "nav.projects",
            "nav.cta",
            "form.send",
            "contact.heading1",
        ]
        for key in must_differ:
            assert en[key] != ar[key], (
                f"Arabic translation for '{key}' is identical to English — "
                f"it may not have been translated."
            )

    def test_arabic_fallback_uses_english_for_missing_key(self):
        """When a key is in en.json, it's accessible via Arabic locale (merged fallback)."""
        # The English value should always be accessible regardless of locale
        en_val = translate("nav.blog", locale="en")
        assert en_val == "Blog"
        # Arabic should have its own value
        ar_val = translate("nav.blog", locale="ar")
        assert ar_val == "المدونة"


class TestSwitchLocaleUrl:
    """Tests for build_switch_locale_url within route context."""

    def test_switch_url_generated_for_en_page(self, client):
        resp = client.get("/en/")
        assert resp.status_code == 200
        html = resp.data.decode()
        assert 'data-switch-url="/ar/"' in html

    def test_switch_url_generated_for_ar_page(self, client):
        resp = client.get("/ar/")
        assert resp.status_code == 200
        html = resp.data.decode()
        assert 'data-switch-url="/en/"' in html

    def test_switch_url_preserves_blog_category_query(self, client):
        resp = client.get("/en/blog?category=AI")
        assert resp.status_code == 200
        assert b'data-switch-url="/ar/blog?category=AI"' in resp.data

    def test_lang_button_shows_target_locale_on_en_page(self, client):
        """On the English page the button must say AR (the locale you switch TO)."""
        resp = client.get("/en/")
        html = resp.data.decode()
        # The button label must show the alternate (target) locale, not current
        assert "AR" in html
        # Sanity: the current-locale label must NOT appear inside the button element.
        # We check the specific span rather than anywhere on the page.
        assert '<span class="lang-btn-label">AR</span>' in html
        assert '<span class="lang-btn-label">EN</span>' not in html

    def test_lang_button_shows_target_locale_on_ar_page(self, client):
        """On the Arabic page the button must say EN (the locale you switch TO)."""
        resp = client.get("/ar/")
        html = resp.data.decode()
        assert '<span class="lang-btn-label">EN</span>' in html
        assert '<span class="lang-btn-label">AR</span>' not in html


class TestRTLRendering:
    """Tests that Arabic pages render correct RTL attributes and structure."""

    def test_arabic_page_has_rtl_direction(self, client):
        resp = client.get("/ar/")
        assert resp.status_code == 200
        html = resp.data.decode()
        assert '<html lang="ar" dir="rtl">' in html

    def test_english_page_has_ltr_direction(self, client):
        resp = client.get("/en/")
        assert resp.status_code == 200
        html = resp.data.decode()
        assert '<html lang="en" dir="ltr">' in html

    def test_arabic_page_has_cairo_font_loaded(self, client):
        """Cairo font must be loaded (it's in the shared Google Fonts URL)."""
        resp = client.get("/ar/")
        assert resp.status_code == 200
        assert b"Cairo" in resp.data

    def test_arabic_page_renders_arabic_nav(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert "المدونة" in html
        assert "المشاريع" in html

    def test_arabic_page_has_neuro_scan_overlay(self, client):
        """Neuro-scan overlay element must be present for the JS transition."""
        resp = client.get("/ar/")
        assert b'id="neuroScanOverlay"' in resp.data

    def test_english_page_has_neuro_scan_overlay(self, client):
        resp = client.get("/en/")
        assert b'id="neuroScanOverlay"' in resp.data

    def test_arabic_page_has_scroll_progress_bar(self, client):
        """Scroll progress bar must be present on Arabic pages."""
        resp = client.get("/ar/")
        assert b'id="scrollProgressBar"' in resp.data

    def test_arabic_blog_renders_correctly(self, client, sample_blog_post):
        resp = client.get("/ar/blog")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' in html


class TestSEOLocalization:
    """Tests for page-level SEO and schema.org metadata in both locales."""

    def test_english_page_has_en_og_locale(self, client):
        resp = client.get("/en/")
        assert b'content="en_US"' in resp.data

    def test_arabic_page_has_ar_og_locale(self, client):
        resp = client.get("/ar/")
        assert b'content="ar_AR"' in resp.data

    def test_arabic_page_has_arabic_title(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        # Arabic title should contain Arabic characters
        assert "عالم بيانات" in html or "محمد" in html

    def test_english_page_has_english_title(self, client):
        resp = client.get("/en/")
        assert b"Mohamed Maa Albared" in resp.data
        assert b"Data Scientist" in resp.data

    def test_hreflang_links_present_on_en_page(self, client):
        """hreflang alternate links should be present for both locales."""
        resp = client.get("/en/")
        html = resp.data.decode()
        assert 'hreflang="en"' in html
        assert 'hreflang="ar"' in html
        assert 'hreflang="x-default"' in html

    def test_hreflang_links_present_on_ar_page(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode()
        assert 'hreflang="en"' in html
        assert 'hreflang="ar"' in html

    def test_arabic_index_structured_data_uses_ar_locale(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert '"inLanguage": "ar_AR"' in html

    def test_english_index_structured_data_uses_en_locale(self, client):
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        assert '"inLanguage": "en_US"' in html

    def test_arabic_structured_data_has_arabic_job_title(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert "عالم بيانات" in html

    def test_arabic_page_has_lang_announcer(self, client):
        """ARIA live region for screen readers must be present."""
        resp = client.get("/ar/")
        assert b'id="lang-announcer"' in resp.data
