"""
Tests for admin routes and security.
"""

import json


class TestAdminLogin:
    """Tests for admin authentication."""

    def test_login_page_200(self, client):
        resp = client.get("/admin/login")
        assert resp.status_code == 200

    def test_login_success(self, client):
        resp = client.post(
            "/admin/login",
            data={"password": "test-password-123"},
            follow_redirects=True,
        )
        assert resp.status_code == 200

    def test_login_failure(self, client):
        resp = client.post(
            "/admin/login",
            data={"password": "wrong-password"},
            follow_redirects=False,
        )
        # Should stay on login page (re-render with error flash)
        assert resp.status_code == 200

    def test_dashboard_requires_auth(self, client):
        resp = client.get("/admin/")
        assert resp.status_code == 302  # Redirect to login

    def test_logout(self, auth_client):
        resp = auth_client.get("/admin/logout", follow_redirects=False)
        assert resp.status_code == 302


class TestAdminDashboard:
    """Tests for the admin dashboard."""

    def test_dashboard_200(self, auth_client):
        resp = auth_client.get("/admin/")
        assert resp.status_code == 200


class TestProjectCRUD:
    """Tests for project CRUD operations."""

    def test_project_new_page(self, auth_client):
        resp = auth_client.get("/admin/project/new")
        assert resp.status_code == 200

    def test_project_create(self, auth_client):
        resp = auth_client.post(
            "/admin/project/new",
            data={
                "title": "New Test Project",
                "description": "A new project description.",
                "category": "GenAI",
                "technologies": "Python",
                "sort_order": "1",
            },
            follow_redirects=True,
        )
        assert resp.status_code == 200

    def test_project_edit(self, auth_client, sample_project):
        resp = auth_client.get(f"/admin/project/{sample_project.id}/edit")
        assert resp.status_code == 200

    def test_project_delete(self, auth_client, sample_project):
        resp = auth_client.post(
            f"/admin/project/{sample_project.id}/delete",
            follow_redirects=True,
        )
        assert resp.status_code == 200


class TestBlogCRUD:
    """Tests for blog CRUD operations."""

    def test_blog_new_page(self, auth_client):
        resp = auth_client.get("/admin/blog/new")
        assert resp.status_code == 200

    def test_blog_create(self, auth_client):
        resp = auth_client.post(
            "/admin/blog/new",
            data={
                "title": "New Blog Post",
                "content": "<p>Blog content here</p>",
                "category": "AI",
                "read_time": "5",
            },
            follow_redirects=True,
        )
        assert resp.status_code == 200

    def test_blog_edit(self, auth_client, sample_blog_post):
        resp = auth_client.get(f"/admin/blog/{sample_blog_post.id}/edit")
        assert resp.status_code == 200

    def test_blog_delete(self, auth_client, sample_blog_post):
        resp = auth_client.post(
            f"/admin/blog/{sample_blog_post.id}/delete",
            follow_redirects=True,
        )
        assert resp.status_code == 200


class TestExperienceCRUD:
    """Tests for experience CRUD operations."""

    def test_experience_new_page(self, auth_client):
        resp = auth_client.get("/admin/experience/new")
        assert resp.status_code == 200

    def test_experience_form_has_highlight_editor(self, auth_client):
        """Experience form should have the chip-based highlight editor."""
        resp = auth_client.get("/admin/experience/new")
        assert b"highlightEditor" in resp.data
        assert b"highlightInput" in resp.data
        assert b"addHighlightBtn" in resp.data

    def test_experience_create(self, auth_client):
        resp = auth_client.post(
            "/admin/experience/new",
            data={
                "role": "ML Engineer",
                "company": "TestCo",
                "date_range": "2024 – Present",
                "sort_order": "0",
            },
            follow_redirects=True,
        )
        assert resp.status_code == 200

    def test_experience_edit(self, auth_client, sample_experience):
        resp = auth_client.get(f"/admin/experience/{sample_experience.id}/edit")
        assert resp.status_code == 200

    def test_experience_update(self, auth_client, sample_experience, app, db):
        """Editing an experience should persist changes to the DB."""
        resp = auth_client.post(
            f"/admin/experience/{sample_experience.id}/edit",
            data={
                "role": "Senior Data Scientist",
                "company": "Updated Corp",
                "location": "Munich",
                "date_range": "Jan 2024 \u2013 Present",
                "description": "Updated role desc",
                "sort_order": "1",
            },
            follow_redirects=True,
        )
        assert resp.status_code == 200
        with app.app_context():
            from app.models import Experience

            exp = Experience.query.get(sample_experience.id)
            assert exp.role == "Senior Data Scientist"
            assert exp.company == "Updated Corp"

    def test_experience_delete(self, auth_client, sample_experience):
        resp = auth_client.post(
            f"/admin/experience/{sample_experience.id}/delete",
            follow_redirects=True,
        )
        assert resp.status_code == 200


class TestTabPersistence:
    """Tests that admin redirects include the correct #tab-* hash."""

    def test_project_create_redirects_to_projects_tab(self, auth_client):
        resp = auth_client.post(
            "/admin/project/new",
            data={
                "title": "Tab Test Project",
                "description": "Desc",
                "category": "NLP",
                "technologies": "Python",
                "sort_order": "1",
            },
            follow_redirects=False,
        )
        assert resp.status_code == 302
        assert "#tab-projects" in resp.headers["Location"]

    def test_experience_create_redirects_to_experience_tab(self, auth_client):
        resp = auth_client.post(
            "/admin/experience/new",
            data={
                "role": "Engineer",
                "company": "Co",
                "date_range": "2024",
                "sort_order": "0",
            },
            follow_redirects=False,
        )
        assert resp.status_code == 302
        assert "#tab-experience" in resp.headers["Location"]

    def test_blog_create_redirects_to_blog_tab(self, auth_client):
        resp = auth_client.post(
            "/admin/blog/new",
            data={
                "title": "Tab Test Blog",
                "content": "<p>Content</p>",
                "category": "AI",
                "read_time": "3",
            },
            follow_redirects=False,
        )
        assert resp.status_code == 302
        assert "#tab-blog" in resp.headers["Location"]

    def test_project_delete_redirects_to_projects_tab(
        self, auth_client, sample_project
    ):
        resp = auth_client.post(
            f"/admin/project/{sample_project.id}/delete",
            follow_redirects=False,
        )
        assert resp.status_code == 302
        assert "#tab-projects" in resp.headers["Location"]


class TestCaseStudyForm:
    """Tests for the case study editor."""

    def test_case_study_form_has_wysiwyg(self, auth_client, sample_project):
        """Case study form textareas should have data-wysiwyg for rich text editing."""
        resp = auth_client.get(f"/admin/project/{sample_project.id}/case-study")
        assert resp.status_code == 200
        assert b"data-wysiwyg" in resp.data


class TestAdminSecurity:
    """Security-specific tests for admin routes."""

    def test_unauthenticated_crud_redirects(self, client, sample_project):
        """All admin CRUD routes should redirect unauthenticated users."""
        routes = [
            "/admin/",
            "/admin/project/new",
            f"/admin/project/{sample_project.id}/edit",
            "/admin/blog/new",
            "/admin/experience/new",
        ]
        for route in routes:
            resp = client.get(route)
            assert resp.status_code == 302, f"{route} did not redirect"

    def test_upload_requires_auth(self, client):
        resp = client.post("/admin/upload-image")
        assert resp.status_code == 302  # Redirect to login


class TestSiteConfig:
    """Tests for site config updates including HTML preservation."""

    def test_site_config_preserves_bio_html(self, auth_client, db):
        """About bio fields should preserve <strong> tags (sanitize_html, not sanitize_input)."""
        from app.models import SiteConfig

        # Set initial config
        SiteConfig.set("about_bio1", "plain text")
        db.session.commit()

        # Update with HTML content
        resp = auth_client.post(
            "/admin/site-config",
            data={
                "cfg_about_bio1": "I have <strong>4 years</strong> of experience in <em>AI</em>.",
            },
            follow_redirects=True,
        )
        assert resp.status_code == 200
        saved = SiteConfig.get("about_bio1")
        assert "<strong>" in saved, "HTML <strong> tags were stripped from about_bio1"
        assert "<em>" in saved, "HTML <em> tags were stripped from about_bio1"

    def test_site_config_strips_html_from_non_bio(self, auth_client, db):
        """Non-bio fields should strip HTML (sanitize_input)."""
        from app.models import SiteConfig

        SiteConfig.set("hero_title", "old")
        db.session.commit()

        resp = auth_client.post(
            "/admin/site-config",
            data={"cfg_hero_title": "Hello <script>alert(1)</script>World"},
            follow_redirects=True,
        )
        assert resp.status_code == 200
        saved = SiteConfig.get("hero_title")
        assert "<script>" not in saved
        assert "Hello" in saved
