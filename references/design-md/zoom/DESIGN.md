---
version: alpha
name: Zoom-design-analysis
description: "A rebranded, editorial-leaning marketing system for Zoom: hero and section headlines are set in the serif 'Newsreader' (54px/500, 46px/400 with -1.4px tracking) rather than the sans-serif grotesk typical of video-conferencing competitors, while body/UI text uses 'Inter'. The primary accent is a saturated electric blue (#0b5cff), used consistently across CTAs as an 8px-radius rectangle — a marked departure from Zoom's older flat corporate-blue identity toward a warmer, more serif-driven brand voice."

colors:
  ink: "#000000"
  h2-ink: "#00053d"
  primary: "#0b5cff"
  on-primary: "#ffffff"

typography:
  display-hero:
    fontFamily: "Newsreader"
    fontSize: 54px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: normal
  h2:
    fontFamily: "Newsreader"
    fontSize: 46px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -1.4px
  body:
    fontFamily: "Inter"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  sm: 8px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
---

## Overview

Zoom's current marketing homepage (zoom.com) is a notable departure from the flat, purely-corporate blue identity long associated with the brand: hero and section headlines are set in the serif **Newsreader** — 54px/500 for the hero, 46px/400 with tight -1.4px tracking (≈-3% of size) for section heads — giving the page an editorial, almost publishing tone uncommon among video-conferencing competitors (Discord, Loom, GitHub all run grotesks). Body and UI text falls back to **Inter**, a standard open grotesk.

The primary accent is a saturated electric blue (`{colors.primary}` #0b5cff), applied consistently to CTA buttons ("Sign Up Free", "Contact Sales") as an 8px-radius rectangle — modestly rounded, not pill-shaped. Section headline ink shifts slightly from pure black (hero) to a near-black navy (`{colors.h2-ink}` #00053d) at the h2 level — a subtle but real distinction between hero and section-level text color.

**Key Characteristics:**
- **Newsreader serif** for display type — an editorial register unusual for the video-conferencing category.
- **Inter** for body/UI — a standard, unbranded grotesk pairing with the custom-feeling serif.
- **Electric blue** (#0b5cff) as the sole chromatic accent, reserved for CTAs.
- **8px-radius rectangular buttons** — modest rounding, not pill.
- Two-tone ink: pure black for hero, near-black navy (#00053d) for section headlines.

## Colors

> Source: zoom.com homepage, computed styles read live via browser DOM inspection.

- **Ink** ({colors.ink}): #000000 — hero headline text.
- **H2 Ink** ({colors.h2-ink}): #00053d — section headline text, a near-black navy distinct from pure hero black.
- **Primary** ({colors.primary}): #0b5cff — electric blue, the sole chromatic CTA accent.
- **On Primary** ({colors.on-primary}): #ffffff — CTA label text.

## Typography

### Font Family
- **Newsreader** — serif used for hero and section-level headlines.
- **Inter** — grotesk used for body copy and UI chrome, including button labels.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 54px | 500 | normal | Hero headline ("Find out what's possible when work connects") |
| `{typography.h2}` | 46px | 400 | -1.4px | Section headlines ("Your new AI note taker") |
| `{typography.body}` | 16px | 400 | normal | Body copy |

## Components

### Buttons

**`button-primary`** — Blue rectangular CTA ("Sign Up Free", "Contact Sales").
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.sm}` (8px), padding 14px 16px.

## Do's and Don'ts

### Do
- Use the Newsreader serif for headline-level type — it's the brand's current signature differentiator from other conferencing tools.
- Keep the blue accent (#0b5cff) reserved for CTAs only.
- Hold button radius at a modest 8px, not a full pill.

### Don't
- Don't set headlines in Inter — the serif/sans pairing (serif for display, sans for body) is load-bearing for the current brand voice.
- Don't flatten hero ink and section-headline ink to the same value — the system distinguishes pure black (hero) from near-black navy (#00053d, section heads).

## Known Gaps

- Analysis covers the marketing homepage only (zoom.com/), read via live computed-style inspection; the in-product meeting/webinar UI (which retains more of Zoom's legacy visual language) was not inspected.
- Card/panel elevation and radius for feature sections were not sampled in this pass.
- Dark-mode variant, if any, was not inspected.
