---
version: alpha
name: GitLab-design-analysis
description: "A white-canvas marketing system built on GitLab's custom variable typeface 'GitLab Sans' at fractional weights (580, 660) rather than round steps, with very aggressive negative tracking at hero size (-2.88px at 96px, ~-3% of size). The primary CTA ('Get free trial') is a deep near-black plum (#171321) rectangular button with a modest 4px radius — restrained rather than pill-shaped. Section headlines run white-on-dark within feature panels at 24px/580."

colors:
  canvas: "#ffffff"
  ink: "#171321"
  ink-inverse: "#ffffff"
  primary: "#171321"
  on-primary: "#ffffff"

typography:
  display-hero:
    fontFamily: "GitLab Sans"
    fontSize: 96px
    fontWeight: 660
    lineHeight: 1.05
    letterSpacing: -2.88px
  h2-panel:
    fontFamily: "GitLab Sans"
    fontSize: 24px
    fontWeight: 580
    lineHeight: 1.2
    letterSpacing: -0.48px
  button:
    fontFamily: "GitLab Sans"
    fontSize: 18px
    fontWeight: 660
    lineHeight: 1.3
    letterSpacing: normal

rounded:
  sm: 4px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 11px 16px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 11px 16px 11px 0px
---

## Overview

GitLab's marketing homepage (about.gitlab.com) runs a white canvas (`{colors.canvas}`) with a near-black plum ink (`{colors.ink}` #171321 — not pure black) for text and the primary CTA fill. Display type uses GitLab's custom variable face **GitLab Sans**, tuned to fractional weights (660 at hero, 580 at panel headlines) rather than round 400/600/700 steps — a variable-font-specific convention — with very steep negative tracking at hero size: -2.88px at 96px, roughly -3% of type size.

The primary CTA ("Get free trial") uses the same near-black plum as body ink, rendered as a compact rectangular button with a modest 4px radius — a restrained shape choice relative to the pill-forward conventions seen at OpenAI/Cloudflare/Robinhood. Section panels invert to dark backgrounds with white 24px/580 headlines.

**Key Characteristics:**
- **Near-black plum** (#171321), not pure black, as both ink and primary CTA fill.
- **GitLab Sans variable font** at fractional weights (580, 660) with steep negative tracking (~-3% at hero size).
- **4px-radius rectangular buttons** — restrained, not pill-shaped.
- Ink-colored CTA (button fill matches body text color) rather than a distinct brand hue.
- Dark feature panels with white headline text nested inside an otherwise white-canvas page.

## Colors

> Source: about.gitlab.com homepage, computed styles read live via browser DOM inspection.

- **Canvas** ({colors.canvas}): #ffffff — page background.
- **Ink** ({colors.ink}): #171321 — headline/body text and primary button fill.
- **Ink Inverse** ({colors.ink-inverse}): #ffffff — text on dark feature panels and on the primary CTA.
- **Primary** ({colors.primary}): #171321 — CTA fill, identical to ink (no separate brand accent observed on the sampled homepage).
- **On Primary** ({colors.on-primary}): #ffffff — CTA label text.

## Typography

### Font Family
- **GitLab Sans** — sole typeface observed across hero, panel headlines, body, and buttons.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 96px | 660 | -2.88px | Hero headline ("Speed you can trust, all the way to prod") |
| `{typography.h2-panel}` | 24px | 580 | -0.48px | Dark-panel section headlines |
| `{typography.button}` | 18px | 660 | normal | Primary CTA label |

## Components

### Buttons

**`button-primary`** — Plum rectangular CTA ("Get free trial", "Get your free trial").
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.sm}` (4px), padding 11px 16px (large) or 8px 12px (compact nav variant).

**`button-ghost`** — Transparent text-link button ("Contact sales").
- Background transparent, text `{colors.ink}`, rounded `{rounded.sm}`, padding 11px 16px 11px 0px (asymmetric, no right-hand visual button chrome).

## Do's and Don'ts

### Do
- Use the near-black plum (#171321) for both ink and CTA fill — GitLab doesn't rely on a separate saturated brand hue on this page.
- Tune type weight to fractional variable-font values (580/660) rather than snapping to 400/700.
- Keep buttons at a modest 4px radius.

### Don't
- Don't pill the CTA — GitLab's convention here is a compact rectangle, not a rounded/pill shape.
- Don't apply hero-level tracking (-3%) to body text — it's a display-only effect.

## Known Gaps

- Analysis covers the marketing homepage only (about.gitlab.com/), read via live computed-style inspection; the in-product GitLab UI (issues, MRs, pipelines) uses a separate design system (Pajamas) and was not inspected.
- A cookie-consent banner was present at capture time; its buttons (dark rectangle, 2px radius) were filtered out of the primary CTA analysis but may reflect a slightly different micro-component than the true marketing CTA.
- GitLab's signature orange (commonly associated with the brand, e.g. the logo/tanuki mark) was not found among sampled button fills on this page and is therefore not documented here as a verified token.
