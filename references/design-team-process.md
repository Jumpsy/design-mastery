# How elite design teams actually operate

Visual/token knowledge (`design-md/`, `plugin87-data/design-systems/`) tells you what
ship-quality output *looks like*. This file covers what a real design org *does* to get
there — the process, rituals, and organizational discipline that separates a
multi-million-dollar product's design output from a solo AI-generated pass. Grounded in
widely published, public practice (design-leadership books/talks, public design-org
retrospectives, and well-documented company practices — e.g. Julie Zhuo's *The Making of
a Manager*/writing on design orgs, Will Larson's org-design writing, Apple's Human
Interface Guidelines process descriptions, public talks from Stripe/Airbnb/Figma/Linear
design leaders, Google's public Material Design governance docs). Company practices are
cited generically by known public pattern, not fabricated internal specifics.

## Table of contents
1. Critique culture and rituals
2. Design systems governance at scale
3. Design ops / leadership structure
4. The real production pipeline — and what AI shortcuts
5. Calibrating quality to context (moat vs. afterthought)
6. The senior-critique lens vs. junior tells

---

## 1. Critique culture and rituals

A **crit** is a scheduled, structured review of in-progress work — not a demo, not a
status update, and not a one-on-one feedback session. Teams that do this well share a
few consistent traits:

- **Cadence is fixed, not ad hoc.** Weekly or twice-weekly, same time, same room
  (physical or virtual), whether or not anyone feels "ready." Waiting until work "feels
  done" to show it is the single most common failure mode — it removes the chance to
  catch a wrong direction cheaply, early.
- **Work is shown in progress, including bad options.** Presenting three directions —
  one safe, one weird, one wrong on purpose — gets better feedback than presenting one
  polished option, because it gives the room something to react against instead of just
  rubber-stamping.
- **Feedback is framed against a goal, not a preference.** Useless feedback: "I don't
  like the blue." Useful feedback: "the CTA and the nav logo are competing for the same
  visual weight, and the goal was for the CTA to win." The difference is a stated
  criterion the work is being measured against, not personal taste. A critique that
  can't point to *why* isn't a critique, it's a vote.
- **The presenter states the goal and constraints before showing the work.** Without
  this, the room critiques against whatever criteria they individually assume, and
  feedback becomes incoherent — half the room says "make it bolder," half says "make it
  quieter," and neither is wrong given what they each assumed the goal was.
- **Critique is separated from decision-making.** The person doing the work — or a
  named decision-maker — makes the call after hearing the room, not the loudest voice in
  the room. Crit generates options and blind spots; it doesn't vote.
- **Silence and "looks great" are treated as a process failure**, not a compliment. If
  nobody has a note, either the work is genuinely resolved (rare) or the room isn't
  looking hard enough — the facilitator's job is to keep asking "what's the weakest part
  of this?" until something real surfaces.

**What this means for this skill**: when producing anything non-trivial, generate at
least two genuinely different directions internally before committing to one (see §4),
and hold your own output to the "what's the weakest part of this?" question before
presenting it as final — this is the crit substitute when there's no room to show it to.

## 2. Design systems governance at scale

A design system serving 50+ product teams fails in one of two ways: it becomes a
bottleneck (every component change needs central approval, teams route around it with
one-offs) or it becomes chaos (every team forks it, "shared" components drift until
they're shared in name only). Systems that scale well use a **tiered contribution
model**, roughly:

- **Tier 0 — Foundations.** Color, type scale, spacing units, elevation, motion curves.
  Owned centrally, changed rarely, changes require a migration plan because everything
  downstream depends on them.
- **Tier 1 — Core components.** Buttons, inputs, cards, nav primitives. Owned centrally
  but built *with* product-team input — RFC-style proposal process, not top-down decree.
  A product team that needs a variant proposes it; the systems team generalizes it if
  more than one team needs it.
- **Tier 2 — Patterns/recipes.** Compositions of core components for common flows
  (a settings page layout, an empty state, a paginated table). Often maintained by
  product teams themselves, reviewed by the systems team for consistency, not authored
  by them — this is where governance loosens on purpose to avoid the bottleneck.
- **Tier 3 — Product-specific, one-off UI.** Not part of the system at all, explicitly
  allowed, because forcing 100% system coverage is what causes teams to fork it instead.

**Versioning and deprecation** are treated like an API contract, not a redesign: breaking
changes ship behind a version bump with a migration codemod where possible, a
deprecation window (old and new coexist), and a visible usage dashboard so the systems
team knows who's still on the old version before removing it — not "we changed it,
everyone update by Friday."

**What this means for this skill**: when asked to build or extend a design system,
default to proposing Tier 0/1 changes conservatively (they have the widest blast radius)
and be generous about Tier 2/3 — a one-off pattern for one product's specific need is not
a governance failure, it's correct scoping.

## 3. Design ops / leadership structure

- **Design-to-engineer ratios** at product-driven companies commonly run in the range of
  roughly 1:6 to 1:10 (one designer per 6–10 engineers) for core product teams, tighter
  (closer to 1:4) on teams where the interface *is* the product's differentiation (e.g.
  a design tool, a consumer app competing on polish). The ratio itself isn't a target to
  hit — the point is that one designer is expected to set direction/systems that many
  engineers execute against, not draw every individual screen.
- **Embedded vs. centralized**: most mature orgs run both simultaneously — designers
  embedded on product teams (own a domain, ship features, know the codebase and users)
  plus a small central team (design systems, brand, research ops) that serves everyone.
  Pure-centralized design becomes a bottleneck; pure-embedded design fragments the
  product's coherence. The central team's job is to be the thing that keeps 10 embedded
  designers' output looking like one product.
- **Design partners with PM and engineering from the brief, not after.** The failure
  mode this avoids: PM writes a spec, hands it to design to "make it look nice," design
  hands a polished mock to engineering who then discovers half of it isn't buildable in
  the sprint. Healthy teams have design in the room when the problem is being scoped,
  not just when it's being decorated.
- **Design debt is tracked and prioritized like technical debt** — inconsistent
  spacing, orphaned one-off components, accessibility gaps — with an explicit budget
  (e.g. a fixed % of each cycle) rather than "we'll clean it up eventually," because
  "eventually" competing against shipped features always loses.

**What this means for this skill**: treat "make this look nicer" requests as an
opportunity to also ask (or infer, if no user is available to ask) whether the
underlying structure/spacing/consistency has debt worth flagging, not just a surface
paint pass.

## 4. The real production pipeline — and what AI shortcuts

The standard pipeline: **brief → exploration/divergence → convergence → critique →
prototype → handoff → QA.**

- **Brief**: the problem, constraints, and success criteria, written down, before any
  visual work starts. Skipping this produces work that's polished but solves the wrong
  problem.
- **Exploration/divergence**: genuinely different directions, not three variations on
  the same idea. The point of divergence is to find out what "different" looks like
  *before* committing — an idea that seems obviously right in isolation often looks
  average next to two real alternatives.
- **Convergence**: picking one direction (or a synthesis) with a stated reason, not by
  default because it was the first one that worked.
- **Critique** (see §1): a real check against the goal, from someone other than the
  person who made the work.
- **Prototype**: the idea made real enough to react to honestly — a static comp hides
  interaction problems (does this hover state make sense, does this form actually flow)
  that only show up once something is clickable/scrollable.
- **Handoff**: specs, tokens, edge cases (empty state, loading state, error state, long
  text, RTL) documented for whoever builds it — not just the happy-path mock.
- **QA**: a real pass against the built result — spacing rhythm, alignment, contrast,
  responsive behavior — checked against the actual rendered/shipped artifact, not
  against memory of what was intended.

**Where AI-generated design output typically skips steps** (this is the part to actively
resist in this skill's own output):

1. **Skips divergence entirely** — jumps straight to one direction and polishes it,
   because generating one plausible-looking answer is what a single-pass generation
   naturally does. This skill's plan-gate step (SKILL.md §0.5) exists specifically to
   force a moment of "is there a better direction" before committing, which substitutes
   for real divergence when there's no team to diverge with.
2. **Skips edge-case/state coverage** — designs the happy path (populated, average-length
   content, logged-in, English, desktop) and stops. A senior designer's first questions
   are "what does this look like empty, what does this look like with a 40-character
   name instead of 'Jane', what does this look like on a bad connection." Always check:
   empty state, loading state, error state, long/short content extremes, and — for
   anything that will actually ship — a responsive/mobile pass.
3. **Skips the QA-against-rendered-output pass** — describes an intent ("clean, spacious
   layout") without verifying the built result actually reads that way. Always render
   and look at (or, for code output, re-read) the actual result before calling it done,
   the same discipline as `references/screenshot-to-build-demo/` and
   `references/plan-gate-live-test/` document elsewhere in this library.
4. **Skips a real critique pass** — takes its own first draft as final. Before
   presenting output, explicitly ask "what's the weakest part of this, and would a
   critique catch something I'm not seeing because I made it" — see §1 and §6.

## 5. Calibrating quality to context: moat vs. afterthought

Not everything should be built to Apple/Stripe-tier polish, and treating every task that
way wastes effort and sometimes produces the wrong result (over-designed internal
tooling is its own anti-pattern). The calibration question is: **does the interface
itself create the competitive advantage, or does it just need to not get in the way?**

- **Design-as-moat** (Apple, Stripe's docs/dashboard, Linear, Figma, a consumer app
  competing on delight): craft is the product. Every pixel, transition, and word choice
  is considered because the interface *is* what's being sold — users could get the
  underlying functionality elsewhere, they stay for the experience. This tier justifies
  the full pipeline in §4, multiple genuine exploration rounds, and obsessive QA on
  motion/spacing/microcopy.
- **Design-as-enabler** (most B2B SaaS, internal admin tools, a feature inside an
  established product): the interface needs to be clear, consistent with the existing
  system, accessible, and fast to use — but doesn't need a novel visual language. Reusing
  the existing design system correctly is *more* valuable here than inventing something
  new; novelty for its own sake is actually a tell of misjudged effort, not craft.
  Over-designing this tier (bespoke illustrations, custom motion, a new type pairing for
  one settings page) is itself a failure of judgment, not a sign of trying harder.
- **The tell that separates them isn't polish, it's restraint applied correctly**: a
  design-as-moat product still uses restraint (Apple's interfaces are not maximalist),
  and a design-as-enabler product still needs real craft in the parts users touch most
  (form validation, error messages, information density) — the difference is *where*
  the effort concentrates, not whether effort exists at all.

**What this means for this skill**: before generating output, form a quick judgment
(stated or inferred from context) about which tier the task is in, and calibrate scope —
don't apply full brand-defining exploration effort to an internal settings toggle, and
don't apply generic-template effort to a marketing landing page meant to convert.

## 6. The senior-critique lens vs. junior tells

Senior and staff-level designers critique with a specific, reusable vocabulary. Learning
to apply these terms *as diagnostic questions* is more useful than learning them as
definitions:

- **Hierarchy** — "if I look at this for one second, what do I see first, and is that
  the thing that should win?" Junior tell: everything is roughly the same visual weight,
  or the loudest element (biggest, brightest, most saturated) isn't the most important
  one.
- **Rhythm** — "does the spacing between elements form a pattern I can feel, or does it
  look arbitrary?" Junior tell: spacing values that are all slightly different from each
  other (18px here, 22px there) instead of drawn from a consistent scale — the eye
  notices inconsistency even when it can't name it.
- **Tension** — "is there one deliberate point of visual friction/interest, or is
  everything equally calm (boring) or equally busy (chaotic)?" Good composition usually
  has exactly one thing that breaks the grid/pattern on purpose. Junior tell: either zero
  tension (a totally symmetric, static layout with nothing to look at twice) or tension
  everywhere (every element trying to stand out, so nothing does).
- **Contrast** — not just color contrast, but *differentiation* generally: type-weight
  contrast, size contrast, density contrast between sections. Junior tell: a design
  where every heading is the same size step apart from body text, every button looks
  like every other button, nothing is allowed to be quiet so nothing can be loud.
- **Restraint** — "what did they choose *not* to add?" Senior work is often
  distinguishable by what's absent — no decorative icon next to every list item, no
  gradient because gradients are available, no extra card border because Tailwind
  defaults to one. Junior tell: every available affordance gets used because it's
  available, not because it's earned; this is the direct root of most "AI slop" visual
  tells (generic 3-icon feature grids, purple-blue gradient hero, left-border accent
  strips) — they're not wrong technically, they're just unearned defaults applied
  without a reason specific to this content.

A useful compressed version of this lens, applicable to any output before calling it
done: **name the one thing that should win the user's attention first, check the spacing
actually forms a rhythm rather than near-misses, check there's exactly one deliberate
point of tension rather than zero or many, and remove anything present only because it
was available rather than needed.**
