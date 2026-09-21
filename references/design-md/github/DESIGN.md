---
version: alpha
name: GitHub-design-analysis
description: "A near-black canvas (#0d1117, GitHub's signature 'canvas-default' dark surface) with off-white text (#f0f6fc), set in GitHub's custom variable typeface 'Mona Sans' at an unusual mid-weight 425 for hero display and very aggressive negative tracking (-2.24px at 64px, roughly -3.5% of size — among the steepest in this collection). The single chromatic accent is GitHub's signature green (#08872b) reserved for the primary 'Sign up' CTA. Secondary buttons use a translucent white wash (rgba(255,255,255,0.12)) rather than a solid fill. Buttons use a modest 6px radius almost universally, with one fully-pill icon control (48px)."

colors:
  canvas: "#0d1117"
  ink: "#f0f6fc"
  primary: "#08872b"
  on-primary: "#ffffff"
  surface-wash: "rgba(255,255,255,0.12)"

typography:
  display-hero:
    fontFamily: "Mona Sans"
    fontSize: 64px
    fontWeight: 425
    lineHeight: 1.1
    letterSpacing: -2.24px
  body:
    fontFamily: "Mona Sans VF"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  sm: 6px
  full: 48px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 6px 20px
  button-secondary-wash:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 10px 28px
  icon-button-round:
    backgroundColor: "#090d0a"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: 0px
---

## Overview

GitHub's current marketing homepage runs dark-canvas-first: `{colors.canvas}` is #0d1117 (GitHub's documented `canvas-default` dark token), with off-white ink (`{colors.ink}` #f0f6fc, not pure white). The sole chromatic accent is GitHub's signature green (`{colors.primary}` #08872b), used exclusively on the primary "Sign up for GitHub" CTA — every other button, including nav-level actions like "Code" and "By industry," uses a translucent white wash (`{colors.surface-wash}` rgba(255,255,255,0.12)) instead of a distinct color.

Display type is set in GitHub's custom variable typeface **Mona Sans**, notable for using an unusual mid-range weight (**425**, not a round 400/500 step — a hallmark of variable-font systems that tune weight precisely rather than snapping to standard steps) at the hero size, with very aggressive negative tracking: -2.24px at 64px, roughly -3.5% of type size, among the steepest tracking values observed in this reference library.

Buttons hold a consistent, modest 6px radius almost everywhere — a deliberately understated shape choice relative to the pill-heavy conventions at OpenAI/Cloudflare — with one exception: circular icon controls use a full 48px (effectively pill/circle) radius.

**Key Characteristics:**
- **Dark canvas-first** (#0d1117) with off-white (not pure white) ink.
- **Green reserved strictly for the primary CTA** — everything else uses a translucent white wash, not a second color.
- **Mona Sans variable font** at fractional weight (425) with steep negative tracking (~-3.5% at hero size).
- **Consistent 6px button radius** — restrained relative to pill-forward competitors.
- Developer-tool restraint: no gradients, no illustration-heavy hero, code/terminal imagery implied through UI screenshots.

## Colors

> Source: github.com homepage, computed styles read live via browser DOM inspection.

- **Canvas** ({colors.canvas}): #0d1117 — page background, GitHub's `canvas-default` dark token.
- **Ink** ({colors.ink}): #f0f6fc — headline and body text, an off-white rather than pure #ffffff.
- **Primary** ({colors.primary}): #08872b — GitHub green, the single chromatic accent, used only on the primary CTA.
- **On Primary** ({colors.on-primary}): #ffffff — text on the green button.
- **Surface Wash** ({colors.surface-wash}): rgba(255,255,255,0.12) — fill for every secondary/nav button.

## Typography

### Font Family
- **Mona Sans** (variable font, `MonaSansFallback` / system fallback stack) — hero and headline type.
- **Mona Sans VF** — body copy and UI chrome, same family, tuned for smaller sizes.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 64px | 425 | -2.24px | Hero headline ("The future of building happens...") |
| `{typography.body}` | 14px | 400 | normal | Default body/UI text |

### Principles
- Weight is tuned to a non-standard fractional value (425) rather than snapping to 400/500 — a variable-font-specific convention worth preserving when implementing with Mona Sans or a similar variable typeface.
- Tracking is unusually tight at display size (~-3.5% of size) — steeper than the -1% to -2.5% norm elsewhere in this library.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.sm}` | 6px | Nearly all buttons — primary CTA, secondary wash buttons, search |
| `{rounded.full}` | 48px | Circular icon-only controls |

## Components

### Buttons

**`button-primary`** — Green CTA ("Sign up for GitHub").
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.sm}`, padding 6px 20px.

**`button-secondary-wash`** — Translucent white-wash button used for every non-primary action ("Code", "By industry", "English").
- Background `{colors.surface-wash}`, text `{colors.ink}`, rounded `{rounded.sm}`, padding 10px 28px.

**`icon-button-round`** — Circular icon control (search toggle, avatar).
- Background near-black (#090d0a), text `{colors.ink}`, rounded `{rounded.full}`, padding 0px.

## Do's and Don'ts

### Do
- Reserve green strictly for the single highest-priority CTA per view.
- Use the translucent white wash, not a second brand color, for every other button.
- Hold button radius at a consistent 6px — resist pill-ifying secondary actions.

### Don't
- Don't introduce a second chromatic accent alongside the green.
- Don't use pure black/white — GitHub's convention is #0d1117 canvas / #f0f6fc ink.
- Don't round buttons past 6px except for genuinely circular icon controls.

## Known Gaps

- Analysis covers the marketing homepage only (github.com/), read via live computed-style inspection; the signed-in product UI (issues, PRs, repo pages) was not inspected and uses a denser, more component-rich design system (Primer).
- Light-mode variant was not inspected — GitHub.com defaults to dark for logged-out visitors in this session.
- Card/repo-tile elevation and radius were not sampled in this pass.
