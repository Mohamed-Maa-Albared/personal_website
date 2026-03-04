# ROADMAP.md

Last updated: 2026-03-04

## Documentation note

Operational architecture, file map, security practices, and backup/export details now live in `MAINTAINER_GUIDE.md`.
This roadmap intentionally focuses only on forward-looking work.

## Near-term priorities

1. **Reduce SQLAlchemy legacy API warnings** — Replace `Query.get(id)` with `db.session.get(Model, id)` across `admin.py` and tests (23 warnings on every test run).
2. **Automate static asset cache-busting** — Currently the `v='20260302'` query string in `base.html` is updated manually; consider computing from file mtime or a build-time env var.
3. **Add CI quality gates** — Run `pytest` + `flake8` in a GitHub Actions workflow before every push to `main`, blocking deploys on test failures.
4. **Dependency CVE audit cadence** — Key packages (Flask, Werkzeug, Pillow, bleach) are pinned to mid-2024 versions. Establish a quarterly audit ritual using `pip-audit` or Dependabot.

## Mid-term priorities

- Add visual regression snapshots for homepage + nav in both locales/themes (light/dark × EN/AR).
- Automate `PageVisit` data retention — current purge is manual-only via admin dashboard; add a scheduled Render cron job or a `before_request` probabilistic sweep.
- Evaluate `rss_language` metadata usage consistency — `i18n.py`'s `SUPPORTED_LOCALES` already defines `rss_language` per locale; ensure all feed-rendering touches only that single source of truth.

## Backlog

- Custom domain + DNS/CDN hardening
- Optional PWA manifest + service worker
- Optional external analytics integration (Plausible / Fathom as privacy-preserving drop-in)
- Server-side rendered OG images for blog posts and case studies
