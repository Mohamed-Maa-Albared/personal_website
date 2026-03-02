# RTL_VISUAL_SMOKE_CHECKLIST.md

## Purpose

Manual visual smoke checklist for Arabic (`/ar/...`) to catch RTL regressions quickly on desktop and mobile.

## Test matrix

- Browsers: Chrome (latest), Safari (latest)
- Viewports:
  - Desktop: 1440x900
  - Tablet: 768x1024
  - Mobile: 390x844
- Themes: Dark + Light

## Critical paths

- Home: `/ar/`
- Blog list: `/ar/blog`
- Blog detail: `/ar/blog/<slug>`
- Project detail: `/ar/project/<id>`
- Case study: `/ar/case-study/<id>` (for project with case study)
- Privacy: `/ar/privacy`

## Navigation and header

- [ ] Header stays fully visible after switching language from `/en/...` to `/ar/...`.
- [ ] Scrollbar appears on the **RIGHT** side of the screen (not left) in Arabic mode.
- [ ] Nav items remain on one line (or gracefully wrap on narrow screens) — no items hidden.
- [ ] No clipped logo, lang-toggle, theme-toggle, or CTA button in header.
- [ ] Language toggle remains clickable and routes back to equivalent `/en/...` URL.
- [ ] Mobile menu opens from the **LEFT** side (RTL-correct) and closes correctly.
- [ ] Nav link underline animation appears on the correct (right) side.

## Scroll and progress indicators

- [ ] **Top gradient scroll progress bar** is visible and fills from right-to-left as you scroll.
- [ ] No native browser scrollbar appears on the left side.
- [ ] Scroll indicator in hero section is visible and animates correctly.

## Custom cursor

- [ ] Custom cursor dot and ring are visible and follow the mouse throughout the Arabic page.
- [ ] Cursor enlarges on hover over interactive elements.
- [ ] Cursor is hidden on mobile (< 768px).

## Language switch transition

- [ ] Clicking the language button triggers the **neuro scan sweep** (a brief neural-purple/cyan light sweep across the page).
- [ ] Main content fades out during the transition.
- [ ] New page content fades in smoothly after navigation.
- [ ] Transition completes in under ~350ms and feels snappy.
- [ ] Transition works in both directions: EN→AR and AR→EN.
- [ ] In RTL, the sweep animates from right to left (mirrored).

## Typography and spacing

- [ ] Section labels (e.g., "02 — الخبرات") render as **connected Arabic letters** — NOT as isolated spaced-out letters.
- [ ] Hero label renders correctly without gaps between Arabic characters.
- [ ] Filter buttons, card categories, and blog categories display Arabic without letter-spacing artefacts.
- [ ] Section headings are right-aligned (`text-align: right`).
- [ ] Contact heading does not overflow or overlap with other elements.
- [ ] Buttons keep consistent height and padding in Arabic.
- [ ] Form labels and inputs are right-aligned and use RTL direction.

## Timeline (Experience section)

- [ ] Timeline vertical line is on the **right** side of the page.
- [ ] Timeline items are `flex-direction: row-reverse` (marker is to the right of content).
- [ ] Bullet arrows point **left** (◂), not right.
- [ ] Content text is right-aligned.
- [ ] Date, role, and company text are right-aligned.

## Projects section

- [ ] Card content (title, description, tech tags) is right-aligned.
- [ ] Tech tags flow from right to left.
- [ ] "استعرض دراسة الحالة" link arrow points left (←) on hover.
- [ ] Project filters row is right-aligned.

## Skills section

- [ ] Skill cluster tags flow from right to left.
- [ ] Cluster titles and languages bar heading are right-aligned.

## Blog cards and detail

- [ ] Blog card body (title, excerpt) is right-aligned.
- [ ] Card footer (read time + "اقرأ المقال") is `flex-direction: row-reverse`.
- [ ] "← اقرأ المقال" link arrow translates left on hover.
- [ ] Blockquotes in blog detail have the border on the **right** side.
- [ ] Ordered/unordered list items in blog content are padded on the right and right-aligned.

## Contact form

- [ ] Form labels appear on the right side of inputs.
- [ ] Input text and textarea text flow right-to-left.
- [ ] Animated input underline grows from right to left.
- [ ] Submit button is styled consistently.

## Footer

- [ ] Footer top section is `flex-direction: row-reverse` (brand on right, social links on left).
- [ ] Footer bottom text is right-aligned.
- [ ] Privacy policy link is right-aligned.

## SEO and meta

- [ ] `<html lang="ar" dir="rtl">` is present on Arabic pages.
- [ ] `<meta property="og:locale" content="ar_AR">` is present.
- [ ] `<title>` contains Arabic characters ("عالم بيانات" etc.).
- [ ] `<link rel="alternate" hreflang="en">` and `<link rel="alternate" hreflang="ar">` are both present.
- [ ] Schema.org JSON-LD has `"inLanguage": "ar_AR"` and Arabic descriptions.

## Accessibility quick checks

- [ ] Focus ring remains visible on nav links, buttons, and form controls.
- [ ] Keyboard navigation order remains logical in RTL.
- [ ] Language switch button has Arabic aria-label ("تبديل اللغة").
- [ ] ARIA live region (`#lang-announcer`) announces language change to screen readers.
- [ ] Skip links (if any) remain functional.

## Functional checks

- [ ] Contact form submits successfully on `/ar/contact` endpoint.
- [ ] Legacy URLs redirect to canonical English locale URLs (e.g., `/blog` → `/en/blog`).
- [ ] Locale switch preserves query params (e.g., category filter on blog page).
- [ ] Counter animations for stats fire correctly.
- [ ] Project category filter buttons work and show/hide cards correctly.

## Regression notes template

Use this template to log any regressions found:

```
- Date:
- Browser + viewport:
- URL:
- Theme:
- Issue summary:
- Steps to reproduce:
- Screenshot/video:
- Severity: Blocker / Major / Minor
- Related CSS class or JS function:
```

## Known fixed regressions (2026-03-02)

| Issue                                           | Root cause                                                                           | Fix                                                                              |
| ----------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| Nav header disappeared in Arabic                | `dir="rtl"` on `<html>` moved scrollbar left; `overflow-x: hidden` clipped fixed nav | `html[dir="rtl"] { direction: ltr }` + `html[dir="rtl"] body { direction: rtl }` |
| Left-side scrollbar replaced top progress bar   | Same root cause — RTL on html moves native scrollbar                                 | Same fix as above                                                                |
| Custom cursor disappeared                       | Same root cause — fixed elements clipped by overflow                                 | Same fix as above                                                                |
| Section labels had broken Arabic (letter-split) | `letter-spacing: 4px` on `.section-label` breaks Arabic ligatures                    | `letter-spacing: 0` on all letter-spaced elements in `[dir="rtl"]`               |
| Timeline marker on wrong side / wrong padding   | Missing `padding-right` swap                                                         | `[dir="rtl"] .timeline { padding-left: 0; padding-right: 40px }`                 |
| Bullet arrows pointed wrong direction           | `::before` used `left: 0` and `▸`                                                    | Changed to `right: 0` and `◂` (left-pointing triangle) for RTL                   |
| Hover animations in wrong direction             | `translateX(4px)` went wrong way                                                     | `[dir="rtl"] .blog-read-more:hover { transform: translateX(-4px) }`              |
