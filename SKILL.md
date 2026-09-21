---
name: design-mastery
description: Master design orchestrator — invoke for ANY design task (websites, apps, decks, brand, motion, illustration) and ALWAYS when the user uploads/pastes a screenshot or reference image and wants it analyzed, rebuilt, or matched. Routes to the right specialist skill, runs the screenshot-to-rebuild pipeline, applies the anti-slop checklist, and injects reference-site pattern knowledge (Stripe, OpenAI, Claude.ai, Wispr Flow, StudyFetch, Linear, Vercel). Composes with taste-skill, image-to-code-skill, redesign-skill, and the designer-skills plugin (design-research, visual-critique, interaction-design, design-systems, ux-strategy, prototyping-testing) when installed.
---

# Design Mastery

You are acting as a design director applying a structured, researched set of principles
across brand, UI, motion, typography, illustration, and front-end craft. The goal is never
"a website that works" — it's a considered, well-crafted result with zero AI-slop tells,
within the scope and limitations documented in `DESIGN_SKILL_V4.md` — the current
dense-judgment ruleset (supersedes `DESIGN_SKILL_V1.md`, `DESIGN_SKILL_V2.md`, and
`DESIGN_SKILL_V3.md`; see `benchmarks/BENCHMARK_REPORT_LIVE_V3.md` for the measured basis of
that pointer).
For motion-design and presentation/deck-craft principles, also see
`references/motion-and-presentation-notes.md`.

## 0. Check for installed specialist skills first

Before working from this file alone, check whether these companion skill packs are
installed and prefer invoking them for their specialty (they contain far more depth than
can live in one file):

- `taste-skill` — anti-slop judgment, aesthetic critique, style presets (minimalist,
  brutalist, soft, redesign).
- `image-to-code-skill` — image-first generation → deep analysis → implementation pipeline.
- `redesign-skill` — taking an existing site/screen and elevating it.
- designer-skills plugin: `design-research`, `visual-critique`, `interaction-design`,
  `design-systems`, `ux-strategy`, `prototyping-testing`, `designer-toolkit`.
- `frontend-design` (superpowers) — for actual implementation quality once direction is set.
- `dataviz` — for any chart/graph/dashboard element inside the design.
- `apple-hig` — official Apple Human Interface Guidelines, 156 distilled files, tiered
  routing index. Use for ANY Apple-platform UI (iOS/iPadOS/macOS/tvOS/visionOS/watchOS)
  and as a general source of rigorous platform-convention thinking even off-Apple.
- Official `anthropics/skills` set: `canvas-design` (posters/static visual art),
  `brand-guidelines` (Anthropic brand application), `theme-factory` (light/dark token
  themes), `web-artifacts-builder` (multi-file HTML/JS artifact scaffolding),
  `webapp-testing` (browser-drive a built app to verify it actually works),
  `algorithmic-art` (generative/procedural visuals).
- `plugin87-*` design-architect pack (19 skills, installed with that prefix): notably
  `plugin87-apply-aesthetic` (resolves a named look into tokens across **138 real design
  systems** — apple, linear-app, stripe, vercel, notion, material, shadcn, spotify, tesla,
  etc.), `plugin87-design-tokens`/`plugin87-brandkit` (DTCG 3-tier token generation),
  `plugin87-design-review` (6-dimension critique + Nielsen heuristics), `plugin87-design-qa`
  (lint/contrast/visual-regression gates), `plugin87-image-to-code`, `plugin87-migrate-design-system`
  (bridge to Material 3/Apple HIG/Fluent/Carbon/Ant/shadcn/Radix/Chakra/Mantine/Bootstrap),
  `plugin87-data-dashboard` (dense data-viz screens). Reference data (138-system library,
  token/framework adapters) copied to `references/plugin87-data/`.

Local copies exist at (not yet installed as Claude Code skills — offer to install into
`~/.claude/skills/` if the user wants them active by name):
`~/Documents/Documents - Jacob's MacBook Air (7)/Codex/taste-skill/skills/*`
`~/Documents/Documents - Jacob's MacBook Air (7)/Codex/designer-skills/*/skills/*`

If none are installed, this file is self-sufficient for judgment; use `frontend-design`
for the actual build.

- `impeccable` — award-winning-design-director mode with a strict pre-edit setup script,
  DESIGN.md/PRODUCT.md context loading, refinement-vs-redesign discipline, and a bounded
  (not open-ended) self-QA pass. Use it for the actual build once direction is chosen; its
  "craft floor" reference is the hard ban-list layer beneath this file's anti-slop checklist.

## 0.5 Plan gate — pass before writing any code

Before generating a single line of UI, state a short plan (layout, one signature motif,
palette/type direction, what makes it distinct) and run it through two questions honestly:

1. **Will the user say "wow"?** — If the plan reads as competent-but-forgettable, it fails.
   Push one element further: a bolder type pairing, a more specific motion idea, a sharper
   layout choice, tighter craft on one signature detail. Competent is the floor, not the bar.
2. **Would anyone look at the result and say "this is vibe-coded"?** — Check the plan against
   §2's anti-slop checklist and `impeccable`'s craft-floor bans *before* building, not after.
   If the plan itself contains a slop tell (generic 3-card grid, purple-blue gradient hero,
   left-border accent strips, default Tailwind spacing with no signature move), redo the plan.

Only proceed to build once the plan clears both checks. This is a real gate, not a
formality — if either answer is "no" or "maybe," revise the plan first.

## 1. Screenshot → analyze → rebuild pipeline

**This is not a separate program to build — it IS the workflow below, run by whichever
model (Claude or any other multimodal model) has this skill loaded.** Any Claude model
can read an uploaded image directly (no OCR/vision API needed — image understanding is
native), so "upload a screenshot and get it analyzed instantly" is satisfied by: the
image lands in context → this skill is triggered → steps 1–5 below execute in that same
turn. Verified working this session: live screenshots of wisprflow.ai and studyfetch.com
were read directly, exact colors/type-treatment/layout were extracted from the pixels
(§4's "serif + italic accent word" pattern was derived this way, not from prior
knowledge), and it was written back into this reference library. The only thing to
maintain is that this skill fires reliably on that trigger — which its `description`
frontmatter is written to do.

Trigger this whenever the user uploads/pastes an image, a URL to a live site, or a video
of an interface and wants it recreated, matched, or critiqued.

1. **Look at the actual pixels, don't guess from vibe.** Read the image at full
   resolution. If it's a URL instead of a file, use browser tools to screenshot it (full
   page + key sections at real viewport widths) before analyzing.
2. **Extract a design token sheet** before writing any code:
   - Color: exact hex/OKLCH for bg, surface, text (primary/secondary/muted), accent,
     borders — note if dark mode exists and how contrast is handled.
   - Type: font family (guess closest match if custom — check for Inter, Geist, Söhne,
     GT America, Styrene, Suisse — these dominate premium SaaS), scale/ratio, weight
     jumps, line-height, letter-spacing on headings.
   - Spacing: base unit (4/8px grid?), section padding, gutter, max content width.
   - Radius: corner radius scale (sharp/4px/8px/16px/full — this alone signals brand
     personality).
   - Shadow/elevation: none (flat), soft ambient, hard offset (brutalist)?
   - Grid: column count, asymmetry, breakout elements.
   - Motion cues visible in a static shot: blur trails, staggered opacity, implied
     parallax, cursor/gradient glow — infer the animation system (see §3).
3. **Name the layout pattern** (hero formula, nav pattern, card system, footer style) —
   see reference library in §4 for what it's probably imitating and how to nail it better
   than a generic clone.
4. **Rebuild with real code**, not an approximation — match spacing and type scale within
   a few px, not "close enough." Build it as its own component/page so it can be diffed
   visually against the reference.
5. **Self-critique against §2 anti-slop checklist** before calling it done. Screenshot
   your own result at the same viewport and compare side-by-side.

## 2. Anti-slop checklist (apply to every output)

Kill these on sight — they are the fingerprint of generic AI output:

- Purple/blue gradient hero on dark background as a default with no brand reason for it.
- Generic 3-icon feature grid with a colored circle behind every icon.
- Centered headline + subhead + two pill buttons + vague abstract blob graphic.
- Cards-inside-cards-inside-cards; nested rounded containers with no visual reason.
- Emoji used as icons in a "professional" product UI.
- Tiny unreadable pills/labels/badges scattered for fake "interface texture."
- Uniform 8px-radius-on-everything with no radius hierarchy.
- Inter/system-ui with default Tailwind spacing and zero typographic point of view.
- Lorem-ipsum-shaped copy that's technically real words but says nothing concrete.
- Stock-photo people smiling at laptops.
- Drop shadows on every element instead of a deliberate elevation system.
- Full-bleed color blocks with low-contrast text "for aesthetic."
- Overuse of `backdrop-blur` glassmorphism as a crutch instead of a chosen material.
- Icon libraries used unstyled and mismatched in stroke weight from the rest of the UI.
- A colored 3–4px left-border accent strip on cards — independently called out across
  multiple design critics as the single most reliable AI-generated-site tell.

Instead: pick 1–2 deliberate signature moves (a distinctive type pairing, one recurring
motif, a specific motion character) and repeat them consistently — restraint plus one
strong idea reads as taste; many small decorative flourishes reads as slop.

## 2.5 The purposefulness rule (highest-priority check, applies everywhere)

Before adding any element — a badge, icon, divider, stat, animation, decorative shape,
extra button, status dot, whatever — ask: does this actually help the user navigate,
understand, or use the thing, or does it make the result look meaningfully better? If
the honest answer is "barely" or "not really," don't add it. This is not a subjective
nice-to-have on top of the anti-slop checklist — it's the reason most of §2's list exists
in the first place: gradient blobs, decorative pill badges, nested cards, icon-behind-a-
circle grids are all instances of adding something because it's a common pattern, not
because it does anything for this specific screen.

This cuts both ways:
- Don't add UI chrome, copy, or motion "to fill space" or "to look more complete" — an
  empty area is not a defect; an unjustified element is.
- Don't keep something from a reference or template just because it was there — every
  element earns its place in *this* build, not by inheritance.
- When self-critiquing (§1 step 5, §5.5's grading loop), explicitly ask of every element
  "what would be lost if this were deleted?" — if the answer is "nothing a user would
  notice," that's a real finding, not a nitpick to wave away.

Applies to actual functional cruft too, not just decoration: an aria-live region no one
reads, a toggle that doesn't change any real state, a second button that duplicates the
first's action — all fail the same test.

## 3. Motion & imagery direction

What to animate and why — not motion for its own sake:

- **Entrance**: content fades/slides in on scroll only if it clarifies reading order
  (staggered by ~40–80ms per sibling). Never animate for decoration on every element —
  pick the 2–3 moments that deserve it (hero, key proof point, CTA).
- **Micro-interaction**: buttons/links get a fast (120–180ms) ease-out response; nothing
  in a UI should feel like it has no feedback on hover/press.
- **Cursor-driven**: gradient glow or spotlight following cursor is a strong, cheap
  differentiator for hero sections (see Linear, Vercel) — use sparingly, one per page.
- **Scroll-driven storytelling** (product demos, feature reveals): pin a section and
  scrub an animation/video tied to scroll position — this is what makes Stripe/Linear/
  Wispr Flow feel "alive" instead of static. Needs real engineering (GSAP ScrollTrigger,
  Framer Motion `useScroll`, or native scroll-timeline) — budget for it, don't fake it
  with a plain CSS animation that ignores scroll position.
- **Measured, not guessed, from live devtools inspection of stripe.com** (via
  `getComputedStyle`, not visual inference): compositional/layout changes (hero
  wave-canvas cross-fade, logo-carousel item rotation) use fast flat `opacity 0.25s
  linear` / `0.15s linear` transitions with no easing curve; small interactive elements
  (icon fill-color) use a distinct overshoot-style `cubic-bezier(0.25, 1, ...)` at 0.3s.
  Takeaway: reserve expressive easing for small interactive elements only — big
  compositional transitions should be fast and linear so they read as "instant," not
  "animated."
- **Imagery choice**: prefer one of — custom illustration with a consistent stroke/fill
  system, real product screenshots in a branded device frame, abstract generative/3D
  renders (gradient mesh, glass, metaballs) matching the type's personality, or nothing
  (confident whitespace + type) over generic stock photography. Match imagery style to
  brand: playful product → custom illustration; infra/dev tool → abstract 3D or pure
  type; consumer AI → soft gradients + real UI.
- **Video/GIF hero**: only when it demonstrates the product doing something in <6s loop;
  never a slow cinematic B-roll with no information content.

## 3.5 AI-generated imagery — when to suggest it, prompts, and where to get it

When a design needs a photo/illustration and no real asset exists (no product screenshot,
no team photo, no licensed stock), proactively suggest AI-generated imagery as an option
instead of defaulting to a generic stock-photo placeholder or an abstract blob graphic —
but flag it as AI-generated so the user can decide, and always write the actual prompt
rather than leaving that step to them.

This is worth surfacing as a standing recommendation, not just a fallback for when
nothing else is available — clients consistently respond well to custom AI-generated
imagery on a site because it looks bespoke rather than recognizably-stock, and it's
cheap to produce in a few variations for them to pick from. When presenting design
options or a finished build to a client, actively mention it as an upgrade path even if
the current draft is using a stock photo or placeholder that technically "works" —
frame it as "I can also generate a few custom AI images matched to your brand instead of
stock photography, want to see options?" rather than waiting to be asked.

**When to suggest it:**
- Hero/marketing imagery where a specific mood, lighting, or subject is needed and no
  real photo exists yet (early-stage product, rebrand, concept mockup).
- Custom illustration in a consistent style across many spots (icon set, empty-state
  art, onboarding graphics) where commissioning real illustration isn't in scope.
- Placeholder imagery for a build-in-progress that's meant to be swapped for a real
  asset later — say so explicitly in the handoff so it isn't shipped as final by mistake.
- Anywhere a generic stock photo is currently doing the job — stock imagery is itself
  one of the recognizable "this looks templated" tells clients react to; a custom
  AI-generated alternative in the brand's actual palette/mood reads as considered rather
  than off-the-shelf, and is worth proposing as a swap even on an otherwise-finished page.
- Not for: testimonial headshots, team photos, or anything implying a real person/event
  that doesn't exist — that crosses from "placeholder art" into fabricated authenticity
  and belongs in the dishonesty/fake-state category the convergence-loop rubric checks
  for (§5.5). Use a generic avatar/initials treatment instead, or omit the photo.

**How to prompt it well (avoid the "AI photo" look):** generic prompts ("a person using
a laptop, modern office") produce the over-smoothed, waxy-skin, centered-subject look
that reads as obviously synthetic. Write prompts the way a working photographer/art
director would brief a shoot:
- Name a specific camera/lens/film treatment (`shot on 35mm, f/1.8, shallow depth of
  field`, `medium format, slight grain`) rather than leaving rendering style to default.
- Specify real lighting conditions (`overcast window light`, `golden hour backlight`,
  `single softbox key light, 45°`) instead of "well lit."
- Give a specific, slightly imperfect composition (`off-center, rule of thirds, candid
  mid-motion`) rather than a centered hero pose — perfectly centered/symmetrical subjects
  are themselves a tell.
- Tie the palette/mood to the project's actual design tokens (reference the extracted
  hex values from §1, not generic adjectives) so the image doesn't fight the UI it sits
  in.
- For illustration (not photography), name a specific reference style and stroke/fill
  system (`flat vector, 2px stroke, single accent color fills, no gradients`) rather than
  "modern illustration style," which defaults to the same generic blob-character look
  §2 already flags.

**Where to generate it:**
- If Claude has the `higgsfield` MCP tools available in this session (`generate_image`,
  `generate_image_batch`, or the broader creative toolset), use them directly — write the
  prompt using the guidance above and generate the asset in-session rather than just
  describing where to go.
- Otherwise, name concrete destinations the user can go to themselves, matched to the
  need: Midjourney (strongest default aesthetic quality, good for hero/editorial
  photography-style imagery, Discord or web-based), Adobe Firefly (commercially safe
  licensing — best choice when the output needs to be safe for a commercial product, has
  a web UI with structured style/lighting controls), Ideogram (strong at rendering
  legible text inside images — logos, posters, anything with in-image typography),
  Recraft (best for vector/flat-icon-style output that exports as SVG, good fit for the
  illustration case above), Flux/Black Forest Labs models (via Replicate or fal.ai — good
  photorealism, open-weight options for self-hosting), Leonardo.Ai (strong control over
  consistent character/style across a batch, useful for a multi-image icon or character
  set). Give the specific prompt text to paste in, not just the tool name.

## 3.6 Programmatic video with Remotion

When a deliverable needs actual video — not a static hero image or a CSS/scroll
animation, but a rendered `.mp4`/`.gif` (product demo reel, animated logo sting, social
promo clip, an animated explainer for a landing page hero) — use
[Remotion](https://remotion.dev) rather than hand-editing in a timeline tool. Remotion
builds video as a React app: every frame is a pure function of a frame number, so the
same design-token/component discipline this skill already applies to UI (§1's token
sheet, §2's anti-slop checklist) carries directly into motion work, and the result is
versionable, diffable code instead of an opaque `.mp4` no one can re-edit.

- **When to reach for it over CSS/scroll-timeline animation (§3)**: §3's scroll-driven
  techniques are for animating a live web page in the browser. Remotion is for producing
  a standalone video *file* — something that gets embedded as `<video>`/GIF, posted to
  social, or dropped into a deck. If the deliverable never needs to exist outside the
  browser as its own file, stay with CSS/GSAP/Framer Motion instead of reaching for
  Remotion.
- **Structure**: a Remotion project is a `Composition` (fixed `durationInFrames`,
  `fps`, `width`/`height`) rendering a tree of normal React components; use
  `useCurrentFrame()` and `interpolate()`/`spring()` from `remotion` to drive per-frame
  values instead of CSS transitions (CSS transitions don't reliably render frame-exact
  across `remotion render`'s headless capture). Reuse the actual brand's design tokens
  (colors/type from §1's extraction or the project's real CSS) inside the video rather
  than re-deriving a new palette — the video should look like it belongs to the same
  brand as the site.
- **Apply the same anti-slop discipline as static work**: a generic bouncing-logo intro
  or a stock "particles drifting on gradient" background reads as templated in video
  exactly the way a purple-gradient hero does in a webpage (§2). Pick one signature
  motion idea tied to the brand (a specific easing character, a recurring transition
  shape, real product UI captured mid-interaction) rather than a generic template.
- **Workflow**: scaffold with `npx create-video@latest`, build compositions under
  `src/`, preview live in the Remotion Studio (`npm run dev`), then render with
  `npx remotion render <composition-id> out/video.mp4`. For a short social/GIF loop,
  render to a sequence and convert, or use `@remotion/gif`.
- **Where it fits with the rest of this skill**: treat it as the implementation layer
  for §3's "video/GIF hero" bullet and for `references/motion-and-presentation-notes.md`'s
  motion-design guidance — read that file alongside this section for the broader
  motion-design principles (timing, easing character, what a "signature motion idea"
  actually means) that apply whether the output is CSS or a rendered Remotion video.

## 4. Reference pattern library

`references/categories/` holds one concise, actionable file per design category — web
landing pages, product UI, mobile UI, dashboards, branding, logos, posters/editorial,
packaging, presentation design, and marketing creative. Each file gives that category's
principles, anti-patterns, composition rules, typography/spacing/hierarchy guidance, and
ends with a "Verified build:" line pointing to a real screenshot-checked demo. **Read the
matching category file before starting any task in that category** — it's the fastest
path to category-specific rules this section doesn't cover.

Study the *pattern*, not just the brand — these are the moves worth stealing:

- **Stripe**: precise multi-column layouts with subtle gradient mesh accents; docs-grade
  information density handled with generous whitespace and a strict type scale; code
  blocks as first-class hero content; very deliberate micro-shadows for depth without
  skeuomorphism.
- **OpenAI**: restrained, editorial, huge type, lots of negative space, monochrome with
  one accent used sparingly, content-led (the writing/imagery carries it, not UI chrome).
- **Claude.ai / Anthropic**: warm off-white/cream backgrounds instead of default gray,
  serif/humanist type pairing for warmth against a technical product, soft coral accent
  used as the single signature color, rounded-but-not-bubbly geometry.
- **Wispr Flow**: product-demo-first hero (real UI captured mid-use, not abstract art),
  confident single-column narrative flow, motion used to show the actual product doing
  the thing it promises within the first viewport.
- **Linear**: near-black UI, cursor-reactive gradient glow, extremely tight/technical
  type, keyboard-shortcut-driven feel reflected even in marketing site copy and icons.
- **Vercel**: monochrome + one signature gradient, terminal/code aesthetic as brand
  texture, heavy use of real product screenshots over illustration.
- **StudyFetch**: playful-but-credible edtech tone — rounded friendly type, bright but
  limited palette, product screenshots framed in device mockups to build trust while
  staying approachable.
- **Wispr Flow**: shares a formula with StudyFetch worth naming on its own — see the
  "serif + italic accent word" hero pattern below.

### The "serif + italic accent word" hero formula (Wispr Flow, StudyFetch)

Large serif/humanist-serif display headline where one phrase breaks into italic serif
for warmth ("Don't type, *just speak.*" / "Learning that *adapts to you*"), set on a
warm cream/off-white (not pure white, not dark) background with a black or saturated-
pastel pill CTA, plus hand-drawn or hand-set decorative elements (curved text paths,
doodle line art). Reads as warm/human/consumer-trustworthy — a strong alternative to
the sans-serif-plus-gradient-mesh formula (Stripe-style, technical) or the monochrome
editorial formula (OpenAI/Anthropic-style, restrained). Good default for consumer AI,
edtech, voice/writing products.

### Real brand design-token library

`references/design-md/` contains 86 real, detailed `DESIGN.md` teardowns (exact hex
colors, full type scale with weights/line-height/letter-spacing, component and spacing
rules) for brands including Stripe, Claude, Vercel, Linear, Notion, Figma, Airbnb,
Shopify, Spotify, **Apple**, and more. Most were pulled from the open-source
`VoltAgent/awesome-design-md` repo; a subset (Duolingo, Robinhood, GitLab, Loom,
Calendly, Patagonia, Zoom, and the current Notion entry) were extracted directly from
live production sites via computed-style DOM inspection rather than the repo. When
matching or drawing on a specific brand, **read that brand's DESIGN.md directly**
rather than relying on memory.
`references/reference-library-notes.md` has the full brand index and grep recipes for
finding cross-brand convergence.

`references/design-team-process.md` covers how elite design orgs actually operate, not
just how their output looks: critique culture and rituals, design-systems governance at
scale, design-ops/leadership structure, the brief→exploration→critique→QA production
pipeline (and which steps AI-generated output tends to skip), a moat-vs-afterthought
calibration framework for matching output quality to context, and the senior-critique
vocabulary (hierarchy/rhythm/tension/contrast/restraint) for self-critiquing a result
before presenting it as final. Read this when the task is about *how* to run the design
process, not just what the artifact should look like.

`references/local-ui-libraries.md` inventories the UI libraries actually installed on
this machine's real projects (Tailwind + Radix UI primitives + shadcn/ui + lucide-react,
found by scanning `node_modules`, not the earlier stray 42-repo GitHub clone-list paste
which was never actually installed anywhere). Check it before introducing a new UI
library into one of this machine's existing React projects.

`references/github-design-corpus-analysis.md` documents a real, verified analysis of
41,031 individually open-source (MIT/Apache/ISC/CC0), permissively-licensed icon assets
shallow-cloned directly from GitHub (Phosphor, Tabler, Material Design, Simple Icons,
Lucide, Iconoir, Ionicons, Radix) — with a sourcing manifest proving the count, and
data-derived (not received-wisdom) conventions on icon canvas sizes, stroke-width scaling
across weight variants, fill-vs-stroke prevalence, and near-universal kebab-case naming.
Read this for icon/glyph-scale decisions specifically.

`references/web-corpus-scan-stats.md` documents an automated, honest, single-GET-per-domain
scan of 346 homepage `<head>` sections (260 succeeded, 86 blocked/timed out/errored — all
disclosed) for `theme-color`, viewport, `og:*`, Google Fonts links, and inline CSS custom
properties. Yield was sparse (e.g. only 26% had a `theme-color`, 9% a Google Fonts link) and
is reported bluntly as a weak statistical signal, not a design audit — a coarser companion to
the 86 deep `design-md/` teardowns, explicitly not a path to a literal 10,000-site corpus.

`references/github-website-corpus-manifest.csv` and its companion
`references/github-website-corpus-analysis.md` catalog **14,425** unique, deduplicated,
pre-2024 (`created_at < 2024-01-01`) open-source WEBSITE repos (portfolio/personal sites,
landing-page templates, Jekyll/Hugo/VuePress themes, Next.js/Astro/Nuxt/Svelte site
boilerplates — not icon libraries), gathered in two rounds: 59 GitHub Search API topic
queries with star-bucket partitioning (8,886 repos), then a second round of 25 additional
topic queries each partitioned by `created:YYYY-01-01..YYYY-12-31` across 2010-2023 to beat
the API's 1,000-results-per-query cap, adding 5,539 net-new unique repos after dedup. The
10,000+ target was crossed legitimately on the second round. Manifest license fields
are unverified API metadata except for a 44-repo sample that was actually shallow-cloned,
had every LICENSE file hand-read (42 MIT + 2 Apache-2.0, 44/44 verified, 0 discrepancies vs.
the API guess), then deleted after analysis. The analysis file has real, source-grounded
findings: Jekyll/Hugo underscore-directory conventions (`_layouts`, `_includes`, `_sass`) vs.
the Astro/Next/Svelte `components+content+config` convention, CSS-approach tracking framework
generation rather than site category (Tailwind only appeared in modern JS-framework repos in
the sample, never in Jekyll/Hugo), near-universal `.github/` presence, and dark-mode support
as a generational split (common post-2022, rare pre-2020) rather than a framework-driven one.

`references/github-repo-design-patterns-analysis.md` extends the manifest work above with
two honestly-separated tracks: full-manifest metadata (language, license, stars, creation
year) computed directly across **all 14,425** manifest repos with no cloning, versus real
design-pattern inspection (CSS methodology, typography, theming, layout, folder
structure, accessibility markers) deep-sampled across **228 newly cloned-then-deleted
repos** stratified by language/star-tier/year — bringing the project's two rounds of
hand/heuristic-inspected repos to **272 total (1.9% of 14,425)**. Read this for
data-backed percentages (e.g. Tailwind adoption tracks framework generation — 0/25 in
PHP repos vs. 48% in TypeScript repos; dark-mode support 39% in 2022-2023 repos vs. 10%
pre-2020) rather than impressions from the smaller 44-repo sample alone.

`references/color-and-ui-physiology.md` grounds this skill's rules in the underlying
vision science and cognition — contrast sensitivity, color-blindness prevalence and why
color can't be the only signal, Fitts's/Hick's Laws, foveal-vs-peripheral acuity and
saccade patterns (F/Z-pattern), working-memory chunking limits, flicker-fusion/peripheral
motion sensitivity, and legibility research (x-height, line length, line-height). Read
this when a design decision needs a "why this is measurably easier to see/read/use"
answer instead of a taste-based one. It also documents two real local projects
(`~/agent-workspace/jacobs-components`, a 62-component 21st.dev library used as the
actual UI source-of-truth for JumpStudy AI, and `~/agent-workspace/tzura`, Jacob's own
anti-slop design tool) that independently converged on several of these same
physiological rules — check those before inventing new UI patterns for their projects.

- **Apple** (`references/design-md/apple/DESIGN.md`): photography-first, edge-to-edge
  product imagery alternating light/dark canvases, SF Pro Display with negative
  letter-spacing, single Action Blue `#0066cc` as the only interactive color, no
  decorative gradients or chrome shadows — the one signature shadow lives under product
  imagery resting on a surface. UI recedes so the product is the hero. For the
  underlying system Apple's own teams design against (not just the marketing site),
  cross-reference Apple's official Human Interface Guidelines
  (developer.apple.com/design/human-interface-guidelines) for platform-level
  interaction/motion/spacing conventions (SF Symbols, Dynamic Type, standard motion
  curves) that the marketing-site teardown alone doesn't capture.

`references/design-systems-index.txt` additionally indexes 166 real production design
systems (Adobe Spectrum, IBM Carbon, Shopify Polaris, Atlassian, Salesforce Lightning,
GOV.UK, etc.) from the open-source `alexpate/awesome-design-systems` list, for when a
task calls for enterprise/systems-level rigor rather than marketing-site polish.

### Video/teardown research

`references/youtube-design-transcripts-notes.md` synthesizes real auto-generated
captions (pulled via local `yt-dlp`, no fabricated content) from **11 of 12** attempted
YouTube videos, each claim attributed to its source video/channel/URL: four Figma Config
talks on design-systems process (2024–2026, including the Dylan Field 2026 keynote), four
AJ&Smart design-sprint methodology videos (a fifth, "Design Sprint 2.0 – User Testing,"
had no captions available and is documented as a real gap, not worked around), and two
The Futur live design-critique sessions with Chris Do. Lower-confidence videos (the two
live/cross-talk Futur sessions) are flagged as such since all captions used were
auto-generated, never official.

Flux Academy (Ran Segall — live redesigns, UX teardown logic), Jesse Showalter (UX
process + frontend), DesignCourse, High Resolution — additional channels for deeper
study, not yet ingested into references, useful for studying *how* a strong designer
talks through trade-offs, not just the end result.

When matching a reference, extract the *underlying system* (spacing rhythm, restraint
level, one signature motif) rather than copying surface decoration — a clone that copies
gradients but misses the restraint reads as slop; one that nails the rhythm and taste
reads as "in the same league."

## 4.5 Synthesized first principles (cross-analyzed from 130+ installed design skills)

`~/.claude/skills/` now hosts the full open-source designer-skills plugin set (Gestalt
laws, motion/animation, typography, spacing, color, IA, research, critique, business
design — ~137 packs, ~15k lines) plus taste-skill's family (anti-slop, image-to-code,
redesign, minimalist/brutalist/soft presets, brandkit). Cross-referencing them for
recurring numbers/rules that show up independently across many packs — i.e. genuine
consensus, not one author's opinion:

**Motion timing (converges across `motion-system`, `animation-principles`,
`interfaces-that-feel`):**
- Micro state changes (checkbox, toggle, button press): 50–100ms, near-instant.
- Standard UI transitions (dropdown, focus ring, tooltip): 150–300ms, ease-out.
- Page/modal/panel-level transitions: 300–400ms.
- Deliberate high-emphasis moments (onboarding reveal): up to 600ms, never longer.
- Staggered siblings: 30–50ms offset each, total sequence under 500–700ms.
- Error recovery: give the user 300–600ms before the next prompt.
- Always define a `duration-instant`/0ms override path for `prefers-reduced-motion`.

**Type scale**: modular scale off a ratio, almost always 1.25 (major third) or 1.333
(perfect fourth) for UI; body line-height ~1.5. Pick one ratio per project and never
mix ad hoc sizes.

**Spacing**: base-unit grid (4px or 8px) with all paddings/margins as multiples of it —
this single rule is the fastest fix for "looks off" layouts and appears as the first
recommendation in nearly every spacing/layout pack.

**Gestalt (`law-of-proximity`, `law-of-common-region`)**: related items are grouped by
spacing/containment before color or borders are added — most "needs more dividers"
instincts are actually a proximity/whitespace problem, not a missing-border problem.

**Critique dimensions (from the `critique-*` family)**: every screen review should pass
through hierarchy → composition → typography → color → density → affordance → brand
consistency, in that order — hierarchy first because a correct hierarchy makes the other
five easier to judge.

**Aesthetic-Usability Effect**: polish reads as *more usable*, independent of actual
usability — meaning visual craft is not "just decoration," it changes measured user trust
and perceived competence. This is the empirical justification for spending real effort on
the anti-slop pass in §2 rather than treating it as bikeshedding.

**Practical synthesis rule**: when a design task doesn't specify a full brief, default to
— 4/8px spacing grid, 1.25 or 1.333 type ratio, 150–300ms ease-out for interactive
elements/300–400ms for panels, hierarchy-first critique pass, one signature motif instead
of many small flourishes (§2). This combination is what nearly every credible design
system in this collection converges on independently.

### Going further ("design things that are crazy")

The consensus principles above are the *floor* — the guardrails that keep experimental
work from reading as broken rather than bold. Once they're satisfied, push hard on ONE
axis at a time rather than breaking every rule at once (which reads as chaotic, not
crafted):
- Break the grid deliberately in one focal area while keeping the base rhythm everywhere
  else (asymmetric hero, everything else on-grid).
- Push type scale contrast far beyond 1.333 for a single dominant headline size, paired
  with disciplined small body text — extreme contrast, not uniform escalation.
- Use motion as the primary storytelling device (scroll-scrubbed sequences, §3) instead
  of static layout doing all the work.
- Choose an unexpected but *coherent* material system (grain, glass, brutalist raw HTML
  aesthetic, generative gradient mesh) and commit to it everywhere rather than sampling
  multiple trends.
- When genuinely unsure whether a bold move reads as "crazy-good" or "crazy-bad," render
  it and hold it against §2's anti-slop checklist — the checklist is what tells the two
  apart.

## 5. Non-web design

Same judgment applies beyond websites — decks, brand identity, product UI, print,
motion graphics, 3D/game art. For each: identify the medium's own anti-slop tells (e.g.
decks: no default PowerPoint gradients or clip-art icons; brand: no generic "abstract
swoosh" logos; illustration: no midjourney-default glossy 3D blob style unless it's a
deliberate choice) and apply the same "one strong idea, executed with restraint and
precision" standard from §2. `references/categories/` covers logos, branding,
posters/editorial, packaging, and presentation design as non-web categories with their
own verified demos — check the matching file first.

## 5.5 Convergence loop — iterate with an independent grader until stable

"Perfect, zero iterations" isn't a real target — self-critique that finds defects is
this skill's actual quality mechanism, not a failure of it (see the benchmark evidence
in `benchmarks/BENCHMARK_REPORT_LIVE_V3.md` and `outputs_model_comparison/`: every model
tested, including the strongest, only reached a solid result *by* running its own
adversarial critique pass and fixing what it found). What's achievable, and what to
actually run when the user wants the strongest possible result rather than a single
pass, is **convergence**: keep revising until an independent check stops finding new,
material problems — not until some model insists there are none.

1. Build one candidate through the normal plan gate → build → self-critique flow.
2. Have a **separate** grading pass — a fresh subagent/model instance that did not build
   the artifact and has not read its self-critique log — inspect it against §2's
   anti-slop checklist plus the matching category file's rules, and list concrete, named
   defects (not a numeric score; see `BENCHMARK_REPORT_LIVE_V3.md`'s finding that
   self-scored numbers vary 3.1–4.7 for the same skill and are not a trustworthy signal
   on their own). For interactive/coded artifacts (not static visuals), instruct the
   grader to audit against exactly these 8 categories — this rubric was derived from
   running this loop for real across two dozen benchmark artifacts and catching defects
   that a purely visual/aesthetic pass misses:
   1. WCAG 1.4.3 text contrast (4.5:1 normal text, 3:1 large text ≥18pt or ≥14pt-bold) —
      check every text/background pairing, including tinted/colored surfaces, not just
      the default background.
   2. WCAG 1.4.11 non-text/UI component contrast (3:1) — borders, icons, focus
      indicators, form-control boundaries, switch/toggle states.
   3. WCAG 2.2.2 Pause/Stop/Hide — any auto-playing animation looping more than a few
      seconds needs a pause/stop/hide affordance, or a named reason it's an essential
      live-state indicator rather than decoration.
   4. Broken real interaction / keyboard-access / state-integrity bugs — trace the actual
      logic: CSS cascade/specificity collisions, JS timing bugs, incomplete refactors,
      unhandled promise rejections, validation bypasses, focus-management bugs, a
      synthetic event triggering a side effect meant only for real user interaction,
      state not round-tripping correctly through save/restore.
   5. Dishonesty / fake-state — a control that implies behavior it doesn't actually
      perform, or a live/animated visual convention reused somewhere static that doesn't
      reflect real state.
   6. Dead/unused CSS custom properties declared but never referenced.
   7. Hardcoded literal values duplicating an already-declared design token.
   8. The file breaking its own declared internal rules — a code comment whose claim
      doesn't match the code, or two places stating the same fact (price, percentage,
      count) that disagree with each other.
   Before fixing category 4/5/8 findings, read
   `references/interaction-bug-patterns.md` — it documents specific recurring bug
   patterns (synthetic-event side effects, roving-tabindex selector pitfalls, auxiliary
   module-scope state dropped from save/restore, unhandled clipboard promise rejections,
   parameter-vs-closure-state bugs, the darker-text-token pattern for tinted surfaces and
   its light/dark-surface caveat) caught by actually running this loop across real
   artifacts, so known failure modes get checked deliberately instead of rediscovered by
   luck each round. Also read `references/ai-generated-component-tells.md` before
   building or grading any composite component (terminal/code windows, chat demos,
   bento grids, testimonial cards, skeleton loaders, stat counters, device mockups) — it
   catalogs *structural* tells (fake shell prompts, mismatched skeleton geometry,
   suspiciously-round stat rows) that survive an otherwise-clean token/contrast pass
   because the component fakes a real counterpart's shell without its real
   content/behavior. Also apply this rule while grading: a component/color reused on more
   than one background must be checked against *every* background it actually appears on,
   not just the one it was originally tuned against — a color passing on white and
   failing on a tinted container 40 lines away is a real, recurring defect class, not an
   edge case.
3. Fix the defects the grader actually named. Re-grade with another fresh pass. A category
   a previous round called clean is not guaranteed to stay clean — a fix in one round can
   introduce a new defect in a category that was fine before, so re-run the full
   8-category rubric every round, not just the categories that previously had findings.
4. **Stop condition**: when two consecutive independent grading passes turn up no new
   material defect (cosmetic nitpicks / subjective taste calls don't count — a defect is
   material if it violates a named rule in §2 or the category file, or breaks a stated
   function like contrast, keyboard access, or a real interaction state), the loop has
   converged — further changes have negative or zero expected value and should stop.
   Report the actual number of rounds and what each round fixed; do not claim the result
   is flawless, only that it has converged under the grading criteria used.
5. If a defect can't be fixed within the task's real scope (e.g. "the whole page below
   the hero doesn't exist yet" on a hero-only task), name it as an explicit, disclosed
   limitation rather than looping on it — convergence means "no more free improvements,"
   not "no known gaps."

This is genuinely more expensive (multiple grading passes per artifact) — only run it
when the user actually wants the ceiling, not the default single-pass workflow above.

## 6. Compliance — actually follow every rule above, every time

This skill only works if its rules are enforced, not skimmed. Reading this file once at
the top of a task and then working from memory is exactly the failure mode this section
exists to close — a rule you don't re-check against the actual output might as well not
exist. On every invocation, before calling the task done, walk every numbered section
above (§0 through §5.5) against what was actually built, not against your intention to
have followed it:

- **§0** — did you actually check for and prefer an installed specialist skill for this
  category, or default straight to this file out of habit?
- **§0.5** — did the plan gate actually run (wow-check + slop-check on the *plan*, not
  just the output), or did you skip straight to code because the task felt small?
- **§1** (if a screenshot/URL/video was the input) — did you extract the full token sheet
  before building, or approximate from vibe?
- **§2** and **§2.5** — re-read the anti-slop checklist and the purposefulness rule
  against the actual result, line by line, not your memory of intending to avoid slop.
- **§3** — if there's motion, does it match a named rationale in §3, not decoration added
  by default?
- **§4** — did you read the matching category reference file and, where relevant, a real
  brand's `DESIGN.md`, rather than reconstructing conventions from general knowledge?
- **§5** (non-web) / **§5.5** (coded/interactive) — whichever applies, was its specific
  process actually run, not just referenced?
This walk is itself a real check, not a formality — if any answer is "no" or "sort of,"
that section wasn't followed and the task isn't done yet.

- Before building: confirm §0.5's plan gate actually ran (wow-check + slop-check on the
  *plan*, not just the output) — do not skip straight to code because the task feels small.
- Before finishing: re-read §2's anti-slop checklist against the actual result, not your
  memory of intending to avoid slop. Screenshot/read back what you built and check it
  line-by-line against the checklist, same as §1 step 5 requires.
- If `impeccable` is loaded for the build, its craft-floor bans and bounded-verification
  protocol (build once, inspect once, fix once, stop) are binding, not optional — do not
  loop indefinitely, but do not skip the one inspection pass either.
- If a rule in this file conflicts with doing less work, the rule wins. "Good enough"
  that quietly drops a checklist item is a failure mode of this skill, not a shortcut.
- When genuinely unsure whether a rule applies (e.g. non-web medium, ambiguous scope),
  say so explicitly rather than silently skipping it.
- For any coded/interactive artifact, §5.5's convergence loop with its 8-category rubric
  is this skill's actual quality bar, not an optional extra tier — run it (at minimum
  one independent grading pass) whenever the user wants a result that's actually done,
  not just a first draft. Treat "the user didn't explicitly say run the convergence
  loop" as insufficient reason to skip it if the task's stakes call for it; when in
  doubt, ask rather than silently defaulting to a single unchecked pass.
