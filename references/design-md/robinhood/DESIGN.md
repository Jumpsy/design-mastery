---
version: alpha
name: Robinhood-design-analysis
description: "A black-canvas, editorial-serif marketing system: white headlines set in the licensed serif 'Martina Plantijn' at 72-90px/400 with tight -1px tracking, paired with a custom grotesk 'Phonic' for section headlines at -1.5px tracking. The single chromatic accent is an acid-lime chartreuse (#ccff00) used on every CTA — a striking, unconventional choice for a finance brand that departs from the industry's default blue/green trust palette. All CTAs are near-full pill buttons (36px radius) with dark near-black text on the lime fill."

colors:
  canvas: "#000000"
  ink-inverse: "#ffffff"
  accent: "#ccff00"
  on-accent: "#110e08"

typography:
  display-hero:
    fontFamily: "Martina Plantijn"
    fontSize: 90px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display-hero-sm:
    fontFamily: "Martina Plantijn"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  h2:
    fontFamily: "Phonic"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1.5px
  body:
    fontFamily: "Capsule Sans Text"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  pill: 36px

components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.pill}"
    padding: 0px 32px
---

## Overview

Robinhood's marketing homepage runs on a pure-black canvas (`{colors.canvas}`) with white headline text (`{colors.ink-inverse}`) — a stark, editorial-magazine register rather than a typical fintech "trust blue" system. Display type is set in the licensed serif **Martina Plantijn** at very large sizes (72-90px, weight 400) with tight -1px tracking — an unusual serif-forward choice among fintech/crypto competitors, who mostly run grotesks.

Section-level headlines switch to **Phonic**, a geometric sans, at 52px with even tighter -1.5px tracking. Body copy and UI chrome use **Capsule Sans Text**, a third distinct typeface — so the system deliberately layers three different type families by role (serif display / grotesk section head / UI sans body) rather than a single unified face.

The sole chromatic accent is an **acid-lime chartreuse** (`{colors.accent}` #ccff00) applied to every CTA ("Get started", "Sign up") as a near-full pill (36px radius) with near-black text (`{colors.on-accent}` #110e08) — a bold, unconventional color choice that trades the finance industry's default blue/green for something closer to a streetwear/tech-forward palette.

**Key Characteristics:**
- **Black canvas, white serif headlines** — an editorial register uncommon among fintech peers.
- **Three-typeface system**: Martina Plantijn (serif display), Phonic (grotesk section heads), Capsule Sans Text (UI/body).
- **Acid-lime chartreuse accent** (#ccff00) reserved exclusively for CTAs, on near-black text.
- **36px-radius pill buttons** — soft but not fully circular.
- Tight negative tracking scales with size (-1px at 72-90px serif, -1.5px at 52px sans).

## Colors

> Source: robinhood.com homepage (CA locale), computed styles read live via browser DOM inspection.

- **Canvas** ({colors.canvas}): #000000 — page background.
- **Ink Inverse** ({colors.ink-inverse}): #ffffff — headline text on the black canvas.
- **Accent** ({colors.accent}): #ccff00 — acid-lime CTA fill, the sole chromatic color observed.
- **On Accent** ({colors.on-accent}): #110e08 — near-black text on the lime CTA.

## Typography

### Font Family
- **Martina Plantijn** — licensed serif for the largest hero display text.
- **Phonic** — geometric sans-serif for section-level headlines.
- **Capsule Sans Text** — UI/body sans, used for both `<body>` default and button labels.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 90px | 400 | -1px | Largest hero statement ("Low-cost. Secure. Powerful...") |
| `{typography.display-hero-sm}` | 72px | 400 | -1px | Secondary hero line ("Trade crypto with zero fees") |
| `{typography.h2}` | 52px | 400 | -1.5px | Section headline ("Protection for your coins...") |
| `{typography.body}` | 16px | 400 | normal | Body copy |

## Components

### Buttons

**`button-primary`** — Lime pill CTA ("Get started", "Sign up").
- Background `{colors.accent}`, text `{colors.on-accent}`, rounded `{rounded.pill}` (36px), padding 0px 32px, rendered as `<a>` elements rather than `<button>`.

## Do's and Don'ts

### Do
- Reserve the lime accent strictly for CTAs — it never appears as a section background or decorative fill in the sampled hero.
- Layer three distinct typefaces by role (serif display / grotesk section / sans UI) rather than one unified face.
- Apply negative tracking that scales with size, not a flat value.

### Don't
- Don't default to blue/green "trust" colors for the CTA — this system deliberately breaks fintech convention with chartreuse.
- Don't set body copy in the display serif — Martina Plantijn is reserved for hero-scale headlines only.

## Known Gaps

- Analysis covers the marketing homepage only (robinhood.com/, CA locale as served), read via live computed-style inspection; the in-app trading UI was not inspected.
- No `<button>` elements with distinct fills were found in the sampled first 400 — all sampled CTAs render as `<a>` tags; native `<button>` styling (e.g. in forms) was not captured.
- Dark/light mode toggling was not tested — the homepage defaults to the black canvas shown here.
