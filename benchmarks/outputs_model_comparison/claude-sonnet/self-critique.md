# Self-critique — benchmark task #1 (developer API hero, "ship webhooks in minutes")

Running as: **Claude Sonnet 5** (model ID `claude-sonnet-5`).

## Plan gate (recorded before writing any code)

**Layout**: Two-column hero — left: eyebrow status pill, headline (with an inline
monospace "code chip" reading `POST /webhooks` set into the sentence itself), subhead,
one primary button + one monospace text-link secondary CTA, a 3-stat strip (p50 latency,
uptime, integration LOC). Right: a live-updating "event log" terminal panel showing
simulated webhook deliveries streaming in (status code, method, path, latency),
newest-row-in-oldest-row-out, capped rows. Below the fold: a plain logo/name proof strip,
no logo images, no carousel.

**Signature motif**: the terminal/event-log panel as the hero image, doing the actual
product's job (delivering + retrying webhooks) instead of decorative art — plus the
inline code-chip embedded directly in the H1 rather than as a separate badge.

**Palette/type direction**: near-black (`#0c0d0d`) background, warm amber accent
(`#ff7a29`) used only for the code chip, primary button, and cursor blink — one accent,
used sparingly, not a gradient. A muted terminal-green (`#7fd88f`) is used only for
live/success status dots, echoing real terminal conventions rather than being decorative.
Type: Space Grotesk (display/body — geometric, technical, not Inter) paired with IBM
Plex Mono (headline code-chip + entire terminal panel) — the mono face is load-bearing,
not a footnote font.

**Distinctiveness**: no gradient mesh, no abstract blob, no 3-icon grid. The hero image
*is* the product's core value prop (webhook delivery + retry) rendered as a believable,
animating log, not an illustration standing in for the feature.

**Gut-check 1 (wow?)**: Initial pass risked reading as "competent infra-hero, seen it."
Pushed further by: (a) making the code path literally inline inside the H1 typography
instead of a separate badge above/below it, (b) giving the terminal panel a real product
behavior — retries with a distinct accent-colored status treatment for 429/502 — instead
of an all-green fake log, (c) a cursor-reactive amber glow confined to the hero only (one
per page, per §3).

**Gut-check 2 (vibe-coded?)**: Checked against §2 before building — no purple/blue
gradient, no colored-circle icon grid, no left-border accent strips, no
cards-in-cards, no emoji, no stock photography, no pill-button pair with vague copy (CTA
copy is concrete: "Start sending events" / a real curl-shaped link). Passed; proceeded to
build.

## Self-critique against §2 anti-slop checklist (post-build)

- Purple/blue gradient hero — **avoided**. Near-black + single amber accent.
- Generic 3-icon feature grid with colored circles — **not present** (no feature grid at
  all in this hero-only scope, correctly matching the frozen prompt which asks only for
  the hero).
- Centered headline + subhead + two pill buttons + abstract blob — **avoided**: layout is
  asymmetric two-column, one primary button is a solid rectangle (5px radius, not a
  pill) and the secondary CTA is a monospace text link, not a second pill.
- Cards-inside-cards — **borderline, checked**: the event rows sit inside the terminal
  panel, which sits inside the page. This is a single level of deliberate containment
  (log line → terminal window) that mirrors a real UI convention (a terminal has rows
  inside a window), not decorative nesting, so I judge it as earning its structure rather
  than being generic card-stacking. Worth flagging as the one place a stricter reviewer
  could push back.
- Emoji as icons — **none used**.
- Tiny unreadable pills for fake texture — **none**; the eyebrow pill is a single,
  legible status line, not scattered badges.
- Uniform 8px-radius-everything — **avoided**: radius hierarchy is deliberate (5px
  buttons/status chips, 7px event rows, 10px nav pill, 16px terminal panel) — panel
  bigger/softer, small controls sharper.
- Inter + default Tailwind spacing, no point of view — **avoided**: Space Grotesk +
  IBM Plex Mono pairing, custom spacing scale (not Tailwind defaults), monospace treated
  as a first-class display element in the H1 itself.
- Lorem-ipsum-shaped vague copy — **avoided**: subhead and stats name concrete
  capabilities (signing, retries, replay) and concrete numbers (41ms p50, 99.98%
  uptime, 6 lines to integrate) rather than "powerful, flexible, seamless" filler.
- Stock-photo people at laptops — **none**; no photography used at all, correct call for
  an infra/API product per the category file's "match imagery to brand" guidance.
- Drop shadows on every element — **avoided**: exactly one soft elevation shadow, under
  the terminal panel only, everything else is flat / border-defined.
- Full-bleed low-contrast color blocks "for aesthetic" — **not present**.
- Glassmorphism/backdrop-blur as a crutch — **not used anywhere**.
- Mismatched icon libraries — **no icon library used** (dots/status chips are drawn with
  CSS, not an icon set), so this doesn't apply.
- Colored left-border accent strip on cards — **explicitly avoided**; checked the event
  rows and stat blocks specifically for this since it's called out as the single most
  reliable tell, and there is no colored left border anywhere in the file.

## Honest weaknesses / things a harsher critic could flag

- The simulated live-log JS is a `setInterval` push/pop, not a real scroll-timeline or
  `useScroll`-driven sequence — acceptable for a static single-file hero demo, but §3
  distinguishes "real engineering" scroll-driven storytelling from "faked" CSS animation;
  this hero doesn't attempt scroll-driven storytelling at all (correctly, since it's an
  above-the-fold hero, not a scroll-triggered feature reveal), but if judged against that
  bar directly it would score as "decorative" rather than "engineered" motion.
  Interaction feedback (button hover/active, link hover) does follow the 120–180ms
  ease-out guidance.
- The event log's retry rows (429/502) reuse the same amber as the brand accent color —
  a stricter design-systems reviewer might want a status-only third color to avoid
  overloading amber with two meanings (brand accent AND "needs retry"). I judged this an
  acceptable trade-off to keep to "one accent" discipline, but it's a real tension worth
  naming rather than hiding.
- No dark/light mode toggle — the whole page assumes dark is the brand default (a
  legitimate technical-product choice, not an oversight), but the frozen prompt didn't
  ask for a mode switch either way, so this is a scope note, not a gap.
- Logo/proof strip is plain text company names rather than actual logomarks — an honest
  placeholder given these are fictional companies for a benchmark; a real build would
  need actual logo assets or should drop the strip rather than fake logos.

## Verification performed

Opened the file directly in Chrome and took a screenshot to confirm actual render (not
just code review): confirmed the near-black background, amber inline code-chip inside
the H1, monospace terminal panel, and status-pill eyebrow all render as designed at
normal viewport width before calling this done.

## Convergence round 1

An independent grader found 7 material defects. All were fixed for real (root-cause
fixes, not surface patches):

1. **`--ink-faint` WCAG contrast failure.** `#63665f` on `--bg` (~3.33:1) and
   `--bg-raised` (~3.16:1) both failed AA 4.5:1. Recalculated relative luminance by hand
   for both backgrounds and solved for the minimum text luminance needed, then picked
   `#8b8e87`, which gives ≈5.86:1 against `--bg` and ≈5.55:1 against `--bg-raised` — both
   pass AA with margin. Since every flagged element (`.proof-label`, `.proof-row span`,
   `.stat span`, `.panel-title`, `.panel-footer`, `.event .method`, `.event .ms`) already
   referenced the `--ink-faint` token, changing the single token value fixed all of them
   at once rather than patching each rule.

2. **Accent color overloaded for brand + error.** `--accent` (`#ff7a29`, orange) was both
   the CTA/brand color and the retry/failed-webhook status color. Added a new
   `--danger:#ff6b6b` token (verified ≈7.0:1 vs `--bg`, ≈6.65:1 vs `--bg-raised`) and
   repointed `.event .status.retry`'s `color` and `background` (converted the rgba to the
   new color's RGB, same ~0.12 alpha) to it. `--accent` is now used only for brand/CTA
   purposes (logo mark, code-chip, primary button, glow, blinking cursor) — this also
   directly resolves the honest-weakness note from the original critique above, which had
   flagged this exact overload as an acceptable-but-real tension; it's no longer a
   tension.

3. **Mobile nav vanished at ≤920px.** `nav{display:none}` removed docs/pricing/changelog/
   sign-in with no replacement. Added a real hamburger button (pure CSS three-line icon
   that morphs to an X via `aria-expanded`), shown only under the breakpoint, wired to a
   slide-down overlay panel (`.mobile-nav`, `max-height` transition) containing the same
   four links, dark-themed to match the rest of the page. Toggle is a small vanilla JS
   listener that flips an `.open` class and updates `aria-expanded`/`aria-label` on the
   button for accessibility.

4. **Fake "live" feed on an obvious loop.** The 10-item array cycled via `i % length` on
   a fixed 1900ms `setInterval`, so it visibly repeated every ~19s. Expanded the pool to
   20 events (mixed paths, more 200s, more varied retry/error cases using the new
   `--danger` styling, varied latencies), switched selection to non-repeating random
   (`nextEvent()` rejects picking the same index twice in a row), and replaced the fixed
   interval with a recursive `setTimeout` jittered between 1400–2600ms. There's no longer
   a fixed period or a fixed sequence to notice on repeat viewing.

5. **Non-grid spacing values.** Audited every padding/margin/gap in the stylesheet and
   snapped anything not a multiple of 4px onto the grid: `.eyebrow` padding
   `5/12/5/9px → 4/12/4/8px`, margin-bottom `26px → 24px`; `h1` margin-bottom
   `22px → 24px`; `.sub` margin-bottom `34px → 32px`; `.cta-row` gap `22px → 24px`;
   `.btn-primary` padding `13px 22px → 12px 24px`; `.stats` gap `34px → 32px` (and its
   920px override `22px → 24px`); `.stat` padding-left `14px → 16px`; `.panel-body`
   padding `14px → 16px`; `.event` padding `11px 13px → 12px 12px`, gap `11px → 12px`;
   `.event .status` padding `2px 7px → 4px 8px`; `.panel-footer` padding
   `11px 16px → 12px 16px`; `.proof-label` margin-bottom `26px → 24px`; `.proof-row`
   padding-top `26px → 24px`. Values already on the grid (`.hero` gap `56px`, `.proof-row`
   gap `52px`, `.cta-row` margin-bottom `44px`, `.panel-bar`/`header` padding, etc.) were
   left untouched.

6. **No defined type scale.** Introduced a 1.25-ratio modular scale anchored at 16px as
   CSS custom properties (`--fs-00:10px`, `--fs-0:12px`, `--fs-1:13px`, `--fs-1b:14px`,
   `--fs-2:16px`, `--fs-3:20px`, `--fs-4:25px`, `--fs-5:31px`, plus `--fs-hero` for the
   display clamp), and replaced every bare ad hoc `font-size` in the stylesheet with the
   nearest token (11→`--fs-00` for the single-glyph logo mark, 12→`--fs-0`,
   12.5/13/13.5→`--fs-1`, 14.5→`--fs-1b`, 15/17→`--fs-2`, 20→`--fs-3`,
   `clamp(38px,4.6vw,62px)`→`--fs-hero`). `--fs-4`/`--fs-5` are defined for scale
   completeness even though this hero-only page doesn't currently need them at those
   sizes. The relative `0.52em` on the inline code-chip was left as-is since it's
   deliberately proportional to the parent H1 size, not an ad hoc absolute size.

7. **No `:focus-visible` styles.** Added designed keyboard-focus rings (brand-accent
   outline, `outline-offset` tuned per element so nothing clips) to every interactive
   element: `nav a` / `.nav-cta`, `.btn-primary`, `.link-ghost`, the new hamburger button,
   and the new mobile-nav links. All use `:focus-visible` (not `:focus`) so the ring only
   appears for keyboard navigation, not mouse clicks.

**Explicitly out of scope, not added:** a separate grader also flagged "missing feature
sections/pricing/footer" as a defect. That grader was reviewing this as if it were a full
landing page, but the frozen benchmark prompt for this file is "design a landing page
hero" — a hero-only section, deliberately paired with just the logo/proof strip. Adding
feature sections, pricing, or a footer would be scope creep beyond what was asked, so
that flag was intentionally not acted on here; the page remains hero + logo-strip only.

**Process note:** the multi-agent coding team (Codex, opencode, agy, freebuff) was tried
first per standing workflow, but all four were unavailable in this session (Codex over
its usage quota until 2026-09-20, opencode's MCP tools unresolved/not connected, agy
rate-limited with a ~2.5h reset, freebuff out of its hourly quota). With no delegate
available, the fixes above were implemented directly rather than blocking on quota
resets.

## Convergence round 2

An independent round-2 grader found 3 more defects. Fixed:

1. **`--accent-dim` and `--radius-md` declared but never referenced.** Both had real
   spots to earn their keep, so both were wired in rather than deleted.
   `--accent-dim` (`#c25e1f`) is now the `.btn-primary:active` background — previously
   `:active` only translated the button back down with no color change, so pressing it
   read identically to the resting state once the translateY settled; it now visibly
   darkens on press, giving a real pressed-state affordance. `--radius-md` (`10px`)
   replaced the hardcoded `border-radius:7px` on `.event` (the terminal feed rows), which
   was the one card-like element using an ad hoc radius between `--radius-sm` (5px) and
   `--radius-lg` (16px) instead of a token; the radius bumps from 7px to 10px, a minor,
   intentional visual nudge to make the row genuinely medium between the two named
   extremes rather than a third unnamed magic number.

2. **Type-scale comment overclaimed a pure 1.25 ratio.** The step values below the 16px
   base (10, 12, 13, 14px) don't follow 1.25 — they're deliberately hand-picked for tight
   UI text (status chips, mono labels) where a strict geometric progression would either
   be too coarse or produce non-integer pixel values. Rather than rewrite the token values
   (which would risk visual regressions across every small-text element already tuned
   against these numbers), the comment was corrected to `/* type scale — 1.25 ratio above
   base (16px); smaller sizes hand-tuned for tight UI text */`, which accurately describes
   what the scale actually does: true 1.25 ratio from 16px up (16→20→25→31), ad hoc below
   it. No pixel values changed.

3. **`-webkit-font-smoothing: antialiased` had no Firefox equivalent.** Added
   `-moz-osx-font-smoothing: grayscale;` immediately after it on `body`, matching the
   standard pairing so text rendering is smoothed consistently on Firefox/macOS as well
   as WebKit/Blink browsers.

## Convergence round 3

An independent round-3 grader found 8 more defects. Fixed:

1. **Mobile nav links stayed keyboard-focusable while visually collapsed (WCAG
   2.4.3/2.1.1).** `.mobile-nav` was hidden only via `max-height:0; overflow:hidden`,
   so its four links remained in the tab order (and exposed to assistive tech) even
   when invisible; the `navToggle` click handler only flipped `aria-expanded` on the
   button, never touching the nav itself. Added the `inert` attribute to `#mobileNav`
   in the closed (default) markup state, and the click handler now removes `inert` when
   opening and re-adds it when closing, in the same listener that already updates
   `aria-expanded`/`aria-label`. `inert` removes the subtree from both tab order and the
   accessibility tree natively, so collapsed links can no longer receive keyboard focus,
   while the existing `max-height` slide animation is untouched.

2. **Dead `--fs-4:25px` / `--fs-5:31px` tokens.** Neither was referenced anywhere in the
   file (confirmed by search). Removed both declarations rather than inventing new
   usages for them, and rewrote the scale comment to describe only the tokens actually
   in use: `/* type scale — small sizes hand-tuned for tight UI text; fs-hero is a
   clamp() for the hero heading */` (the old comment's "1.25 ratio above base" claim no
   longer applies once the only tokens above `--fs-2` are `--fs-3` and the already-clamp
   `--fs-hero`).

3. **`.logo-mark` hardcoded `border-radius:5px`.** Replaced with `var(--radius-sm)`,
   which is already defined as `5px` — same rendered radius, now token-driven.

4. **`.code-chip` used a one-off `border-radius:7px`.** Matched to the nearest declared
   radius step: `var(--radius-sm)` (5px), closer than `--radius-md` (10px). Replaced the
   magic number with the token.

5. **`.nav-cta{color:var(--ink) !important;}`.** The `!important` was only needed
   because `.nav-cta` (specificity 0,1,0) was losing to `nav a{color:var(--ink-dim);}`
   (specificity 0,1,1). Rewrote the selector to `nav a.nav-cta` (specificity 0,2,1),
   which legitimately outranks `nav a` without any `!important` hack; the `:hover`/
   `:focus-visible` rules referencing `.nav-cta` alone were left as-is since they don't
   touch `color` and aren't affected by this specificity fight.

6. **Simulated "live" event feed had no disclosure.** The `events / production` panel
   with its pulsing green "live" dot streams `Math.random()`-generated rows with nothing
   telling a viewer it's fake. Added a small visible `simulated` tag (`.panel-sim-tag`,
   monospace, faint border, uppercase, tiny letter-spacing) next to the `events /
   production` panel title in the panel header — visually consistent with the existing
   terminal-chrome aesthetic, not a comment or hidden attribute.

7. **`--fs-1b:14px` broke the numeric naming convention** (`00, 0, 1, 2, 3, ...`). Since
   14px sits only 1px from the existing `--fs-1` (13px) — versus 3px from `--fs-2`
   (16px) — folded it into `--fs-1` rather than inventing another numeric slot: removed
   the `--fs-1b` declaration and repointed its one usage (`.btn-primary`'s `font-size`)
   to `var(--fs-1)`. The scale comment (already rewritten per item 2) no longer
   references the retired token.

8. **`.mobile-nav{display:none;}` redundantly re-declared inside `@media
   (min-width:921px)`**, identical to the base rule already in effect above 920px (the
   `@media (max-width:920px)` block is what turns it on). Removed the no-op duplicate
   media query block entirely; behavior is unchanged since the base rule already covers
   it.

## Convergence round 4

An independent round-4 grader found 1 more defect. Fixed:

1. **Terminal panel told three contradictory stories at once.** The panel header showed
   `events / production` as its title, a `simulated` tag (added in round 3) right next to
   it, and a green pulsing `.dot` labeled `live` — plus a `listening…` cursor in the
   footer. Production vs. simulated vs. live-pulsing-green are mutually contradictory
   signals for the same panel: a viewer can't tell if this is a real production
   connection, a simulated demo, or a live stream. Root cause was that round 3 patched the
   disclosure gap by adding the `simulated` tag without reconciling it against the
   pre-existing `production` title and green `live` indicator it now directly contradicted.
   Resolved by converging on one honest story instead of three competing labels:
   - `.panel-title` text changed from `events / production` to `events / simulated`,
     matching the `simulated` tag it now agrees with rather than contradicts.
   - `.panel-live`'s label changed from `live` to `demo`, and its color source changed
     from `var(--ok)` (terminal green, a "this is really live" signal) to
     `var(--ink-faint)` (the same neutral gray already used for `.panel-title` and other
     faint chrome text) on both the text color and the `.dot` background. The pulse
     animation and the `tail -f events.log` / `listening…` cursor in the footer were left
     untouched — a neutral-colored pulsing dot labeled "demo" reads as "this animation is
     running" rather than "this is a live production feed," so the footer's terminal-tail
     flavor text no longer conflicts with it once the color/label are neutral.
   No other panel markup, the event-generation script, or any element outside this panel
   was touched.

## Convergence round 5

An independent round-5 grader found 3 more defects. Fixed:

1. **`--line` (`#26282a`) on `--bg` (`#0c0d0d`) failed WCAG 1.4.11 (~1.3:1) as the sole
   border on `.hamburger` and `.nav-cta`.** Both are interactive-component boundaries, so
   their border needed ≥3:1 against the page background. Rather than lighten `--line`
   globally (which would also brighten every decorative divider/hairline still using it —
   `.eyebrow`, `.code-chip`, `.panel`, `.panel-dots`, `.panel-sim-tag` — none of which are
   required to meet 1.4.11 since they're not interactive-component boundaries), added a
   new token `--line-strong:#6b6e70` and repointed only `.nav-cta`'s and `.hamburger`'s
   `border` to it. Hand-computed relative luminance: `--bg` luminance ≈0.00395,
   `--line-strong` luminance ≈0.1546, giving a contrast ratio ≈3.79:1 — comfortably over
   the 3:1 floor while staying a dark, desaturated gray consistent with the near-black
   aesthetic (not a jump to a light gray). Every other `--line` usage (dividers, non-
   interactive chrome) was left untouched.

2. **The simulated event feed (`#feed`) auto-updated indefinitely (~1.4–2.6s cadence) with
   no pause/stop/hide control and no live-region announcement (WCAG 2.2.2).** Added a
   visible, keyboard-accessible `Pause`/`Play` toggle button (`#feedToggle`, new
   `.feed-toggle` class using the same `--line-strong` border for its own 1.4.11
   compliance as an interactive control) placed in the panel header next to the existing
   `demo` indicator, wrapped together in a new `.panel-bar-right` flex group so the
   existing `.panel-bar{justify-content:space-between}` layout still works with two right-
   side children instead of one. The feed-scheduling JS was restructured around a
   `feedPaused` flag and a stored `feedTimeoutId`: `scheduleNext()` now bails immediately
   if paused, and the click handler either `clearTimeout`s the pending push (a real stop,
   not just a visual hide) or calls `scheduleNext()` again to resume the same jittered
   cadence, updating the button's label, `aria-pressed`, and `aria-label` each toggle.
   Separately, added `aria-live="polite"` (plus `aria-label="Simulated event feed"` for
   context) directly to the `#feed` container, so each new row is announced to assistive
   tech when the feed is running, and naturally goes silent while paused since no DOM
   mutations occur. No other panel behavior (the initial 4-row burst, jitter range, retry
   styling, decorative pulse/cursor animations) was changed.

3. **Type scale wasn't a real modular scale, and `--fs-1:13px` was a near-duplicate of
   `--fs-0:12px` used in identical contexts** (nav links, button label, ghost link,
   terminal feed text, proof-row text — all small mono/UI labels) with no distinguishing
   purpose from `--fs-0`. Removed the `--fs-1` token and repointed all four of its call
   sites (`nav a`, `.btn-primary`, `.link-ghost`, `.event`) to `var(--fs-0)` — chosen over
   `--fs-2` (16px) because 12px is 1px from 13px versus 16px being 3px away, so
   consolidating into `--fs-0` preserves the original visual output far more closely than
   consolidating into `--fs-2` would. Rewrote the type-scale comment to stop implying any
   ratio claim and instead honestly describe the resulting four-token set: `/* type
   scale — not a strict modular progression; --fs-00/--fs-0 cover tight mono/UI text,
   --fs-2/--fs-3 cover body/stat text, each hand-tuned per context rather than derived
   from a fixed ratio; fs-hero is a clamp() for the hero heading */`. No pixel values on
   `--fs-00`, `--fs-0`, `--fs-2`, `--fs-3`, or `--fs-hero` were changed — only `--fs-1`
   was removed and its four references repointed.

## Convergence round 6

An independent round-6 grader found 2 more defects. Fixed:

1. **Type scale used three different ratios and skipped a numeric slot.** With
   `--fs-00:10px`, `--fs-0:12px`, `--fs-2:16px`, `--fs-3:20px`, the actual step ratios
   were 12/10=1.2, 16/12=1.333, 20/16=1.25 — three different ratios in a four-token scale,
   and the naming jumped `00 → 0 → 2 → 3` with no `--fs-1` (a leftover from round 5's
   removal of the old `--fs-1`, which the round-5 fix correctly repointed usages away from
   but left the name gapped). Picked 1.25 as the single ratio (closest to the existing
   16→20 step, and `--fs-2`/`--fs-3` were left as the most-referenced, least-disruptive
   anchor) and derived the two smaller steps from it: `16/1.25 = 12.8 → rounded to 13px`,
   `12.8/1.25 = 10.24 → rounded to 10px`. Renamed the tokens sequentially with no gaps:
   `--fs-00 → --fs-0` (10px, was 10px — value unchanged, only renamed),
   `--fs-0 → --fs-1` (13px, was 12px — 1px rounding nudge), `--fs-2`/`--fs-3` unchanged
   (16px/20px). Updated every call site across the stylesheet (nav, logo mark, ghost link,
   panel title/tag/live text, event rows, stat labels, proof row, media-query overrides —
   26 usages total) to the renamed tokens; verified via `grep` that no bare `--fs-00` or
   orphaned old-name reference remained. Rewrote the type-scale comment to describe the
   real, now-consistent scale: `/* type scale — a consistent ~1.25 ratio anchored on
   --fs-2:16px, rounded to clean pixel values (16/1.25=12.8→13, 12.8/1.25≈10.24→10);
   --fs-0/--fs-1 cover tight mono/UI text, --fs-2/--fs-3 cover body/stat text; fs-hero is
   a clamp() for the hero heading */`.

2. **Several `gap` values didn't fit the file's 4px spacing grid.** Checked every flagged
   selector's actual value against multiples of 4 (4, 8, 12, 16, 20, 24, 28, 32…) before
   touching anything:
   - `.panel-bar-left{gap:9px}` — 9 ÷ 4 = 2.25, **genuine violation**. Nearest grid value
     is 8 (distance 1) vs. 12 (distance 3) → changed to `8px`.
   - `.link-ghost{gap:6px}` — 6 ÷ 4 = 1.5, **genuine violation**, equidistant between 4
     and 8. Chosen `8px` for visual consistency with the file's other icon+label pairs
     that already use `gap:8px` (the header brand mark and the nav CTA, both
     `display:(inline-)flex; align-items:center; gap:8px`), since `.link-ghost` is the
     same icon-plus-text-link pattern.
   - `.panel-dots{gap:6px}` — same 1.5 ratio, genuine violation. Chosen `4px` instead,
     since these are three small decorative status dots (a tight traffic-light-style
     cluster), where the tighter grid step reads better than spreading them to 8px.
   - `.panel-live{gap:6px}` — same violation. This is a small dot + one-word label (a
     compact status indicator, not a full icon+text link), so also set to `4px` to match
     the tight-cluster treatment used for `.panel-dots` rather than the wider link
     spacing used for `.link-ghost`.
   - `nav{gap:28px}` — 28 ÷ 4 = 7 exactly. **Not a violation**; left unchanged, per the
     task's own note that the grader may have been imprecise here.
   - `.proof-row{gap:52px}` — 52 ÷ 4 = 13 exactly. **Not a violation**; left unchanged,
     same reasoning.

   Left untouched, deliberately: `.link-ghost:hover{gap:9px}` (the hover-state gap on the
   same selector whose base value was fixed above) was not in the grader's named list of
   violations, and the task's explicit instruction was to change only genuinely-listed,
   off-grid values and touch nothing else — so this hover value was left as-is rather than
   speculatively "fixed" to match the new 8px base.

## Convergence reached (round 8)

Rounds 7 and 8 were independent cold-read grading passes (fresh grader instances, no
access to this file's prior grading history or this critique document) checking WCAG
1.4.3/1.4.11 contrast (via actual computed relative-luminance ratios, not estimates),
WCAG 2.2.2 pause/stop compliance on the auto-updating feed, keyboard/focus integrity
(including the `inert`-based mobile-nav collapse), dishonesty/fake-state labeling, dead
CSS tokens, hardcoded-literal token bypass, and internal type-scale consistency. **Both
passes independently found zero material defects.** Per the convergence-loop stop
condition (two consecutive clean independent grading passes), this file has converged
after **8 total rounds** of grade→fix→re-grade. This is not a claim of flawlessness —
only that two independent fresh readers, checking against the full named-defect
checklist, found nothing further worth changing.
