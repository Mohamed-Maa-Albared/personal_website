"""
Shared pytest fixtures for the personal_website test suite.
"""

import os

import pytest

# Ensure testing env vars are set before app factory runs
os.environ.setdefault("FLASK_ENV", "testing")
os.environ.setdefault("ADMIN_PASSWORD", "test-password-123")

from app import create_app
from app import db as _db
from app.models import (
    BlogPost,
    Experience,
    ImpactCard,
    LanguageItem,
    Message,
    PageVisit,
    Project,
    SiteConfig,
    SkillCluster,
)


@pytest.fixture(scope="session")
def app():
    """Create and configure a test application instance (once per session)."""
    application = create_app("testing")
    yield application


@pytest.fixture(autouse=True)
def _setup_db(app):
    """Create all tables before each test, drop after."""
    with app.app_context():
        _db.create_all()
        yield
        _db.session.remove()
        _db.drop_all()


@pytest.fixture()
def client(app):
    """Flask test client."""
    return app.test_client()


@pytest.fixture()
def db(app):
    """Database session — alias for convenience."""
    return _db


@pytest.fixture()
def auth_client(client, app):
    """Test client that is already logged in as admin."""
    with client.session_transaction() as sess:
        sess["admin_logged_in"] = True
    return client


@pytest.fixture()
def sample_project(app, db):
    """Insert and return a sample Project."""
    with app.app_context():
        project = Project(
            title="Test Project",
            description="A test project description",
            short_description="Short desc",
            technologies="Python, Flask",
            category="NLP",
            year="2024",
            featured=True,
            sort_order=1,
        )
        db.session.add(project)
        db.session.commit()
        db.session.refresh(project)
        return project


@pytest.fixture()
def sample_blog_post(app, db):
    """Insert and return a sample published BlogPost."""
    with app.app_context():
        post = BlogPost(
            title="Test Blog Post",
            slug="test-blog-post",
            excerpt="A test excerpt",
            content="<p>Test blog content that is long enough.</p>",
            category="AI",
            tags="test, ai",
            read_time=3,
            published=True,
            featured=False,
        )
        db.session.add(post)
        db.session.commit()
        db.session.refresh(post)
        return post


@pytest.fixture()
def sample_experience(app, db):
    """Insert and return a sample Experience."""
    with app.app_context():
        exp = Experience(
            role="Data Scientist",
            company="Test Corp",
            location="Berlin",
            date_range="Jan 2024 – Present",
            description="Test role",
            sort_order=1,
        )
        db.session.add(exp)
        db.session.commit()
        db.session.refresh(exp)
        return exp
