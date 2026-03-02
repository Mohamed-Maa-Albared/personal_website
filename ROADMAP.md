# ROADMAP.md

Last updated: 2026-03-02

## Documentation note

Operational architecture, file map, security practices, and backup/export details now live in `MAINTAINER_GUIDE.md`.
This roadmap intentionally focuses only on forward-looking work.

## Near-term priorities

1. Localize page-level SEO/meta/schema copy for `/ar/*` pages.
2. Choose strategy for DB-backed multilingual content:
   - Option A: per-locale columns
   - Option B: translation table per model
3. Add automated browser smoke tests for RTL critical paths.
4. Evaluate locale-specific RSS feeds (`/en/feed.xml`, `/ar/feed.xml`) if needed for indexing.

## Mid-term priorities

- Add CI quality gates (lint + tests) before deploy.
- Add visual regression snapshots for homepage + nav in both locales/themes.
- Reduce SQLAlchemy `Query.get()` legacy usage to session-based access patterns.

## Backlog

- Custom domain + DNS/CDN hardening
- Optional PWA
- Optional external analytics integration
