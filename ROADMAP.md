# 🗺️ Personal Website — Roadmap & Guide

## ✅ Current Features
- Neural network animated background (80-node particle canvas with mouse-reactive connections)
- Custom cursor with dot + ring (dark purple/dark navy per theme, hidden on mobile)
- Dark/Light mode toggle with localStorage persistence
- GSAP ScrollTrigger animations (hero parallax fade, timeline marker dots)
- Scroll progress bar
- Scroll-reveal animations
- Project showcase with filtering
- Case studies — deep-dive pages for featured projects with metrics
- Blog section with 4 articles (AI, neuroscience, art, recommendation systems)
- Blog listing with category filtering + blog preview on homepage
- Experience timeline
- Contact form with honeypot spam protection
- Admin panel at `/admin` with 6-tab dashboard (Analytics, Site Content, Projects, Experience, Blog, Messages)
- Visitor analytics — page views, top pages, referrers, locales, unique visitors (privacy-safe: IPs hashed)
- Editable site content — hero text, about bio editable from admin without code changes
- Dynamic impact cards — add/edit/delete impact metrics from admin panel
- Dynamic skill clusters — manage skills & capabilities from admin (no HTML needed)
- Dynamic language items — manage spoken languages from admin
- Rich text toolbar — format blog content (bold, italic, headings, links, images) without writing HTML
- HTML/Visual toggle — switch between WYSIWYG visual editor and raw HTML source in blog editor
- Local image upload — upload blog cover images from your computer (stored in static/uploads/)
- Enhanced analytics — daily visits chart (Chart.js), browser/device/OS breakdown, bounce rate, avg pages per visit, readable locale names
- Email notifications — automatic email when someone submits the contact form (smtplib, configurable via env vars)
- Email diagnostics — config status panel in admin dashboard, test email button with SMTP error feedback
- SEO: Open Graph meta tags, sitemap.xml, robots.txt, RSS feed
- Skeleton loading screens for images
- Button ripple micro-interactions
- Responsive design (mobile-first)
- Security hardened (CSRF, CSP, rate limiting, input sanitisation, production enforcement, custom error pages, structured logging)
- Automated daily DB backup via GitHub Actions

---

## 🔧 How to Make Changes

### Edit content from the browser
1. Go to `https://your-site.onrender.com/admin`
2. Log in with your admin password
3. Add/edit/delete projects, experiences, and read messages

### Edit code locally
```bash
cd ~/Documents/Python_Projects/personal_website
source venv/bin/activate
# make changes
python run.py  # test locally at http://localhost:5001
git add -A && git commit -m "your message" && git push origin main
# Render auto-deploys
```

---

## 🚀 Future Enhancements

### Content
- [x] **Blog section** — 4 researched articles on AI, neuroscience, art, and recommendation systems
- [x] **Case studies** — deep-dive pages for 3 major projects with metrics
- [ ] **Testimonials** — quotes from colleagues, clients, professors
- [ ] **Downloadable CV** — PDF download button in the about section
- [ ] **Talks & Publications** — list any conferences, workshops, papers

### Design & UX
- [x] **Dark/Light mode toggle** — with localStorage persistence
- [x] **Page transitions** — GSAP ScrollTrigger animations between sections
- [x] **Parallax scrolling** — hero content fades/translates on scroll via GSAP
- [x] **Micro-interactions** — button ripples, scroll progress bar, custom cursor in both themes
- [x] **Loading skeleton screens** — shimmer animation for blog card images
- [ ] **Lottie animations** — lightweight animated illustrations

### Technical
- [ ] **Custom domain** — buy from Namecheap/Cloudflare (~$10/year), point to Render
- [ ] **Analytics** — add Plausible (privacy-friendly, free self-hosted) or Umami for external analytics (built-in lightweight analytics already implemented)
- [x] **SEO optimization** — Open Graph meta tags, sitemap.xml, robots.txt
- [x] **RSS feed** — for blog posts at `/feed.xml`
- [ ] **Image optimization** — WebP format, lazy loading, CDN (Cloudflare free tier)
- [ ] **Progressive Web App (PWA)** — offline support, installable on mobile
- [x] **Email notifications** — get notified when someone submits the contact form
- [x] **Database upgrade** — PostgreSQL on Render for production (psycopg2-binary driver)
- [ ] **CI/CD pipeline** — GitHub Actions for linting, testing before deploy
- [x] **Automated backups** — daily PostgreSQL backup to GitHub via pg_dump (GitHub Actions)

### Integrations
- [ ] **GitHub API** — auto-fetch and display your latest repos
- [ ] **LinkedIn API** — pull recommendations or activity
- [ ] **Spotify API** — show what you're listening to (personal touch)
- [ ] **Goodreads/reading list** — show books you're reading (neuroscience, art)
- [ ] **Medium/Dev.to** — cross-post blog articles

### Security (ongoing)
- [x] **HMAC-salted IP hashing** — visitor IPs hashed with SECRET_KEY via HMAC-SHA256 (not rainbow-tableable)
- [x] **Hardened file uploads** — extension + MIME + Pillow magic-byte validation, SVG blocked, rate-limited
- [x] **Login lockout** — exponential backoff after 5 failed login attempts (10-minute cooldown)
- [x] **Audit logging** — all admin CRUD operations logged with context
- [x] **SRI integrity hashes** — GSAP, ScrollTrigger, and Chart.js CDN scripts verified with SHA-384
- [x] **CSP hardened** — added `base-uri`, `form-action` directives
- [x] **Privacy policy** — transparent data collection disclosure at `/privacy`
- [x] **Data retention** — admin can purge analytics older than 90 days
- [x] **Comprehensive test suite** — 70 pytest tests covering routes, admin, utils, and security
- [ ] **2FA for admin panel** — TOTP-based two-factor authentication
- [ ] **Cloudflare** — free DDoS protection + CDN + SSL
- [ ] **Dependency scanning** — GitHub Dependabot or Snyk
- [ ] Review [LSY Security Golden Path](https://github.com/lsy-central/lsy-security-golden-path) for updates

### Performance
- [ ] **Minify CSS/JS** — Flask-Assets or build step
- [ ] **Gzip compression** — Flask-Compress (already in requirements)
- [ ] **Cache headers** — static assets with long cache TTL
- [ ] **Lighthouse audit** — aim for 90+ on all categories

---

## 💰 Cost Summary

| Item                            | Cost              |
| ------------------------------- | ----------------- |
| Render hosting (free tier)      | $0/month          |
| Custom domain (optional)        | ~$10/year         |
| Cloudflare DNS + CDN (optional) | $0                |
| **Total**                       | **$0 – $10/year** |

---

## 📁 Project Structure
```
personal_website/
├── app/
│   ├── __init__.py          # Flask app factory, visitor tracking, error handlers
│   ├── models.py            # Database models (Project, Experience, Message, BlogPost, SiteConfig, PageVisit, ImpactCard, SkillCluster, LanguageItem)
│   ├── routes.py            # Public routes + blog + SEO
│   ├── admin.py             # Admin panel (6-tab dashboard, analytics, email diagnostics, site config, CRUD)
│   ├── utils.py             # Shared helpers (sanitize, validate, email notifications with diagnostics, locale/UA parsing)
│   ├── templates/           # Jinja2 HTML templates
│   │   ├── base.html        # Base layout (CDN libs with SRI, dark/light toggle)
│   │   ├── index.html       # Single-page + blog preview
│   │   ├── blog.html        # Blog listing
│   │   ├── blog_detail.html # Blog post
│   │   ├── case_study.html  # Case study
│   │   ├── privacy.html     # Privacy policy
│   │   ├── sitemap.xml      # SEO sitemap
│   │   ├── feed.xml         # RSS feed
│   │   ├── errors/          # Custom error pages (400, 404, 429, 500)
│   │   ├── project_detail.html
│   │   └── admin/           # Admin panel templates (dashboard, forms)
│   └── static/
│       ├── css/style.css    # All styles (~2312 lines, dark + light themes)
│       ├── js/main.js       # All interactions (~403 lines, GSAP, dark mode, ripples)
│       ├── js/admin.js      # Admin UI (~480 lines, WYSIWYG + HTML toggle, upload, charts)
│       ├── images/          # Logo, profile photo
│       └── uploads/         # User-uploaded blog images
├── .github/workflows/
│   └── backup.yml           # Daily automated PostgreSQL backup via pg_dump
├── config.py                # App configuration (with production enforcement)
├── run.py                   # Entry point (port 5001)
├── seed.py                  # Database seeder (5 experiences, 12 projects, 4 blog posts, site configs, 4 impact cards, 4 skill clusters, 3 languages)
├── requirements.txt         # Python dependencies
├── requirements-dev.txt     # Dev/test dependencies (pytest, black, flake8)
├── tests/                   # Pytest test suite (70 tests)
│   ├── conftest.py          # Fixtures (app, client, auth_client, sample data)
│   ├── test_routes.py       # Public route tests
│   ├── test_admin.py        # Admin CRUD + security tests
│   └── test_utils.py        # Utility function tests
├── render.yaml              # Render deployment config
├── .python-version          # Python version for Render
├── .env                     # Secrets (never commit!)
└── .gitignore
```

---

## 📖 Refer to
- [docSpace](https://docspace.2sirius.2.2.2) for any org-specific deployment guidance
- [LSY Security Golden Path](https://github.com/lsy-central/lsy-security-golden-path) for security workflows