# Dashboards / data-dense UI

**Hierarchy order** (per the critique-family convergence): hierarchy → composition →
typography → color → density → affordance → brand. Fix hierarchy first — most "too
busy" dashboards are a hierarchy problem, not a density problem.

**Layout**: key metric(s) top-left or top-row, largest type on the page. Supporting
charts/tables below in a grid (12-col typical), consistent card padding (16–24px for
dense dashboards, tighter than marketing UI).

**Color in data**: reserve saturated color for data encoding only (chart series,
status states) — UI chrome (nav, cards, labels) stays neutral so data reads as the
one colorful layer. Status colors: 1 red (error/down), 1 green (success/up), 1 amber
(warning) — never invent a second red or green.

**Density**: base-unit grid still applies (4/8px) even in dense layouts — tight spacing
uses smaller multiples of the same unit, not an ad hoc smaller grid.

**Anti-patterns**: rainbow chart palettes with no semantic meaning, shadow on every
card, every metric the same visual weight (no hierarchy), gridlines heavier than the
data itself.

**Verified build**: `dashboard-demo/dashboard.html` — one dominant metric card top-left,
3 secondary metric cards, one bar chart, neutral chrome with a single accent color used
only for the primary metric's up-indicator and chart bars. Rendered and confirmed.
