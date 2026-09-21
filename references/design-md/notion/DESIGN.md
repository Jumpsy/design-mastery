---
version: alpha
name: Notion-design-analysis
description: "A white-canvas marketing system with extremely aggressive hero tracking: 96px/600 headline text at -4.6px letter-spacing (~-4.8% of size, among the steepest in this collection), set in a custom face 'NotionInter' (an Inter derivative). The primary CTA uses a mid-blue (#0075de) on an 8px-radius rectangle, with a matching pale-blue-wash secondary button (#e6f3fe) for 'Request a demo' — a clean two-tier blue system rather than a single flat accent."

colors:
  ink: "rgba(0,0,0,0.95)"
  canvas: "#ffffff"
  primary: "#0075de"
  on-primary: "#ffffff"
  secondary-wash: "#e6f3fe"
  on-secondary-wash: "#005bab"

typography:
  display-hero:
    fontFamily: "NotionInter"
    fontSize: 96px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -4.6px
  body:
    fontFamily: "NotionInter"
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
    padding: 6px 15px
  button-secondary-wash:
    backgroundColor: "{colors.secondary-wash}"
    textColor: "{colors.on-secondary-wash}"
    rounded: "{rounded.sm}"
    padding: 6px 15px
---

## Overview

Notion's marketing homepage runs a plain white canvas (`{colors.canvas}`) with near-black ink at 95% opacity (`{colors.ink}`, rgba(0,0,0,0.95) rather than a flat hex — a soft-black convention). The hero headline ("Where teams and agents Ship together.") is set at an unusually large 96px/600 in the custom face **NotionInter** (a branded Inter derivative), with extremely aggressive negative tracking: -4.6px, roughly -4.8% of type size — among the steepest tracking values measured across this reference library, well past GitHub's -3.5% and Cloudflare's -2.5%.

The button system is a clean two-tier blue: a solid mid-blue (`{colors.primary}` #0075de) primary CTA ("Get Notion free") and a pale-blue-wash secondary (`{colors.secondary-wash}` #e6f3fe, text `{colors.on-secondary-wash}` #005bab) for lower-priority actions ("Request a demo") — both sharing the same modest 8px radius and near-identical padding, differing only in fill weight/prominence.

**Key Characteristics:**
- **Extremely tight hero tracking** (-4.6px at 96px, ~-4.8% of size) — the steepest measured in this collection.
- **Two-tier blue button system**: solid mid-blue primary, pale-wash secondary, same 8px radius.
- **NotionInter** custom face (Inter-derived) for both display and body.
- **Soft-black ink** (rgba(0,0,0,0.95)) rather than a flat hex value.
- Compact button padding (6px 15px) relative to peers' larger CTA sizing.

## Colors

> Source: notion.com homepage, computed styles read live via browser DOM inspection.

- **Ink** ({colors.ink}): rgba(0,0,0,0.95) — headline/body text, a soft rather than pure black.
- **Canvas** ({colors.canvas}): #ffffff — page background.
- **Primary** ({colors.primary}): #0075de — primary CTA fill ("Get Notion free").
- **On Primary** ({colors.on-primary}): #ffffff — CTA label text.
- **Secondary Wash** ({colors.secondary-wash}): #e6f3fe — pale-blue secondary button fill ("Request a demo").
- **On Secondary Wash** ({colors.on-secondary-wash}): #005bab — darker blue text on the pale wash.

## Typography

### Font Family
- **NotionInter** (with `Inter` fallback) — sole typeface observed for both hero display and body/UI text.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 96px | 600 | -4.6px | Hero headline ("Where teams and agents Ship together.") |
| `{typography.body}` | 16px | 400 | normal | Body copy |

## Components

### Buttons

**`button-primary`** — Solid blue CTA ("Get Notion free").
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.sm}` (8px), padding 6px 15px.

**`button-secondary-wash`** — Pale-blue wash CTA ("Request a demo").
- Background `{colors.secondary-wash}`, text `{colors.on-secondary-wash}`, rounded `{rounded.sm}`, padding 6px 15px — identical shape/size to the primary, differentiated only by fill weight.

## Do's and Don'ts

### Do
- Push hero tracking aggressively negative (~-5% of size) — this is a defining, deliberate characteristic of Notion's current display type.
- Pair a solid-fill primary CTA with a same-shape pale-wash secondary, rather than a ghost/outline secondary.
- Keep button padding compact (6px 15px) — Notion's CTAs read smaller/denser than most SaaS peers.

### Don't
- Don't apply hero-level tracking to body text — it's scoped to the largest display size only.
- Don't use a flat pure-black hex for ink — the system's convention is 95%-opacity black.

## Known Gaps

- Analysis covers the marketing homepage only (notion.com/), read via live computed-style inspection; the in-app workspace/editor UI (Notion's core product) was not inspected and likely uses a denser, more utilitarian component system.
- Card/panel elevation and radius for feature sections were not sampled in this pass.
- Dark-mode variant, if any, was not inspected.
