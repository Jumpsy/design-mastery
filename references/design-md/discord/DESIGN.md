---
version: alpha
name: Discord-design-analysis
description: "A saturated indigo canvas (#1a2081, Discord's deep 'blurple'-adjacent background) paired with a bright signal-green accent (#35ed7e) on the primary CTA — a notable departure from Discord's older pure-blurple (#5865F2) brand identity toward a punchier lime-green call-to-action. Display type runs in Discord's custom condensed/expanded display face ('gg sans'/'ABC Ginto Discord Nord') at heavy weights (700-800) with aggressive negative tracking. Buttons use a consistent 12-16px rounded-rectangle radius, not full pills. The page is playful and maximalist: mascot illustration, animated stickers, and bold color-blocked sections."

colors:
  canvas: "#1a2081"
  primary-cta: "#35ed7e"
  on-primary-cta: "#000000"
  ink-inverse: "#ffffff"

typography:
  display-hero:
    fontFamily: "ABC Ginto Discord Nord"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.56px
  h2-lg:
    fontFamily: "ABC Ginto Discord Nord"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.48px
  h2-sm:
    fontFamily: "ABC Ginto Discord Nord"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.66px
  body:
    fontFamily: "gg sans"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  sm: 12px
  md: 16px

components:
  button-primary:
    backgroundColor: "{colors.primary-cta}"
    textColor: "{colors.on-primary-cta}"
    rounded: "{rounded.sm}"
    padding: 13px 24px
  button-ghost-inverse:
    backgroundColor: "transparent"
    textColor: "{colors.ink-inverse}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
---

## Overview

Discord's marketing homepage sits on a saturated deep-indigo canvas (`{colors.canvas}` #1a2081) — noticeably more purple-blue and darker than the brand's classic "blurple" (#5865F2) used in-product. Against this, the single high-contrast CTA is a **signal-green** (`{colors.primary-cta}` #35ed7e) button with black text — a striking, almost lime-neon accent rather than the brand's historical purple.

Display type runs in Discord's custom condensed/expanded grotesk (referenced in CSS as `Abcgintodiscordnord`, i.e. **ABC Ginto Discord Nord**, with Arial fallback) at heavy weights — 700 at hero, ramping to **800** on the boldest section headline ("MAKE YOUR GROUP CHATS MORE FUN"), with negative tracking scaling from -0.48px to -0.66px depending on size (not strictly monotonic with size — the 22px h2 carries more tracking than the 48px h2, an unusual inversion). Body copy uses **gg sans**, Discord's in-product UI font, on marketing surfaces too.

Buttons use a consistent rounded-rectangle radius (12-16px) rather than full pills — a deliberately "softer but structured" shape distinct from the pill-everything approach seen at OpenAI/Cloudflare.

**Key Characteristics:**
- **Deep indigo canvas** (#1a2081), darker/more saturated than classic Discord blurple.
- **Signal-green CTA** (#35ed7e) with black text — a bold departure from purple-brand convention.
- **Heavy display weights** (700-800) on a custom condensed grotesk.
- **12-16px rounded-rectangle buttons**, not pills.
- Maximalist, illustration- and mascot-driven page (Wumpus/Clyde characters, animated stickers).

## Colors

> Source: discord.com homepage, computed styles read live via browser DOM inspection.

- **Canvas** ({colors.canvas}): #1a2081 — page background, deep indigo.
- **Primary CTA** ({colors.primary-cta}): #35ed7e — signal green, the one high-contrast button fill on the page.
- **On Primary CTA** ({colors.on-primary-cta}): #000000 — black text on the green button.
- **Ink Inverse** ({colors.ink-inverse}): #ffffff — headline and body text against the indigo canvas.

## Typography

### Font Family
- **ABC Ginto Discord Nord** — custom condensed display face for headlines (Arial fallback).
- **gg sans** — Discord's in-product UI font, reused for marketing body copy.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 56px | 700 | -0.56px | Hero headline |
| `{typography.h2-lg}` | 48px | 800 | -0.48px | Boldest section headline |
| `{typography.h2-sm}` | 22px | 700 | -0.66px | Smaller section subheads |
| `{typography.body}` | 16px | 400 | normal | Body copy |

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.sm}` | 12px | Primary CTA, ghost buttons |
| `{rounded.md}` | 16px | Icon/pill-style social links |

## Components

### Buttons

**`button-primary`** — Green CTA ("Skip to main content" nav skip-link and equivalent primary actions).
- Background `{colors.primary-cta}`, text `{colors.on-primary-cta}`, rounded `{rounded.sm}`, padding 13px 24px.

**`button-ghost-inverse`** — Transparent nav link button ("Download", "Nitro").
- Background transparent, text `{colors.ink-inverse}`, rounded `{rounded.sm}`, padding 10px 16px.

## Do's and Don'ts

### Do
- Use the green CTA sparingly — it's the one saturated-bright element against the indigo field.
- Push display weight to 700-800 for maximum impact headlines.
- Keep buttons rounded-rectangle (12-16px), not pill.

### Don't
- Don't default to purple/blurple for the primary CTA on marketing surfaces — this page uses green instead.
- Don't flatten the indigo canvas to pure black or navy — the specific #1a2081 hue is load-bearing for brand feel.

## Known Gaps

- Analysis covers the marketing homepage only (discord.com/), read via live computed-style inspection; in-app product UI (which does use the classic blurple #5865F2) was not inspected.
- Illustration/mascot asset styling (Wumpus, Clyde) was observed visually but not measured programmatically.
- Card and panel elevation/radius for feature sections were not sampled in this pass.
