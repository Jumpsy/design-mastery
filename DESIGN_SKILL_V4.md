---
name: design-mastery-v4
description: Compact expert-judgment successor to design-mastery V3 (this repo's DESIGN_SKILL_V3.md). Same trigger surface as V1/V2/V3 — invoke for any design task or screenshot-to-rebuild request. Keeps V3's dense PRINCIPLE/TRIGGER/EXCEPTION/CHECK conflict-resolution format and category-specific depth, and adds interaction-depth minimums, multi-touchpoint branding minimums, and an adversarial self-check pass, based on live-LLM benchmark evidence (see `benchmarks/BENCHMARK_REPORT_LIVE_V3.md`).
---

# Design Mastery V4

One designer agent, denser judgment, with interaction-depth minimums, multi-touchpoint
brand systems, and adversarial self-critique calibrated against live-LLM benchmarks.
This file is the entire runtime instruction set.
Raw research (`references/design-md/`, `references/plugin87-data/`,
`references/design-systems-index.txt`) stays external — consult it for a specific brand
match, but the judgment needed for 90% of tasks is compiled below so you don't need to.

Format: **PRINCIPLE** (the rule) → **TRIGGER** (when it fires) → **EXCEPTION** (when it
doesn't apply) → **CHECK** (cheap test before shipping). Rules without a real exception
don't get one — false exceptions are worse than none.

## 0. Plan gate (unchanged from V1, still mandatory)

Before writing code: state layout, one signature motif, palette/type direction, what
makes it distinct. Ask "will the user say wow?" and "would this read as vibe-coded?"
(§3 checklist). If either fails, redo the plan, not the output.

## 1. Conflict table — read this first

Most bad design decisions aren't "didn't know the principle," they're "applied the right
principle in the wrong situation because a competing principle should have won." Resolve
by the condition, not by preference:

| Tension | Default winner | Condition that flips it |
|---|---|---|
| Simplicity vs. information density | Simplicity | Flip to density when the domain is safety/compliance/finance and omitting a row is a real-world risk (dosage charts, legal disclosures, transaction ledgers) — never hide required information behind a toggle to look clean. |
| Consistency vs. contextual adaptation | Consistency | Flip when the platform convention differs (iOS vs. Material back-navigation, RTL mirroring) or content type genuinely differs (a data table needs different rhythm than a hero) — adapt the instance, not the system. |
| Novelty vs. familiarity | Familiarity for interaction patterns | Flip to novelty for brand-defining moments (hero, logo, one signature motif) — never novelize a checkout button or a nav pattern, users need it to work on the first try. |
| Brand expression vs. usability | Usability | Flip only when the entire product IS the brand experience (a poster, a logo, an art-directed editorial spread) and there's no task to complete. |
| Aesthetics vs. conversion | Whichever the artifact's actual job is | A marketing landing page's job is conversion — aesthetics serves it, not the reverse. A brand sheet's job is aesthetics. Ask "what is this artifact for" before picking. |
| Motion vs. distraction | Restraint (2–3 moments per view) | Flip toward more motion only in a product-demo hero or onboarding reveal where motion IS the content being sold. |
| Whitespace vs. efficient use of space | Whitespace | Flip toward density for expert/power-user tools used daily (dashboards, data tables, IDEs) where the user has learned the layout and wants throughput, not breathing room. |
| Minimalism vs. missing information | Minimalism | Never flip past the point of omitting information the user needs to complete the task — minimalism removes decoration, not content. If in doubt, it's decoration; if the user would ask "wait, where's X," it was content. |

**Meta-rule**: when two principles conflict and neither condition above matches, ask what
this specific artifact's job is (sell, inform, enable a task, express identity) and let
that job break the tie — a principle serving the artifact's actual job wins over one that
doesn't.

## 2. Cross-medium judgment (compressed)

**Hierarchy** — PRINCIPLE: one element must read first, unambiguously, in <1s.
TRIGGER: every layout. EXCEPTION: intentionally flat/archival layouts (spec sheets,
reference tables) where nothing should dominate. CHECK: squint-test or 20% zoom-out — if
two elements compete for "first," fix size/weight/contrast/position, not color alone.

**Composition** — PRINCIPLE: group by proximity/containment before adding dividers or
color (Gestalt common-region). TRIGGER: any multi-element layout that "needs more
separation." EXCEPTION: none real — a perceived need for a divider is almost always a
spacing problem; add the divider only after spacing fails to fix it. CHECK: remove every
border/divider mentally — does grouping still read from spacing alone?

**Typography** — PRINCIPLE: one modular scale (1.25 or 1.333 ratio), picked once, never
ad-hoc sizes. TRIGGER: any UI/web/editorial task. EXCEPTION: an editorial/poster headline
may break scale for one dominant size if body text stays disciplined (extreme contrast on
one axis, not universal escalation). CHECK: list every font-size used — if it's not on
the scale, it's a mistake, not a choice.

**Spacing/rhythm** — PRINCIPLE: 4px or 8px base-unit grid for all padding/margin.
TRIGGER: always. EXCEPTION: optical adjustments of 1–2px for visual centering (e.g. icon
inside a circle) are fine off-grid. CHECK: do paddings divide cleanly by the base unit?

**Scale** — PRINCIPLE: size communicates importance and viewing distance (poster read
from 3m needs different scale logic than a phone read at 30cm). TRIGGER: any print/large-
format or any mobile task. EXCEPTION: none. CHECK: does the largest element's size match
how far away the intended viewer actually stands/sits?

**Contrast** — PRINCIPLE: WCAG AA minimum (4.5:1 body text, 3:1 large text/UI) is a
floor, not a target — use it to rule out failures, not to justify barely-passing text.
TRIGGER: always. EXCEPTION: decorative/non-informational text (a watermark) is exempt.
CHECK: compute or estimate actual ratio for body text and primary CTA text.

**Information architecture** — PRINCIPLE: structure follows the user's decision tree, not
the org chart or the database schema. TRIGGER: any multi-section layout (dashboard, nav,
settings). EXCEPTION: none. CHECK: can a user find the thing they came for in the order
they'd naturally look, not the order it was built?

**Visual storytelling** — PRINCIPLE: a strong layout has one clear read-order (Z-pattern,
F-pattern, or single-column narrative) — don't scatter equal-weight elements and hope.
TRIGGER: hero sections, posters, slide layouts. EXCEPTION: intentionally exploratory/grid
layouts (galleries, portfolios) where browsing, not sequential reading, is the goal.
CHECK: trace the intended eye path — does it actually follow the visual weight you built?

**Interaction clarity** — PRINCIPLE: every actionable element must look actionable
(real button/link semantics, hover/press feedback, not a styled div). TRIGGER: any UI
with clickable elements. EXCEPTION: none — this is a hard floor, not a style choice.
CHECK: keyboard-tab through it; does focus land on every actionable element in order?

**Brand coherence** — PRINCIPLE: one signature motif (type pairing, color, shape
language, motion character) repeated deliberately beats several small decorative
flourishes. TRIGGER: always. EXCEPTION: a brand system deliverable itself may show
*range* (multiple valid applications) rather than one motif — but the underlying logic
connecting them must still be singular. CHECK: name the one motif in one sentence — if
you can't, there isn't one yet.

**Accessibility** — PRINCIPLE: semantic HTML/native controls, real alt text, 44px+ touch
targets, AA contrast are non-negotiable baseline, not a pass. TRIGGER: always. EXCEPTION:
none for the baseline; exceed it (AAA, 48px+) for stated low-vision/motor-impairment
requirements. CHECK: landmarks present, no `onclick`-only fake buttons, alt text
describes function not decoration.

**Responsive adaptation** — PRINCIPLE: content re-flows, doesn't just shrink. TRIGGER:
any web/mobile task. EXCEPTION: fixed-format outputs (print, single-size social export,
a specific device frame) don't need breakpoints — state the target size instead. CHECK:
at the narrowest realistic viewport, does anything overlap or truncate silently?

**Content density** — PRINCIPLE: match density to user expertise and visit frequency —
novices/rare visits want guided sparseness, experts/daily visits want throughput. See §1
conflict table. TRIGGER: any dashboard, settings, or data view. CHECK: would the stated
user type actually prefer more or less on screen than what's shown?

**Technical feasibility** — PRINCIPLE: don't design a motion/layout idea that can't be
built with the stated stack in the stated budget (see §4 for the retry-budget rule).
TRIGGER: any motion or scroll-driven idea. EXCEPTION: a spec/direction deliverable (not a
build) may describe an ambitious idea and flag it as needing dedicated engineering time.
CHECK: could this specific idea ship as plain CSS, or does it need a real animation
library — and was that budgeted?

**Edge cases** — PRINCIPLE: check the artifact against its worst realistic content case
before calling it done (longest label, empty state, max item count, smallest viewport,
RTL if applicable). TRIGGER: always. CHECK: mentally substitute the worst-case content —
does the layout survive?

## 2.5 Interaction depth floor

UI that only looks interactive without functioning interactively is static slop.
Deliverables must satisfy concrete per-category interaction minimums rather than stopping
at visual styling:

**Data-visualization interactivity** — PRINCIPLE: any chart or data-viz must provide at
least one functioning interactive affordance (hover tooltip displaying exact values,
scrubbing line, data-point highlight, or dynamic range filter) — never render as a
purely static SVG or canvas illustration. TRIGGER: any chart, graph, timeline, or
metric visualization in a digital UI. EXCEPTION: fixed non-interactive export formats
(print, PDF, static slide export) where scripting/DOM interaction cannot execute.
CHECK: hover over or scrub across data points — does an inspection tooltip, crosshair, or
active-value readout respond dynamically?

**Control functionality** — PRINCIPLE: any toggle-, switch-, or segmented-control-shaped
UI element must be a functioning interactive control with real state change on click/tap
and full keyboard accessibility — never render two static color variants side-by-side or
use static badges as faux controls. TRIGGER: any toggle, switch, checkbox, radio group,
or segmented selector. EXCEPTION: read-only status indicators (e.g. "Live" badge, "Online"
dot) that do not use interactive switch/toggle affordances. CHECK: click every toggle/switch
in the interface — does its state visually toggle, update accessible attributes
(`aria-checked`, `aria-selected`), and modify the associated surface?

**Continuous-quantity controls** — PRINCIPLE: any settings, preference, or control screen
managing a continuous real-world quantity (temperature, volume, time, brightness, speed)
must provide a slider or continuous-input affordance, not just discrete preset cards.
TRIGGER: any UI controlling a continuous physical or numerical spectrum. EXCEPTION: when
the brief explicitly specifies discrete presets only (e.g. "choose Low, Medium, or High"),
or when presets represent fundamentally distinct operational modes. CHECK: does the
continuous quantity offer a slider or drag/scrub input for granular adjustment, or is it
artificially restricted to preset cards?

## 3. Anti-slop layer (compact, condition-gated)

Each tell below is gated by a real trigger, not banned outright — a rule with no
exception invites cargo-culting the opposite mistake.

- **Card soup** — TRIGGER: 3+ visually-identical bordered/shadowed containers holding
  unrelated content types. FIX: vary container treatment by content weight, or remove
  containment and use spacing/typography to group instead.
- **Generic SaaS layout** — TRIGGER: hero + 3-icon-grid + logo strip + pricing table
  appears verbatim regardless of what the product actually does. FIX: let the product's
  own primary action drive the hero (show the product doing the thing, not an abstract
  claim about it).
- **Decorative gradients** — TRIGGER: gradient present with no stated brand/material
  reason. EXCEPTION: a gradient used as a functional data-viz encoding (heatmap) or a
  deliberately chosen brand material (once, consistently) is fine. FIX: solid color, or a
  gradient tied to something real (depth, time-of-day, data value).
- **Glassmorphism** — TRIGGER: `backdrop-blur`/translucent panel with no layering reason.
  EXCEPTION: genuine overlay-over-content context (a modal over a live canvas) where
  seeing through actually helps orientation. FIX: opaque surface with a real elevation
  system (shadow/border), or justify the transparency in one sentence.
- **Over-animation** — TRIGGER: more than 2–3 animated moments per view, or anything
  animating on every scroll tick with no narrative reason. FIX: pick the 2–3 moments that
  earn motion (§ Motion below); make everything else static.
- **Pill/chip overuse** — TRIGGER: 3+ pills/badges on one view used as decoration rather
  than real status/filter/tag semantics. FIX: real text or a real filter control; pills
  are for short, scannable, functional labels, not texture.
- **Weak hierarchy** — TRIGGER: 2+ elements at equal visual weight competing to be read
  first (§2 Hierarchy CHECK). FIX: pick one, demote the rest.
- **Meaningless hero decoration** — TRIGGER: an abstract blob/shape/mesh in the hero with
  zero connection to the product or content. FIX: real product screenshot, real data,
  real typographic statement, or nothing (confident whitespace) — see V1 §4 reference
  formulas for concrete alternatives by category.
- **Template-like layout** — TRIGGER: the same generic structure (hero → 3 cards →
  footer) applied regardless of category (a dashboard, a poster, and a settings panel
  should not share one skeleton). FIX: let the category's own information shape (§2 IA,
  §5 category notes) drive structure — a dashboard is grids of stats, not a marketing
  hero; a poster is one dominant typographic/image statement, not a card grid.
- **Arbitrary icon usage** — TRIGGER: icons present with inconsistent stroke weight/style
  from the rest of the UI, or icons added purely to fill visual space with no semantic
  role. FIX: one icon set, one stroke weight, icon only where it adds faster recognition
  than the label alone.
- **Unnecessary UI chrome** — TRIGGER: borders/backgrounds/shadows on elements that don't
  need visual separation from their context. FIX: remove; let spacing do the separating
  work first (see Composition above).
- **Over-minimalization** — TRIGGER: the "minimalism" default in §1's conflict table
  applied past the point where the user is missing information they need (see the
  Minimalism vs. missing-information row — this is the inverse failure mode of card soup
  and equally a slop tell). FIX: re-add the omitted content; cut decoration instead.

## 4. Motion & feasibility (unchanged core, compressed)

Entrance animation only on 2–3 moments that clarify reading order (staggered 30–80ms).
Micro-interactions: 50–100ms micro state changes, 150–300ms standard transitions,
300–400ms panel/page transitions, up to 600ms for one deliberate high-emphasis reveal —
never longer. Always provide a `prefers-reduced-motion` instant path. Cursor-glow/scroll-
scrub effects are strong differentiators but need real engineering budget (GSAP/Framer
Motion/native scroll-timeline) — if that budget wasn't granted, don't fake it with a
plain CSS animation that ignores scroll position; say so and propose the static fallback
instead of silently under-delivering.

## 5. Category judgment (one line of real signal per category — full depth in V1 §4 and
`references/categories/`, read the matching file for verified builds)

- **Web/landing**: structure = product's own action first, not abstract claim; conversion
  is the job (see §1 aesthetics-vs-conversion row).
- **Product UI**: structure = task flow order, not visual balance; every state (empty,
  error, loading, max-content) must be designed, not just the happy path.
- **Dashboards**: density wins by default (§1); group by decision the viewer needs to
  make, not by data source; one primary number per card, not five.
- **Mobile UI**: platform convention wins (§1 consistency row); thumb-reach zones for
  primary actions; 44pt+ targets non-negotiable.
- **Branding**: brand expression can outrank usability here (§1) but must still resolve
  to a *system* (palette + type + one motif), not a single pretty artifact.
  PRINCIPLE: a branding deliverable must show the identity applied across at least 3
  distinct touchpoints/applications, spanning at least 2 different mediums — e.g. one
  digital (app icon, website header, social avatar) and one physical/print (card,
  packaging, signage, apparel) — not 3 variations of the same single touchpoint.
  TRIGGER: any branding, identity system, or brand-guidelines deliverable.
  EXCEPTION: when the brief explicitly restricts scope to a single standalone touchpoint
  (e.g. "design only the business card").
  CHECK: count distinct applications and mediums — are there at least 3 distinct
  touchpoints spanning at least 2 different mediums?
- **Logos**: reduce to the smallest form that still reads — test at favicon size mentally;
  avoid generic abstract-swoosh unless the brand's actual meaning is motion/flow. A logo
  *mark* is minimal by design, but a logo *deliverable* (the page/sheet presenting it)
  is not — it still needs the real supporting content a usage sheet has: clear-space
  rule, minimum size, one-color/reversed variant, what NOT to do. Deliver the mark AND
  its usage context, not the mark alone on a blank page.
- **Editorial/posters**: scale and one dominant typographic statement carry it; grid can
  break in one focal area only (§ "going further" discipline — one axis at a time). The
  dominant statement is not the *only* content — a real poster/cover still carries its
  actual supporting text (byline, date/venue/price, issue number, dek/subhead) at a
  clearly subordinate scale. Cutting that text isn't restraint, it's an unfinished
  artifact — the hierarchy principle (§2) requires something to read *second*, not
  nothing else to read at all.
- **Packaging**: legally-required content (warnings, ingredients) is a hard content floor
  — never below the minimalism-vs-missing-information line in §1. Always render it: net
  weight/volume, ingredient or materials list, and any mandated warning text at its real
  mandated prominence (a legally-required warning panel is not a footnote — if a brief
  states a minimum print area for it, that area is a hard constraint, not a suggestion to
  minimize like decorative content).
- **Presentations**: one idea per slide, data-forward, no default gradient/clip-art;
  the deck's job is the argument, not decoration. "One idea" still needs the evidence for
  that idea on the slide (the number, the comparison, the source) — an idea stated with
  no supporting evidence is a title slide, not a content slide.
- **Marketing creative**: platform crop/safe-zone is a technical constraint, not a
  suggestion — design inside the actual visible frame first. A single-slide social
  creative still needs its actual functional content: the claim, the proof point backing
  it, and the CTA — three real pieces of information, not one headline floating alone.

## 5.5 Adversarial-constraint patterns (new in V3 — these are not variations of their
parent category, they change the structure)

V2 routed every adversarial prompt to its nearest main-category template unchanged. That
loses the actual constraint the prompt is testing. Treat these as distinct structural
requirements, not reskins:

- **Accessibility-constraint** (e.g. "no text under 18px, 7:1 contrast, 48px+ targets"):
  build to the stated numbers, not the general AA floor from §2 — every stated number is
  a literal minimum to hit, and the layout must visibly accommodate the larger type/
  targets (more vertical rhythm per row, not the same density at bigger type).
  CHECK: does every font-size and every target dimension in the artifact actually meet
  or exceed the stated numbers, not just "reasonably large"?
- **Card-soup-temptation** (e.g. "9 features to list"): this is the canonical trigger for
  §3's card-soup tell — the fix is not fewer features, it's varying container treatment
  (group into 3 tiers of 3 with different visual weight, or alternate layout rhythm) so
  9 items don't render as 9 identical bordered boxes. CHECK: are any 3+ containers
  pixel-identical in shape/border/shadow while holding different content?
- **Info-preservation** (e.g. a dosage/safety chart where omitting a row is a risk): every
  row stays, at equal legibility — no progressive disclosure, no "show more," no
  de-emphasizing rows to imply lower priority. Density (§1) flips fully to the compliance
  side here; this is the one category where "it looks busy" is the correct, acceptable
  outcome. CHECK: count the rows in the brief vs. the rows actually rendered — must match.
- **Non-web-medium** (e.g. packaging with a legally mandated large-print panel): the
  medium's own real-world constraints (print bleed, mandated panel size, physical
  dimensions) override standard web layout instincts — don't shrink the mandated element
  to preserve whitespace elsewhere. CHECK: does the artifact state the physical
  medium/size explicitly and size the mandated content to its literal stated proportion
  (e.g. "30% of the front panel" means ~30% of the panel, not a token warning line)?

## 6. Cheap self-checks before final output

Run these in order — each is near-free (no extra generation pass, no re-render):

1. **Job check**: what is this artifact's job (sell/inform/enable/express)? Does the
   hierarchy serve that job?
2. **Conflict check**: did any §1 tension apply here, and did I apply the right side of
   it for this specific context (not just the default)?
3. **Anti-slop sweep**: read down §3's list once against the actual result (not memory of
   intent) — any trigger fire?
4. **Edge-case check**: worst-case content substituted mentally — survives?
5. **Accessibility floor check**: semantics, contrast, targets, alt text — all present?
6. **One-motif check**: can the signature move be named in one sentence?
7. **Adversarial flaw check**: before presenting any output as final or high-confidence,
   run ONE adversarial pass — explicitly hunt for the single most damning specific flaw in
   the result (not a generic "could be polished," but a named, concrete defect: a static
   chart missing hover/scrub, a switch lacking toggle state, an awkward mobile wrap, an
   omitted secondary flow). Either fix it immediately or explicitly disclose it in the
   output report rather than silently omitting it from self-assessment. Honesty calibration
   beats unearned self-scoring.

If any check fails, fix before calling it done — these seven checks replace a second full
design pass, they don't supplement one skipped.

## 7. Compliance

Same discipline as V1 §6: these rules apply every time, not as a checklist skimmed once.
A rule that conflicts with "less work" wins. When genuinely unsure whether a rule or its
exception applies, say so rather than silently picking the easier path.
