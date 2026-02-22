# 🗺️ Personal Website — Roadmap & Guide

## ✅ Current Features
- Neural network animated background
- Custom cursor with trailing ring
- Scroll-reveal animations
- Project showcase with filtering
- Experience timeline
- Contact form with honeypot spam protection
- Admin panel at `/admin` for managing all content
- Responsive design (mobile-first)
- Security hardened (CSRF, CSP, rate limiting, etc.)

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
python run.py  # test locally at http://localhost:5000
git add -A && git commit -m "your message" && git push origin main
# Render auto-deploys
```

---

## 🚀 Future Enhancements

### Content
- [ ] **Blog section** — write articles about AI, neuroscience, art
- [ ] **Case studies** — deep-dive pages for each major project with metrics
- [ ] **Testimonials** — quotes from colleagues, clients, professors
- [ ] **Downloadable CV** — PDF download button in the about section
- [ ] **Talks & Publications** — list any conferences, workshops, papers

### Design & UX
- [ ] **Dark/Light mode toggle** — with localStorage persistence
- [ ] **Page transitions** — smooth GSAP or Barba.js transitions between pages
- [ ] **Parallax scrolling** — depth layers on hero and about sections
- [ ] **3D elements** — Three.js brain visualization (neuroscience theme)
- [ ] **Micro-interactions** — button ripples, hover particles, scroll progress bar
- [ ] **Loading skeleton screens** — instead of spinner for perceived speed
- [ ] **Lottie animations** — lightweight animated illustrations

### Technical
- [ ] **Custom domain** — buy from Namecheap/Cloudflare (~$10/year), point to Render
- [ ] **Analytics** — add Plausible (privacy-friendly, free self-hosted) or Umami
- [ ] **SEO optimization** — Open Graph meta tags, sitemap.xml, robots.txt
- [ ] **RSS feed** — for blog posts
- [ ] **Image optimization** — WebP format, lazy loading, CDN (Cloudflare free tier)
- [ ] **Progressive Web App (PWA)** — offline support, installable on mobile
- [ ] **Email notifications** — get notified when someone submits the contact form
- [ ] **Database upgrade** — migrate to PostgreSQL on Render ($0 for 90 days)
- [ ] **CI/CD pipeline** — GitHub Actions for linting, testing before deploy
- [ ] **Automated backups** — scheduled DB export to GitHub or cloud storage

### Integrations
- [ ] **GitHub API** — auto-fetch and display your latest repos
- [ ] **LinkedIn API** — pull recommendations or activity
- [ ] **Spotify API** — show what you're listening to (personal touch)
- [ ] **Goodreads/reading list** — show books you're reading (neuroscience, art)
- [ ] **Medium/Dev.to** — cross-post blog articles

### Security (ongoing)
- [ ] **2FA for admin panel** — TOTP-based two-factor authentication
- [ ] **Cloudflare** — free DDoS protection + CDN + SSL
- [ ] **Content Security Policy tuning** — tighten as you add features
- [ ] **Dependency scanning** — GitHub Dependabot or Snyk
- [ ] Review [LSY Security Golden Path](https://github.com/lsy-central/lsy-security-golden-path) for updates

### Performance
- [ ] **Minify CSS/JS** — Flask-Assets or build step
- [ ] **Gzip compression** — Flask-Compress (already in requirements)
- [ ] **Cache headers** — static assets with long cache TTL
- [ ] **Lighthouse audit** — aim for 90+ on all categories

---

## 💰 Cost Summary

| Item | Cost |
|---|---|
| Render hosting (free tier) | $0/month |
| Custom domain (optional) | ~$10/year |
| Cloudflare DNS + CDN (optional) | $0 |
| **Total** | **$0 – $10/year** |

---

## 📁 Project Structure
```
personal_website/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes/
│   │   ├── main.py          # Public routes
│   │   ├── admin.py         # Admin panel
│   │   └── api.py           # REST API
│   ├── templates/           # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── admin/           # Admin panel templates
│   │   └── project_detail.html
│   └── static/
│       ├── css/style.css    # All styles
│       ├── js/main.js       # All interactions
│       └── images/          # Logo, profile photo, project images
├── config.py                # App configuration
├── run.py                   # Entry point
├── seed.py                  # Database seeder
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