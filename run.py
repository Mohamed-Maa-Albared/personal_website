import os

from app import create_app, db
from app.models import BlogPost, Experience, Message, PageVisit, Project, SiteConfig

app = create_app(os.environ.get("FLASK_ENV", "development"))


@app.shell_context_processor
def make_shell_context():
    """Register shell context for flask shell"""
    return {
        "db": db,
        "Project": Project,
        "Message": Message,
        "Experience": Experience,
        "BlogPost": BlogPost,
        "SiteConfig": SiteConfig,
        "PageVisit": PageVisit,
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(port=port)
