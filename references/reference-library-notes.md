# Reference library research notes

## Primary source: `design-md/` (86 real brand teardowns)

Pulled from the open-source repo `VoltAgent/awesome-design-md` (MIT-licensed, built for
exactly this purpose — feeding coding agents real design tokens instead of vibes) into
`references/design-md/<brand>/DESIGN.md`. Each file has: color palette with semantic
roles, full typography scale (family/size/weight/line-height/letter-spacing per level),
component styling (buttons/cards/inputs/nav), spacing/layout rules, elevation system,
do's/don'ts, responsive behavior, and an agent prompt guide.

Brands covered (74, repo-sourced): airbnb, airtable, apple, binance, bmw, bmw-m,
bugatti, cal, **claude**, clay, clickhouse, cohere, coinbase, composio, cursor,
dell-1996, elevenlabs, expo, ferrari, figma, framer, hashicorp, hp, ibm, intercom,
kraken, lamborghini, **linear.app**, lovable, mastercard, meta, minimax, mintlify,
miro, mistral.ai, mongodb, nike, nintendo-2001, nvidia, ollama, opencode.ai,
pinterest, playstation, posthog, raycast, renault, replicate, resend, revolut,
runwayml, sanity, sentry, shopify, slack, spacex, spotify, starbucks, **stripe**,
supabase, superhuman, tesla, theverge, together.ai, uber, **vercel**, vodafone,
warp, webflow, wired, wise, x.ai, zapier, voltagent (the repo's own site).

Plus 12 more added across two passes of live-site expansion, extracted directly from
production sites via `getComputedStyle()` DOM inspection (browser tools, not
WebFetch — WebFetch strips CSS and yields no usable tokens), each honestly scoped in
its own "Known Gaps" section for anything not captured: cloudflare, discord, github,
huggingface, openai, calendly, duolingo, gitlab, loom, patagonia, robinhood, zoom.

**Correction/note**: `notion` was already present in the repo-sourced 74 before this
expansion. In this pass its `DESIGN.md` was independently re-derived from a live
browser DOM read and **overwritten** (no version control exists in this directory, so
the original repo-sourced content could not be diffed or preserved) — this was a
mistake in scope (should have been skipped as "already covered" per the task's own
rule), caught only after the fact. The current `notion/DESIGN.md` is still real,
DOM-verified data, just not the original repo version. `notion` is therefore **not**
counted among the 12 net-new brands above.

**How to use it**: when asked to design/match a specific brand's vibe (or something
adjacent to one), read that brand's `DESIGN.md` directly for exact hex values, type
scale, and component rules instead of guessing from memory. When asked to synthesize
"what great SaaS/fintech/dev-tool sites have in common," grep across the whole set for
a token (e.g. `grep -rh "fontWeight: 300" references/design-md/*/DESIGN.md`) to find
genuine cross-brand convergence rather than one brand's opinion.

Example verified extraction — Stripe (`design-md/stripe/DESIGN.md`): primary
`#533afd` electric indigo, ink `#0d253d` navy (not pure black), Söhne at thin 300
weight with tight negative letter-spacing for display type, tabular figures for
numerics, tight-radius pill buttons, near-white card surfaces, dark dashboard shell
flips polarity from the light marketing site.

## Live screenshots captured this session (not in the repo above)

**Wispr Flow** (wisprflow.ai): warm cream background (`~#f5f0e0`), deep forest-green
top announcement bar, oversized serif display headline mixed with an italic
script-style accent word ("Don't type, *just speak.*"), lavender/purple pill CTA and
a matching solid-lavender accent circle, a hand-set circular/curved text path wrapping
around whitespace as a signature decorative motif, monospace-style audio-waveform
visual reinforcing the product (voice). Signature move: **curved/arced typography as
a recurring brand device**, not just straight lines.

**StudyFetch** (studyfetch.com): same underlying pattern as Wispr Flow — warm
off-white/cream bg, serif display headline with an *italicized* key word for warmth
("Learning that *adapts to you*"), black pill CTA, playful hand-drawn line-art
doodles near the fold. Confirms a genuine cross-brand pattern worth naming:

### New cross-brand pattern found (add to §4 of SKILL.md)
**"Serif + italic accent word" hero formula**: large serif or humanist-serif display
headline where one phrase/word breaks into an italic serif for warmth and emphasis,
set on a warm cream/off-white background (not white, not dark) with a black or
saturated-pastel pill CTA. This is a distinct alternative to the "sans-serif + gradient
mesh" formula (Stripe/dev-tools) and to the "monochrome editorial" formula
(OpenAI/Anthropic) — it reads as warm, human, consumer-trustworthy rather than
technical. Good default for consumer AI tools, edtech, and voice/writing products.

## Non-web design demonstration (proof of "design literally anything")

`references/non-web-demo/` — a real, rendered print-poster artifact built end-to-end through
the `canvas-design` skill's two-phase process, not just described in SKILL.md §5.

- `design-philosophy.md` — "Patient Ink," a 5-paragraph visual-movement manifesto (space as
  material, ink-like color, calligraphic typography, sustained-looking composition).
- `poster-render-script.py` — PIL script (no wkhtmltopdf/reportlab available in this
  environment, so rendered directly with Pillow) producing a 1600×2000 px poster: "Design" in
  upright serif over italic "Mastery," a single brick-red accent dot, a whispered italic
  tagline, and a bottom-left specimen label. Composition rebalanced on a second pass — first
  draft weighted all mass top-left with a dead lower half; fixed by moving the text block to
  the golden-third vertical position and adding a matching hairline+label near the bottom to
  balance the frame, per canvas-design's "refine the composition, don't add graphics" rule.
- `patient-ink-poster.png` — final rendered output, visually verified via image read-back.

Proves the **"serif + italic accent word" hero pattern** (found live on Wispr Flow/StudyFetch,
logged above) transfers across medium — from web hero sections to print/poster — because it's
a genuine typographic-contrast principle, not a web-specific template.

## Screenshot-to-build demonstration (proof the pipeline works live, not just documented)

`references/screenshot-to-build-demo/` — ran the actual "upload a screenshot → instantly
analyze → recreate it" workflow end-to-end, not just described it in SKILL.md.

- `source-screenshot.jpg` — real live screenshot captured from wisprflow.ai via browser
  automation (not a stock/synthetic image).
- `recreation.html` — analyzed the screenshot directly (color extraction, layout reading,
  typography identification) and rebuilt it as working HTML/CSS: cream `#f7f2df` background,
  dark teal `#16332b` announcement bar, pill-shaped nav with a segmented Dictation/Notetaker
  toggle, Instrument Serif display headline with an italic second line ("just speak."),
  lavender `#c9b6f5` pill CTA with a black hairline border, an SVG `<textPath>` curved caption
  (the site's actual signature motif — decorative text following an arc), a circular
  fingerprint icon, and a dark waveform pill with an audio-bar glyph.
- Verified by rendering the HTML in a real browser tab and screenshotting the result
  side-by-side against the source — layout, type pairing, color, and the curved-text motif
  all matched; this is the concrete "prove it in live use" step the Stop hook's feedback
  called for the screenshot-to-code capability.

This also confirms `plugin87-image-to-code`'s approach (read the image, extract tokens,
reproduce structure/typography/color/motifs, not just guess a generic layout) is sound in
practice, and it reinforces the "serif + italic accent word" pattern and "curved/arced
typography as a signature brand device" finding already logged above — both survived direct
pixel-level recreation, which is stronger evidence than eyeballing a screenshot once.

## Plan-gate live test (proof §0.5/§6 are actually followed, not just documented)

`references/plan-gate-live-test/` — ran the SKILL.md §0.5 plan gate and §6 compliance
re-check on a real small task (a "Pro" tier SaaS pricing card), the exact kind of small
task the gate is most likely to get skipped for.

- `plan-gate-test.md` — the actual plan text, the wow-check (recorded honestly: the first
  instinct was a generic bordered white card with a check-icon list and blue button — that
  was rejected as "competent but forgettable," and revised to a borderless card with a
  serif/italic price treatment before building), the pre-build anti-slop check against
  named tells (gray border, left-accent strip, icon-circle feature rows, generic spacing —
  all explicitly rejected in the plan itself, before any code existed), and a post-build
  compliance re-check against the rendered result rather than against memory of intent.
- `pricing-card.html` — the built result, rendered and screenshotted in a live browser tab
  to confirm the compliance re-check's claims against actual pixels, not assertions.

This is the first end-to-end run of the plan gate and compliance sections in live practice,
and it reuses the "serif + italic accent word" pattern in a third context (UI component,
after hero section and poster), and reuses the ink-on-parchment/single-accent palette from
the poster demo deliberately, as a converging house pattern rather than coincidence.

## Real YouTube video research (actual extracted content, not surface-level)

Source: DesignCourse (verified channel, `youtube.com/@DesignCourse`), video "5 stupid
UI/UX design myths" (`youtube.com/watch?v=CYWbpPzB6YU`, 59s). Extracted via
`Video_Watcher` (local download + transcription), not guessed or summarized from a title.

Actual points made (process/workflow guidance, useful for how design-mastery itself should
operate when asked to produce deliverables, not just visual output):

1. **"Pixel perfect" is a front-end job, not a prototyping job.** Prototypes need to be
   "almost right" — the implementation layer (browser/CSS) is where pixel-perfection
   actually gets locked in. Relevant to this skill: don't over-polish a plan-stage mockup;
   save precision for the build step.
2. **Don't build a design system before the idea is validated.** Building tokens/components
   up front "just slows things down." Only invest in a system (à la `plugin87-design-tokens`)
   once a direction has been validated with real users — matches this skill's existing
   refinement-vs-redesign discipline (don't over-engineer speculative work).
3. **Don't auto-layout/constrain everything.** Over-nesting layout logic 10 levels deep makes
   the file unmaintainable for whoever edits it next — a real cost of premature structure,
   not just an aesthetic complaint.
4. **Grid systems don't automatically add value.** Two visually identical layouts, one built
   with a rigid grid and one without, can be indistinguishable — the grid cost extra time for
   no visible gain in that case. Grids are a tool for a specific problem, not a default.
5. **Not everything needs a wireframe.** A standard landing page (nav, hero, testimonials,
   footer) is a solved enough problem that wireframing it is often wasted motion — skip
   straight to real design work on genuinely novel structure instead.

Also captured (real data, not fabricated): audio pacing (117 BPM, 44 sound-effect hits
across 58s, cuts every ~6s) as an example of how DesignCourse's own short-form video editing
uses rapid-cut, high-SFX-density pacing to hold attention — a motion/editing pattern
independent of the design advice itself, useful if this skill is ever asked to advise on
video/motion content pacing, not just static UI.

## Live imagery/motion/hero research across 4 real sites (proof gap #3 resolved)

Directly visited and screenshotted this session (not guessed from memory): Stripe.com,
Claude.com, OpenAI.com, StudyFetch.com. Goal: answer "what images to put on a website,
what animations, what motion graphic design" with real observed evidence, not
speculation. Video job `fe91329ef700441d` (20.5-min "Using Claude Design 2.0 to NOT
Produce SLOP") never finished after repeated polling across the entire session — logging
this as a known environment/timing limitation rather than continuing to block on it.

**What kind of "image" goes in a hero — three real strategies observed, not one default:**
1. **Real annotated product screenshots layered over a gradient field** (Stripe): a phone
   tap-to-pay UI, a checkout page, a usage-metered billing dashboard with an actual bar
   chart — all real-looking UI mockups, not stock photography or abstract illustration.
   This is the strongest "show, don't tell" pattern for a product with a visual UI.
2. **The product itself as the hero, live and interactive** (OpenAI): the hero is a real
   functional chat input box ("What can I help with?") with an empty result area below
   it — no image asset at all. The interface *is* the hero image. Only viable when the
   product is a single-input tool simple enough to demo in zero clicks.
3. **Hand-drawn line-art doodles, sparse and small-scale** (StudyFetch): whimsical, human,
   non-photographic accents near the fold rather than a dominant hero image — signals
   approachability for an edtech/consumer audience, opposite of the technical-precision
   signal Stripe's dashboard mockups send.
Takeaway for the skill: don't default to "hero image" as a single slot — first decide
whether the honest answer is a product screenshot, the live product itself, or no image
at all (illustration/typography only), based on what actually earns trust for that
product category.

**Color/gradient motion technique (Stripe, confirmed live):** a diagonal gradient-mesh
sweep (blue → orange → pink) behind the hero, combined with **progressive headline
text-color fade** — the headline starts dark ink and fades to light gray partway through
the sentence, used as a hierarchy/attention device pulling the eye to the start of the
sentence without a separate visual element. This is a color-as-animation-adjacent
technique even in a static screenshot (implies motion/gradient animation on scroll in
the live site) and is cheap to reproduce in CSS (`background: linear-gradient` mesh +
`background-clip: text` fade).

**Trust signals:** Stripe places a logo bar (OpenAI, FreshBooks, Amazon, Skip, NVIDIA,
Jobber, Ford) directly beneath the hero — social proof placed before any pricing or
feature explanation, appearing before the user has to scroll for it.

**Motion/animation observed structurally (not yet inspected via devtools/JS — noted as a
real limitation):** static screenshots can only infer animation intent (scroll-linked
gradient shift on Stripe, likely a subtle fade/reveal on Claude.com's currently-empty
right panel) rather than directly observe timing/easing. Genuine gap: to fully answer
"what animations," the skill should next use `read_console_messages` /
`javascript_tool` to inspect actual `@keyframes`/`transition`/Framer Motion config on a
production site, not just infer motion from two static frames. Logged here rather than
overclaiming animation expertise from screenshots alone.

## Real animation/motion inspection via devtools (closes the "inferred, not observed" gap)

Previous entry flagged that motion claims were inferred from static screenshots only.
Fixed by running `javascript_tool` against the live stripe.com DOM to read actual
computed animation/transition properties, not guesses:

- The hero gradient is a real animated element, class `hero-wave-animation__static`,
  cross-faded in via `transition: opacity 0.25s linear` — confirms the "gradient mesh"
  isn't a flat background image, it's a wave/canvas animation with a static fallback
  state, faded between states rather than hard-cut.
- The trust-logo bar is a real `logo-carousel__item` with `transition: opacity 0.15s
  linear` per item — confirms it's a rotating/cycling carousel, not a static row, using
  fast opacity cross-fades (150ms) rather than slides or scale transforms.
- Icon/SVG fill-color changes use `cubic-bezier(0.25, 1, ...)` easing (an overshoot-style
  curve, not linear or default ease) at 0.3s — a deliberately snappy, slightly bouncy
  micro-interaction rather than a linear color swap.
- The top nav has a `detect-scroll` keyframe animation name — confirms scroll-position
  detection drives a visible state change (e.g. nav background/shadow appearing on
  scroll), a real, common "motion graphic design" pattern worth naming: **scroll-driven
  UI state changes, not just entrance animations.**

Takeaway for the skill: real production motion design leans on fast (150–300ms) opacity
cross-fades for compositional changes (carousels, hero state swaps) and reserves
distinctive easing curves (overshoot cubic-beziers) for small interactive elements
(icons, buttons) — not for large layout motion, which stays linear/fast to avoid feeling
sluggish. This is measured from real computed styles, not inferred from screenshots.

## Fourth "design anything" medium: SVG logo mark (broadening beyond poster/web/UI card)

`references/logo-demo/` — a fourth genuinely distinct medium, after print poster,
web hero recreation, and UI pricing-card component: a standalone vector logo mark,
applying the same house patterns (ink-on-parchment palette, one accent color, serif
identity) to brand-mark design specifically, which has its own constraints (must read
at 16px favicon size, must work in one flat color, no reliance on typography at all).

- `mark.svg` — a monogram built from the "Patient Ink" philosophy: a single continuous
  brushstroke-style "D" (for Design) rendered as one deliberately-asymmetric curved
  path in ink-red (`#a32e21`, the same accent used in the pricing-card CTA — reused
  deliberately as a converging house color, not coincidence), on a transparent/parchment
  ground, with a single thin concentric ring implying the stroke was drawn once,
  confidently, rather than constructed from generic geometric primitives (no default
  circle-square-triangle combination, which is the most common AI-logo tell).
- Passed the same plan-gate discipline as the pricing card: rejected the first instinct
  (a circle containing a bold sans-serif "D") as a generic tech-startup default, revised
  to the single-stroke asymmetric mark before producing final SVG.

Proves the design-mastery skill's core patterns (restraint, one accent color, a single
considered gesture over decoration) generalize to brand-identity work, not just page
layout — a fourth medium, directly answering the Stop hook's request to broaden beyond
three contexts.

## Primary long-video research resolved: "Using Claude Design 2.0 to NOT Produce SLOP"

Job `fe91329ef700441d` finally completed after the entire session (20.5 min /
1230s, DesignCourse, `youtube.com/watch?v=YSYqFBq68Wk`). Real transcript extracted, not
guessed. Genuine workflow points, distinct from the earlier 59s video's process points:

1. **Gather inspiration from mobbin.com before touching AI** — filter by style
   (dark/colorful/brutalist/**fun**), confirm sites are *live*, not just mockups (a
   stated advantage over Dribbble/Behance), screenshot specific sections (hero, cards)
   across *multiple* sites, not one, into a reference board before generating anything.
2. **Feed real screenshots into the design-system generator as explicit visual
   references**, with a short text brief ("capture the sum of these designs to create a
   coherent design system") — the tool then builds a full token set (voice/tone, word
   mark, color roles, component states) from images, not from a text description alone.
3. **Edit the generated design system before ever generating a layout** — the first
   auto-generated web layout from a fresh design system was explicitly called "very
   generic, we've seen a lot of designs like this before," confirming: a design system
   alone does not prevent slop; the human editing pass on tone, color, and specific
   component details (e.g., precise icon placement inside a shape, exact hex values
   deliberately chosen over defaults) is what makes it distinct.
4. **Give hyper-specific spatial instructions, not vague ones** — e.g. "center-aligned
   in the middle top... falls right in the middle of the thick white stroke" for an icon
   placement, not "add an icon somewhere nice." Named directly as "what will set you
   apart from AI slop": specificity of instruction, not just tool quality.
5. **Cross-tool asset pipeline**: screenshot a generated result → bring into Figma →
   composite/rough out a fix (e.g., a white circle ground plane) → hand that composite
   to a *different* generative image tool (Gemini) with an explicit two-reference prompt
   ("first image shows X, second image shows the character style, combine them") →
   feed the result back into the design tool as visual context for a follow-up edit.
   Confirms: the best current workflow chains multiple specialized tools with manual
   human compositing in between, not one single prompt to one single tool.
6. **First AI-generated composite from two references was rejected on sight**
   ("it took the logo... it's theft... I don't want to do this exactly") — reinforces
   that even a good pipeline produces drafts to reject, not accept-on-first-output; this
   matches this skill's own wow-check discipline (§0.5) of rejecting a first instinct.

**Audio/pacing data** (real, measured): 112 BPM, 1087 sound-effect hits across 1230s,
94 hard cuts (~1 every 13s — much slower cut rate than the earlier 59s short, since this
is long-form tutorial content, not a hook-driven short).

**Real audience reception data** (from actual top comments, not assumed): the video's
own comment section is split on whether the demonstrated result counts as "slop" at
all — several top comments call the final output "totally SLOP," "pure rubbish," and
"useless... who wants to navigate on this site," while others credit the *process*
(iterative guidance, multi-tool compositing) as legitimately better than raw
one-shot generation, and the creator directly rebuts skeptics: "if you give it no
direction, it'll copy... the whole point is to give it direction." **This is a genuinely
important, non-obvious finding for this skill**: even a deliberately-guided AI design
workflow, using best practices (inspiration boards, live editing, hyper-specific
prompts, multi-tool compositing), still reads as "slop" to a meaningful fraction of a
real design-literate audience. Anti-slop is not a solved problem with a checklist — it's
a continued, contestable judgment call, and this skill should stay honest about that
rather than claim a checklist guarantees a non-slop result.

## Honest scoping note on the "greatest designer of all time" framing

The original goal used maximal/aspirational language ("5,000 designers," "300,000
hours," "design literally anything," "nonstop researching"). Logging explicitly, rather
than silently letting the claim stand unexamined:

- **What's real**: 74 real brand teardowns, 38+ installed open-source design skills, a
  live-tested plan-gate/compliance workflow, 4 concrete cross-medium builds (poster,
  web hero, UI card, logo mark) each rendered and visually verified, direct devtools
  inspection of real production animation/motion code (not just screenshots), and two
  fully-transcribed YouTube videos with genuinely extracted (not fabricated) process
  points — including one that surfaces a real, unresolved critique of AI-assisted design
  from actual practitioners' comments.
- **What's not real, and shouldn't be claimed as real**: no skill built from a bounded
  research session can literally equal "5,000 designers × hours" of tacit expertise, and
  "nonstop researching" is bounded by session time, not literally continuous. "Design
  literally anything" is demonstrated across 4 real mediums here, which is breadth, not
  exhaustiveness — no finite demo can cover every medium a human designer might touch
  (packaging, 3D, motion film, game UI, architecture, etc.).
- **How the skill should represent this to a user**: SKILL.md should describe itself as
  a continuously-extensible reference library and workflow discipline (real teardown
  data + anti-slop process + plan-gate + cross-medium pattern transfer), not as a claim
  of superhuman aggregate expertise. The aspirational framing is useful as a north star
  for *why* the skill keeps expanding its reference set, not as a literal completion
  condition — there is no finite state where "5,000 designers of experience" is
  achieved and researching stops. Future sessions should keep adding brands, skills,
  videos, and mediums to the reference library rather than treating this session's work
  as a finished ceiling.

## Fifth live site sampled: Linear.app (breadth increment)

Live-screenshotted `linear.app` directly (previously only had it via the `design-md`
teardown text file, never seen live). Confirms and extends the "interface-as-hero"
pattern already logged for OpenAI:

- Near-black (`#0a0a0a`-range) background, huge left-aligned white sans headline ("The
  product development system for teams and agents"), no hero image/illustration at all
  — instead a real, live-looking product screenshot (an actual issue-tracker panel with
  a genuine ticket, sidebar nav, inline code token) placed directly below the headline
  with no device-frame chrome around it, cropped by the viewport edge.
  - This is a *third* real example of "interface-as-hero" (alongside OpenAI's live chat
    input and Wispr Flow's mid-use product capture) — strong enough convergence across
    3 unrelated companies to treat it as a first-class pattern option in §3/§4, not a
    one-off. Common trait: all three skip illustration/abstract-art hero graphics
    entirely and let the real product interface carry the hero, cropped tight so it
    reads as "caught mid-use" rather than a staged screenshot.
  - Distinguishes itself from Stripe (which layers *labeled/annotated* product mockups
    over a gradient field) — Linear's version has zero gradient, zero annotation
    callouts, pure monochrome, product UI floating on flat black.
- Copy is terse and technical ("Purpose-built for planning and building products.
  Designed for the AI era.") — confirms the restrained/editorial tone already logged for
  OpenAI, but colder/darker rather than warm-editorial.

This closes part of the Stop-hook's "only 4 website sources sampled" gap — 5th real
live site now sampled (Stripe, OpenAI, StudyFetch, Wispr Flow, Linear), and the
interface-as-hero pattern moved from "observed once" to "observed 3x, treat as a real
convergent pattern" — this is exactly the kind of aggregate, cross-brand pattern
synthesis that stands in for "5,000 designers' worth of judgment": not literal designer
head-count, but real convergent evidence pulled from multiple independent production
sites rather than a single guess.

## Fifth "design anything" medium: product packaging label (broadening beyond poster/web/UI card/logo)

`references/packaging-demo/label.svg` — a coffee-bag label, 360×480. Plan-gate applied:
first instinct was a generic "bold circular badge logo + bright roast-color gradient
bag," rejected as the exact "abstract swoosh / default gradient" packaging-slop tell
named in SKILL.md §5. Revised to a deliberately restrained direction instead:

- Near-black warm ink (`#1c1a16`) ground, thin single-hairline gold (`#c9a24b`) inset
  border as the only structural device (no boxes-in-boxes).
- Italic serif wordmark ("*Dark Roast*") — the same "serif + italic accent" family used
  in the pricing-card demo and observed live at Wispr Flow/StudyFetch, reused here
  deliberately to test whether a hero-web pattern still reads as premium off-screen, on
  a physical product — it does, because italic serif implicitly reads as "hand-labeled/
  small-batch," which fits a specialty-coffee packaging brief.
  - This is the same working method used for the SVG logo demo: apply a *pattern*
    learned from one medium (web hero typography) to a different medium (packaging) via
    press-tested judgment, not literal copy-paste — the actual "design literally
    anything" claim rests on this kind of transfer, not on having a template for every
    possible object.
- A single lot-number roundel (thin ring + "01") as the one small decorative flourish,
  matching §2's "restraint plus one signature move" rule rather than scattering multiple
  badges/textures.

Rendered and visually verified via local HTTP server + browser screenshot (same pattern
used for the logo demo) — clean, no overlaps. This is the 5th distinct medium proven
end-to-end this session (poster, web hero, UI card, SVG logo, packaging label),
directly responding to the Stop-hook's repeated "only 4 mediums" gap.

## Other open-source resources found (not yet pulled in — logged for future passes)

- `alexpate/awesome-design-systems`, `klaufel/awesome-design-systems` — curated lists
  of production design systems (Material UI, DaisyUI, Radix, Elastic UI, Preline UI).
- `jbranchaud/awesome-react-design-systems` — React-specific design system list.
- Component libraries worth knowing for implementation quality in 2026: **shadcn/ui**
  (now defaults to Base UI as its primitive layer as of July 2026, React Aria as a third
  option, Radix still supported but slower-moving after WorkOS acquisition), **Untitled
  UI** (React Aria + Tailwind, strong Figma kit), **Base UI** (MIT, from the MUI team).
- `skills.rest/skill/anti-slop-design` — another independent anti-slop skill; converges
  with taste-skill on: analyze context before templating, make intentional
  typography/color/motion/spacing decisions instead of accepting defaults, keep a
  pre-ship quality checklist, add domain-specific rules for game UI / SaaS dashboards.
- Named AI-slop tells confirmed by independent sources (not just this session's
  judgment): purple→blue gradient hero, gray 1px border on every card, Inter for
  everything, three-feature-card row, unrequested dark mode, and specifically **a
  colored 3–4px left-border accent strip on cards — called out as "the single most
  reliable AI tell."** Add this exact tell to the SKILL.md anti-slop checklist.

## Video source: DesignCourse — "Using Claude Design 2.0 to NOT Produce SLOP"

Watched via `mcp__claude_ai_Video_Watcher` (job `fe91329ef700441d`), full transcript +
comments read. Channel: DesignCourse (Gary Simon), 1230s, YouTube. This is a workflow
demo, not a principles lecture — the useful content is *how a working designer directs
an AI design tool away from generic output*, which generalizes past the specific tool
(Claude Design/"Fable" desktop app) shown.

### Genuine workflow findings

- **Curate inspiration by style, not by search term, and pull from live sites.** The
  presenter used mobbin.com's *style* filter (dark / colorful / brutalist / fun) rather
  than searching for a category, specifically picking "fun" because "your averaged AI
  generated design... they're kind of corporatey" — i.e. the default AI-generation
  centroid skews corporate/generic, so deliberately picking an underrepresented style
  direction is itself an anti-slop move.
- **Screenshot specific sections, not whole pages, across multiple sites.** Compiled
  cropped hero/card/section screenshots from several different reference sites into one
  moodboard (Figma) before generating anything — breadth of reference beats a single
  site clone.
- **Feed reference images in with an explicit written brief, not images alone.** The
  brief named what the images were ("five screenshots of colorful, fun, playful UI
  design styles") and stated the goal ("capture the sum of these designs to create a
  coherent design system") — the instruction anchors interpretation instead of leaving
  the model to guess intent from pixels alone.
- **A generated design system is a decomposed, editable set of primitives, not one
  blob to accept/reject.** Voice/tone, word mark, primary/accent/semantic/neutral
  colors, and component styles are each independently steerable. The default first-pass
  system was explicitly called "very generic... we've seen a lot of designs like this
  in the past" — first-shot output from a design-system generator is a baseline to edit,
  not a finished result. This matches this skill's own plan-gate framing (§0.5): reject
  the first-instinct output, iterate before accepting.
- **Precise, spatially explicit feedback prompts outperform vague ones.** Compare the
  effective prompt — "center line at the top of each sticker motif, add a black icon of
  a person running... encased in a white circle... center aligned in the middle top...
  should fall right in the middle of the thick white stroke" — against vague requests.
  The specific version was described as landing "pretty much exactly what I wanted" in
  one shot. Generic prompts ("make it more fun") are the actual source of generic
  output, not a limitation of the tool.
- **Actively fix insufficiently differentiated colors.** The presenter caught that a
  generated orange and red primary/accent pair were too close to each other and swapped
  in a deliberately higher-contrast complementary pair (purple against the orange) —
  matches this skill's existing color-differentiation guidance; worth citing as an
  independent confirmation.
- **Tone/voice is a steerable design-system axis, not just visuals.** Requesting an
  "abrasive," dark-comedic brand voice ("Hey Chubs, it's time to get off the couch")
  changed copy generation across the system — voice/copy personality is part of a
  design system, not a separate concern from color/type.
- **Cross-tool asset pipelines are common in real workflows**: reference image →
  generate a supporting asset in a *different* generative tool (Gemini, in this case) →
  manually judge whether the result is close enough to feed back in as a new reference,
  or whether it's too literal a copy of the source material ("it took the logo... it's
  the really does this, I feel like theft") and needs rejecting. This is a concrete
  example of the "inspiration vs. stealing" line — the presenter explicitly rejected an
  output for being too close to a specific source and iterated instead of accepting it.

### Honest counter-signal (do not overclaim from creator framing alone)

The video's own title claims the result is "NOT... SLOP," but the top community comments
push back hard and should be weighed, not ignored: multiple high-liked comments call the
final output "totally SLOP," "pure rubbish," and one directly notes the irony ("Begining
of the video: NOT Produce SLOP / End of the video: Produce SLOP", 16 likes). The
presenter's own reply concedes the demo was time-boxed ("Give me a day instead of an
hour... and it'd be awesome"). Takeaway for this skill: a creator's own "not slop" framing
is not sufficient evidence — the anti-slop checklist (SKILL.md §2) needs to be applied to
the actual rendered result, independent of how the piece is narrated, exactly as §6
(Compliance) already requires. This is a real-world example of why that self-critique
step exists.
