# AGENTS.md — AI Agent Instructions for personal_website

> Last updated: 2025-07-23

## Project Overview

Personal portfolio website for **Mohamed Maa Albared**, Data Scientist at zeroG (Lufthansa Group). Built with Flask, styled with a dark neural/neuroscience aesthetic (deep navy + electric purple/cyan). Deployed on Render (free tier).

**Live URL:** `https://mohamed-maa-albared-portfolio.onrender.com/`
**Repo:** `https://github.com/Mohamed-Maa-Albared/personal_website`

---

## Tech Stack

| Layer              | Technology                                          | Version |
| ------------------ | --------------------------------------------------- | ------- |
| Backend            | Flask                                               | 3.0.0   |
| ORM                | Flask-SQLAlchemy                                    | 3.1.1   |
| CSRF               | Flask-WTF                                           | 1.2.1   |
| Rate Limiting      | Flask-Limiter                                       | 3.5.0   |
| Input Sanitization | bleach                                              | 6.1.0   |
| WSGI Server        | gunicorn                                            | 21.2.0  |
| Database (dev)     | SQLite                                              | —       |
| Python             | 3.11.x                                              | —       |
| Frontend           | Vanilla HTML/CSS/JS                                 | —       |
| CDN: Animation     | GSAP + ScrollTrigger                                | 3.12.2  |
| CDN: Charts        | Chart.js                                            | 4.4.4   |
| Fonts              | Google Fonts (Space Grotesk, Inter, JetBrains Mono) | —       |

---

## Project Structure

```
personal_website/
├── app/
│   ├── __init__.py              # App factory, extensions, security headers, CSP, error handlers, visitor tracking
│   ├── models.py                # SQLAlchemy models: Project, Experience, Message, BlogPost, SiteConfig, PageVisit, ImpactCard, SkillCluster, LanguageItem
│   ├── routes.py                # Public routes: index, blog, case_study, sitemap, robots, rss, contact, api
│   ├── admin.py                 # Admin blueprint: CRUD, analytics dashboard, site config editor
│   ├── utils.py                 # Shared helpers: sanitize, validate, email notifications, locale/UA parsing, generate_slug
│   ├── templates/
│   │   ├── base.html            # Base layout (CDN libs, dark/light toggle, scroll progress bar, nav)
│   │   ├── index.html           # Single-page: Hero, About, Impact, Timeline, Projects, Skills, Blog Preview, Contact
│   │   ├── project_detail.html  # Individual project detail page
│   │   ├── blog.html            # Blog listing with category filtering
│   │   ├── blog_detail.html     # Individual blog post (OG tags, author card, related posts)
│   │   ├── case_study.html      # Deep-dive case study (challenge/approach/results/metrics)
│   │   ├── sitemap.xml          # SEO sitemap template
│   │   ├── feed.xml             # RSS feed template
│   │   ├── errors/              # Custom error pages (400, 404, 429, 500)
│   │   └── admin/
│   │       ├── base.html        # Admin layout + tab/config CSS
│   │       ├── login.html       # Admin login form
│   │       ├── dashboard.html   # Admin dashboard (6 tabs: Analytics, Site Content, Projects, Experience, Blog, Messages)
│   │       ├── project_form.html      # Create/edit project form
│   │       ├── experience_form.html   # Create/edit experience form
│   │       ├── blog_form.html         # Create/edit blog post form
│   │       ├── case_study_form.html   # Edit case study for a project
│   │       └── message_detail.html    # View contact message
│   └── static/
│       ├── css/style.css        # ~2250 lines, dark/light themes, blog, case study, skeleton screens
│       ├── js/
│       │   ├── main.js          # ~392 lines: neural canvas, GSAP parallax, dark mode, ripples
│       │   └── admin.js         # ~220 lines: rich text toolbar, image upload, Chart.js init
│       ├── images/
│       │   ├── logo.png         # Site logo
│       │   └── profile.png      # Profile photo
│       └── uploads/             # User-uploaded blog images (.gitkeep)
├── .github/
│   └── workflows/
│       └── backup.yml           # Automated daily DB backup to GitHub
├── config.py                    # Config classes: Development, Production, Testing (with production enforcement)
├── run.py                       # Entry point, shell context (default port 5001)
├── seed.py                      # Seeds DB: experiences, projects, blog posts, site configs, impact cards, skill clusters, languages
├── requirements.txt             # Python dependencies
├── render.yaml                  # Render deployment config
├── .env.example                 # Environment variable template
├── .gitignore                   # Ignores .env, *.db, venv/, Achievements.md, etc.
├── ROADMAP.md                   # Roadmap with status tracking
└── AGENTS.md                    # This file
```

---

## Architecture & Patterns

### Application Factory
- `create_app(config_name)` in `app/__init__.py`
- Extensions initialized via `init_app()` pattern: `db`, `csrf`, `limiter`
- Blueprints: `main_bp` (public), `admin_bp` (at `/admin`)
- `before_request` hook for visitor tracking (skips static/admin/api/robots/sitemap/feed)
- Custom error handlers: 400, 404, 429, 500
- Structured logging via `_configure_logging()`

### Database Models
- **Project**: title, description, short_description, image_url, demo_url, github_url, technologies (comma-separated), category, year, client, featured, sort_order, **case_study** (Text), **metrics** (JSON), **challenge** (Text), **approach** (Text), **results** (Text), **has_case_study** (Boolean)
- **Experience**: role, company, location, date_range, description, highlights (JSON string), sort_order
- **Message**: name, email, subject, message, is_read, created_at
- **BlogPost**: title, slug (unique), excerpt, content (HTML), cover_image, category, tags (comma-separated), read_time, published, featured, created_at, updated_at, sort_order
- **SiteConfig**: key (unique, indexed), value, label, group — Key-value store for editable homepage content (hero, about). Static helpers: `get(key)`, `set(key, value)`, `get_group(group)`
- **PageVisit**: path, referrer, user_agent, ip_hash (SHA-256), country (from Accept-Language), visited_at (indexed) — Lightweight visitor analytics
- **ImpactCard**: icon, value, prefix, suffix, description, sort_order — Dynamic impact metrics on homepage
- **SkillCluster**: icon, title, tags (comma-separated), sort_order — Skill categories on homepage
- **LanguageItem**: name, level, sort_order — Spoken languages on homepage

### Routing
- `/` — Single-page index (loads projects, experiences, latest 3 blog posts from DB)
- `/project/<int:id>` — Project detail page
- `/blog` — Blog listing with optional `?category=` filter
- `/blog/<slug>` — Individual blog post with related articles
- `/case-study/<int:id>` — Deep-dive case study page (404 if project has no case study)
- `/contact` (POST, JSON) — Contact form submission (CSRF-exempt, rate-limited 3/min)
- `/api/projects` (GET) — JSON API for projects
- `/sitemap.xml` — Auto-generated XML sitemap
- `/robots.txt` — SEO robots file (disallows `/admin/`)
- `/feed.xml` — RSS feed for blog posts
- `/admin/` — Dashboard with 6 tabs: Analytics, Site Content, Projects, Experience, Blog, Messages
- `/admin/login` (GET/POST) — Login (rate-limited 5/min)
- `/admin/site-config` (POST) — Update editable site content (hero, about)
- `/admin/projects/new|edit|delete` — Project CRUD
- `/admin/experiences/new|edit|delete` — Experience CRUD
- `/admin/messages/<id>` — View/delete messages
- `/admin/blog/new|edit|delete` — Blog post CRUD
- `/admin/project/<id>/case-study` — Case study editor
- `/admin/impact-cards/new|edit|delete` — Impact card CRUD
- `/admin/skill-clusters/new|edit|delete` — Skill cluster CRUD
- `/admin/languages/new|edit|delete` — Language item CRUD
- `/admin/upload-image` (POST, JSON) — Blog image file upload

### Frontend
- **Single-page layout** — all public content in `index.html` with anchor navigation (`#about`, `#experience`, `#projects`, `#skills`, `#blog`, `#contact`)
- **Neural canvas** — animated particle network in hero section (80 nodes, vanilla Canvas API, mouse-reactive connections)
- **Dark/Light mode** — toggle button in nav, persisted via `localStorage`, CSS variables swap via `[data-theme="light"]`
- **GSAP ScrollTrigger** — hero parallax fade, timeline marker dot scale animations
- **Custom cursor** — dot + ring, dark purple in dark mode, dark navy in light mode, hidden on mobile
- **Scroll reveals** — IntersectionObserver-based `.reveal-up` class for all sections, cards, labels
- **Scroll progress bar** — fixed gradient bar at top tracking page scroll
- **Scroll reveals** — IntersectionObserver-based `.reveal-up` class
- **Project filters** — client-side category filtering with animated transitions
- **Counter animations** — count-up effect for impact numbers
- **Blog preview** — latest 3 posts section on index page
- **Skeleton screens** — shimmer loading animation for blog card images
- **Button ripple effect** — click micro-interaction on all buttons
- **Contact form** — AJAX POST with honeypot spam field, client-side validation
- **Rich text toolbar** — admin blog editor toolbar (bold, italic, headings, links, images, lists) — no HTML typing needed
- **Chart.js analytics** — daily visits line chart, browser/device doughnut charts in admin dashboard
- **Image upload** — local file upload for blog cover images (stored in static/uploads/)

---

## Security Stack

All security measures are already implemented. Do not remove or weaken them.

| Measure                 | Location                  | Details                                                                                   |
| ----------------------- | ------------------------- | ----------------------------------------------------------------------------------------- |
| CSRF Protection         | `app/__init__.py`         | `CSRFProtect()` on all forms; `/contact` is `@csrf.exempt` (JSON endpoint)                |
| Rate Limiting           | `app/__init__.py`         | Global 200/min; login 5/min; contact 3/min                                                |
| Input Sanitization      | `utils.py`, `admin.py`    | `sanitize_input()` strips HTML; `sanitize_html()` allowlists safe tags                    |
| Password Comparison     | `admin.py`                | `hmac.compare_digest()` (timing-safe)                                                     |
| Content Security Policy | `app/__init__.py`         | Full CSP header in `after_request`                                                        |
| Security Headers        | `app/__init__.py`         | X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy, HSTS (prod) |
| Session Security        | `config.py`               | `HTTPONLY=True`, `SAMESITE=Lax`, `SECURE=True` (prod), 2-hour expiry                      |
| Honeypot                | `index.html`, `routes.py` | Hidden `website` field to catch bots                                                      |
| CSRF Tokens             | All admin templates       | `<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">` in every POST form   |
| Custom Error Pages      | `app/templates/errors/`   | 400, 404, 429, 500 — no Flask internals leaked                                            |
| Production Enforcement  | `config.py`               | App refuses to start with default `SECRET_KEY` or `ADMIN_PASSWORD`                        |
| Structured Logging      | `app/__init__.py`         | Security events (login attempts, contact submissions) logged with context                 |
| Privacy-safe Analytics  | `app/__init__.py`         | Visitor IPs are SHA-256 hashed — no raw IP addresses stored                               |

---

## Environment Variables

Defined in `.env` (never committed). See `.env.example` for template.

| Variable             | Required   | Description                                             |
| -------------------- | ---------- | ------------------------------------------------------- |
| `FLASK_ENV`          | Yes        | `development` or `production`                           |
| `SECRET_KEY`         | Yes (prod) | Random 32+ char string for session signing              |
| `DATABASE_URL`       | No         | Defaults to `sqlite:///personal_website.db`             |
| `ADMIN_PASSWORD`     | Yes        | Password for `/admin` login                             |
| `MAIL_SERVER`        | No         | SMTP host for email notifications (e.g. smtp.gmail.com) |
| `MAIL_PORT`          | No         | SMTP port (default 587)                                 |
| `MAIL_USERNAME`      | No         | SMTP login username                                     |
| `MAIL_PASSWORD`      | No         | SMTP login password / app password                      |
| `NOTIFICATION_EMAIL` | No         | Address to receive contact form notifications           |

---

## Development Workflow

```bash
# Setup
cd personal_website
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # edit with your values

# Seed database
python seed.py

# Run locally
python run.py
# → http://localhost:5001

# Run with Flask shell
flask shell
>>> Project.query.all()
```

---

## Deployment (Render)

- Config: `render.yaml`
- Python version: `.python-version` → 3.11.7
- Build: `pip install -r requirements.txt && python seed.py`
- Start: `gunicorn run:app --bind 0.0.0.0:$PORT --workers 2`
- Auto-deploys on `git push origin main`

---

## Conventions & Rules

### Code Style
- Python: PEP 8, Black-formatted
- HTML: Jinja2 templates, 4-space indent
- CSS: Custom properties (CSS variables), BEM-adjacent naming
- JS: Vanilla ES6+, no frameworks, no build step

### CSS Variables (Theme)
```css
--accent: #7c5cfc;        /* Electric purple */
--accent-cyan: #00e5ff;    /* Cyan accent */
--bg-deep: #06080d;        /* Deepest background */
--bg-dark: #0a0e17;        /* Card/section background */
--bg-card: #111827;        /* Card surface */
--text-primary: #e2e8f0;   /* Main text */
--text-secondary: #94a3b8; /* Muted text */
--border-subtle: rgba(124, 92, 252, .12); /* Borders */
```

### Key Decisions
- **No JavaScript frameworks** — vanilla JS only for simplicity and performance
- **No CSS frameworks** — fully custom styles
- **SQLite for dev/prod** — sufficient for a personal portfolio
- **Session-based admin auth** — no user model, single password from env var
- **Single-page public site** — all content on index with anchor links
- **No build tools** — no webpack, no SASS, no bundler

### Do NOT
- Remove or weaken any security headers or CSRF protection
- Add `debug=True` to `run.py` or production configs
- Commit `.env`, `*.db`, or `Achievements.md` (contains private CV data)
- Use `==` for password comparison (use `hmac.compare_digest`)
- Add inline `<script>` tags (violates CSP)
- Introduce npm/node dependencies (keep it pure Python + vanilla JS)

### Do
- Run `python seed.py` after model changes to repopulate data
- Add CSRF tokens to any new admin POST forms
- Sanitize all user inputs with `sanitize_input()` or `sanitize_html()` from `app/utils.py`
- Add rate limiting to any new POST endpoints
- Keep all static assets in `app/static/`
- Test locally before pushing (`python run.py`)
- Review [LSY Security Golden Path](https://github.com/lsy-central/lsy-security-golden-path) for security updates
- Refer to docSpace for org-specific deployment instructions

---

## Testing

No test framework is set up yet. To validate manually:

```python
python -c "
from app import create_app
app = create_app('development')
with app.test_client() as c:
    r1 = c.get('/')
    r2 = c.get('/admin/login')
    r3 = c.post('/contact', json={'name':'t','email':'a@b.com','subject':'t','message':'test message long enough'})
    r4 = c.get('/admin/')
    r5 = c.get('/blog')
    r6 = c.get('/blog/architecture-of-thought-neuroscience-ai-agents')
    r7 = c.get('/case-study/1')
    r8 = c.get('/sitemap.xml')
    r9 = c.get('/robots.txt')
    r10 = c.get('/feed.xml')
    print(f'Index: {r1.status_code}')          # 200
    print(f'Admin login: {r2.status_code}')    # 200
    print(f'Contact: {r3.status_code}')        # 200
    print(f'Admin redirect: {r4.status_code}') # 302
    print(f'Blog: {r5.status_code}')           # 200
    print(f'Blog detail: {r6.status_code}')    # 200
    print(f'Case study: {r7.status_code}')     # 200
    print(f'Sitemap: {r8.status_code}')        # 200
    print(f'Robots: {r9.status_code}')         # 200
    print(f'RSS: {r10.status_code}')           # 200
    print(f'CSP: {\"Content-Security-Policy\" in r1.headers}')  # True
"
```

---

## File Sizes (approximate)

| File                   | Lines | Purpose                                             |
| ---------------------- | ----- | --------------------------------------------------- |
| `style.css`            | ~2257 | All styles (dark + light themes)                    |
| `admin/base.html`      | ~664  | Admin layout + tab/config CSS                       |
| `index.html`           | ~647  | Full single-page + blog preview                     |
| `seed.py`              | ~642  | Data seeder (projects, blog, site config)           |
| `main.js`              | ~392  | Canvas, GSAP parallax, toggle                       |
| `admin/dashboard.html` | ~450  | Admin dashboard (6 tabs, charts, inline CRUD)       |
| `admin.py`             | ~550  | Admin CRUD + analytics + site config + image upload |
| `routes.py`            | ~278  | Public + blog + SEO routes                          |
| `models.py`            | ~190  | 9 database models                                   |
| `__init__.py`          | ~148  | App factory + visitor tracking + error handlers     |
| `utils.py`             | ~200  | Sanitisation, validation, email, locale/UA          |
| `case_study.html`      | ~102  | Case study template                                 |
| `base.html`            | ~95   | Base layout + CDN scripts                           |
| `blog_detail.html`     | ~87   | Blog post template                                  |
| `blog.html`            | ~73   | Blog listing template                               |
| `config.py`            | ~69   | Configuration + production enforcement              |
