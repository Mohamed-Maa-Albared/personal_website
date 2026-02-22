import os

from app import create_app, db
from app.models import About, Message, Project

app = create_app(os.environ.get("FLASK_ENV", "development"))


@app.shell_context_processor
def make_shell_context():
    """Register shell context for flask shell"""
    return {"db": db, "Project": Project, "Message": Message, "About": About}


if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True)
