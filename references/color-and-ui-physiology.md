# Color and UI physiology — why the rules work, not just that they exist

The rest of this skill's reference library is aesthetic/compositional (what good design
looks like, brand by brand). This file is the layer underneath: the actual biology and
cognition of how eyes and brains process color, contrast, motion, and layout — so a
design choice can be justified as "this is measurably easier to read/see/scan" rather
than "this looks nice." Use it to settle arguments the aesthetic references can't (e.g.
"is this contrast ratio actually a problem" has a physiological answer, not a taste one).

## Color physiology

- **Rods vs. cones**: cones (color, high acuity, daylight) cluster in the fovea; rods
  (monochrome, motion/low-light sensitive, no color discrimination) dominate the
  periphery. Practical effect: a color-coded status dot or badge placed outside a user's
  foveal focus (far in peripheral vision — a corner toast, a sidebar badge) will be
  *seen* as a shape/motion but its color often won't register until the eye saccades to
  it. Don't rely on color alone for peripheral notifications — pair with motion or shape
  change, which peripheral rod vision actually resolves well.
- **Opponent-process theory**: human color perception isn't RGB-additive at the
  neural level — it's encoded as three opponent channels (red-green, blue-yellow,
  black-white/luminance). This is why red-green and blue-yellow pairs read as maximally
  "opposed"/vibrating when placed adjacent at equal saturation (simultaneous contrast —
  see below), and why there is no such thing as a "reddish-green" perceptually, but
  "yellowish-green" is easy to picture. Use opponent pairs deliberately for alert/success
  contrast (red/green is a real perceptual axis, not an arbitrary convention), but never
  as the *only* channel distinguishing two states — see color-blindness below.
- **Color-blindness prevalence and design implications**: red-green deficiency (the
  overwhelming majority of color-vision deficiency) affects roughly 1 in 12 men (~8%) and
  1 in 200 women (~0.5%) — meaning a meaningful fraction of male users literally cannot
  reliably distinguish a red "error" badge from a green "success" badge at matched
  lightness. This is why WCAG's "don't use color as the only means of conveying
  information" (1.4.1) is a physiological necessity, not a compliance checkbox: pair
  color with an icon, shape, or text label on every status/error/success signal, and when
  choosing an accent pair for a chart or diff view, prefer luminance-separated pairs
  (e.g. distinguishing by lightness, not just hue) or add a pattern/texture channel.
- **Chromatic adaptation**: the visual system continuously white-balances against the
  ambient light/dominant color in a scene (why a white page looks pure white next to a
  saturated background but looks slightly tinted in isolation). Practical effect: a
  brand's "white" surface color will read differently depending on what's next to it —
  test hero surfaces against the actual adjacent sections, not in isolation.
- **Simultaneous contrast**: the perceived color/lightness of a patch shifts based on
  what surrounds it — the same mid-gray looks lighter on a dark background and darker on
  a light one, and the same accent color looks more saturated against a desaturated
  background. This is the physiological reason a "flat gray card on gray background"
  (the tzura `AntiSlopManifesto` slop-example below names this directly) reads as inert:
  low local contrast plus this effect makes the boundary nearly disappear. It's also why
  a single accent color (the "one signature color" pattern already recommended in §4 of
  `SKILL.md`) reads as more vivid when it has real neighbor contrast to play against,
  rather than being surrounded by other saturated colors competing for the same effect.
- **Contrast sensitivity function (CSF)**: human contrast sensitivity isn't flat across
  spatial frequency — it peaks around 2-5 cycles/degree of visual angle and falls off at
  both very fine detail and very coarse shapes, and peaks at higher contrast for color
  differences than luminance differences at fine scale. Practical effect: for small text
  and thin UI strokes (icons, dividers, form borders), *luminance* contrast (light vs.
  dark) is what the eye is best equipped to resolve — color-only contrast at small sizes
  (e.g. a light-blue-on-white 1px border) is fighting the eye's actual sensitivity curve,
  not just an accessibility guideline. This is the physiological basis under WCAG's
  higher contrast-ratio requirements for smaller text (4.5:1 vs. 3:1 for large text).

## Dark-UI physiology

Dark mode isn't just "light mode with inverted colors" physiologically — the eye behaves
differently against a dark surface, and several common dark-theme mistakes are
predictable consequences of that, not random taste failures:

- **Halation/irradiation on light-text-on-dark**: bright text on a dark background
  visually "bleeds" into the surrounding dark area more than dark text bleeds into a
  light background — a real optical/neural effect (irradiation illusion), worsened for
  anyone with astigmatism or other minor refractive error (a large share of adults) where
  it becomes actual perceived blur/glow around letterforms, not just a subjective
  impression. Practical effect: pure white (`#fff`) text on pure black (`#000`) at
  regular/bold weight is measurably harder to read cleanly for a meaningful fraction of
  users than the reverse polarity is — this is why almost every serious dark theme (iOS,
  Material, GitHub) uses an off-white/warm-gray foreground (e.g. `#e8e8e8`-`#f0f0f0`
  range, not `#ffffff`) and a **lighter font weight than the equivalent light-theme
  text**, not the same weight — a Regular weight that looks correctly proportioned on
  white looks artificially bold/glowing on black at the same weight, so dark themes
  should either drop the weight one step or use a font with a dark-mode-tuned optical
  size.
- **True black vs. near-black backgrounds**: pure black (`#000`) maximizes contrast
  ratio on paper, but perceptually it also maximizes the halation effect above and gives
  the eye no "surface" to read elevation against (see next point) — most production dark
  themes use a near-black (`#111`-`#1a1a1a` range, e.g. Material's baseline `#121212`)
  specifically to leave room for lighter elevation surfaces above it while still reading
  as "dark," and to reduce the harshness of the light-on-dark contrast jump. Pure black
  is still the right choice for OLED-battery-sensitive contexts (a screen that's
  genuinely mostly-black draws meaningfully less power on OLED, since black pixels are
  off) — a legitimate physiological/hardware tradeoff distinct from the readability one,
  worth naming explicitly when true-black is chosen for that reason rather than by
  default.
- **Elevation reads through lightness, not shadow, in the dark**: on a light surface,
  elevation/depth is conveyed by cast shadow (a physically real cue — the eye infers
  height from shadow softness/offset). On a dark surface, a dark drop-shadow against an
  already-dark background produces almost no visible contrast, so shadow alone stops
  working as an elevation cue. This is why Material Design's dark theme spec adds a
  literal semi-transparent white overlay that gets *more opaque* at higher elevation
  levels (surfaces closer to the "light source" appear lighter, inverting the light-theme
  logic) — elevation in dark UI has to be communicated primarily through surface
  lightness steps, with shadow as a secondary/minor cue at most.
- **Pupil dilation and low-light viewing context**: dark UIs are disproportionately used
  in dim ambient environments (a dark room at night is exactly when someone reaches for
  dark mode), and a dilated pupil admits more light and has reduced depth of focus,
  slightly softening acuity at the same nominal screen contrast a well-lit room would
  render sharp. Practical effect: don't shrink type size or thin stroke weights in a dark
  theme relative to light theme "because it's the same design" — if anything, hold body
  text size steady or slightly larger, since the viewing conditions where dark mode gets
  used are themselves acuity-reducing.
- **Saturated color on dark backgrounds reads more intensely**: because of simultaneous
  contrast (see above) and the eye's reduced overall adaptation luminance in a dark UI, a
  saturated accent color (a bright red, a vivid blue) appears more vibrant and can
  produce more visual fatigue/glare against a near-black surface than the identical hex
  value would against white. This is why most dark-theme design systems (Material,
  Apple's dark appearance guidance) explicitly recommend *desaturating* and/or *lightening*
  brand accent colors for dark mode rather than reusing the light-mode accent value
  unchanged — a straight color-token swap without this adjustment is a common, physiologically
  explainable reason a "we just added dark mode" retrofit looks harsher than the original.
- **Blue light and circadian/melatonin sensitivity** (the actual biological reason dark
  mode exists as a category, beyond aesthetics): the eye's intrinsically photosensitive
  retinal ganglion cells (ipRGCs) are most sensitive to short-wavelength (blue-heavy)
  light and drive circadian phase-shifting and melatonin suppression when stimulated at
  night. A bright, blue-heavy white UI viewed at night measurably suppresses melatonin
  more than a dim, warm-toned dark UI does — this is the legitimate physiological basis
  for "night mode" existing at all (not purely a battery or preference feature), and it's
  also why the better implementations warm the whole palette (shift toward amber/warm
  grays) at night rather than just dropping surface luminance while keeping a cool-white
  color temperature.

## UI / visual physiology

- **Foveal vs. peripheral acuity**: the fovea (about 2° of visual angle, roughly the
  width of a thumbnail at arm's length) is where sharp detail and color are resolved;
  acuity drops off sharply outside it. A user's eye can only truly *read* one small
  region at a time — everything else is being processed at much lower resolution as a
  shape/contrast/motion field. This is why hierarchy through size/weight/contrast
  matters more than most designers give it credit for: a page is not "seen" all at once
  at full fidelity, it's scanned via a sequence of foveal fixations, and layout has to
  guide where those fixations land.
- **Saccades and fixation patterns (F-pattern / Z-pattern)**: eye-tracking studies
  (originally Nielsen Norman Group's heatmap work) show text-heavy pages get scanned in
  an F-shaped pattern — a full read across the top, a shorter pass partway down, then a
  vertical scan down the left edge — while simpler, more visual layouts (landing pages,
  ads) tend toward a Z-pattern (top-left → top-right → diagonal → bottom-right, tracing
  where a CTA typically sits). Practical effect: put the most important word/number at
  the start of a heading or bullet (front-load meaning within the first ~2 words, since
  the F-pattern's horizontal passes get shorter as they go down the page), and place a
  primary CTA where the Z-pattern's terminal diagonal naturally lands (bottom-right of a
  hero, or directly below the eye's last scan point).
- **Fitts's Law**: the time to acquire a target with a pointer is a function of the
  distance to it and inversely of its size (`T = a + b·log2(D/W + 1)`). Practical effect:
  primary actions should be both close to where attention already is *and* large enough
  to hit fast — this is the physiological reason mobile bottom-sheet primary buttons run
  full-width and ~44-48px tall (Apple HIG's minimum touch target isn't arbitrary, it's
  sized to finger contact-patch precision), and why screen edges/corners are effectively
  "infinite width" targets (the cursor can't overshoot past a screen edge) — a reason
  OS-level menus and Fitts-optimized UI historically pin controls to screen edges.
- **Hick's Law**: decision time increases logarithmically with the number of choices
  (`T = b·log2(n+1)`), not linearly. Practical effect: an 8-item nav with no grouping is
  disproportionately slower to scan than two 4-item grouped clusters — this is the
  physiological backing for progressive disclosure (settings sections, "More" overflow
  menus, tabbed groupings) as a real speed win, not just visual tidiness.
- **Working-memory limits (~7±2, more realistically ~4 for unaided chunking)**: George
  Miller's original "seven plus or minus two" has been refined since — modern working-
  memory research (e.g. Cowan) puts unaided chunk capacity closer to 3-4 items without
  external support. Practical effect: don't design multi-step flows or nav structures
  that require holding more than about 4 unlabeled things in mind at once (form fields
  visible without a label reminder, breadcrumb depth, simultaneous open modals/panels);
  chunk into labeled groups instead of a flat long list.
- **Flicker-fusion and peripheral motion sensitivity**: above roughly 50-60Hz, discrete
  flicker fuses into perceived-continuous motion for foveal vision — but the peripheral
  visual field is *more* sensitive to motion and flicker than the fovea is (a survival
  trait for detecting movement at the edge of the visual field). Practical effect: subtle
  animated elements placed in peripheral UI regions (a pulsing badge in a sidebar while
  the user reads center content) will be noticed and can be distracting/anxiety-inducing
  even when the user never looks directly at it — reserve continuous/looping motion for
  content the user is actively focused on, and make ambient peripheral motion (loading
  indicators, live-updating counters off to the side) slow and low-amplitude specifically
  because peripheral vision will catch it regardless of gaze.
- **Legibility research — x-height, line length, line-height**: type with a taller
  x-height (the height of lowercase letters like "x", relative to cap height) reads as
  more legible at small sizes because more of each letterform's distinguishing shape
  sits in the zone the eye actually resolves fastest — this is part of why UI-focused
  typefaces (Inter, Söhne, SF Pro) have larger x-heights than classic print serifs
  optimized for large-size elegance. Optimal measure (line length) for sustained reading
  is commonly cited around 50-75 characters per line — much narrower than an
  unconstrained full-viewport paragraph, which is why editorial/long-form layouts
  constrain body text to a max-width column rather than letting it stretch edge to edge.
  Line-height around 1.4-1.6× the font size is the common comfortable range for body
  text (tighter for display/headline sizes, where fewer lines need holding in memory
  between saccades).

## Real local grounding: Jacob's own component work

Two real, in-use local projects ground these principles in actual shipped code on this
machine — cited here (not as a wishlist) because both are genuine artifacts, not
examples invented for this file:

- **`~/agent-workspace/jacobs-components`** — a real 62-component library pulled
  verbatim from 21st.dev (`21st get <id>`, source + demo + raw search result kept per
  pick) and used as the actual UI source-of-truth for JumpStudy AI (an ed-tech app).
  Its own README states the rule directly: "every visible piece of the app must be built
  from one of these... no generic/placeholder Tailwind markup." Relevant to this file
  specifically: many of its picks are physiology-driven choices already — a dedicated
  `Skeleton` component (loading-skeleton) exists because a blank/white loading state
  reads as broken (nothing for the eye's motion-detection to register as "in progress"),
  a `Streak Calendar`/heatmap exists for the pattern-completion effect (spatial memory
  over a grid reads faster than a numeric streak count), and `Toast Notification` /
  `Notification Center` are separate components because transient vs. persistent
  attention-getting needs different peripheral-motion behavior (a toast should catch
  peripheral motion sensitivity briefly then get out of the way; a notification center
  badge is a static peripheral cue meant to persist). See its `README.md` and
  `MANIFEST.json` for the full 62-component index with sources when a specific pattern
  (dropdown, drawer, command palette, etc.) is needed for a project on this machine.
- **`~/agent-workspace/tzura/src/components`** — Jacob's own anti-slop design-generation
  tool, which independently converged on several of the same physiological rules this
  skill already enforces, worth citing because it's corroborating evidence from a
  separate real project, not received wisdom copied twice:
  - `AntiSlopManifesto.tsx` names the exact same failure modes as this skill's §2
    checklist (arbitrary non-grid spacing like `p-[17px]`, flat textureless gray cards
    with "zero optical depth," untracked default-kerning headings) and frames the fix in
    the same physiological terms used above — e.g. its "flat opaque gray card" slop
    example is a direct instance of the simultaneous-contrast failure (low local contrast
    against a similarly gray background reads as inert, not calm).
  - `DesignTokenMatrix.tsx` enforces a strict 8pt spatial grid (4/8/16/24/32/48/64px) as
    a live, adjustable master token rather than ad hoc values — the same working-memory
    argument above (fewer, chunked, predictable values are faster to scan and reason
    about) applied to a spacing system instead of a nav.
  - `ComponentFoundry.tsx` and `CustomIcons.tsx` exist as dedicated, hand-maintained
    surfaces specifically to avoid mismatched-stroke-weight icon sets and inconsistent
    component styling — the same "icon libraries used unstyled and mismatched in stroke
    weight" anti-pattern already called out in this skill's §2 checklist, independently
    arrived at in a separate real codebase.

When a task on this machine touches JumpStudy AI, lumen-shell, jumpnote, pmux, or tzura
specifically, check that project's own component directory first (`src/components` in
each) before introducing new UI patterns — consistent with how `local-ui-libraries.md`
already recommends checking a project's real `package.json`/`node_modules` rather than
assuming a stack.
