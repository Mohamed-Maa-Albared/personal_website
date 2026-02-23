"""
Tests for public routes (main blueprint).
"""

import json


class TestIndex:
    """Tests for the homepage."""

    def test_index_returns_200(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_index_contains_meta(self, client):
        resp = client.get("/")
        assert b"Mohamed Maa Albared" in resp.data

    def test_index_has_security_headers(self, client):
        resp = client.get("/")
        assert "Content-Security-Policy" in resp.headers
        assert resp.headers["X-Content-Type-Options"] == "nosniff"
        assert resp.headers["X-Frame-Options"] == "SAMEORIGIN"
        assert "Permissions-Policy" in resp.headers

    def test_csp_contains_required_directives(self, client):
        resp = client.get("/")
        csp = resp.headers["Content-Security-Policy"]
        assert "default-src 'self'" in csp
        assert "script-src" in csp
        assert "frame-ancestors 'none'" in csp
        assert "base-uri 'self'" in csp
        assert "form-action 'self'" in csp


class TestProjectDetail:
    """Tests for the project detail page."""

    def test_project_detail_200(self, client, sample_project):
        resp = client.get(f"/project/{sample_project.id}")
        assert resp.status_code == 200

    def test_project_detail_404(self, client):
        resp = client.get("/project/9999")
        assert resp.status_code == 404


class TestCaseStudy:
    """Tests for the case study page."""

    def test_case_study_404_when_no_case_study(self, client, sample_project):
        resp = client.get(f"/case-study/{sample_project.id}")
        assert resp.status_code == 404

    def test_case_study_200_when_has_case_study(self, client, sample_project, db, app):
        with app.app_context():
            from app.models import Project

            project = Project.query.get(sample_project.id)
            project.has_case_study = True
            project.challenge = "Test challenge"
            project.approach = "Test approach"
            project.results = "Test results"
            db.session.commit()
        resp = client.get(f"/case-study/{sample_project.id}")
        assert resp.status_code == 200


class TestBlog:
    """Tests for blog pages."""

    def test_blog_listing_200(self, client):
        resp = client.get("/blog")
        assert resp.status_code == 200

    def test_blog_detail_200(self, client, sample_blog_post):
        resp = client.get(f"/blog/{sample_blog_post.slug}")
        assert resp.status_code == 200

    def test_blog_detail_404_unpublished(self, client, sample_blog_post, db, app):
        with app.app_context():
            post = BlogPost.query.get(sample_blog_post.id)
            post.published = False
            db.session.commit()
        resp = client.get(f"/blog/{sample_blog_post.slug}")
        assert resp.status_code == 404

    def test_blog_category_filter(self, client, sample_blog_post):
        resp = client.get("/blog?category=AI")
        assert resp.status_code == 200


from app.models import BlogPost


class TestContact:
    """Tests for the contact form endpoint."""

    def test_contact_success(self, client):
        resp = client.post(
            "/contact",
            json={
                "name": "Test User",
                "email": "test@example.com",
                "subject": "Test Subject",
                "message": "This is a valid test message that is long enough.",
            },
        )
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["success"] is True

    def test_contact_missing_fields(self, client):
        resp = client.post(
            "/contact",
            json={"name": "Test", "email": "", "subject": "", "message": ""},
        )
        assert resp.status_code == 400

    def test_contact_invalid_email(self, client):
        resp = client.post(
            "/contact",
            json={
                "name": "Test",
                "email": "not-an-email",
                "subject": "Test",
                "message": "Long enough test message here.",
            },
        )
        assert resp.status_code == 400

    def test_contact_message_too_short(self, client):
        resp = client.post(
            "/contact",
            json={
                "name": "Test",
                "email": "test@example.com",
                "subject": "Test",
                "message": "Short",
            },
        )
        assert resp.status_code == 400

    def test_contact_honeypot_silently_succeeds(self, client):
        resp = client.post(
            "/contact",
            json={
                "name": "Bot",
                "email": "bot@spam.com",
                "subject": "Spam",
                "message": "Spam message long enough",
                "website": "http://spam.com",
            },
        )
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["success"] is True

    def test_contact_rejects_non_json(self, client):
        resp = client.post("/contact", data="not json")
        assert resp.status_code == 400


class TestAPI:
    """Tests for the JSON API."""

    def test_api_projects(self, client, sample_project):
        resp = client.get("/api/projects")
        assert resp.status_code == 200
        data = resp.get_json()
        assert isinstance(data, list)
        assert len(data) >= 1
        assert data[0]["title"] == "Test Project"


class TestSEO:
    """Tests for SEO routes."""

    def test_sitemap_xml(self, client):
        resp = client.get("/sitemap.xml")
        assert resp.status_code == 200
        assert b"<urlset" in resp.data

    def test_robots_txt(self, client):
        resp = client.get("/robots.txt")
        assert resp.status_code == 200
        assert b"Disallow: /admin/" in resp.data

    def test_rss_feed(self, client):
        resp = client.get("/feed.xml")
        assert resp.status_code == 200
        assert b"<rss" in resp.data or b"<channel" in resp.data
