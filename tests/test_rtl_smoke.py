"""
Automated RTL smoke tests for Arabic critical paths.

These tests verify that all major public pages correctly set the HTML
``lang`` and ``dir`` attributes, expose the right locale metadata, surface
Arabic DB-backed content, and that English variants never carry RTL markup.

They run against the existing Flask test client — no real browser required.
Coverage intentionally mirrors the manual RTL_VISUAL_SMOKE_CHECKLIST.md so
the checklist can be kept in sync with what is already automatically verified.
"""

import pytest

from app.models import BlogPost, Experience, ImpactCard, Project, SkillCluster

# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture()
def ar_project(app, db):
    """Published project with Arabic translations (and a case study)."""
    with app.app_context():
        p = Project(
            title="English Project Title",
            description="English description.",
            short_description="Short EN",
            title_ar="عنوان المشروع بالعربية",
            description_ar="وصف المشروع بالعربية.",
            short_description_ar="وصف قصير",
            technologies="Python, AI",
            category="GenAI",
            year="2024",
            featured=True,
            has_case_study=True,
            challenge="Challenge EN",
            challenge_ar="التحدي بالعربية",
            approach="Approach EN",
            approach_ar="المنهج بالعربية",
            results="Results EN",
            results_ar="النتائج بالعربية",
            case_study="<p>Case study content EN</p>",
            case_study_ar="<p>محتوى دراسة الحالة بالعربية</p>",
            sort_order=1,
        )
        db.session.add(p)
        db.session.commit()
        db.session.refresh(p)
        return p


@pytest.fixture()
def ar_blog_post(app, db):
    """Published blog post with Arabic title and excerpt."""
    with app.app_context():
        post = BlogPost(
            title="English Title",
            slug="rtl-smoke-test-post",
            excerpt="English excerpt.",
            content="<p>English body content that is long enough.</p>",
            title_ar="عنوان المقال بالعربية",
            excerpt_ar="ملخص بالعربية.",
            content_ar="<p>محتوى المقال بالعربية وهو طويل بما يكفي.</p>",
            category="AI",
            tags="rtl, test",
            read_time=2,
            published=True,
        )
        db.session.add(post)
        db.session.commit()
        db.session.refresh(post)
        return post


# ── HTML lang / dir attributes ─────────────────────────────────────────────


class TestArabicHtmlAttributes:
    """All Arabic pages must set lang=ar and dir=rtl on the <html> element."""

    def test_ar_index_has_lang_and_dir(self, client):
        resp = client.get("/ar/")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' in html

    def test_ar_blog_listing_has_lang_and_dir(self, client):
        resp = client.get("/ar/blog")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' in html

    def test_ar_blog_detail_has_lang_and_dir(self, client, ar_blog_post):
        resp = client.get("/ar/blog/rtl-smoke-test-post")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' in html

    def test_ar_project_detail_has_lang_and_dir(self, client, ar_project):
        resp = client.get(f"/ar/project/{ar_project.id}")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' in html

    def test_ar_case_study_has_lang_and_dir(self, client, ar_project):
        resp = client.get(f"/ar/case-study/{ar_project.id}")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' in html

    def test_ar_privacy_has_lang_and_dir(self, client):
        resp = client.get("/ar/privacy")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' in html


class TestEnglishHtmlAttributes:
    """English pages must NOT carry RTL direction markup."""

    def test_en_index_has_lang_en(self, client):
        resp = client.get("/en/")
        assert resp.status_code == 200
        html = resp.data.decode("utf-8")
        assert 'lang="en"' in html

    def test_en_index_no_dir_rtl(self, client):
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        # The <html> element must not carry dir="rtl"
        assert '<html lang="en" dir="rtl">' not in html
        assert '<html lang="ar"' not in html

    def test_en_blog_listing_no_rtl(self, client):
        resp = client.get("/en/blog")
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' not in html

    def test_en_blog_detail_no_rtl(self, client, ar_blog_post):
        resp = client.get("/en/blog/rtl-smoke-test-post")
        html = resp.data.decode("utf-8")
        assert '<html lang="ar" dir="rtl">' not in html


# ── Body locale attribute ──────────────────────────────────────────────────


class TestBodyLocaleAttribute:
    """<body data-current-locale="..."> drives JS locale logic."""

    def test_ar_body_locale_attribute(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert 'data-current-locale="ar"' in html

    def test_en_body_locale_attribute(self, client):
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        assert 'data-current-locale="en"' in html


# ── Arabic navigation ──────────────────────────────────────────────────────


class TestArabicNavigation:
    """Key navigation labels must appear in Arabic on /ar/* pages."""

    ARABIC_NAV_TERMS = [
        "المدونة",  # Blog
        "المشاريع",  # Projects
        "تواصل",  # Contact (contains label in about or nav)
    ]

    def test_ar_index_has_arabic_nav_blog(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert "المدونة" in html

    def test_ar_index_has_arabic_nav_projects(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert "المشاريع" in html

    def test_ar_blog_listing_has_arabic_nav(self, client):
        resp = client.get("/ar/blog")
        html = resp.data.decode("utf-8")
        assert "المدونة" in html


# ── Arabic DB-backed content ───────────────────────────────────────────────


class TestArabicContent:
    """DB-backed content must surface in Arabic on localized pages."""

    def test_ar_index_renders_arabic_project_title(self, client, ar_project):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert "عنوان المشروع بالعربية" in html

    def test_en_index_renders_english_project_title(self, client, ar_project):
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        assert "English Project Title" in html
        assert "عنوان المشروع بالعربية" not in html

    def test_ar_blog_detail_renders_arabic_title(self, client, ar_blog_post):
        resp = client.get("/ar/blog/rtl-smoke-test-post")
        html = resp.data.decode("utf-8")
        assert "عنوان المقال بالعربية" in html

    def test_en_blog_detail_renders_english_title(self, client, ar_blog_post):
        resp = client.get("/en/blog/rtl-smoke-test-post")
        html = resp.data.decode("utf-8")
        assert "English Title" in html
        assert "عنوان المقال بالعربية" not in html

    def test_ar_project_detail_renders_arabic_title(self, client, ar_project):
        resp = client.get(f"/ar/project/{ar_project.id}")
        html = resp.data.decode("utf-8")
        assert "عنوان المشروع بالعربية" in html

    def test_ar_case_study_renders_arabic_challenge(self, client, ar_project):
        resp = client.get(f"/ar/case-study/{ar_project.id}")
        html = resp.data.decode("utf-8")
        assert "التحدي بالعربية" in html

    def test_ar_blog_listing_renders_arabic_excerpt(self, client, ar_blog_post):
        resp = client.get("/ar/blog")
        html = resp.data.decode("utf-8")
        assert "ملخص بالعربية" in html


# ── Language switch / hreflang ─────────────────────────────────────────────


class TestHreflangAndLanguageSwitch:
    """Hreflang alternates and language switch widget must be present."""

    def test_ar_index_contains_hreflang_en(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert 'hreflang="en"' in html

    def test_en_index_contains_hreflang_ar(self, client):
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        assert 'hreflang="ar"' in html

    def test_ar_index_contains_switch_url(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert 'data-switch-url="/en/"' in html

    def test_en_index_contains_switch_url(self, client):
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        assert 'data-switch-url="/ar/"' in html


# ── RSS feeds (locale-specific) ────────────────────────────────────────────


class TestRSSFeeds:
    """Both English and Arabic RSS feeds must be available and correct."""

    def test_english_rss_feed_is_accessible(self, client):
        resp = client.get("/feed.xml")
        assert resp.status_code == 200
        assert b"<rss" in resp.data

    def test_arabic_rss_feed_is_accessible(self, client):
        resp = client.get("/ar/feed.xml")
        assert resp.status_code == 200
        assert b"<rss" in resp.data

    def test_english_rss_language_tag(self, client):
        resp = client.get("/feed.xml")
        assert b"<language>en-us</language>" in resp.data

    def test_arabic_rss_language_tag(self, client):
        resp = client.get("/ar/feed.xml")
        assert "<language>ar</language>".encode() in resp.data

    def test_arabic_rss_channel_title_is_arabic(self, client):
        resp = client.get("/ar/feed.xml")
        html = resp.data.decode("utf-8")
        assert "إرسالات عصبية" in html

    def test_arabic_rss_renders_arabic_post_title(self, client, ar_blog_post):
        resp = client.get("/ar/feed.xml")
        html = resp.data.decode("utf-8")
        assert "عنوان المقال بالعربية" in html

    def test_english_rss_renders_english_post_title(self, client, ar_blog_post):
        resp = client.get("/feed.xml")
        html = resp.data.decode("utf-8")
        assert "English Title" in html

    def test_ar_rss_content_type(self, client):
        resp = client.get("/ar/feed.xml")
        assert "application/rss+xml" in resp.content_type

    def test_both_rss_feeds_linked_in_head(self, client):
        """<head> must include <link> alternates for both EN and AR RSS feeds."""
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        assert "application/rss+xml" in html
        # Both feed links should appear
        assert "Blog RSS (English)" in html
        assert "Blog RSS (العربية)" in html

    def test_invalid_locale_rss_returns_404(self, client):
        resp = client.get("/xx/feed.xml")
        assert resp.status_code == 404


# ── OG locale attribute ────────────────────────────────────────────────────


class TestOGLocale:
    """OpenGraph locale meta must match the page locale."""

    def test_ar_index_og_locale_is_ar(self, client):
        resp = client.get("/ar/")
        html = resp.data.decode("utf-8")
        assert 'og:locale" content="ar_AR"' in html

    def test_en_index_og_locale_is_en(self, client):
        resp = client.get("/en/")
        html = resp.data.decode("utf-8")
        assert 'og:locale" content="en_US"' in html
