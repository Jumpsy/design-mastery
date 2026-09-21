---
version: alpha
name: Loom-design-analysis
description: "A white-canvas marketing system for Loom (Atlassian) built on two custom faces — 'Charlie Display' for large 70px/700 bold headlines with no negative tracking, and 'Charlie Text' for body/UI. The single chromatic CTA color is a confident mid-blue (#1868db) rendered as a fully-pill button (9999px radius) with white text — a simpler, single-accent system relative to the multi-hue palettes seen elsewhere."

colors:
  canvas: "#ffffff"
  ink: "#101214"
  ink-secondary: "#292a2e"
  primary: "#1868db"
  on-primary: "#ffffff"

typography:
  display-hero:
    fontFamily: "Charlie Display"
    fontSize: 70px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: normal
  h2:
    fontFamily: "Charlie Display"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: normal
  body:
    fontFamily: "Charlie Text"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    padding: 16px 24px
---

## Overview

Loom's marketing homepage runs a plain white canvas (`{colors.canvas}`) with near-black ink (`{colors.ink}` #101214 for headlines, `{colors.ink-secondary}` #292a2e for body). Display type is set in **Charlie Display**, a custom bold (700) grotesk at large sizes (70px hero, 48px section) with no negative tracking applied — a plainer, less aggressively-tightened treatment than most SaaS peers in this collection (Linear, OpenAI, GitHub all apply visible negative tracking at similar sizes).

The sole chromatic accent is a confident mid-blue (`{colors.primary}` #1868db), used exclusively on the "Get Loom for free" CTA, rendered as a fully-pill button (9999px radius, explicit rather than a computed near-infinite value) with white text. Body/UI copy switches to the companion face **Charlie Text**.

**Key Characteristics:**
- **Single-accent blue system** (#1868db) — no secondary brand hue observed.
- **Charlie Display / Charlie Text** two-weight custom type pairing (display face for headlines, text face for body/UI).
- **No negative tracking** on display type — untightened, unlike most peers.
- **Fully-pill CTA button** (explicit 9999px radius) with generous 16px/24px padding.
- Clean white-canvas, product-screenshot-led layout (no dark mode observed on marketing surfaces).

## Colors

> Source: loom.com homepage, computed styles read live via browser DOM inspection.

- **Canvas** ({colors.canvas}): #ffffff — page background.
- **Ink** ({colors.ink}): #101214 — headline text.
- **Ink Secondary** ({colors.ink-secondary}): #292a2e — body text.
- **Primary** ({colors.primary}): #1868db — CTA fill, the sole chromatic accent.
- **On Primary** ({colors.on-primary}): #ffffff — CTA text.

## Typography

### Font Family
- **Charlie Display** — custom bold display face for hero and section headlines.
- **Charlie Text** — companion custom face for body copy and UI chrome.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 70px | 700 | normal | Hero headline ("One video is worth a thousand words") |
| `{typography.h2}` | 48px | 700 | normal | Section headlines ("Millions of people across 400,000 companies...") |
| `{typography.body}` | 16px | 400 | normal | Body copy |

## Components

### Buttons

**`button-primary`** — Blue pill CTA ("Get Loom for free").
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.pill}` (explicit 9999px), padding 16px 24px (large) or 8px 16px (compact nav variant).

## Do's and Don'ts

### Do
- Keep the blue accent as the single chromatic CTA color — don't introduce a second brand hue.
- Leave display type at normal (untightened) tracking — this is a deliberate, plainer register than most SaaS peers.
- Use the full 9999px pill radius on CTAs.

### Don't
- Don't apply negative letter-spacing to headlines — not part of this system's convention.
- Don't confuse the cookie-consent banner's amber (#ffab00) OneTrust buttons with the brand's real CTA color — the actual primary accent is blue (#1868db).

## Known Gaps

- Analysis covers the marketing homepage only (loom.com/), read via live computed-style inspection; the in-app recording/editing product UI was not inspected.
- A third-party cookie-consent banner (OneTrust, amber #ffab00 buttons) was present at capture time and excluded from the brand palette above as it is not Loom's own design system.
- Card/panel elevation and radius for feature sections were not sampled in this pass.
