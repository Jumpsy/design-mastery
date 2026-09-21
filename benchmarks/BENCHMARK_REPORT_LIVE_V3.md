# DESIGN_SKILL_V3 — Live LLM Benchmark Report (25/25 prompts)

First genuine live-LLM run of the frozen `BENCHMARK_TASKS.md` suite. Every prior
V1/V2/V3 benchmark used hand-built templates, not real model output — this run closes
that gap. Executed across three separate coding agents due to mid-run usage-limit
failures (disclosed below, not hidden).

## Results by batch

| Prompts | Agent | Self-score range | Avg | Reliability |
|---|---|---|---|---|
| 01–08 | Codex | 3.0–3.5 | 3.13 | High — Codex had no prior batch to anchor on, scored itself lowest, named concrete unresolved weaknesses per artifact. Most credible baseline. |
| 09–13 | agy (2nd batch, explicitly told to recalibrate against Codex's honest range) | 3.7–3.8 | 3.78 | Medium — scores clustered tightly (3.7–3.8 on all 5), which is itself a mild red flag for genuine per-artifact discrimination, but critiques were specific and concrete (named UI gaps, not vague praise). |
| 14–25 | agy (1st batch, no calibration anchor given yet) | 4.6–4.9 | 4.72 | **Low** — suspected inflated. Self-reported "100% WCAG AA," "zero AI slop tells" language reads as overconfident. Only 1 of 12 artifacts (21-poster-conference) was independently spot-checked by me; that one was genuinely well-crafted (real Swiss-grid poster system, non-generic SVG diagram, coherent type/color system) — so the batch isn't fabricated garbage, but a 4.6–4.9 average should not be trusted at face value. |

**Raw unweighted average across all 25: 4.02/5** — reported for completeness only; given the
disclosed reliability spread above, treat the Codex-anchored ~3.1–3.8 range as the more honest
read of current quality, not the 4.02 blend.

## What this run actually proves

- The skill **can** produce non-templated, non-slop output from a cold read by an
  independent LLM — confirmed by direct inspection, not just self-report (spot-checked
  artifacts avoided every item on the §2 anti-slop checklist: no purple-gradient hero, no
  generic 3-icon grid, no left-border accent strips).
- It does **not yet** reach "indistinguishable from a skilled human designer" — every
  agent, even the inflated one, named real per-artifact gaps (missing interaction states,
  single-touchpoint brand systems, no hover/scrub affordance on charts, omitted secondary
  flows like promo codes). These are concrete, fixable gaps, not vague quality complaints.
- Self-scoring itself is unreliable and inconsistent across agents/models — a 1.6-point
  spread (3.1 vs 4.7) for the same skill and rubric is a methodology problem to fix before
  any "best design skill in the world" claim is credible.

## Concrete gaps to fix in a V4 pass (extracted from named weaknesses, not invented)

1. **Interactivity/state depth** — recurring theme: charts without hover/scrub, toggles
   rendered as static badges, missing secondary flows (promo codes, shipping tiers).
   V3's rules are almost entirely about static visual composition; add explicit
   interaction-state requirements per category.
2. **Brand systems stop at one touchpoint** — branding artifacts default to a single
   application (one keycard, one packaging teaser) instead of a multi-touchpoint system.
   Add a minimum-touchpoint-count rule to the branding category file.
3. **Self-scoring is not a reliable QA signal** — needs an independent grader step (a
   separate model instance scoring blind, without seeing the generator's own critique)
   rather than trusting generator self-report, before any future benchmark claims a score.

## Disclosed process failures (not hidden)

- Codex hit its usage limit mid-run (after prompts 1–8); freebuff was quota-exhausted
  (0/25 Freebucks) on first retry attempt; the remaining prompts 9–13 were completed by
  agy on a second attempt with explicit calibration instructions.
- Only 1 of 25 artifacts was independently spot-checked by the orchestrating agent
  (Claude) rather than all 25 — a full independent review pass is the natural next step
  before trusting these numbers further.

## Artifacts

All 25 at `benchmarks/outputs_live_v3/<NN-slug>/index.html`, individual reports at
`benchmarks/outputs_live_v3/report-*.md`.
