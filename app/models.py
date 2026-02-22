from datetime import datetime

from app import db


class Project(db.Model):
    """Model for portfolio projects"""

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(300))
    image_url = db.Column(db.String(500))
    demo_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    technologies = db.Column(db.String(500))  # Comma-separated
    category = db.Column(db.String(100))  # e.g. "NLP", "Computer Vision", "GenAI"
    year = db.Column(db.String(20))
    client = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    featured = db.Column(db.Boolean, default=False)
    sort_order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Project {self.title}>"


class Experience(db.Model):
    """Model for work experience timeline"""

    __tablename__ = "experiences"

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    date_range = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    highlights = db.Column(db.Text)  # JSON array of highlight strings
    sort_order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Experience {self.role} at {self.company}>"


class Message(db.Model):
    """Model for contact form messages"""

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Message from {self.name}>"
