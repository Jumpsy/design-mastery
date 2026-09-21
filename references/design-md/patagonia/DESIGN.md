---
version: alpha
name: Patagonia-design-analysis
description: "A photography-led, black-and-white marketing system: pure black pill CTAs (30px radius) on white text, custom light-weight typeface 'Ridgeway Sans' at 300-500 weight with negative tracking on the hero (-1.28px at 64px), and an unusually light body-text weight (300) for a retail brand — restrained and editorial rather than product-forward. No chromatic brand accent was found on the sampled homepage; the system relies entirely on black/white and large lifestyle photography for its identity."

colors:
  ink: "#000000"
  ink-inverse: "#ffffff"
  primary: "#000000"
  on-primary: "#ffffff"

typography:
  display-hero:
    fontFamily: "Ridgeway Sans"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -1.28px
  body:
    fontFamily: "Ridgeway Sans"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: normal
  button:
    fontFamily: "Ridgeway Sans"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: normal

rounded:
  pill: 30px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    padding: 5px 20px
---

## Overview

Patagonia's marketing homepage (served regionally at patagonia.ca) is entirely black-and-white and photography-led — hero headline text is set in white (`{colors.ink-inverse}`) directly over large lifestyle photography, with the single interactive accent being a solid black pill button. No chromatic brand color was found among the sampled buttons/links — a deliberate restraint distinct from every other brand in this collection, which all carry at least one saturated accent hue.

Type runs in the custom **Ridgeway Sans**, at a notably light body weight (300, uncommon among retail/e-commerce sites which typically run 400+ for legibility) and a mid-weight 500 for both the hero headline and button labels. The hero applies tight -1.28px tracking (≈-2% of size) at 64px, consistent with the editorial/understated register.

**Key Characteristics:**
- **No chromatic brand accent observed** — the system runs entirely on black/white against photography.
- **Solid black pill CTAs** (30px radius) with white text — small, compact button sizing (12px label, 5px/20px padding).
- **Ridgeway Sans** custom face at an unusually light 300 body weight.
- Tight negative tracking on hero display (-2% at 64px).
- Photography-first layout — type is secondary to large full-bleed imagery.

## Colors

> Source: patagonia.ca homepage (regional redirect from patagonia.com), computed styles read live via browser DOM inspection.

- **Ink** ({colors.ink}): #000000 — primary CTA fill and default text color.
- **Ink Inverse** ({colors.ink-inverse}): #ffffff — headline text set over photography, and CTA label text.
- **Primary** ({colors.primary}): #000000 — same as ink; the CTA fill and body-ink color are identical, no separate accent.
- **On Primary** ({colors.on-primary}): #ffffff — CTA label text.

## Typography

### Font Family
- **Ridgeway Sans** — sole custom typeface observed, spanning hero, body, and button labels at varying weights (300-500).

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 64px | 500 | -1.28px | Hero headline ("Relentlessly Refined") |
| `{typography.body}` | 14px | 300 | normal | Default body text — unusually light weight |
| `{typography.button}` | 12px | 500 | normal | CTA button labels |

## Components

### Buttons

**`button-primary`** — Solid black pill CTA ("Take Action").
- Background `{colors.primary}`, text `{colors.on-primary}`, rounded `{rounded.pill}` (30px), padding 5px 20px — notably compact/small relative to most other brands' hero CTAs.

## Do's and Don'ts

### Do
- Let photography carry the visual identity — don't compensate with a chromatic UI accent.
- Use the light 300 body weight for a quieter, editorial register.
- Keep CTA buttons small and black/white, not brand-colored.

### Don't
- Don't introduce a saturated accent color — this system's restraint is a deliberate brand signal.
- Don't inflate button size/weight — the sampled CTA is deliberately compact (12px label, 5px/20px padding).

## Known Gaps

- Analysis covers the marketing homepage only, served via a regional (.ca) redirect from patagonia.com; the direct .com experience for a US visitor was not independently re-verified and may differ slightly.
- Product listing/PDP (product detail page) styling, which likely introduces price/badge colors, was not inspected.
- No chromatic accent was found in the sampled homepage buttons/links — this is reported as an honest finding, not a claim that Patagonia's broader design system never uses color (e.g. product imagery, sale badges).
