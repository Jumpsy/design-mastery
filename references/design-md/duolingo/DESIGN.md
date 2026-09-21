---
version: alpha
name: Duolingo-design-analysis
description: "A white-canvas, mascot-driven marketing system built on Duolingo's two signature hues: bright leaf-green (#58cc02) and a deep navy (#042c60), both used as headline text colors rather than fills in the sampled hero. Display type runs in Duolingo's custom rounded geometric sans 'feather' at a bold 700 weight with unusually aggressive negative tracking for a 'friendly' brand (-1.28px at 64px, ≈ -2% of size) — proof that playful/rounded brands can still track tight. A secondary custom face, 'duolingo-sans', handles a smaller sub-headline at 32px/700 with normal tracking. The page leans heavily on character illustration (the Duo owl) rather than photography."

colors:
  canvas: "#ffffff"
  brand-green: "#58cc02"
  brand-navy: "#042c60"
  ink-secondary: "#4b4b4b"
  ink-tertiary: "#3c3c3c"

typography:
  display-hero:
    fontFamily: "feather"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1.28px
  subhead:
    fontFamily: "duolingo-sans"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: normal
  body:
    fontFamily: "sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: normal
---

## Overview

Duolingo's marketing homepage sits on a plain white canvas (`{colors.canvas}`) and leans on two brand hues used as **text color**, not fill, in the sampled hero: the signature leaf-green (`{colors.brand-green}` #58cc02, on "learn a language with duolingo") and a deep navy (`{colors.brand-navy}` #042c60, on "learn anytime, anywhere") — both set at the same 64px/700 size, splitting the hero headline across two colors rather than one.

Display type runs in **feather**, Duolingo's custom rounded-geometric display face, at weight 700 with -1.28px tracking at 64px (≈ -2% of size) — notably tight for a brand whose visual language (rounded mascot, bubble UI) otherwise reads as maximally friendly/soft. A second custom face, **duolingo-sans**, carries a smaller 32px/700 sub-headline at normal (untracked) spacing — so the two custom faces are used deliberately at different tracking disciplines depending on size/role.

**Key Characteristics:**
- **Two-hue brand system** (green #58cc02, navy #042c60) applied as headline text color, splitting a single hero statement across both.
- **feather** custom rounded-geometric face for the largest display text, with tight tracking (-2% at 64px) despite the brand's otherwise soft/playful register.
- **duolingo-sans** secondary custom face for mid-size subheads at normal tracking.
- Body/secondary text uses muted grays (#4b4b4b, #3c3c3c) rather than pure black.
- Character-illustration-led (the Duo owl mascot) rather than photography-led.

## Colors

> Source: duolingo.com homepage, computed styles read live via browser DOM inspection.

- **Canvas** ({colors.canvas}): #ffffff — page background.
- **Brand Green** ({colors.brand-green}): #58cc02 — Duolingo's signature leaf-green, used as headline text color.
- **Brand Navy** ({colors.brand-navy}): #042c60 — deep navy, used as headline text color paired with the green line.
- **Ink Secondary** ({colors.ink-secondary}): #4b4b4b — sub-headline text.
- **Ink Tertiary** ({colors.ink-tertiary}): #3c3c3c — body copy.

## Typography

### Font Family
- **feather** — custom rounded-geometric display face for the largest hero headline text.
- **duolingo-sans** — custom face for mid-size sub-headlines.
- System sans-serif fallback for body copy.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 64px | 700 | -1.28px | Hero headline, split across brand-green and brand-navy |
| `{typography.subhead}` | 32px | 700 | normal | "The most fun way to learn languages" sub-headline |
| `{typography.body}` | 17px | 500 | normal | Body copy |

## Do's and Don'ts

### Do
- Reserve the two brand hues (green, navy) for headline text — Duolingo doesn't rely on colored button fills in the sampled hero region.
- Apply tight tracking (~-2%) even on a playful/rounded display face — friendliness and typographic discipline aren't mutually exclusive.
- Use muted grays (#4b4b4b / #3c3c3c), not pure black, for secondary/body text.

### Don't
- Don't flatten the two-color headline split into a single hue — the green/navy pairing is a deliberate brand device.
- Don't set body text in the display faces (feather/duolingo-sans) — body falls back to plain system sans.

## Known Gaps

- Button/CTA fill colors were not captured in this pass — the sampled DOM subset (first ~400 buttons/links) returned no colored button elements, likely because primary CTAs render below-the-fold, behind a cookie-consent iframe, or via client-side hydration not yet complete at sample time. This should be treated as an honest gap, not a claim that Duolingo has no colored buttons — the brand's product UI is well known for its bold green CTA buttons, but that was not independently re-verified here.
- Analysis covers the marketing homepage only (duolingo.com/), read via live computed-style inspection; in-app lesson UI was not inspected.
- Card/panel radius and shadow treatment were not sampled.
