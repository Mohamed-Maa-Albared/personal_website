# Personal Portfolio Website

Modern, immersive portfolio for **Mohamed Maa Albared** — Data Scientist at zeroG (Lufthansa Group). Built with Flask, styled with a dark neural/neuroscience aesthetic (deep navy + electric purple/cyan).

**Live:** <https://mohamed-maa-albared-portfolio.onrender.com/>

---

## Features

- **Single-page layout** — Hero, About, Impact, Timeline, Projects, Skills, Blog Preview, Contact — all on one page with smooth anchor navigation
- **Dynamic timeline** — Experience section rendered from database (description + highlights), fully editable from admin
- **Dynamic projects grid** — Projects rendered from database with category filters, tech tags, and case study links
- **Blog** — Full blog system with category filtering, RSS feed, and related posts
- **Case studies** — Deep-dive project pages with challenge/approach/results/metrics
- **Admin dashboard** — Tabbed interface with six panels: Analytics, Site Content, Projects, Experience, Blog Posts, Messages
- **Visitor analytics** — Lightweight page-view tracking with top pages, referrers, locales, and unique visitor counts
- **Editable site content** — Hero text, about bio, impact numbers, and more — all editable from the admin dashboard without code changes
- **Rich text editing** — WYSIWYG toolbar with HTML toggle for blog posts and case studies
- **Admin tab persistence** — Cancel/back links and post-save redirects return to the correct tab
- **Dark / light mode** — Toggle with `localStorage` persistence, CSS variable theming
- **Neural canvas** — Animated particle network in the hero section (80 nodes, mouse-reactive)
- **GSAP animations** — Hero parallax fade, timeline marker dot scaling via ScrollTrigger
- **Custom cursor** — Dot + ring, visible in both themes (purple / dark navy)
- **SEO** — Sitemap, robots.txt, Open Graph tags, RSS feed
- **Security hardened** — CSP, CSRF, rate limiting, input sanitisation, session expiry, custom error pages
- **Automated backups** — GitHub Actions workflow for daily DB backup

## Tech Stack

| Layer      | Technology                                                |
| ---------- | --------------------------------------------------------- |
| Backend    | Flask 3.0.0, Flask-SQLAlchemy 3.1.1                       |
| Security   | Flask-WTF 1.2.1 (CSRF), Flask-Limiter 3.5.0, bleach 6.1.0 |
| WSGI       | gunicorn 21.2.0                                           |
| Database   | SQLite (dev), PostgreSQL (prod)                           |
| Frontend   | Vanilla HTML / CSS / JS (no frameworks)                   |
| Animation  | GSAP 3.12.2 + ScrollTrigger (CDN)                         |
| Fonts      | Google Fonts — Space Grotesk, Inter, JetBrains Mono       |
| Deployment | Render (free tier)                                        |
| Python     | 3.11.x                                                    |

## Project Structure

```
personal_website/
├── app/
│   ├── __init__.py              # App factory, extensions, security headers, error handlers, visitor tracking
│   ├── models.py                # SQLAlchemy models: Project, Experience, Message, BlogPost, SiteConfig, PageVisit, ImpactCard, SkillCluster, LanguageItem
│   ├── routes.py                # Public routes: index, blog, case_study, sitemap, robots, rss, contact, api
│   ├── admin.py                 # Admin blueprint: CRUD, analytics dashboard, email diagnostics, site config editor
│   ├── utils.py                 # Shared helpers: sanitize_input, sanitize_html, validate_email, safe_int, generate_slug
│   ├── templates/
│   │   ├── base.html            # Base layout (CDN libs, theme toggle, nav, scroll bar)
│   │   ├── index.html           # Dynamic single-page: Jinja2 loops for experiences & projects + blog preview
│   │   ├── project_detail.html  # Individual project page
│   │   ├── blog.html            # Blog listing with category filtering
│   │   ├── blog_detail.html     # Individual blog post (OG tags, author card, related posts)
│   │   ├── case_study.html      # Deep-dive case study (challenge / approach / results / metrics)
│   │   ├── sitemap.xml          # SEO sitemap template
│   │   ├── feed.xml             # RSS feed template
│   │   ├── errors/              # Custom error pages (400, 404, 429, 500)
│   │   └── admin/
│   │       ├── base.html        # Admin layout
│   │       ├── login.html       # Admin login
│   │       ├── dashboard.html   # Admin dashboard (6 tabs: Analytics, Site Content, Projects, Experience, Blog, Messages)
│   │       ├── project_form.html
│   │       ├── experience_form.html
│   │       ├── blog_form.html
│   │       ├── case_study_form.html
│   │       └── message_detail.html
│   └── static/
│       ├── css/style.css        # All styles (~2319 lines, dark + light themes)
│       ├── js/main.js           # Neural canvas, GSAP, cursor, reveals, contact AJAX (~403 lines)
│       ├── js/admin.js          # Rich text + HTML toggle, image upload, Chart.js (~480 lines)
│       └── images/              # logo.png, profile.png
├── .github/workflows/backup.yml # Daily automated DB backup to GitHub
├── config.py                    # Dev / Prod / Test configs with production enforcement
├── run.py                       # Entry point (default port 5001)
├── seed.py                      # Seeds DB with experiences, projects, blog posts, site config, impact cards, skill clusters, languages
├── render.yaml                  # Render deployment config
├── requirements.txt             # Python dependencies
├── requirements-dev.txt         # Dev/test dependencies (pytest, black, flake8)
├── .env.example                 # Environment variable template
├── AGENTS.md                    # AI agent instructions
└── ROADMAP.md                   # Roadmap with status tracking
```

## Setup

```bash
# Clone & enter
cd personal_website

# Virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Dependencies
pip install -r requirements.txt

# Environment
cp .env.example .env            # Edit with your values

# Seed database
python seed.py

# Run
python run.py                   # → http://localhost:5001
```

## Environment Variables

| Variable         | Required   | Description                                 |
| ---------------- | ---------- | ------------------------------------------- |
| `FLASK_ENV`      | Yes        | `development` or `production`               |
| `SECRET_KEY`     | Yes (prod) | Random 32+ char string for session signing  |
| `DATABASE_URL`   | No         | Defaults to `sqlite:///personal_website.db` |
| `ADMIN_PASSWORD` | Yes        | Password for `/admin` login                 |

> **Production enforcement:** The app refuses to start in production if `SECRET_KEY` or `ADMIN_PASSWORD` are missing or set to defaults.

## Routes

### Public

| Route              | Method | Description                             |
| ------------------ | ------ | --------------------------------------- |
| `/`                | GET    | Single-page index                       |
| `/project/<id>`    | GET    | Project detail page                     |
| `/case-study/<id>` | GET    | Deep-dive case study                    |
| `/blog`            | GET    | Blog listing (`?category=` filter)      |
| `/blog/<slug>`     | GET    | Individual blog post                    |
| `/contact`         | POST   | Contact form (JSON, rate-limited 3/min) |
| `/api/projects`    | GET    | JSON API for projects                   |
| `/sitemap.xml`     | GET    | Auto-generated XML sitemap              |
| `/robots.txt`      | GET    | SEO robots file                         |
| `/feed.xml`        | GET    | RSS feed for blog posts                 |

### Admin (session-authenticated)

| Route                              | Method   | Description                 |
| ---------------------------------- | -------- | --------------------------- |
| `/admin/login`                     | GET/POST | Login (rate-limited 5/min)  |
| `/admin/`                          | GET      | Dashboard (tabbed)          |
| `/admin/site-config`               | POST     | Update site content         |
| `/admin/project/new\|<id>/edit`    | GET/POST | Project CRUD                |
| `/admin/experience/new\|<id>/edit` | GET/POST | Experience CRUD             |
| `/admin/blog/new\|<id>/edit`       | GET/POST | Blog post CRUD              |
| `/admin/project/<id>/case-study`   | GET/POST | Case study editor (WYSIWYG) |
| `/admin/message/<id>`              | GET      | View contact message        |

## Database Models

### Project
`title`, `description`, `short_description`, `image_url`, `demo_url`, `github_url`, `technologies` (comma-sep), `category`, `year`, `client`, `featured`, `sort_order`, `case_study`, `metrics` (JSON), `challenge`, `approach`, `results`, `has_case_study`

### Experience
`role`, `company`, `location`, `date_range`, `description`, `highlights` (JSON), `sort_order`

### Message
`name`, `email`, `subject`, `message`, `is_read`, `created_at`

### BlogPost
`title`, `slug` (unique), `excerpt`, `content` (HTML), `cover_image`, `category`, `tags` (comma-sep), `read_time`, `published`, `featured`, `created_at`, `updated_at`, `sort_order`

### SiteConfig
`key` (unique, indexed), `value`, `label`, `group` — Key-value store for editable homepage content (hero, about, impact). Static helpers: `get(key)`, `set(key, value)`, `get_group(group)`

### PageVisit
`path`, `referrer`, `user_agent`, `ip_hash` (SHA-256, no raw IPs), `country` (from Accept-Language), `visited_at` (indexed) — Lightweight visitor analytics

### ImpactCard
`icon`, `value`, `prefix`, `suffix`, `description`, `sort_order` — Dynamic impact metrics on homepage

### SkillCluster
`icon`, `title`, `tags` (comma-sep), `sort_order` — Skill categories on homepage

### LanguageItem
`name`, `level`, `sort_order` — Spoken languages on homepage

## Security

| Measure                | Detail                                                                          |
| ---------------------- | ------------------------------------------------------------------------------- |
| CSRF Protection        | `CSRFProtect()` on all forms; `/contact` exempt (JSON + honeypot)               |
| Rate Limiting          | Global 200/min; login 5/min; contact 3/min                                      |
| Input Sanitisation     | `sanitize_input()` strips all HTML; `sanitize_html()` allowlists safe tags      |
| Password Comparison    | `hmac.compare_digest()` (timing-safe)                                           |
| CSP                    | Strict Content-Security-Policy header                                           |
| Security Headers       | X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy    |
| HSTS                   | Enabled in production (`max-age=31536000; includeSubDomains`)                   |
| Session Hardening      | HttpOnly, SameSite=Lax, Secure (prod), 2-hour expiry                            |
| Custom Error Pages     | 400, 404, 429, 500 — no Flask internals leaked                                  |
| Production Enforcement | App refuses to start with default `SECRET_KEY` or `ADMIN_PASSWORD`              |
| Structured Logging     | Security events (login attempts, contact submissions) logged with context       |
| Privacy-safe Analytics | Visitor IPs are HMAC-SHA256 hashed with SECRET_KEY — no raw IP addresses stored |

## Deployment

Deployed on [Render](https://render.com) — see `render.yaml`:

- **Build:** `pip install -r requirements.txt && python seed.py`
- **Start:** `gunicorn run:app --bind 0.0.0.0:$PORT --workers 2`
- Auto-deploys on `git push origin main`


## Testing

```bash
python -c "
from app import create_app
app = create_app('development')
with app.test_client() as c:
    routes = [
        ('Index', '/'),
        ('Admin login', '/admin/login'),
        ('Blog', '/blog'),
        ('Sitemap', '/sitemap.xml'),
        ('Robots', '/robots.txt'),
        ('RSS', '/feed.xml'),
        ('404 page', '/nonexistent'),
    ]
    for name, path in routes:
        r = c.get(path)
        status = '✓' if r.status_code in (200, 302, 404) else '✗'
        print(f'  {status} {name}: {r.status_code}')
"
```

## License

MIT License — feel free to use this as a starting point for your own portfolio.
