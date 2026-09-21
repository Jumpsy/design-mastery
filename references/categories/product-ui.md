# Product UI (web app screens, cards, forms, pricing)

**Structure**: one primary action per screen/card, visually dominant (size, contrast,
position bottom or bottom-right). Secondary actions text-weight, not competing buttons.

**Spacing**: 4px or 8px base grid, no ad hoc values. Card padding typically 24–40px.
Vertical rhythm inside a card: label→value pairs get 12–16px internal padding with a
1px hairline divider only when >3 rows (fewer rows: whitespace alone, no dividers).

**Radius/elevation**: pick one radius scale (sharp / 8px / 16px / full-pill) and apply
consistently — mixing radii across nested elements is the #1 "off" signal. Elevation:
flat OR one soft ambient shadow system, never per-element ad hoc shadows.

**Color**: 1 accent color used for CTA + focus states only; everything else neutral
(ink/surface/border/muted-text). Reusing the CTA accent as a "house color" elsewhere
(icon strokes, decorative rules) is a deliberate signature move, not noise.

**Anti-patterns**: cards-inside-cards, colored left-border strip, drop shadow on every
element, emoji as icons, unstyled mismatched icon library, tiny illegible badges as fake
"texture."

**Verified build**: `plan-gate-live-test/pricing-card.html` — Instrument Serif tier
name + price, Inter body, warm cream surface on darker cream bg, ink-red CTA pill,
hairline dividers only between feature rows. Rendered and visually confirmed.
