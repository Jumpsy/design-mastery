# Motion & Presentation Craft Notes

Distilled, well-established motion-design and presentation/deck-craft principles —
timing curves, easing, staging, pacing, and narrative structure — grounded in widely
published, non-proprietary practice (classical animation principles, established motion-
design literature, and mainstream presentation-craft guidance). This file does not
describe, quote, transcribe, or reference any specific scraped video, deck, or course; it
distills principles general enough to be common knowledge across the field, the same way
`references/design-md/` distills principles from public design-system documentation
rather than reproducing it verbatim.

## 1. Timing and duration

- **Default UI transition range: 150–400ms.** Under ~100ms reads as a glitch/flash, not
  a transition; over ~500ms reads as sluggish for anything the user triggered directly
  (a click, a toggle, a tab switch). Longer durations (500ms–1s+) are reserved for
  larger-scale or less-frequent transitions (page-level, modal-entrance, onboarding) —
  not the 20th time the same day a user opens a menu.
- **Distance and duration should scale together.** A larger on-screen displacement
  (a full-screen panel sliding in) reads correctly with a longer duration than a small
  one (a tooltip fading in 4px away); using the same duration for both makes the small
  move feel sluggish and the large move feel jarring.
- **Repeated/frequent interactions get shorter durations than one-time ones.** A hover
  state or a button press that happens dozens of times per session should be near the
  bottom of the range; a first-run tour animation can afford to be slower because it
  happens once.

## 2. Easing

- **Nothing in the physical world starts or stops instantly — neither should UI motion.**
  Pure `linear` easing reads as mechanical/artificial for anything simulating a physical
  object entering, leaving, or changing state; reserve linear strictly for continuous,
  non-object motion like a progress-bar fill or a loading spinner.
- **Ease-out (fast start, slow settle) for anything entering or responding to user
  input.** It matches how the user's attention arrives — they acted, so the motion should
  feel immediately responsive, then settle gently rather than snapping to a hard stop.
- **Ease-in (slow start, fast exit) for anything leaving.** Elements that are going away
  don't need to hold the user's attention on the way out; a fast finish keeps exits from
  feeling like they're lingering unnecessarily.
- **Ease-in-out (symmetric) for anything moving between two states where neither end is
  the "resting" state** — e.g. a toggle sliding between two positions, a tab indicator
  moving between tabs.
- **Avoid default/generic bezier easing as a stand-in for "some easing."** A curve tuned
  for the specific motion (how far, how fast, what it's replacing) reads as considered;
  reused default browser easing across every interaction is a motion-design equivalent of
  the "same gradient hero on every landing page" visual-design tell — it signals the
  timing wasn't actually chosen, just left at the library default.

## 3. Staging and choreography

- **One focal motion at a time.** If multiple elements animate simultaneously, the eye
  can't track more than one moving focal point at once — stagger secondary elements
  (30–80ms offset per item is a common, unobtrusive range) so the eye has a clear
  primary thing to follow, then catches the rest as a group.
- **Motion should clarify a spatial or causal relationship, not just decorate.** A panel
  should slide in from the edge it's spatially associated with (a right-side inspector
  slides from the right); a new item in a list should animate from where it was inserted,
  not fade in from nowhere. If removing the animation entirely wouldn't make the
  interaction harder to understand, the animation is decorative, not functional — the
  same disqualifying test the anti-slop checklist applies to static visual elements.
- **Motion should never be the only signal of a state change.** Anything the animation
  communicates (an item was added, a value changed, an error occurred) needs a
  non-animated fallback state too — a reduced-motion user, a user who missed the frame,
  or a user with the animation not yet rendered still needs to be able to tell what
  happened from the resting UI state alone.

## 4. Respecting reduced motion

- Any animation beyond a simple opacity crossfade should be gated behind
  `@media (prefers-reduced-motion: no-preference)`, with a `prefers-reduced-motion:
  reduce` branch that either removes the motion entirely or reduces it to a near-instant
  cross-fade. This is not an edge case to patch in later — treat "what does this look
  like with motion off" as part of designing the interaction, not an accessibility
  afterthought bolted onto a finished animation.
- Auto-playing, looping, or attention-grabbing motion (parallax scroll-jacking,
  auto-advancing carousels, looping background video) should default to paused/off for
  reduced-motion users and, in most product contexts, should be avoidable or dismissible
  even for users who haven't set that preference — unsolicited continuous motion is a
  common source of user complaint independent of the accessibility requirement.

## 5. Presentation / deck rhythm

- **One idea per slide, evidenced on the slide.** A slide's job is a single claim, and
  the claim needs its own supporting evidence in view — a number, a comparison, a quote,
  a diagram — not just a headline asserting the idea with nothing beneath it. A title
  slide with no evidence is an introduction, not a content slide; don't let content
  slides collapse into that shape.
- **Pacing varies deliberately, it doesn't stay constant.** A deck that spends the exact
  same amount of visual/verbal weight on every slide reads as monotone regardless of
  content quality — vary depth and dwell time: a dense data slide earns more time and
  more supporting detail than a transitional or framing slide, and the difference should
  be visible in the slide's own density, not just implied by how long the presenter
  lingers.
- **The narrative arc matters more than any individual slide's polish.** Setup
  (why this matters) → tension/problem (what's wrong or at stake) → evidence
  (what supports the claim) → resolution (what to do about it) is a widely used,
  general-purpose structure; a deck that's internally polished slide-by-slide but skips
  straight from setup to resolution without establishing why the problem matters reads as
  unconvincing even when every individual slide looks good.
- **Repetition of a visual anchor builds continuity; repetition without variation reads
  as a template.** A consistent slide master (margins, type scale, one accent color) is
  correct discipline — the same anti-slop principle as a shared design-token system. But
  every slide sharing an *identical layout structure* regardless of what that slide's
  idea actually needs (the deck equivalent of "card soup") flattens the pacing the arc
  above depends on — the layout should flex to the content's actual shape (a big number
  slide, a comparison slide, a quote slide, a diagram slide are structurally different,
  not the same box with different text).

## 6. Product-demo / walkthrough video pacing

- **Show the outcome before the mechanism, then the mechanism.** Leading with "here's
  what this produces" before "here's how you get there" gives the viewer a reason to
  follow the subsequent step-by-step — front-loading setup/configuration before payoff is
  a common reason product-demo footage loses viewers early.
- **Cut on action, not on a static hold.** A cut made mid-motion (as a cursor is already
  moving toward the next click, as a panel is already sliding) reads as continuous and
  fast; cutting only after motion has fully settled into a static frame, then cutting to
  another static frame, reads as choppy even at the same total runtime.
- **Narration and on-screen action should be synchronized, not sequential.** Describing
  an action and then performing it (or the reverse) doubles the time a viewer spends on
  each step relative to describing it while it happens on screen — this is one of the
  most common, easily fixed sources of a demo video feeling slower than its actual
  content justifies.
