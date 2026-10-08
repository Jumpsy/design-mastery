---
version: alpha
name: Cloudflare-design-analysis
description: "A white-canvas marketing system anchored by Cloudflare's signature burnt-orange (#ff5e1f), set in the licensed display grotesk 'FT Kunst Grotesk' with aggressive negative tracking (-1.4px at 56px, roughly -2.5% of size — among the tightest in this collection). Dark near-black text (#262626, not pure black) carries body and secondary headings. All CTA buttons are fully pill-shaped regardless of size. The page mixes dense data-forward sections ('Cloudflare powers 45% of the Fortune 500') with an editorial, almost publishing-house display-type treatment."

colors:
  primary: "#ff5e1f"
  primary-hover: "#ff7038"
  on-primary: "#ffffff"
  ink: "#262626"
  ink-inverse: "#ffffff"
  canvas: "#ffffff"

typography:
  display-hero:
    fontFamily: "FT Kunst Grotesk"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1.4px
  h2:
    fontFamily: "FT Kunst Grotesk"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -1.2px
  body:
    fontFamily: "FT Kunst Grotesk"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  pill: 3.36e7px

spacing:
  button-sm: 6px 12px
  button-lg: 12px 24px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
  badge-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 6px 6px 6px 16px
---

## Overview

Cloudflare's marketing canvas is white (`{colors.canvas}`) with dark near-black text (`{colors.ink}` #262626 — deliberately not pure black, giving slightly softer contrast than the OpenAI/Linear pure-black approach). The signature accent is a **burnt orange** (`{colors.primary}` #ff5e1f), used exclusively for CTA buttons and a small event-announcement pill — never as a section background.

Display type runs in the licensed grotesk **FT Kunst Grotesk** at weight 500 with unusually aggressive negative tracking: -1.4px at 56px (hero) and -1.2px at 48px (h2), both roughly -2.5% of type size — tighter than most systems in this collection (which typically run -1% to -4% but at larger sizes).

All buttons, regardless of size, use an effectively infinite border-radius (`{rounded.pill}`), rendering as true pills from the smallest 6px-padding chip to the largest 24px-padding CTA.

**Key Characteristics:**
- **Burnt-orange accent** (#ff5e1f) reserved strictly for CTAs and small badges.
- **Off-black ink** (#262626) instead of pure #000000 — softer text contrast.
- **FT Kunst Grotesk** licensed display face with steep negative tracking (~-2.5% of size).
- **Universal pill buttons** — no square or slightly-rounded button variant observed.
- Mixes data-statistic sections ("powers 45% of the Fortune 500") with large editorial display type.

## Colors

> Source: cloudflare.com homepage, computed styles read live via browser DOM inspection.

- **Primary** ({colors.primary}): #ff5e1f — primary CTA fill, event badge fill.
- **Primary Hover** ({colors.primary-hover}): #ff7038 — lighter orange, hover state on "View docs" style CTAs.
- **On Primary** ({colors.on-primary}): #ffffff — text on orange buttons.
- **Ink** ({colors.ink}): #262626 — default heading/body text (off-black, not pure black).
- **Canvas** ({colors.canvas}): #ffffff — page background.

## Typography

### Font Family
- **FT Kunst Grotesk** — licensed display/body grotesk used across all sampled headings and body text; no secondary typeface observed on marketing surfaces.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 56px | 500 | -1.4px | Hero headline |
| `{typography.h2}` | 48px | 500 | -1.2px | Section headlines |
| `{typography.body}` | 16px | 400 | normal | Body copy |

### Principles
- Negative tracking scales aggressively with size (~-2.5% of size) — steeper than the -1% norm seen in most other brands in this library.
- Weight caps at 500 — no bold/700 display weight observed.

## Shapes

- **Pill radius everywhere**: buttons use a functionally-infinite border-radius (33554432px, i.e. `border-radius: 50%`-style pill rendering) regardless of button size — from the 6px-padding badge to the 24px-padding hero CTA.

## Components

### Buttons

**`button-primary`** — Orange pill CTA ("Start building", "View docs").
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.pill}`, padding 12px 24px (large) or 6px 12px (compact nav CTA).
- Hover state (`button-primary-hover`) shifts to `{colors.primary-hover}` (#ff7038).

**`badge-pill`** — Small event-announcement chip ("Connect 2026 · The Agentic...").
- Background `{colors.primary}`, text `{colors.ink}` (dark text on orange, unlike the white-on-orange CTA — a deliberate contrast choice for the badge), rounded `{rounded.pill}`, padding 6px 6px 6px 16px (asymmetric — tighter on the icon side).

## Do's and Don'ts

### Do
- Reserve orange strictly for CTAs and small badges — never as a large fill or section background.
- Pill every button regardless of size.
- Use off-black (#262626) rather than pure black for text — it's the house convention here.

### Don't
- Don't square off button corners — no non-pill button variant was found.
- Don't push display weight past 500.
- Don't use pure black (#000000) for ink — Cloudflare's convention is the softer #262626.

## Known Gaps

- Analysis covers the marketing homepage only (cloudflare.com/), read via live computed-style inspection; product dashboard UI was not inspected.
- Card/panel elevation and border-radius on non-button containers were not sampled in this pass.
- Dark-mode variant, if any, was not inspected.
