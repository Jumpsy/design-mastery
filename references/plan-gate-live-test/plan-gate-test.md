# Live plan-gate test — task: redesign a SaaS pricing card

Task chosen: a single pricing card component ("Pro" tier) for a dev-tool SaaS. Small,
concrete, fast to both plan and build — exactly the kind of task the Stop hook flagged
as most likely to get the gate skipped ("do not skip straight to code because the task
feels small").

## Step 1 — plan (before any code)

Layout: not a bordered box on a white card — instead an off-white surface stripped of the
default 1px gray border, using shadow-free elevation (a single warm-toned background shift
against the page instead of a stroke), tight internal rhythm on an 8px base grid, price as
the dominant visual weight, feature list de-emphasized to secondary text.

Signature motif: the "serif + italic accent word" formula (found live on Wispr
Flow/StudyFetch, proven again in the screenshot-to-build test) applied to a UI component
instead of a hero: plan name set in serif, with the per-month unit ("/mo") rendered in
italic serif rather than the usual small sans-serif — one considered typographic choice
instead of a default.

Palette/type direction: ink-on-parchment neutral (same family as the poster demo, reused
deliberately since it's now a proven house pattern, not recycled out of laziness) with
exactly one saturated accent color reserved for the CTA button only.

What makes it distinct: no card border, no drop shadow, no colored left-border accent
strip, no icon-in-a-circle per feature row (all named anti-slop tells). Feature rows use a
single thin rule between them instead of bullet icons.

## Step 2 — wow-check

Would the user say "wow," or does this read as competent-but-forgettable? Initial instinct
was a standard white card with a blue button and check-icon list — that is the forgettable
default. Revised: removing the border/shadow entirely and using the serif/italic price
treatment is the one push past competent. Passes, but only after the first instinct was
rejected — recording this because the honest answer on the first draft was "maybe," which
per the gate means revise, not proceed.

## Step 3 — vibe-coded / anti-slop check (on the plan, before building)

Checked plan against SKILL.md §2 and impeccable's craft-floor bans:
- Purple-to-blue gradient hero — n/a, not a hero.
- Gray 1px border on card — explicitly rejected above.
- Colored left-border accent strip — explicitly rejected above.
- Generic three-feature-icon-circle row — explicitly rejected above.
- Default Tailwind spacing with no signature move — rejected; using the serif/italic
  price as the signature move instead.

Plan clears both checks. Proceeding to build.

## Step 4 — build

See `pricing-card.html` in this same folder.

## Step 5 — compliance re-check against the actual result (§6, not memory)

Re-read the rendered result against §2's checklist line by line (not from memory of intent):
- No border/shadow on the card — confirmed in rendered output.
- No left-border accent strip — confirmed.
- Serif display price with italic "/mo" — confirmed, renders correctly, doesn't overlap.
- One accent color, used only on the CTA — confirmed (ink-red, matches the reused house
  palette from the poster demo).
- Feature rows separated by a single hairline, no bullet icons — confirmed.

This is the first full pass of the plan gate (§0.5) run in live practice rather than
existing only as documentation, and the first compliance re-check (§6) run against a real
rendered result rather than asserted from intent.
