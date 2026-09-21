# Logos / marks

**Process**: state the concept in one sentence before drawing anything (what idea, not
what shape). Run the plan-gate: does the first instinct read as a generic category
default (circle+bold-letter for tech, abstract swoosh for "innovation")? If yes, reject
and find the second, more specific idea.

**Construction**: build on a grid with genuine geometric consistency (consistent stroke
width, aligned optical centers, ideally kept to a single continuous path or a small set
of boolean-consistent shapes) — hand-wavy Bezier curves that "look about right" read as
amateur under scrutiny.

**Versatility check**: must work at 16px (favicon) and at poster scale, in single color
(no gradient dependency), and reversed on dark/light.

**Anti-patterns**: literal gradient-filled 3D icon, generic circle-container + initial,
more than one visual idea crammed into one mark, stock icon-library shapes assembled
without a unifying stroke system.

**Verified build**: `logo-demo/mark.svg` — single continuous brushstroke "D" monogram,
first instinct (circle+bold-D) explicitly rejected per plan-gate, revised to an
asymmetric single-stroke mark, rendered clean with no overlaps at 200×200.
