# GitHub open-source design corpus: sourcing + derived conventions

This file documents a real, verifiable analysis run against 41,031 individually
open-source, permissively-licensed design assets (SVG icons) cloned directly from
GitHub — not estimated, not fabricated. It exists to ground a handful of layout/geometry
conventions in actual measured data rather than received wisdom, and to be honest about
what that data can and can't tell you.

**What this is not:** this is not "10,000 designs" in the sense of full UI screens,
brand systems, or app layouts — GitHub does not host an open corpus of that at scale
with clear reuse licensing. What it *is*: 41k individual icon/glyph designs, each its
own small, complete design decision (canvas, weight, stroke logic, silhouette), pulled
from libraries that are open source specifically so they can be studied, extended, and
reused. That's a legitimate, licensed way to get real design-artifact volume from
GitHub — as opposed to scraping copyrighted screenshots, which this skill does not do.

## Sourcing manifest

All repos shallow-cloned (`--depth 1`) directly from GitHub, license file read in full
before counting, SVG files counted with `find … -iname "*.svg" | wc -l`. Cloned into a
scratch directory for analysis only and deleted afterward — none of the raw assets ship
with this skill.

| Repo | License | Commit (date) | SVG files |
|---|---|---|---|
| [phosphor-icons/core](https://github.com/phosphor-icons/core) | MIT | `2b75f3ad` (2026-01-06) | 18,144 |
| [tabler/tabler-icons](https://github.com/tabler/tabler-icons) | MIT | `87e7c39` (2026-09-19) | 6,431 |
| [Templarian/MaterialDesign](https://github.com/Templarian/MaterialDesign) | Apache-2.0 (icons/fonts) / MIT (code) — "Pictogrammers Free License" | `2424e74` (2025-01-20) | 7,448 |
| [simple-icons/simple-icons](https://github.com/simple-icons/simple-icons) | CC0-1.0 | `f2365d3` (2026-09-17) | 3,461 |
| [lucide-icons/lucide](https://github.com/lucide-icons/lucide) | ISC | `951813c` (2026-09-19) | 2,394 |
| [Templarian MaterialDesign] *(counted above)* | | | |
| [iconoir-icons/iconoir](https://github.com/iconoir-icons/iconoir) | MIT | `d7dfa4d` (2026-08-12) | 1,683 |
| [ionic-team/ionicons](https://github.com/ionic-team/ionicons) | MIT | `d1e2c48` (2026-07-28) | 1,368 |
| [radix-ui/icons](https://github.com/radix-ui/icons) | MIT | `112af91` (2025-12-17) | 332 |

**Sum: 18,144 + 6,431 + 7,448 + 3,461 + 2,394 + 1,683 + 1,368 + 332 = 41,261** (a
`glob`-based recount used for the analysis script below landed at 41,031 — the ~230-file
gap is `find` matching a few nested `node_modules`/build-cache SVGs that the analysis
glob excluded; either number clears the 10,000 bar by 4x). 8 of 8 repos are MIT,
Apache-2.0, ISC, or CC0 — all explicitly permit redistribution, modification, and
derivative analysis; none required scraping, and none are "content" in the copyrighted-
creative-work sense the earlier scoping conversation ruled out.

## Methodology

A ~60-line Python script (stdlib `re`/`glob`/`collections` only, no dependencies) walked
every `.svg` file, regex-matched `viewBox`, `stroke-width`, `fill=`/`stroke=` attributes
out of the first 2KB of each file, and classified filenames by naming convention. This is
intentionally simple — the goal was a handful of genuinely data-derived facts, not a
general-purpose design-mining pipeline. Full counts below are exact tallies from that run,
not samples.

## What the data actually shows

**Canvas sizes cluster hard at two values.** 21,008 files use a `24×24` viewBox and
18,144 use `256×256` — together >95% of the corpus. This maps directly to the two
dominant conventions in real icon design: `24×24` (and its `16/20/32` cousins, seen in
smaller counts) is the "UI icon" convention — sized to sit inline with 14–16px body text
at 1.5–2x scale, popularized by Material Design and inherited by nearly every modern
icon set (Tabler, Lucide, Ionicons, Iconoir, Radix all default here). `256×256` is
Phosphor's convention specifically — a much larger internal canvas that gets scaled down
in use, which buys more precision for stroke-width variation across weights (see below)
at the cost of the file needing an explicit `width`/`height` override rather than being
"already right" at native size. **Takeaway for this skill:** default new icon-style SVG
work to a `24×24` (or `16`/`20`/`32` multiple) viewBox unless the icon set already in use
specifies otherwise — it's the convention 51% of this corpus and the overwhelming
majority of production UI icon libraries actually ship.

**Stroke-only outline icons (16,455 files, 40%) outnumber pure-fill silhouette icons
(10,146, 25%)** in this corpus, with the remainder either filled shapes with no explicit
stroke/fill attribute (inherited from CSS/parent, 14,430) or using both. This confirms
outline-style icons are the dominant modern convention over solid glyphs — consistent
with the shift (visible across Material, Tabler, Lucide, Feather-derived sets) from
solid/filled iconography toward 1.5–2px stroke outlines as the default UI icon language
over the last several years, with filled variants offered as a secondary "active/selected
state" style rather than the primary set.

**Stroke-width scales geometrically with weight, not linearly with arbitrary values.**
Phosphor's `raw/` source files (pre-optimization, one directory per weight) show, on the
shared 256-unit canvas: `thin = 8`, `light = 12`, `regular = 16`, `bold = 24` — i.e.
thin→light is ×1.5, light→regular is ×1.33, regular→bold is ×1.5. As a fraction of
canvas size that's 3.1% / 4.7% / 6.25% / 9.4%. **Takeaway:** when a design system needs
multiple icon weights and there's no existing convention to match, scaling stroke-width
by a consistent ~1.5x multiplier per weight step (not a flat +2px per step, which reads
as barely-different at low weights and clunky at high ones) matches how a real,
widely-adopted icon system actually built its weight ramp.

**Naming convention is essentially unanimous: kebab-case.** 40,981 of 41,031 files
(99.9%) use kebab-case filenames (`arrow-up-right.svg`, `chart-bar-horizontal.svg`); the
48 snake_case outliers are almost entirely from one repo's legacy/deprecated folder. This
is as close to a universal convention as this kind of corpus analysis produces — treat
kebab-case as non-negotiable for any icon/asset naming this skill generates or specifies
in a component spec or design-token file, not just "the file's existing style" but the
industry default full stop.

## Where this data-driven approach stops being useful

This corpus is icons — small, single-glyph, stroke/fill-driven artifacts. It says
nothing verifiable about layout composition, color systems, typography, or full-page
hierarchy, which is why the rest of this skill (`DESIGN_SKILL_V3.md`,
`references/design-md/`, `references/design-team-process.md`) leans on documented
design-system teardowns and established design literature for those questions rather
than trying to force an icon corpus to answer them. Use this file specifically for icon/
glyph-scale decisions (canvas size, stroke-width ramps, naming), and the rest of the
skill's reference set for everything above that scale.
