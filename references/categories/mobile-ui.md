# Mobile UI

**Frame**: design at real device width (375–430px), not a scaled-down desktop layout.
Single-column by default; bottom-anchored primary actions (thumb reach), not top.

**Nav**: bottom tab bar (4–5 items max, icon+label) for primary navigation, or a single
back-arrow + title header for stacked flows — never both a hamburger and a tab bar.

**Touch targets**: minimum 44×44px hit area regardless of visible icon size. Spacing
between adjacent tappable rows ≥8px to prevent mis-taps.

**Typography**: base body 15–17px (mobile OS default), never below 13px for body text.
One display size for screen titles, one for section headers, one body size — resist
adding intermediate sizes.

**Motion**: screen transitions slide (push/pop), not fade, to preserve spatial model.
Sheet/modal presentations slide up + backdrop dim. Keep all transitions ≤300ms.

**Anti-patterns**: cramming desktop nav (top horizontal menu) onto mobile width, tiny
tap targets under 44px, text below 13px, more than one FAB-style floating button.

**Verified build**: `mobile-ui-demo/screen.html` at 390×844 — bottom nav bar (4 tabs),
top header with single title + icon, card list with 44px+ row height, rendered and
visually confirmed at native mobile viewport.
