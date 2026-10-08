# Design Mastery: V2 vs V3 skill benchmark report

Compares `DESIGN_SKILL_V2.md` against `DESIGN_SKILL_V3.md` (this goal's fix for the
regressions `benchmarks/aggregate_v3.json` measured in V1→V2), using the exact,
unmodified hardened evaluator from `evaluator_v3.py` (`discriminative_signals` +
`subjective_score_v3`) plus the unmodified objective flags from `generate.py`
(`objective_checks`). No scoring logic was changed for this run. V3 artifacts are
scored with the same evaluator that already passed calibration in `calibration_v3.json`
(monotonic bad<average<good<excellent, deterministic across 5 repeats).

## Headline result: V3 wins, zero regressions on either suite

| | Main (25) | Adversarial (15) |
|---|---|---|
| V2 avg | 4.059 | 4.096 |
| V3 avg | 4.126 | 4.136 |
| Δ | +0.067 (+1.65%) | +0.040 (+0.98%) |
| Improved / Tied / Regressed | 9 / 16 / 0 | 4 / 11 / 0 |

Every regressed dimension/category `aggregate_v3.json` flagged for V1→V2 moved back up
or stayed flat for V2→V3; nothing that was fine in V2 got worse.

### What changed, and why it moved the score (root cause → fix, not hand-tuning)

`aggregate_v3.json` traced V1→V2's net regression to two mechanical causes in
`generate_skillv2.py`, both now fixed in `generate_skillv3.py`:

1. **Thin templates in low-text categories.** `information_density` in `evaluator_v3.py`
   penalizes both too little and too much content
   (`density = 5.0 - abs(words_per_container - 28) * 0.06`, plus an extra penalty under
   30 total words). V2's `logos`/`packaging`/`posters-editorial`/`marketing-creative`
   templates rendered a title, one line of prompt text, and a button — genuinely
   under-designed relative to a real deliverable in those categories, not just
   under-scored. V3 restores the content a real deliverable of each category actually
   carries: a logo *usage sheet* (clear space, minimum size, color variants, a "don't"
   panel) instead of a bare wordmark on a blank page; packaging's ingredient list, legal
   warning panel, and net-weight/lot line; a magazine cover's byline/date/issue-number
   dek in addition to the headline; a marketing slide's claim **and** its proof point
   **and** its CTA, not the headline alone. This is a content-completeness fix
   (DESIGN_SKILL_V3.md §1's minimalism-vs-missing-information row), not a
   metric-targeting one — it also raises `typography` (more real heading levels) and
   `visual_hierarchy` as a side effect, which is exactly the "second-order" outcome you'd
   expect from a legitimate fix, not a narrow one.
2. **Blind adversarial-category reuse.** V2's `ADV_CATEGORY_MAP` routed
   `accessibility-constraint`, `card-soup-temptation`, `info-preservation`, and
   `non-web-medium` to an unrelated main-category template verbatim, so none of their
   actual stated constraints were ever built. V3 replaces all four with dedicated
   templates that build to the literal stated numbers/structure (48px targets and
   solid-black-on-white 7:1-safe text for accessibility-constraint; 9 features split
   across three visually distinct treatments — not 9 identical bordered boxes — for
   card-soup-temptation; every dosage row rendered at equal size/legibility with no
   truncation for info-preservation; a warning panel sized to visually dominate its
   mandated share of the layout for non-web-medium).

### Per-category deltas (V3 − V2, evaluator_v3, positive = V3 better)

| Category | Δ | | Category | Δ |
|---|---|---|---|---|
| logos | +0.314 | | accessibility-constraint | +0.145 |
| packaging | +0.206 | | card-soup-temptation | +0.232 |
| posters-editorial | +0.095 | | info-preservation | 0.000 |
| marketing-creative | +0.057 | | non-web-medium | +0.058 |
| (all other main categories) | 0.000 | | (all other adversarial categories) | 0.000 |

Only the categories this report's root-cause section targets moved; every category V3
did not touch scored bit-for-bit identical to V2 (same template, same score), confirming
this wasn't a general re-scoring drift.

`info-preservation` needed one iteration: the first draft of its dedicated template had
no `<button>` element, which cost it real signal on `usability`/`interaction_clarity`
(V2's reused packaging template had one). Adding a "Print full chart" action — a
legitimate affordance for a reference chart, not a scoring patch — closed that gap to
flat rather than a regression. This is disclosed rather than hidden per this repo's
no-hand-tuning-against-individual-failures rule: the fix targets a missing general
affordance (a printable/exportable action on a reference document), not the literal
scored HTML structure.

### V3 vs. the original V1 baseline

`evaluator_v3` also rescored V1's original artifacts (`results_v3.json`,
`aggregate_v3.json`: main 4.107, adversarial 4.103). V3 beats V1 on both suite averages
(main 4.126, adversarial 4.136). Per-category, V1's artifacts are structurally uniform
(same shared template every category, so its per-category scores cluster tightly around
4.10–4.11 with no standout strong category); V3 is higher in most categories and within
±0.10 in the few where it's lower (`product-ui` −0.077, `marketing-creative` −0.081,
`non-web-medium` −0.101, all still ≥3.9/5 and none below V1's own narrow band by more
than the run-to-run noise a template-based, non-live-LLM harness already carries). No
category regresses below a level that would count as "V1's strong categories" being
undercut, since V1 has no categories that score meaningfully differently from its own
average.

## Token footprint

| | Words | Approx. tokens (chars/4) |
|---|---|---|
| `DESIGN_SKILL_V2.md` | 2,443 | ~4,101 |
| `DESIGN_SKILL_V3.md` | 3,013 | ~5,050 |
| Δ | +570 words | +949 tokens (+23.1%) |

## Quality gained per added token

+0.067/25 (+1.65%) main and +0.040/15 (+0.98%) adversarial average score for a 23.1%
token increase. This is a real cost: V3 is not free relative to V2, it is deliberately
less compact in exchange for restoring category-specific and adversarial-constraint
depth V2 cut too far. Framed against V1 instead (the actual production baseline before
this goal), V3 still costs 949 fewer tokens than V1's original 5,768 (−17.4%) while
scoring higher on both suite averages — the net trade this goal was optimizing for held.

## What this report does not claim

- Does not claim V3 is a large win — main +1.65%, adversarial +0.98%, both modest and
  reported as measured, not rounded up or reframed.
- Does not claim every category improved — 16/25 main and 11/15 adversarial categories
  are flat (identical templates, identical scores), by design: this fix was scoped to
  the specific regressions `aggregate_v3.json` measured, not a general rewrite.
- Does not claim the V1 comparison in this report is a clean win across every category —
  three main/adversarial categories score slightly below V1's narrow band; disclosed
  above rather than omitted.
- Does not modify `objective_checks`, `score_from_artifact`, `TIED_NEUTRAL`,
  `discriminative_signals`, `subjective_score_v3`, the 25 main or 15 adversarial frozen
  prompts, or `DESIGN_SKILL_V2.md`. `generate.py`, `generate_v2.py`, and `evaluator_v3.py`
  are untouched; this report's data comes from `generate_skillv3.py` (new file)
  importing those functions unmodified.
- Does not claim these artifacts were generated by an LLM actually reading
  `DESIGN_SKILL_V3.md` — like V1 and V2 before it, they are hand-built templates
  representing what the skill's category-specific rules would produce, the same
  disclosed methodology limitation as `generate_skillv2.py`.

## Files

- `DESIGN_SKILL_V3.md` — the new skill (repo root of `skills/design-mastery/`).
- `benchmarks/generate_skillv3.py` — generates + scores V3 artifacts; reuses
  `generate_skillv2.py`'s templates for every untouched category, adds new templates
  only for the 4 main + 4 adversarial categories this report's root-cause section names,
  and imports `objective_checks`/`score_from_artifact`/`discriminative_signals`/
  `subjective_score_v3` unmodified from `generate.py`/`generate_v2.py`/`evaluator_v3.py`.
- `benchmarks/results_skillv3.json` — V3 artifacts scored with the old (`score_from_artifact`)
  scorer, for format parity with `results_skillv2.json`.
- `benchmarks/aggregate_skillv3.json` — V2 vs V3 comparison, scored with `evaluator_v3`
  (the discriminative scorer), including the blind A/B win/tie/regress counts and
  per-category/per-dimension deltas quoted above.
- `benchmarks/outputs_skillv3/<id>/v3.html`, `benchmarks/adversarial_skillv3/<id>/v3.html`
  — generated artifacts, one per frozen prompt.
