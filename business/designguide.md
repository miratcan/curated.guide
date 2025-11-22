# curated.guide – Design Guide

This document is the single source of truth for all visual decisions.  
Every pixel must serve **[ZEN-PROUD]** – the guide must feel like something the creator is proud to put their name on.

---

## 1. Core Philosophy (new – must read first)

We are ultra-minimal, calm, and tasteful.  
Think: Are.na + Notion + Pinterest’s quiet elegance.  

No decoration for decoration’s sake.  
Whitespace is our most powerful tool.  
Beauty comes from perfect typography, generous spacing, and subtle warmth – never from loud colors or effects.

If something doesn’t make the guide feel more “owned” or more shareable, kill it.

---

## 2. Color Palette (simplified & warmed for pride)

We keep the warm neutrals (they work perfectly), but make the accent softer and more elegant.

### Base
- **Page background:** `#FDFCFB` → token: `--color-bg`  
  (slightly warmer than pure white, feels like thick paper)
- **Surface / card background:** `#FFFFFF` → token: `--color-surface`
- **Soft alternate surface:** `#FAF8F5` → token: `--color-soft-surface` (for hover states, subtle separation)

### Borders & Dividers
- **Default border:** `#E8E2DB` → token: `--color-border`  
  (warm gray, never cold)

### Text
- **Primary text:** `#1F1A17` → token: `--color-text-primary` (almost black, warm tone)
- **Secondary text:** `#6B5E52` → token: `--color-text-secondary`
- **Muted text:** `#9A8C7F` → token: `--color-text-muted`

### Accent (new – softer, more sophisticated)
- **Main accent:** `#B76E54` → token: `--color-accent`  
  (muted terracotta / burnt sienna – warm but not aggressive)  
  Hover: `#A65F47`  
  Active: `#954F3C`

- **Secondary accent (rare):** `#8B7A6A` → token: `--color-sage` (warm stone gray)

All colors defined as CSS variables in `globals.css`.  
Hard-coded hex = forbidden.

---

## 3. Typography (unchanged – perfect already)

- Font: System stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`)
- Base size: 16px
- Line height: 1.6
- Weights: 400 (body), 500 (medium), 600 (semibold headings)
- Bold (700) only for very rare emphasis

Headings use same font, just larger size + slightly tighter line height.

---

## 4. Spacing (strict 8px grid)

Tokens only: `--spacing-xs` (8px), `--spacing-sm` (16px), `--spacing-md` (24px), `--spacing-lg` (40px), `--spacing-xl` (64px)

Rules:
- Page max-width: 800px on desktop, full-width on mobile
- Section vertical spacing: `--spacing-xl` (64px) between major sections
- Inside guide: `--spacing-md` (24px) between items
- Item padding: `--spacing-sm` vertical, `--spacing-md` horizontal
- Never use raw px or arbitrary values

---

## 5. Border Radius, Borders, Shadows

- Radius: **8px** everywhere (cards, buttons, images, inputs)  
  (4px → 8px change: feels more modern and generous)
- Borders: 1px solid `--color-border`
- Shadows: very subtle  
  `box-shadow: 0 4px 20px rgba(0,0,0,0.04)` for cards on hover  
  No shadow on default state – flat until interaction

---

## 6. Component Rules

### Guide Card / Page
Hierarchy:
1. Cover image (full bleed, 8px bottom radius if no image → soft gradient default)
2. Title (large, 32–40px on desktop)
3. Byline: “Curated by @username” in muted text
4. Description (generous spacing)
5. Items (clean, generous vertical rhythm)
6. Footer: subtle “Share this guide” + date updated

### Items
- Left: optional image/thumbnail (8px radius)
- Right: title + optional note
- If links exist: small pill buttons below note (accent background, white text, 8px radius)
- Entire item hover: soft background tint `--color-soft-surface`

### Buttons
- Height: 44px minimum (touch-friendly)
- Padding: `--spacing-lg` horizontal
- Radius: 8px
- Primary: `--color-accent` background, white text
- Secondary/ghost: no background, `--color-accent` text + border on hover
- Text always capitalized only first letter (“Copy link”, not “COPY LINK”)

### Inputs & Forms
- Clean, bottom border only on focus
- No heavy outlines
- Placeholder text in `--color-text-muted`

---

## 7. Dark Mode (optional but planned)

Will be added later.  
When we do: invert to off-black background `#0F0D0B`, warm white text, same accent.

---

## 8. Checklist (use before every PR)

- [ ] Colors from tokens only  
- [ ] Spacing from 8px grid only  
- [ ] Radius 8px everywhere  
- [ ] Guide feels like something you’d screenshot and post  
- [ ] Mobile: thumb-friendly, no cramped text  
- [ ] Hover states subtle and warm  
- [ ] No loud animations (fade-in max)

---

## 9. Implementation Rules (strict)

- CSS Modules + semantic class names only  
- No Tailwind forbidden (keeps us disciplined)  
- All colors/spacing/radius from `globals.css` tokens  
- No inline styles, no !important  
- Every new component must be reviewed against this doc

