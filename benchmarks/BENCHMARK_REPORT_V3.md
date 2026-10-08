# Design Mastery: v3 evaluator upgrade — V1 vs V2 re-scored

This goal upgrades the *benchmark evaluator*, not either skill. `SKILL.md`
(V1, frozen `52e9be3`) and `DESIGN_SKILL_V2.md` (V2, frozen `ec1447f`) were
not touched. `generate.py`'s `objective_checks` and `generate_v2.py`'s
`score_from_artifact`/`TIED_NEUTRAL` are imported unmodified and left in
place — this upgrade adds a new, additional layer (`evaluator_v3.py`),
it does not edit the frozen v1/v2 harness files.

## Why v2's harness needed this upgrade

`BENCHMARK_REPORT_DESIGN_SKILL_V2.md` found and disclosed a **measurement
ceiling**: v2's scorer has 8 real-signal rubric dims and 6 dims hardcoded to
`TIED_NEUTRAL = 3.0` for every artifact, because v2 had no static-analysis
signal for typography/spacing/composition/brand-fit/density/complexity.
Once two artifacts both clear the same 8 boolean flags, v2 scores them
*identically* — confirmed empirically: V1 vs DESIGN_SKILL_V2 tied 3.643 =
3.643 on all 25 main + 15 adversarial benchmarks, 0 improved / 0 regressed.
That is not evidence the two skills are equally good; it is evidence the
harness ran out of headroom to tell them apart.

## What v3 adds

`evaluator_v3.py` adds two new functions, kept deliberately separate:

- `discriminative_signals(html)` — **objective**, deterministic static
  measurements: distinct font sizes/families, heading-order validity,
  palette size, accent-color discipline, spacing-scale (4px-grid)
  consistency, responsive breakpoint count, landmark-tag variety,
  card-soup repetition ratio, decorative-complexity tells (gradients,
  pill-radius, glassmorphism), animation + `prefers-reduced-motion`
  respect, content-density ratio, alt-text substance.
- `subjective_score_v3(html, o, d)` — **subjective** banding of those
  measurements plus v2's existing 8 real-signal flags into 0–5 scores.
  Continuous formulas, not single pass/fail thresholds, so scores keep
  separating as quality keeps improving instead of saturating at the first
  threshold crossed. No identity/label argument, same discipline as v2.

This directly replaces the 6 previously-flat `TIED_NEUTRAL` dimensions
(`typography`, `spacing_rhythm`, `composition_layout`, `brand_context_fit`,
`information_density`, `unnecessary_complexity`) with discriminative,
content-derived scores, and sharpens 6 more (`responsiveness`,
`visual_hierarchy`, `consistency`, `originality_antislop`, plus refined
`usability`/`accessibility` banding retained from v2 where already
real-signal).

## Calibration (bad / average / good / excellent fixtures)

`calibration_fixtures.py` hand-authors 4 landing-page artifacts spanning a
deliberate quality gradient (not V1/V2 artifacts). `run_v3.py` refuses to
re-score V1/V2 unless calibration passes.

| Fixture | Overall score |
|---|---|
| bad | 2.368 |
| average | 3.971 |
| good | 4.164 |
| excellent | 4.349 |

Result: **strictly monotonic** overall ordering (bad < average < good <
excellent), **14/14 rubric dimensions monotonic** across the 4 fixtures,
and the repeatability check confirms 0 variance re-scoring the same
artifact (`calibration_v3.json`). Calibration passed — the run proceeded to
re-score V1/V2.

## Blind A/B re-score: V1 vs V2 under v3

Each benchmark id's V1-experiment and V2-skill artifact scores were placed
into randomized anonymous slots, compared, and only re-labeled after
scoring (`run_v3.py:blind_ab`) — the scorer itself never receives a label.

| | Main (25) | Adversarial (15) |
|---|---|---|
| V1 avg | 4.107 | 4.103 |
| V2 avg | 4.059 | 4.096 |
| Δ | −0.048 | −0.007 |
| Improved / Tied / Regressed (V2 vs V1) | 6 / 0 / 19 | 7 / 0 / 8 |

**The tie is gone.** Under v3's discriminative layer, V1 and V2 no longer
score identically on every benchmark — v3 has real headroom now. The
result is a **net regression for V2's hand-built benchmark artifacts on
main prompts** (19/25), smaller-magnitude but still net-negative on
adversarial (8/15 regressed vs 7/15 improved). This is reported as found:
no tuning of either skill occurred during this goal, and no benchmark
artifact was hand-edited after seeing its score.

### Root cause of the regression (disclosed, not hidden)

Per-dimension averages (main suite) show where the gap comes from:

| Dimension | V1 | V2 | Δ |
|---|---|---|---|
| information_density | 4.924 | 3.599 | **−1.325** |
| typography | 2.30 | 2.82 | +0.52 |
| visual_hierarchy | 3.56 | 3.81 | +0.25 |
| composition_layout | 3.60 | 3.79 | +0.19 |
| spacing_rhythm | 4.75 | 4.53 | −0.22 |
| consistency | 4.38 | 4.26 | −0.12 |
| brand_context_fit | 3.68 | 3.71 | +0.03 |
| usability / interaction_clarity / accessibility / responsiveness / clarity / unnecessary_complexity / originality_antislop | tied (same real-signal flags both hit) |

V2 *wins* typography, visual_hierarchy, and composition_layout — its
10 category-specific templates (§5 of `DESIGN_SKILL_V2.md`) produce more
distinct font sizes and more landmark-tag variety than V1's single reused
hero+3-card+footer skeleton, which is exactly the qualitative difference
`BENCHMARK_REPORT_DESIGN_SKILL_V2.md` flagged as invisible to v2's old
harness but real. v3 now measures it, and it shows up as a genuine
improvement on those 3 dimensions.

But V2 *loses heavily* on `information_density`: v3's density formula
penalizes both starved and overloaded words-per-container ratios, banded
around a ~28-word midpoint calibrated from the fixtures. Several of V2's
hand-built category templates (dashboards, logos, packaging,
posters-editorial) are intentionally terse for their medium (a logo page
has almost no body copy; a dashboard favors numbers over prose) and land
outside that band, while V1's uniform hero+card-grid structure happens to
sit closer to it on most of the 25 prompts. This is disclosed as a
**known evaluator limitation**, not corrected mid-run (correcting it now,
after seeing this specific result, would violate the "do not tune the
skills, do not optimize against individual benchmark failures" constraint
this goal and the previous one both impose) — see Remaining limitations.

## Evaluator variance

`subjective_score_v3` is a deterministic pure function of
`(html, objective_checks(html), discriminative_signals(html))`; repeated
scoring of the same artifact has 0 variance by construction, confirmed by
`calibration_v3.json`'s `repeatability_pass: true`. This measures the
evaluator's internal consistency, not run-to-run generation variance
(both V1's and V2's artifacts are static hand-built HTML, not live model
output, so there is no generation variance to measure in this harness).

## Remaining limitations

- **Density band is content-type-blind.** The ~28-word-per-container
  target was calibrated from one landing-page fixture family, not
  per-category. A logo page and a dashboard should not share a density
  target with a landing page; v3 does not yet condition the density
  formula on category. This is the single largest driver of V2's measured
  regression and is the most valuable next fix — but fixing it *after*
  seeing it produces the opposite result would be exactly the
  "optimizing against individually-observed benchmark failures" this goal
  prohibits, so it is left as a disclosed limitation, not patched.
- **Still fully static-analysis based, not live rendering or an LLM
  judge.** v3 adds real regex/count-based signal but still cannot see
  actual visual rendering (real contrast in context, real alignment,
  real whitespace balance) — it infers these from markup/CSS patterns.
- **Artifacts are hand-built per benchmark, not generated by an LLM
  reading the skill file.** Neither v1, v2, nor v3 changes this
  architecture (`generate.py`'s templates are structurally disconnected
  from skill prose, as documented in the prior two reports); v3 only
  changes how the resulting HTML is scored.
- **Calibration fixtures are landing-page-shaped**, not one per category;
  they establish that the evaluator *can* rank quality tiers at all, not
  that it is equally well-calibrated across all 10 categories.
- **Discriminative signal set is not exhaustive** — e.g. it has no signal
  for genuine visual-storytelling quality, real icon/imagery relevance, or
  brand-voice fit beyond palette/accent discipline.

## Preserved prior results

No prior results were modified or deleted. `results_v1.json`,
`results_v2.json`, `results_skillv2.json`, `aggregate_v1.json`,
`aggregate_v2.json`, `aggregate_skillv2.json`, `calibration_v2.json`,
`BENCHMARK_REPORT_V1.md`, `BENCHMARK_REPORT_V2.md`, and
`BENCHMARK_REPORT_DESIGN_SKILL_V2.md` are untouched. This report and its
data (`results_v3.json`, `aggregate_v3.json`, `calibration_v3.json`) are
new, additional files.

## Files

- `evaluator_v3.py` — discriminative signals + subjective scoring (new).
- `calibration_fixtures.py` — bad/average/good/excellent HTML fixtures (new).
- `run_v3.py` — calibration gate, blind A/B, re-score driver (new).
- `calibration_v3.json`, `results_v3.json`, `aggregate_v3.json` — outputs (new).
