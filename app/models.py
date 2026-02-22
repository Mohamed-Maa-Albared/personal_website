from datetime import datetime

from app import db


class Project(db.Model):
    """Model for portfolio projects"""

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500))
    demo_url = db.Column(db.String(500))
    github_url = db.Column(db.String(500))
    technologies = db.Column(db.String(500))  # Comma-separated
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    featured = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Project {self.title}>"


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


class About(db.Model):
    """Model for about/bio information"""

    __tablename__ = "about"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    bio = db.Column(db.Text)
    profile_image_url = db.Column(db.String(500))
    skills = db.Column(db.Text)  # JSON string
    social_links = db.Column(db.Text)  # JSON string
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<About {self.title}>"

    def __repr__(self):
        return f"<About {self.title}>"
