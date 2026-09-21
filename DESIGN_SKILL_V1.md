# Design Mastery — V1

A finite, verifiable milestone for the `design-mastery` skill. This document describes
what V1 actually is: its architecture, sources, principles, and — explicitly — what it
cannot do. It supersedes earlier open-ended "greatest designer" framing from this skill's
development history; V1 makes no claim to infinite research, equivalent-designer-hours,
or universal design capability.

## Architecture

Two layers:

1. **`SKILL.md`** — the orchestrator. Routes to installed specialist skills when present
   (taste-skill, image-to-code-skill, redesign-skill, designer-skills plugin, apple-hig,
   dataviz, etc.), holds the plan-gate discipline (§0.5), the anti-slop checklist (§2),
   motion/imagery direction (§3), and a compliance section (§6) requiring the checklist
   actually be re-applied before finishing, not just at plan time.
2. **`references/`** — the research and evidence layer:
   - `references/categories/*.md` — one file per required category (below), each concise
     and actionable: principles, anti-patterns, composition rules, typography/spacing/
     hierarchy/interaction guidance, ending in a `Verified build:` pointer to a real,
     screenshot-checked demo. This is the structured reference library the goal requires
     — not an inspiration dump.
   - `references/design-md/` — 74 real brand teardowns (exact hex, type scale, spacing)
     sourced from the open-source `VoltAgent/awesome-design-md` repo.
   - `references/design-systems-index.txt` — index of 166 production design systems
     (`alexpate/awesome-design-systems`).
   - `references/plugin87-data/` — 138-system token/style library from the installed
     `plugin87-*` design-architect pack.
   - `references/reference-library-notes.md` — running research log: live-site
     inspections (OpenAI, Wispr Flow, StudyFetch, Linear.app), derived patterns (e.g. the
     "serif + italic accent word" hero formula, the "interface-as-hero" pattern), and
     plan-gate decisions made during demo construction.

## Categories covered (required minimum, all present)

| Category | Reference file | Verified build |
|---|---|---|
| Web/landing pages | `categories/web-landing.md` | `screenshot-to-build-demo/recreation.html` |
| Product UI | `categories/product-ui.md` | `plan-gate-live-test/pricing-card.html` |
| Mobile UI | `categories/mobile-ui.md` | `mobile-ui-demo/screen.html` |
| Dashboards | `categories/dashboards.md` | `dashboard-demo/dashboard.html` |
| Branding | `categories/branding.md` | `brand-guidelines-demo/sheet.html` |
| Logos | `categories/logos.md` | `logo-demo/mark.svg` |
| Posters/editorial | `categories/posters-editorial.md` | `non-web-demo/patient-ink-poster.png` |
| Packaging | `categories/packaging.md` | `packaging-demo/label.svg` |
| Presentation design | `categories/presentation.md` | `presentation-demo/slide.html` |
| Marketing creative | `categories/marketing-creative.md` | `marketing-creative-demo/ad.html` |

## Sources

- Live-site pixel inspection (OpenAI, Wispr Flow, StudyFetch, Linear.app, and earlier
  Stripe/Claude.ai/Vercel research) — read directly from screenshots/DOM, not from
  training-data recall alone, and logged with what was actually observed.
- `VoltAgent/awesome-design-md` (74 brand teardowns) and `alexpate/awesome-design-systems`
  (166 systems) — open-source, credited, not claimed as original research.
- The installed `plugin87-*` design-architect pack and `apple-hig` skill, used as
  reference layers rather than re-derived from scratch.
- Cross-analysis of ~137 installed `designer-skills`-plugin packs for genuinely
  convergent numeric rules (motion timing bands, 4/8px spacing grid, 1.25/1.333 type
  ratios) — reported only where multiple independent packs agreed, in §4.5 of SKILL.md.

## Principles (see SKILL.md for full text)

- Plan-gate before building (§0.5): reject the first generic idea, check it against the
  anti-slop checklist, revise before writing code.
- Anti-slop checklist (§2): a concrete, checkable list of generic-AI-output tells to kill
  on sight (purple/blue gradient heroes, generic 3-icon grids, left-border accent strips,
  etc.), with the counter-instruction to pick one or two deliberate signature moves
  instead of many small decorative flourishes.
- Motion/imagery direction (§3) grounded partly in live devtools measurement (stripe.com
  transition timing), not just aesthetic opinion.
- Cross-medium pattern transfer: a pattern learned in one medium (e.g. a typography
  pairing from a web hero) is deliberately reapplied in an unrelated medium (a packaging
  label wordmark, a brand-guidelines type sample, a marketing ad) to demonstrate the
  skill generalizes principles rather than memorizing per-object templates. Demonstrated
  concretely via the shared "Fieldnote" brand system reused across the packaging,
  branding, and marketing-creative demos.

## Verification method

Every demo listed above was rendered as real HTML/SVG/PNG, served locally
(`python3 -m http.server`), and visually inspected via Chrome screenshot (or direct image
read, for the PNG poster) to confirm it renders without overlap, cropping, or broken
layout, before being marked verified. This is a rendering/composition check, not a
subjective taste judgment — it confirms the output *works*, not that it is optimal.

## Known limitations (explicit, per the V1 goal's requirement)

- **Not exhaustive.** Ten categories, one demo each, is a breadth sample, not full
  category coverage. Each category file is concise guidance distilled from a limited
  number of real references, not a comprehensive textbook.
- **No claim to designer-equivalence.** This skill does not claim the judgment of any
  number of human designers, any amount of design-hours, or infinite research. It is a
  structured checklist-and-reference system built from a bounded research pass.
- **No user testing.** "Works" here means renders correctly and follows the documented
  principles — it has not been validated with real users, A/B tests, or accessibility
  audits (contrast ratios, screen-reader behavior, keyboard navigation are not verified
  beyond what's visually obvious).
- **Static demos only.** None of the 10 verified builds include real interactivity,
  animation, or responsive behavior at multiple breakpoints — §3's motion guidance is
  documented but not demonstrated in a working animated build in this pass.
- **English/Latin-script bias.** All reference material and demos assume Latin
  typography; RTL languages, CJK type systems, and non-Latin script design conventions
  are not covered.
- **Reference libraries are third-party and may drift.** `design-md`, the design-systems
  index, and the plugin87 data are snapshots of external open-source projects at the time
  they were pulled in; they are not live-synced and may go stale.
- **No print-production rigor.** Packaging/poster demos are screen renders (SVG/PNG), not
  press-ready files (no bleed, CMYK conversion, dieline, or physical-material accounting).
- **Single reviewer.** All plan-gate and anti-slop judgments in this pass were made by
  one model instance in one session — there was no independent second opinion or
  human-designer review step.

## Files used

- `SKILL.md` — the single entry point another agent invokes. Self-contained: §0 specialist-
  skill routing, §0.5 plan gate, §1 screenshot-to-rebuild pipeline, §2 anti-slop checklist
  (core + anti-patterns), §3 motion/imagery direction, §4/§4.5 reference pattern library and
  synthesized first principles, §5 non-web design routing, §6 compliance re-check.
- `references/categories/*.md` (10 files, ~20–30 lines each) — context-specific rules per
  category, each ending in a `Verified build:` pointer.
- `references/benchmark-fixtures.json` — 10 machine-rerunnable render/verification fixtures
  tied to the 10 verified demos (for re-checking existing builds still render correctly).
- `BENCHMARK_TASKS.md` — 25 frozen test prompts for the next (separate) evaluation goal;
  not run or optimized against in V1.
- `references/reference-library-notes.md`, `references/design-md/` (74 teardowns),
  `references/design-systems-index.txt` (166 systems), `references/plugin87-data/` —
  reference notes (bucket 4). Raw research material, intentionally kept out of the main
  execution path; SKILL.md points into these files rather than inlining their content.
- The 10 demo directories (`screenshot-to-build-demo/`, `plan-gate-live-test/`,
  `mobile-ui-demo/`, `dashboard-demo/`, `brand-guidelines-demo/`, `logo-demo/`,
  `non-web-demo/`, `packaging-demo/`, `presentation-demo/`, `marketing-creative-demo/`) —
  the rendered, screenshot-verified proof artifacts referenced by both the category files
  and `benchmark-fixtures.json`.

## Content architecture (four-way separation)

1. **Core rules** — SKILL.md §0.5 (plan gate), §1 (pipeline), §3 (motion/imagery), §6
   (compliance) — apply to every task regardless of medium.
2. **Context-specific rules** — `references/categories/*.md`, one per required category,
   plus SKILL.md §5's non-web routing.
3. **Anti-patterns** — SKILL.md §2 (the anti-slop checklist) plus each category file's own
   anti-pattern list.
4. **Reference notes** — `references/reference-library-notes.md` and the raw third-party
   directories (`design-md/`, `design-systems-index.txt`, `plugin87-data/`) — consulted on
   demand, never required reading to use the skill correctly.

## What "done" means for V1

Every category above has a concise reference file and one rendered, screenshot-verified
demo; SKILL.md routes to those reference files and contains no forbidden claims; this
document exists; and a machine-rerunnable benchmark fixture list
(`references/benchmark-fixtures.json`) exists for the next evaluation goal to use. Beyond
that, this is explicitly a V1 baseline, not a claim of completeness for the domain of
design as a whole.
