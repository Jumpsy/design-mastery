---
version: alpha
name: OpenAI-design-analysis
description: "A pure black-and-white marketing canvas with no chromatic accent at all — every affordance is carried by weight and contrast, not color. Background is true white (#ffffff), text is true black (#000000), and the only 'brand color' is black itself: the primary CTA is a solid black pill. Secondary buttons sit on a near-invisible 4%-black wash (rgba(0,0,0,0.04)) rather than a bordered outline. Type runs in OpenAI's own custom grotesk (OpenAI Sans) with tight negative tracking at every size. Every interactive control — nav links, buttons, toggles — is fully pill-shaped (border-radius 40px/9999px). The page reads as engineering-lab austerity: monochrome, dense, no gradients, no illustration."

colors:
  ink: "#000000"
  canvas: "#ffffff"
  surface-wash: "rgba(0,0,0,0.04)"
  border-hairline: "#e5e7eb"
  on-ink: "#ffffff"

typography:
  h2:
    fontFamily: "OpenAI Sans"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.26
    letterSpacing: -0.22px
  body:
    fontFamily: "OpenAI Sans"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: -0.17px
  eyebrow-link:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: normal
  button:
    fontFamily: "OpenAI Sans"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: normal

rounded:
  pill: 40px
  full: 9999px
  none: 0px

spacing:
  button-sm: 8px 16px
  button-md: 0px 20px

components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 0px 20px
  button-secondary:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  icon-button:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: 0px
---

## Overview

OpenAI's marketing site is deliberately **achromatic**. There is no brand hue anywhere on the page — `{colors.canvas}` is pure white (#ffffff), `{colors.ink}` is pure black (#000000), and the single "accent" is black itself: the primary CTA (`button-primary`, "Try ChatGPT") is a solid black pill with white text. Everything else — nav links, secondary buttons, the "Log in" control — sits on a barely-there 4%-black wash (`{colors.surface-wash}`, `rgba(0,0,0,0.04)`) rather than a stroked border.

Every interactive control is a **full pill** — `border-radius: 40px` on standard buttons/links, `9999px` on icon-only controls. There is no intermediate radius scale; UI is either sharp (0px, for layout containers) or fully rounded (pill).

Type runs entirely in OpenAI's own custom grotesk, **OpenAI Sans**, at negative tracking across every size (body: -0.17px at 17px; h2: -0.22px at 22px — both roughly -1% of size, tighter than most SaaS marketing type). Body copy sets unusually large at 17px/28px, giving the page a slightly more "editorial" body-text scale than typical dense SaaS sites.

**Key Characteristics:**
- **Zero chromatic accent** — the entire palette is black, white, and gray washes of black.
- **Full-pill interactive controls** — no small-radius buttons; radius is binary (0 or pill).
- **Solid black CTA** — the one high-contrast element on an otherwise monochrome page.
- **4%-black wash** for secondary/hover surfaces instead of borders.
- **Negative tracking at ~-1%** consistently across headline and body sizes.
- **Custom "OpenAI Sans" typeface** — geometric grotesk, no serif or mono accents on marketing surfaces.

## Colors

> Source: openai.com homepage, computed styles read live via browser DOM inspection (getComputedStyle on body, headings, buttons, links).

- **Ink** ({colors.ink}): #000000 — all text, primary button fill.
- **Canvas** ({colors.canvas}): #ffffff — page background, primary button text.
- **Surface Wash** ({colors.surface-wash}): rgba(0,0,0,0.04) — secondary button fill, hover states, nav pill backgrounds.
- **Border Hairline** ({colors.border-hairline}): #e5e7eb — used only as a 0px-width border definition (effectively unused on this page; borders are near-invisible).
- **On Ink** ({colors.on-ink}): #ffffff — text on the black primary CTA.

## Typography

### Font Family
- **OpenAI Sans** (with "OpenAI Sans Variable Scripts" fallback, then generic sans-serif) — used for every text role on the page, headlines through buttons. No secondary typeface.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.h2}` | 22px | 500 | 1.26 | -0.22px | Section headings ("Recent news", "Stories", "Latest research") |
| `{typography.body}` | 17px | 400 | 1.65 | -0.17px | Default body copy |
| `{typography.eyebrow-link}` | 14px | 500 | 1.40 | normal | In-body link/label text |
| `{typography.button}` | 13px | 500 | 1.0 | normal | All button/pill labels |

### Principles
- Negative tracking scales with size (roughly -1% consistently), same discipline as other high-end SaaS marketing systems but applied uniformly rather than only at display sizes.
- Weight 500 is the ceiling on this page — no bold (700+) headlines observed in the sampled sections.
- Body text is set unusually large (17px) for a tech marketing site, giving a more relaxed reading rhythm than the 14-16px norm.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Layout containers, cards |
| `{rounded.pill}` | 40px | Standard buttons and nav links |
| `{rounded.full}` | 9999px | Icon-only circular controls |

There is no intermediate radius step — this is a binary sharp/pill system, distinct from most brands in this library which use a 4–6 step radius ramp.

## Components

### Buttons

**`button-primary`** — Solid black CTA ("Try ChatGPT").
- Background `{colors.ink}`, text `{colors.on-ink}`, type `{typography.button}`, rounded `{rounded.pill}`, padding 0px 20px.

**`button-secondary`** — Low-contrast wash button ("Log in", nav utility links).
- Background `{colors.surface-wash}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.pill}`, padding 8px 16px.

**`icon-button`** — Circular icon-only control (menu toggles, carousel arrows).
- Background `{colors.surface-wash}`, text `{colors.ink}`, rounded `{rounded.full}`, padding 0px.

## Do's and Don'ts

### Do
- Keep the palette strictly black/white/wash-of-black — resist adding any hue.
- Use the solid black pill only for the single highest-priority CTA per view.
- Apply negative tracking (~-1% of size) at every text size, not just display.
- Round every interactive control fully (pill/circle) — never a small 4-8px radius.

### Don't
- Don't introduce a chromatic brand color on marketing surfaces.
- Don't use bordered/outlined buttons — use the 4%-black wash instead.
- Don't mix radius scales — it's sharp (0) or pill, nothing between.
- Don't set body text below 16px; this system reads larger than typical SaaS body copy.

## Known Gaps

- This analysis is based on the OpenAI marketing homepage only (openai.com/), read via live computed-style inspection (getComputedStyle), not a full crawl of product/pricing/docs subpages.
- Dark-mode variant was not inspected — the homepage renders light-only at time of analysis.
- Card/panel components (news tiles, research cards) were sampled for radius (0px, confirming the sharp-container rule) but not fully cataloged for shadow/elevation treatment.
