# Tech Stack – curated.guide

This document is the single source of truth for technologies.
**AI agents / future contributors: Follow these rules religiously. No exceptions.**

---

## Core Principles (non-negotiable)

- **Solo-founder forever** → stack must be simple, fast, cheap, and executable by one person.
- **No bloat** → if we can solve it without a new dependency, we do.
- **Beauty & performance first** → everything must feel instant and look tasteful.
- **No Docker unless absolutely necessary** → keep development simple and fast.

---

## Backend

**Framework:** Django (latest stable)
**Why:** Battle-tested, batteries-included, perfect for solo dev. Ships with admin, ORM, auth foundation, migrations.

**Key Libraries:**
- `django-htmx` → server-side interactivity, no heavy JS framework needed
- `django-allauth` → auth (social + email), production-ready
- `django-anymail` → email sending (works with any provider)
- `django-ninja` → if REST API needed (faster than DRF, simpler)
- `django-filters` → if filtering guides/items needed

**Database:**
- **Local:** SQLite3 (zero config, fast iteration)
- **Production:** PostgreSQL (robust, full-text search, JSON fields if needed)

**Deployment:** TBD (likely Railway, Render, or DigitalOcean App Platform)

---

## Frontend

**Approach:** Server-rendered HTML + HTMX + minimal vanilla JS
**Why:** No build step, no hydration, instant page loads, SEO perfect by default.

**Styling:**
- Pure CSS Modules (semantic class names)
- All tokens in `globals.css` (colors, spacing, radius)
- **No Tailwind** (keeps us disciplined, no class soup)

**Interactivity:**
- HTMX for live updates (add item, edit guide, toggle privacy)
- Vanilla JS only when truly needed (copy to clipboard, image upload preview)

---

## Payments

**Provider:** Stripe
**Integration:** Stripe Checkout + Customer Portal (no custom billing UI)
**Pricing:** Single plan ($5/month or $48/year), 14-day trial via Stripe

---

## Email

**Library:** django-anymail
**Provider:** TBD (Resend, SendGrid, or Mailgun based on pricing/deliverability)
**Use cases:** Welcome, trial ending, payment receipt, password reset

---

## File Storage

**Local/Dev:** Django default (MEDIA_ROOT)
**Production:** TBD (likely Cloudflare R2 or DigitalOcean Spaces – S3-compatible, cheaper than AWS)

---

## Analytics & Monitoring

**Product Analytics:** PostHog (cloud, 1M events free)
**Performance:** Vercel Analytics or built-in server timing
**Errors:** Sentry (free tier)
**Search Console:** Google (organic traffic tracking)

---

## Development Workflow

**Local Setup:**
1. Clone repo
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`

**No Docker** unless we hit a wall (keeps onboarding instant).

**Version Control:** Git + GitHub
**CI/CD:** GitHub Actions (run tests + deploy on push to main)

---

## Forbidden Technologies

❌ No React/Next.js/Vue (HTMX is enough)
❌ No Tailwind (we use CSS Modules + tokens)
❌ No complex GraphQL (django-ninja REST if needed)
❌ No microservices (monolith forever)
❌ No Docker in dev (unless absolutely necessary)

---

## Future Considerations (only if needed)

- Full-text search → PostgreSQL built-in or Meilisearch (lightweight)
- Image optimization → Cloudflare Images or sharp.js via minimal Node script
- Custom domain DNS → Cloudflare API
- Rate limiting → django-ratelimit

---

## The Rule

> **"Pick boring technology. Ship fast. Stay solo."** 
