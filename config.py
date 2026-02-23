import logging
import os
import sys
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class Config:
    """Base configuration"""

    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-key-change-in-production"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "sqlite:///personal_website.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session hardening
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    WTF_CSRF_TIME_LIMIT = 3600  # 1 hour

    # Upload settings
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB max upload
    UPLOAD_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "app", "static", "uploads"
    )


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration — enforces secure defaults"""

    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True

    def __init__(self) -> None:
        super().__init__()
        # Refuse to start with insecure defaults
        if self.SECRET_KEY == "dev-key-change-in-production":
            logger.critical("SECRET_KEY is not set — refusing to start in production")
            sys.exit(1)
        if os.environ.get("ADMIN_PASSWORD") in (None, "", "changeme123"):
            logger.critical(
                "ADMIN_PASSWORD is missing or still the default — refusing to start in production"
            )
            sys.exit(1)


class TestingConfig(Config):
    """Testing configuration — in-memory DB, CSRF disabled for test clients."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False  # Disable CSRF for test POST requests
    SERVER_NAME = "localhost"  # Required for url_for in tests
    RATELIMIT_ENABLED = False  # Disable rate limiting during tests


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
