---
version: alpha
name: Calendly-design-analysis
description: "A warm off-white canvas (#fcfbf8, not pure white) marketing system paired with a deep navy ink (#071a31) used as both text color and the primary CTA fill — an inversion of the more common white-button-on-dark convention. Display type runs in the custom face 'Calendly Sans' at 72px/500 with tight -2px tracking, while body/UI text uses 'Geist'. A pale sky-blue (#84c1ff) appears as a small announcement-banner accent, distinct from the primary navy CTA."

colors:
  canvas: "#fcfbf8"
  ink: "#071a31"
  on-primary: "#fcfbf8"
  banner-accent: "#84c1ff"

typography:
  display-hero:
    fontFamily: "Calendly Sans"
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -2px
  h2:
    fontFamily: "Geist"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: normal
  body:
    fontFamily: "Geist"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: normal

rounded:
  pill: 16px

components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.pill}"
    padding: 12px 16px
  banner-pill:
    backgroundColor: "{colors.banner-accent}"
    textColor: "{colors.ink}"
    rounded: 0px
    padding: 8px 48px 8px 32px
---

## Overview

Calendly's marketing homepage sits on a warm off-white canvas (`{colors.canvas}` #fcfbf8 — noticeably not pure #ffffff, giving a slightly paper-like warmth) with a deep navy ink (`{colors.ink}` #071a31) used for both headline/body text and, notably, the primary CTA fill — an inversion of the more common pattern (dark text, colored button); here the CTA borrows the same navy as the body ink rather than introducing a separate brand hue.

Display type runs in the custom face **Calendly Sans** at 72px/500 with tight -2px tracking (≈-2.8% of size), while body and secondary headlines use **Geist**, a widely-adopted open grotesk, at normal tracking — so the system pairs one custom face for the largest display moment with a standard face for everything else.

A pale sky-blue (`{colors.banner-accent}` #84c1ff) appears as a small top-of-page announcement banner ("Introducing the new Calendly") — a distinct, softer accent from the primary navy CTA, used for low-priority/informational surfaces rather than action buttons.

**Key Characteristics:**
- **Warm off-white canvas** (#fcfbf8), not pure white.
- **Navy-on-cream CTA** — the button borrows the body-ink color rather than a separate brand hue.
- **Calendly Sans** custom face reserved for hero display only; **Geist** for everything else.
- **16px-radius buttons** — soft rounded-rectangle, not full pill despite the visual impression.
- Sky-blue (#84c1ff) reserved for low-priority banner/announcement surfaces.

## Colors

> Source: calendly.com homepage, computed styles read live via browser DOM inspection.

- **Canvas** ({colors.canvas}): #fcfbf8 — page background, warm off-white.
- **Ink** ({colors.ink}): #071a31 — headline/body text and primary CTA fill.
- **On Primary** ({colors.on-primary}): #fcfbf8 — CTA label text (the canvas color, reused).
- **Banner Accent** ({colors.banner-accent}): #84c1ff — pale sky-blue, announcement banner only.

## Typography

### Font Family
- **Calendly Sans** — custom face reserved for the largest hero headline.
- **Geist** — open grotesk used for section headlines, body, and UI chrome.

### Hierarchy

| Token | Size | Weight | Letter Spacing | Use |
|---|---|---|---|---|
| `{typography.display-hero}` | 72px | 500 | -2px | Hero headline ("All the work around meetings, handled.") |
| `{typography.h2}` | 36px | 500 | normal | Section headline ("Book meetings with the world's #1 scheduling tool") |
| `{typography.body}` | 16px | 400 | normal | Body copy |

## Components

### Buttons

**`button-primary`** — Navy rounded-rectangle CTA ("Get started for free").
- Background `{colors.ink}`, text `{colors.on-primary}`, rounded `{rounded.pill}` (16px), padding 12px 16px.

**`banner-pill`** — Sky-blue announcement banner, square-cornered with asymmetric right-heavy padding.
- Background `{colors.banner-accent}`, text `{colors.ink}`, rounded 0px, padding 8px 48px 8px 32px.

## Do's and Don'ts

### Do
- Reuse the navy ink color for the primary CTA rather than introducing a separate brand hue.
- Keep the canvas warm off-white (#fcfbf8), not pure white.
- Reserve Calendly Sans for hero-scale display text only.

### Don't
- Don't treat the sky-blue banner accent as the primary CTA color — it's scoped to low-priority announcement surfaces.
- Don't round buttons into a full pill — this system uses a 16px rounded-rectangle, not 9999px.

## Known Gaps

- Analysis covers the marketing homepage only (calendly.com/), read via live computed-style inspection; the in-app scheduling/booking product UI was not inspected.
- Card/panel elevation and shadow treatment were not sampled in this pass.
- Dark-mode variant, if any, was not inspected.
