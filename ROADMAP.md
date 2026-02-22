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
- Editable site content — hero text, about bio, impact numbers editable from admin without code changes
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
- [ ] **Email notifications** — get notified when someone submits the contact form
- [ ] **Database upgrade** — migrate to PostgreSQL on Render ($0 for 90 days)
- [ ] **CI/CD pipeline** — GitHub Actions for linting, testing before deploy
- [x] **Automated backups** — daily DB export to GitHub via GitHub Actions workflow

### Integrations
- [ ] **GitHub API** — auto-fetch and display your latest repos
- [ ] **LinkedIn API** — pull recommendations or activity
- [ ] **Spotify API** — show what you're listening to (personal touch)
- [ ] **Goodreads/reading list** — show books you're reading (neuroscience, art)
- [ ] **Medium/Dev.to** — cross-post blog articles

### Security (ongoing)
- [ ] **2FA for admin panel** — TOTP-based two-factor authentication
- [ ] **Cloudflare** — free DDoS protection + CDN + SSL
- [ ] **Content Security Policy tuning** — tighten as you add features (currently allows cdnjs, jsdelivr for GSAP)
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
│   ├── models.py            # Database models (Project, Experience, Message, BlogPost, SiteConfig, PageVisit)
│   ├── routes.py            # Public routes + blog + SEO
│   ├── admin.py             # Admin panel (6-tab dashboard, analytics, site config, CRUD)
│   ├── utils.py             # Shared helpers (sanitize_input, sanitize_html, validate_email, safe_int)
│   ├── templates/           # Jinja2 HTML templates
│   │   ├── base.html        # Base layout (CDN libs, dark/light toggle)
│   │   ├── index.html       # Single-page + blog preview
│   │   ├── blog.html        # Blog listing
│   │   ├── blog_detail.html # Blog post
│   │   ├── case_study.html  # Case study
│   │   ├── sitemap.xml      # SEO sitemap
│   │   ├── feed.xml         # RSS feed
│   │   ├── errors/          # Custom error pages (400, 404, 429, 500)
│   │   ├── project_detail.html
│   │   └── admin/           # Admin panel templates (dashboard, forms)
│   └── static/
│       ├── css/style.css    # All styles (~2257 lines, dark + light themes)
│       ├── js/main.js       # All interactions (~392 lines, GSAP, dark mode, ripples)
│       └── images/          # Logo, profile photo
├── .github/workflows/
│   └── backup.yml           # Daily automated DB backup
├── config.py                # App configuration (with production enforcement)
├── run.py                   # Entry point (port 5001)
├── seed.py                  # Database seeder (5 experiences, 12 projects, 4 blog posts, 20 site configs)
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deployment config
├── .python-version          # Python version for Render
├── .env                     # Secrets (never commit!)
└── .gitignore
```

---

## 📖 Refer to
- [docSpace](https://docspace.2sirius.2.2.2) for any org-specific deployment guidance
- [LSY Security Golden Path](https://github.com/lsy-central/lsy-security-golden-path) for security workflows