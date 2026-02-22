# Personal Website Project

A modern, Flask-based personal portfolio website with backend support for projects, contact messages, and portfolio management.

## Features

- **Home Page**: Hero section with featured projects
- **Projects Portfolio**: Grid layout with pagination for all projects
- **Project Details**: Individual project pages with technologies and links
- **About Page**: Bio, profile image, and skills showcase
- **Contact Form**: Backend contact form with message storage
- **Responsive Design**: Mobile-friendly layout
- **Database**: SQLAlchemy ORM for data management

## Project Structure

```
personal_website/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── models.py             # Database models
│   ├── routes.py             # Application routes
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css     # Main stylesheet
│   │   ├── js/
│   │   │   └── main.js       # JavaScript utilities
│   │   └── images/           # Image assets
│   └── templates/
│       ├── base.html         # Base template
│       ├── index.html        # Homepage
│       ├── projects.html     # Projects listing
│       ├── project_detail.html
│       ├── about.html        # About page
│       └── contact.html      # Contact form
├── config.py                 # Configuration settings
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
└── .gitignore               # Git ignore rules
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
cd personal_website
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

### 4. Initialize Database

```bash
flask shell
>>> from app import db, create_app
>>> app = create_app()
>>> with app.app_context():
>>>     db.create_all()
```

### 5. Run Development Server

```bash
python run.py
```

Visit `http://localhost:5000` in your browser.

## Database Models

### Project
- title: Project title
- description: Detailed description
- image_url: Project image
- demo_url: Live demo link
- github_url: GitHub repository
- technologies: Comma-separated tech stack
- featured: Featured on homepage
- created_at / updated_at: Timestamps

### Message
- name: Visitor name
- email: Contact email
- subject: Message subject
- message: Message content
- created_at: Submission timestamp
- is_read: Read status

### About
- title: Professional title
- bio: Biography
- profile_image_url: Profile picture
- skills: Comma-separated skills
- social_links: JSON string of social profiles

## API Endpoints

- `GET /` - Homepage
- `GET /projects` - Projects listing (paginated)
- `GET /project/<id>` - Project details
- `GET /about` - About page
- `GET /contact` - Contact form page
- `POST /contact` - Submit contact form
- `GET /api/projects` - JSON projects API

## Customization

### Add a New Project

```python
from app import db, create_app
from app.models import Project

app = create_app()
with app.app_context():
    project = Project(
        title="My Awesome Project",
        description="Project description here...",
        technologies="Python, Flask, SQLAlchemy",
        demo_url="https://demo.example.com",
        github_url="https://github.com/user/project",
        featured=True
    )
    db.session.add(project)
    db.session.commit()
```

### Update About Information

```python
from app.models import About

about = About(
    title="Full Stack Developer",
    bio="Your bio here...",
    skills="Python, JavaScript, React, Flask"
)
db.session.add(about)
db.session.commit()
```

## Deployment

For production deployment, see [docSpace deployment instructions](https://docspace.com/deploy).

Follow the [LSY Security Golden Path](https://github.com/lsy-central/lsy-security-golden-path) for security best practices.

## Technologies Used

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **WSGI**: Werkzeug

## License

MIT License - feel free to use this for your personal website.
