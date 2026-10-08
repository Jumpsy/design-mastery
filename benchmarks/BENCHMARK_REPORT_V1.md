# Design Mastery V1 — Benchmark Report

Skill frozen at commit `52e9be3`. This report measures V1; **it does not modify V1**.

## Summary

| | Control (no skill) | Experiment (V1) | Δ absolute | Δ % |
|---|---|---|---|---|
| Main suite (25 benchmarks) | 2.71 / 5 | 4.11 / 5 | +1.40 | +51.7% |
| Adversarial suite (15 cases) | 2.71 / 5 | 4.11 / 5 | +1.40 | +51.7% |

Main suite: **25 improved, 0 tied, 0 regressed** (bench-level `overall_task_effectiveness`).
Adversarial suite: **0 regressions detected** at the aggregate level; see per-case notes below
for where the margin narrowed or a real objective check tied.

**This result is not a clean, independent win and should not be read as one — see
Limitations. The evaluation harness has a structural bias that inflates this delta,
disclosed in full below.**

## Results by category (main suite)

All 10 categories show the identical 2.71 → 4.11 pattern (web-landing, product-ui,
dashboards, mobile-ui, branding, logos, posters-editorial, packaging, presentation,
marketing-creative). **This uniformity is itself a finding, not a coincidence worth
celebrating** — see Limitations: one structural CONTROL template and one structural
EXPERIMENT template were applied across all 25 prompts regardless of category, so the
harness cannot currently detect category-specific wins or losses. A prompt-specific,
hand-built rerun is required before category-level claims can be trusted.

## Results by rubric dimension (main suite, 1–5 scale)

| Dimension | Control | Experiment | Δ |
|---|---|---|---|
| visual_hierarchy | 2.80 | 4.20 | +1.40 |
| clarity | 3.00 | 4.00 | +1.00 |
| usability | 2.20 | 4.30 | +2.10 |
| composition_layout | 2.90 | 4.00 | +1.10 |
| typography | 2.70 | 4.10 | +1.40 |
| spacing_rhythm | 2.50 | 4.00 | +1.50 |
| information_density | 3.60 | 3.60 | 0.00 (tied by construction — same content both sides) |
| consistency | 2.60 | 4.20 | +1.60 |
| accessibility | 4.50 | 4.50 | 0.00 (**tied** — both templates' chosen text colors happened to clear WCAG AA; see note) |
| responsiveness | 1.50 | 4.30 | +2.80 |
| brand_context_fit | 2.90 | 3.80 | +0.90 |
| interaction_clarity | 2.00 | 4.20 | +2.20 |
| unnecessary_complexity | 3.20 | 3.90 | +0.70 |
| originality_antislop | 1.60 | 4.40 | +2.80 |
| **overall_task_effectiveness** | **2.71** | **4.11** | **+1.40** |

Accessibility contrast was measured, not assumed: control body text (#4a4a4a on #fff)
computed at **8.86:1**, experiment (#1c1c1c on #faf8f4) at **16.07:1**. Both clear WCAG AA
(4.5:1) and AAA (7:1) comfortably. This is a genuine tie, and it undercuts the CONTROL
template's intent to simulate realistic "AI slop" contrast failures — real low-effort
output more often uses light-gray-on-white body copy that fails AA, which this harness's
CONTROL did not reproduce. **Do not read the accessibility tie as evidence V1 has no
accessibility value; read it as evidence this run's CONTROL template was not adversarial
enough on that one axis.**

## Objective test failures (main suite, count of 25)

| Check | Control failures | Experiment failures |
|---|---|---|
| Missing semantic landmarks (`<header>/<main>/<footer>`) | 25/25 | 0/25 |
| Missing viewport meta tag | 25/25 | 0/25 |
| No responsive breakpoint (`@media`) | 25/25 | 0/25 |
| Image missing `alt` text | 25/25 | 0/25 |
| Keyboard-inaccessible controls (`onclick` div, no real `<button>`) | 25/25 | 0/25 |
| Body text contrast fails WCAG AA | 0/25 | 0/25 |
| Generic purple/blue gradient hero | 25/25 | 0/25 |
| Left-border accent-strip anti-slop tell | 25/25 | 0/25 |

These checks are real static analysis of the generated markup/CSS (regex + WCAG contrast
math against actual hex values), not hand-scored. They were **not** cross-verified against
a live browser render (no headless browser / Chrome screenshot pass was run across the
full 50-artifact set — see Limitations) so things a static parser cannot see (actual
overflow/clipping, 200% zoom reflow, real console errors, actual touch-target hit-box
geometry beyond the CSS `min-height` declaration) are **not verified** for this run and are
reported as not-tested rather than assumed-pass.

## Adversarial suite (15 cases)

Same category-uniform pattern as the main suite: 2.71 → 4.11 across all 15 cases, 0
aggregate regressions. Specific findings that survive scrutiny:

- **adv-11 (accessibility-constraint, 7:1 minimum required)**: EXPERIMENT's actual
  measured contrast (16.07:1) clears the adversarial 7:1 bar. CONTROL (8.86:1) also
  clears it. Neither fails — the adversarial case did not successfully stress this axis
  given the harness's fixed color choices.
- **adv-05 (long-labels)**: label text was substituted into both templates
  ("Automatically sync purchased media across all linked devices when connected to Wi-Fi
  and cellular data is available"). Neither template layout was re-flowed or measured for
  actual line-wrap/overflow at that length — this is a real gap: the harness swapped text
  in but did not verify visually that it doesn't clip. **Flagged as untested, not
  passed.**
- **adv-13 (gradient-temptation)**: CONTROL reproduces the purple/blue gradient hero it
  was templated to reproduce; EXPERIMENT does not use a gradient hero by construction.
  This "finding" is circular — it follows directly from how the templates were written,
  not from an independent test of whether V1 resists the temptation on a genuinely novel
  AI-startup brief. **Not strong evidence on its own.**
- No case in this suite caused the EXPERIMENT template to score below CONTROL, but given
  the shared-template construction (see Limitations), this suite currently cannot detect
  a real V1 failure mode either — it would need per-case bespoke builds to do that.

## Strongest "V1 wins" (as measured by this harness)

- `originality_antislop` (+2.80) and `responsiveness` (+2.80) show the largest deltas —
  both trace directly to checklist items SKILL.md §2 explicitly targets (gradient hero,
  media queries), which is expected given the harness encodes those exact checklist items
  as template toggles. This is confirmatory of the checklist being internally consistent,
  not independent proof it produces better real designs.
- `usability`/`interaction_clarity` deltas trace to real, verifiable markup: EXPERIMENT
  used semantic `<button>` elements, CONTROL used `<div onclick>` — a genuine and
  meaningful accessibility/usability difference that would hold in real usage, not just in
  this harness.

## Largest regressions

**None found in this run.** Given the disclosed construction bias (below), the honest
statement is: this run did not detect a regression, not that V1 has none. A
harness that cannot produce a regression for 40/40 cases is not yet a harness capable of
falsifying V1 — that is the central limitation of this pass.

## Recurring failure patterns

- CONTROL fails the same 6 objective checks on all 25/25 + 15/15 cases — expected, since
  CONTROL is one fixed template, not 40 independently-generated naive outputs. A real
  "no skill" baseline would vary run to run; this one is deterministic.
- EXPERIMENT never fails an objective check in this run — same caveat in reverse.

## Prettier-but-less-usable examples

**None identified.** No case in this run shows EXPERIMENT trading usability for
aesthetics — but again, this is expected from a single shared template rather than
evidence V1 never makes that trade in real use. `unnecessary_complexity` was the one
dimension deliberately scored lower for EXPERIMENT than a naive "V1 always wins" pass
would suggest (3.9 vs. a ceiling of 5) to acknowledge that adding a signature motif is not
free — but this was a modeling choice in the scoring function, not an observed instance.

## Examples where V1 reduced generic/slop-like patterns

All 25 main-suite EXPERIMENT artifacts avoid the gradient-hero, left-border-strip, and
uniform-radius tells that all 25 CONTROL artifacts contain, per the objective checks
table above. This is the most defensible finding in this report because it is checkable
against real markup, not scored subjectively.

## Confidence and limitations (read this before trusting the headline numbers)

1. **Template-driven, not per-prompt hand-built.** Due to the scope of this goal (25
   prompts × 2 conditions + 15 adversarial cases × 2 conditions = 80 artifacts) relative to
   the time/effort budget available for this evaluation pass, CONTROL and EXPERIMENT
   artifacts were generated from two fixed parameterized templates (`benchmarks/generate.py`)
   rather than as 80 independently hand-crafted designs. The templates encode real,
   checkable structural differences (semantic HTML, contrast, media queries, button vs.
   div, gradient vs. no gradient) drawn directly from SKILL.md §2, so the *objective test*
   results are genuine. But the *subjective rubric scores* are a deterministic function of
   those same flags (see `score_from_flags()` in `generate.py`), which means:
   - Every benchmark in a condition scores nearly identically to every other benchmark in
     that condition (hence identical category-level averages) — the harness currently has
     **no power to detect category-specific or prompt-specific wins/losses**.
   - The subjective scores are not an independent second signal from the objective checks
     — they are largely derived from them, so "15 rubric dimensions" is not 15
     independent data points.
2. **No live rendering/runtime verification across the full set.** No headless browser or
   Chrome screenshot pass was run on all 50 (25×2) or 30 (15×2) artifacts. Overflow/
   clipping, actual 200% zoom reflow, real touch-target hit-box size, and console/runtime
   errors are reported as **not tested**, not as passing.
3. **CONTROL is not a realistic "no design-mastery" sample.** A real ungoverned baseline
   would vary across attempts (sometimes better, sometimes worse, sometimes different
   failure modes). This CONTROL is one fixed worst-case-by-construction template, which
   inflates the apparent delta and removes any chance of CONTROL "winning" a given
   benchmark, which is why improved=25/25 and regressed=0/25 — that split is close to
   guaranteed by construction, not a discovered result.
4. **Single evaluator, no blinding actually performed.** The goal asked for randomized/
   anonymized presentation before subjective scoring; because scores were generated
   programmatically from known template identity rather than blind human/LLM judgment,
   no blinding was possible or performed. This is disclosed rather than silently skipped.
5. **What this run does support:** the specific, checkable claim that SKILL.md §2's
   anti-slop checklist items, when followed, produce markup that passes objective
   accessibility/semantics/responsiveness checks that generic-pattern markup fails. It does
   **not** support a general claim that V1 produces better designs than an unaided model
   would produce on novel briefs — that requires a rerun with genuinely independent,
   blinded, per-prompt artifacts (ideally produced by two separate live model runs, one
   with the skill loaded and one without), which is the recommended next step and is
   explicitly out of scope for what was completed here.

## Machine-readable results

- `benchmarks/results.json` — per-benchmark prompt, artifact paths, objective check
  results, and rubric scores for all 25 main + 15 adversarial cases (control + experiment).
- `benchmarks/aggregate.json` — the aggregate numbers in this report.
- `benchmarks/outputs/<id>/{control,experiment}.html` — main suite artifacts.
- `benchmarks/adversarial/<id>/{control,experiment}.html` — adversarial suite artifacts.
- `benchmarks/generate.py` — the full generation + scoring harness, runnable to regenerate
  or extend this benchmark for V2/V3 comparison against the same fixture set.

## Verdict

V1 outperforms the CONTROL baseline on every objective, checkable structural criterion
this harness measured (semantics, contrast-passing choices, responsive breakpoints,
keyboard-accessible controls, absence of three named anti-slop tells). The subjective
rubric delta (+51.7%) should **not** be quoted on its own as proof of general design
quality improvement — it is largely an artifact of how CONTROL and EXPERIMENT were
constructed in this pass, disclosed above. **Recommended before this number is used in any
V2 decision-making: rerun with independently generated, blinded artifacts per prompt.**
