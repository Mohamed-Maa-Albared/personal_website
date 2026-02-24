# AGENTS.md — AI Agent Instructions for personal_website

> Last updated: 2026-02-24

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
| Image Processing   | Pillow                                              | 10.4.0  |
| WSGI Server        | gunicorn                                            | 21.2.0  |
| Database (dev)     | SQLite                                              | —       |
| Database (prod)    | PostgreSQL (via psycopg2-binary)                    | 18.x    |
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
│   ├── admin.py                 # Admin blueprint: CRUD, analytics dashboard, email diagnostics, site config, login lockout
│   ├── utils.py                 # Shared helpers: sanitize, validate, email notifications (with diagnostics), locale/UA parsing, generate_slug
│   ├── templates/
│   │   ├── base.html            # Base layout (CDN libs, dark/light toggle, scroll progress bar, nav)
│   │   ├── index.html           # Single-page: Hero, About, Impact, Timeline (dynamic), Projects (dynamic), Skills, Blog Preview, Contact
│   │   ├── project_detail.html  # Individual project detail page
│   │   ├── blog.html            # Blog listing with category filtering
│   │   ├── blog_detail.html     # Individual blog post (OG tags, author card, related posts)
│   │   ├── case_study.html      # Deep-dive case study (challenge/approach/results/metrics)
│   │   ├── privacy.html         # Privacy policy page
│   │   ├── sitemap.xml          # SEO sitemap template
│   │   ├── feed.xml             # RSS feed template
│   │   ├── errors/              # Custom error pages (400, 404, 429, 500)
│   │   └── admin/
│   │       ├── base.html        # Admin layout + tab/config CSS
│   │       ├── login.html       # Admin login form
│   │       ├── dashboard.html   # Admin dashboard (6 tabs: Analytics, Site Content, Projects, Experience, Blog, Messages)
│   │       ├── project_form.html      # Create/edit project form (URL fields are text, not url-validated)
│   │       ├── experience_form.html   # Create/edit experience form
│   │       ├── blog_form.html         # Create/edit blog post form (WYSIWYG toolbar)
│   │       ├── case_study_form.html   # Edit case study for a project (WYSIWYG toolbar)
│   │       └── message_detail.html    # View contact message
│   └── static/
│       ├── css/style.css        # ~2319 lines, dark/light themes, blog, case study, skeleton screens
│       ├── js/
│       │   ├── main.js          # ~403 lines: neural canvas, GSAP parallax, dark mode, ripples
│       │   └── admin.js         # ~480 lines: rich text toolbar + HTML toggle, image upload, Chart.js init
│       ├── images/
│       │   ├── logo.png         # Site logo
│       │   └── profile.png      # Profile photo
│       └── uploads/             # User-uploaded blog images (.gitkeep)
├── tests/
│   ├── conftest.py              # Pytest fixtures (app, client, auth_client, sample data)
│   ├── test_routes.py           # Public route + SEO tests
│   ├── test_admin.py            # Admin CRUD + security tests
│   └── test_utils.py            # Utility function tests
├── .github/
│   └── workflows/
│       └── backup.yml           # Automated daily PostgreSQL backup via pg_dump to GitHub
├── config.py                    # Config classes: Development, Production, Testing (with production enforcement)
├── run.py                       # Entry point, shell context (default port 5001)
├── seed.py                      # Seeds DB: experiences, projects, blog posts, site configs, impact cards, skill clusters, languages
├── requirements.txt             # Python dependencies
├── requirements-dev.txt         # Dev/test dependencies (pytest, black, flake8)
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
- `/privacy` — Privacy policy page
- `/api/projects` (GET) — JSON API for projects
- `/sitemap.xml` — Auto-generated XML sitemap
- `/robots.txt` — SEO robots file (disallows `/admin/`)
- `/feed.xml` — RSS feed for blog posts
- `/admin/` — Dashboard with 6 tabs: Analytics, Site Content, Projects, Experience, Blog, Messages
- `/admin/login` (GET/POST) — Login (rate-limited 5/min, lockout after 5 failures)
- `/admin/logout` (GET) — Logout and clear session
- `/admin/test-email` (POST) — Send test email with diagnostic flash messages
- `/admin/site-config` (POST) — Update editable site content (hero, about)
- `/admin/purge-analytics` (POST) — Delete analytics data older than 90 days
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
- **Dynamic experience timeline** — rendered from database via Jinja2 loop over `experiences`; description + highlights displayed per entry
- **Dynamic projects grid** — rendered from database via Jinja2 loop over `all_projects`; category filters, tech tags, and case study links generated automatically
- **Neural canvas** — animated particle network in hero section (80 nodes, vanilla Canvas API, mouse-reactive connections)
- **Dark/Light mode** — toggle button in nav, persisted via `localStorage`, CSS variables swap via `[data-theme="light"]`
- **GSAP ScrollTrigger** — hero parallax fade, timeline marker dot scale animations
- **Custom cursor** — dot + ring, dark purple in dark mode, dark navy in light mode, hidden on mobile
- **Scroll reveals** — IntersectionObserver-based `.reveal-up` class for all sections, cards, labels
- **Scroll progress bar** — fixed gradient bar at top tracking page scroll
- **Project filters** — client-side category filtering with animated transitions
- **Counter animations** — count-up effect for impact numbers
- **Blog preview** — latest 3 posts section on index page
- **Skeleton screens** — shimmer loading animation for blog card images
- **Button ripple effect** — click micro-interaction on all buttons
- **Contact form** — AJAX POST with honeypot spam field, client-side validation
- **Rich text toolbar** — admin blog editor and case study editor toolbar (bold, italic, headings, links, images, lists) — no HTML typing needed
- **HTML/Visual toggle** — switch between WYSIWYG visual editor and raw HTML source in blog and case study editors
- **Chart.js analytics** — daily visits line chart, browser/device doughnut charts in admin dashboard
- **Email diagnostics** — email config status panel in admin dashboard, test email button with error feedback
- **Dual email providers** — Resend HTTP API (recommended for Render free tier) with SMTP fallback
- **Image upload** — local file upload for blog cover images (stored in static/uploads/, validated with extension + MIME + Pillow magic bytes)
- **Admin tab persistence** — cancel/back links and post-CRUD redirects include `#tab-*` URL hashes so users return to the correct tab

---

## Security Stack

All security measures are already implemented. Do not remove or weaken them.

| Measure                 | Location                    | Details                                                                                   |
| ----------------------- | --------------------------- | ----------------------------------------------------------------------------------------- |
| CSRF Protection         | `app/__init__.py`           | `CSRFProtect()` on all forms; `/contact` is `@csrf.exempt` (JSON endpoint)                |
| Rate Limiting           | `app/__init__.py`           | Global 200/min; login 5/min; contact 3/min                                                |
| Input Sanitization      | `utils.py`, `admin.py`      | `sanitize_input()` strips HTML; `sanitize_html()` allowlists safe tags                    |
| Password Comparison     | `admin.py`                  | `hmac.compare_digest()` (timing-safe)                                                     |
| Login Lockout           | `admin.py`                  | Exponential backoff after 5 failed attempts (10-minute cooldown)                          |
| Content Security Policy | `app/__init__.py`           | Full CSP header with `base-uri`, `form-action` directives                                 |
| SRI Integrity Hashes    | `base.html`                 | GSAP + ScrollTrigger CDN scripts verified with SHA-384                                    |
| Security Headers        | `app/__init__.py`           | X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy, HSTS (prod) |
| Session Security        | `config.py`                 | `HTTPONLY=True`, `SAMESITE=Lax`, `SECURE=True` (prod), 2-hour expiry                      |
| Honeypot                | `index.html`, `routes.py`   | Hidden `website` field to catch bots                                                      |
| CSRF Tokens             | All admin templates         | `<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">` in every POST form   |
| Custom Error Pages      | `app/templates/errors/`     | 400, 404, 429, 500 — no Flask internals leaked                                            |
| Production Enforcement  | `config.py`                 | App refuses to start with default `SECRET_KEY` or `ADMIN_PASSWORD`                        |
| Structured Logging      | `app/__init__.py`           | Security events (login attempts, contact submissions) logged with context                 |
| Audit Logging           | `admin.py`                  | All admin CRUD operations logged with user context                                        |
| Privacy-safe Analytics  | `app/__init__.py`           | Visitor IPs HMAC-SHA256 hashed with SECRET_KEY — not rainbow-tableable                    |
| Data Retention          | `admin.py`                  | Admin can purge analytics older than 90 days via `/admin/purge-analytics`                 |
| Hardened File Uploads   | `admin.py`                  | Extension + MIME + Pillow magic-byte validation, SVG blocked, rate-limited                |
| Privacy Policy          | `routes.py`, `privacy.html` | Transparent data collection disclosure at `/privacy`                                      |

---

## Environment Variables

Defined in `.env` (never committed). See `.env.example` for template.

| Variable             | Required   | Description                                                  |
| -------------------- | ---------- | ------------------------------------------------------------ |
| `FLASK_ENV`          | Yes        | `development` or `production`                                |
| `SECRET_KEY`         | Yes (prod) | Random 32+ char string for session signing                   |
| `DATABASE_URL`       | No         | Defaults to `sqlite:///personal_website.db`                  |
| `ADMIN_PASSWORD`     | Yes        | Password for `/admin` login                                  |
| `RESEND_API_KEY`     | No*        | Resend HTTP email API key (recommended for Render)           |
| `RESEND_FROM`        | No         | Sender address for Resend (default: `onboarding@resend.dev`) |
| `NOTIFICATION_EMAIL` | No*        | Address to receive contact form notifications                |
| `MAIL_SERVER`        | No         | SMTP host (fallback if Resend not set)                       |
| `MAIL_PORT`          | No         | SMTP port (default 587)                                      |
| `MAIL_USERNAME`      | No         | SMTP login username                                          |
| `MAIL_PASSWORD`      | No         | SMTP login password / app password                           |

*Set `RESEND_API_KEY` + `NOTIFICATION_EMAIL` for email on Render free tier (SMTP ports are blocked).

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
- **SQLite for dev, PostgreSQL for prod** — SQLite locally, psycopg2-binary + Render PostgreSQL in production
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

85 pytest tests covering routes, admin CRUD, security, and utility functions.

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/ -v

# Quick smoke test
python -m pytest tests/ -q
```

Test files:
- `tests/conftest.py` — Fixtures: app factory, test client, authenticated client, sample data
- `tests/test_routes.py` — Public routes, blog, SEO endpoints, contact form
- `tests/test_admin.py` — Admin login/lockout, CRUD operations, file upload, security
- `tests/test_utils.py` — Sanitization, validation, email helpers, locale/UA parsing

---

## File Sizes (approximate)

| File                   | Lines | Purpose                                                     |
| ---------------------- | ----- | ----------------------------------------------------------- |
| `style.css`            | ~2319 | All styles (dark + light themes)                            |
| `admin.py`             | ~838  | Admin CRUD + analytics + email diagnostics + image upload   |
| `admin/base.html`      | ~841  | Admin layout + tab/config CSS                               |
| `admin/dashboard.html` | ~738  | Admin dashboard (6 tabs, charts, email config, inline CRUD) |
| `seed.py`              | ~701  | Data seeder (projects, blog, site config)                   |
| `index.html`           | ~352  | Dynamic single-page (Jinja2 loops) + blog preview           |
| `utils.py`             | ~603  | Sanitisation, validation, email diagnostics, locale/UA      |
| `admin.js`             | ~480  | Rich text + HTML toggle, image upload, Chart.js             |
| `main.js`              | ~403  | Canvas, GSAP parallax, dark mode toggle                     |
| `routes.py`            | ~339  | Public + blog + privacy + SEO routes                        |
| `models.py`            | ~321  | 9 database models                                           |
| `__init__.py`          | ~150  | App factory + HMAC visitor tracking + error handlers        |
| `blog_form.html`       | ~132  | Blog editor with WYSIWYG toolbar + HTML toggle              |
| `case_study_form.html` | ~59   | Case study editor with WYSIWYG toolbar                      |
| `base.html`            | ~99   | Base layout + CDN scripts with SRI                          |
| `blog_detail.html`     | ~87   | Blog post template                                          |
| `config.py`            | ~82   | Configuration + production enforcement                      |
| `blog.html`            | ~73   | Blog listing template                                       |
