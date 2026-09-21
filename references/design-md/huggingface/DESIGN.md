---
version: alpha
name: HuggingFace-design-analysis
description: "A white-canvas, black-and-white-forward marketing system: the primary CTA ('Sign Up') is a near-black slate pill (oklch(0.21 0.034 264.665), a cool dark charcoal rather than pure black), and secondary utility buttons sit on a pale gray wash (oklch(0.928 0.006 264.531)). Hero type is Source Sans Pro at 60px/700 with normal (not negative) letter-spacing — a plainer, more community/documentation-flavored type choice than the tightly-tracked custom grotesks used by most AI-lab competitors. Buttons mix full-pill CTAs with 8px-radius utility buttons."

colors:
  canvas: "#ffffff"
  ink: "#000000"
  primary-cta: "oklch(0.21 0.034 264.665)"
  on-primary-cta: "#ffffff"
  surface-wash: "oklch(0.928 0.006 264.531)"
  surface-wash-dark: "oklab(0.999994 0.0000455678 0.0000200868 / 0.1)"

typography:
  display-hero:
    fontFamily: "Source Sans Pro"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: normal
  body:
    fontFamily: "Source Sans Pro"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  pill: 3.36e7px
  sm: 8px

components:
  button-primary:
    backgroundColor: "{colors.primary-cta}"
    textColor: "{colors.on-primary-cta}"
    rounded: "{rounded.pill}"
    padding: 6px 10px
  button-utility:
    backgroundColor: "{colors.surface-wash}"
    textColor: "{colors.primary-cta}"
    rounded: "{rounded.sm}"
    padding: 4px 14px
  button-utility-inverse:
    backgroundColor: "{colors.surface-wash-dark}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: 8px 16px
---

## Overview

Hugging Face's marketing homepage runs a plain white canvas (`{colors.canvas}`) with black ink (`{colors.ink}`) — a deliberately unadorned, community/open-source aesthetic rather than a heavily branded one. The primary CTA ("Sign Up") uses a near-black cool-charcoal fill defined in the modern `oklch()` color space (`{colors.primary-cta}`, oklch(0.21 0.034 264.665) — a very dark slate, not pure #000000), rendered as a full pill.

Secondary/utility links ("Getting started") sit on a pale gray wash (`{colors.surface-wash}`, oklch(0.928 0.006 264.531)) with 8px-radius corners rather than a pill — so the page mixes two distinct button shapes: **pill for the primary CTA, 8px-radius rectangle for utility actions** — the opposite convention from brands that pill everything.

Hero type is set in **Source Sans Pro** at 60px/700 with normal (unmodified) letter-spacing — notably plainer than the negative-tracked custom grotesks (OpenAI Sans, Mona Sans, FT Kunst Grotesk) used by most other AI/dev-tool brands in this collection, reinforcing Hugging Face's community-documentation register over a slick product-marketing one.

**Key Characteristics:**
- **Plain white canvas, black ink** — no dark-mode-first design on marketing surfaces.
- **oklch()-defined near-black CTA** rather than pure black or a branded hue.
- **Two-shape button system**: pill for primary, 8px rectangle for utility.
- **Source Sans Pro at normal tracking** — unusually un-tightened compared to peer AI-brand type systems.
- No custom/licensed display typeface observed — uses a standard open web font.

## Colors

> Source: huggingface.co homepage, computed styles read live via browser DOM inspection (colors returned in oklch/oklab by the browser; hex approximations noted where relevant).

- **Canvas** ({colors.canvas}): #ffffff — page background.
- **Ink** ({colors.ink}): #000000 — headline/body text.
- **Primary CTA** ({colors.primary-cta}): oklch(0.21 0.034 264.665) — dark cool-charcoal, ≈ #1c2130 in sRGB — "Sign Up" button fill.
- **On Primary CTA** ({colors.on-primary-cta}): #ffffff — text on the dark CTA.
- **Surface Wash** ({colors.surface-wash}): oklch(0.928 0.006 264.531) — pale cool-gray, ≈ #e4e5e9 — utility button fill on light sections.
- **Surface Wash Dark** ({colors.surface-wash-dark}): oklab(0.999994 0.0000455678 0.0000200868 / 0.1) — a 10%-opacity near-white wash used for utility buttons on dark sub-sections (e.g. the Enterprise feature list).

## Typography

### Font Family
- **Source Sans Pro** (with `-apple-system, system-ui, Segoe UI, Roboto` fallback stack) — the sole typeface observed for both hero display and body text.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 60px | 700 | normal | Hero headline ("The AI community building the future.") |
| `{typography.body}` | 16px | 400 | normal | Default body text |

### Principles
- No negative tracking applied anywhere sampled — a deliberate plainness relative to peer AI-brand type systems.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.pill}` | ~33554432px (effectively infinite/pill) | Primary "Sign Up" CTA |
| `{rounded.sm}` | 8px | Utility buttons ("Getting started", enterprise feature links) |

## Components

### Buttons

**`button-primary`** — Dark pill CTA ("Sign Up").
- Background `{colors.primary-cta}`, text `{colors.on-primary-cta}`, rounded `{rounded.pill}`, padding 6px 10px (compact nav-level sizing).

**`button-utility`** — Light-gray 8px-radius utility link on white/light sections.
- Background `{colors.surface-wash}`, text `{colors.primary-cta}`, rounded `{rounded.sm}`, padding 4px 14px.

**`button-utility-inverse`** — 10%-opacity white wash for utility links on dark sub-sections.
- Background `{colors.surface-wash-dark}`, text white, rounded `{rounded.sm}`, padding 8px 16px.

## Do's and Don'ts

### Do
- Keep the primary CTA as a pill; keep utility actions as 8px-radius rectangles — don't collapse the two shapes into one.
- Use the near-black oklch charcoal for the primary CTA rather than pure black.
- Leave hero type at normal tracking — this brand doesn't rely on tightened display type for polish.

### Don't
- Don't apply negative letter-spacing to headlines — it's not part of this system's convention.
- Don't introduce a saturated brand hue as a CTA fill on the sampled homepage sections — the observed CTAs are neutral (charcoal/gray), not colorful.

## Known Gaps

- Analysis covers the marketing homepage only (huggingface.co/), read via live computed-style inspection; a targeted color scan for Hugging Face's commonly-referenced yellow brand mark (used on the logo/emoji) returned no matches in the sampled DOM subset, so it is not documented here as a verified token — only what was actually measured is included.
- Model/dataset card UI (the core product surface) was not inspected in this pass.
- Dark-mode variant was not inspected.
