# Interaction & state-integrity bug patterns

Concrete, recurring defect patterns caught by running the §5.5 convergence loop for real
across multiple rounds on coded/interactive artifacts (not from theory). A fresh
independent grader kept finding these even in files that had already passed several
prior rounds — read this before grading or fixing Category 4/5/8 findings so known
patterns get checked deliberately instead of rediscovered by luck each time.

## Category 4 — interaction / keyboard-access / state-integrity

**Synthetic-event side effects.** Reusing an existing input/change handler by setting a
control's `.value`/`.checked` and dispatching a synthetic `input`/`change` event (or
calling `.click()`) is a good way to avoid duplicating state-sync logic — e.g. a
`restoreFromSnapshot()` function driving the same handlers real user interaction would.
But audit every handler being reused this way for state mutations that assume
human-originated intent. A classic failure: a text-input handler unconditionally sets a
`somethingManuallyEdited = true` flag on every `input` event — a synthetic restore event
then corrupts that flag even though the user never touched the field. Fix: persist the
auxiliary flag alongside the main state in the save payload and explicitly restore it
*after* the synthetic dispatch, overriding the side effect.

**Roving-tabindex + `querySelector` first-match pitfall.** A comma-separated selector
list (`querySelector('input, select, button[role="radio"]')`) returns the first match in
*DOM order*, not the first match that's actually focusable/selected in a roving-tabindex
group. If a group only has one real tab-stop (`tabindex="0"`), an unqualified selector
will always land on the first item in the group regardless of which one is selected.
Fix: qualify the selector with `[tabindex="0"]` (or whatever marks the live tab-stop).

**Auxiliary module-scope state not included in save/restore round-trips.** When a
save/restore feature persists a `state` object but a related flag lives outside that
object (a module-scope `let`), the round-trip silently drops or corrupts it unless the
flag is explicitly included in both the serialize and the restore step.

**Unhandled promise rejections on user-facing async actions.** `navigator.clipboard
.writeText(...).then(...)` (or any async “this succeeded” UI update) needs a `.catch()`
— permission-denied or non-secure-context failures otherwise fail silently with no
user-visible feedback.

**Parameter-vs-closure-state bugs.** A function that takes an explicit parameter but
internally reads stale ambient/closure state instead of the parameter in one of its
branches. Trace every branch of validation/state functions against the parameter that
was actually passed, not just the happy path.

**Incomplete refactors.** A function renamed or restructured (e.g.
`validateCurrentStep()` → `validateStep(stepNum)`) where a caller elsewhere still
depends on the old implicit-state behavior instead of using the new parameter — check
every call site after a signature change, not just the definition.

## Category 5 — dishonesty / fake-state

A control that visually or textually implies it performs an action must actually perform
that action, or be reworded to be literally true. Recurring real examples: a "Save
Progress" button that writes to `localStorage` but has no corresponding restore-on-load
logic; a "Restart" action that reloads the page without clearing the very save state
that would make it a real restart; a deployment/log line that hardcodes a value (e.g. a
region name) that should reflect actual selected state, shown briefly enough to be easy
to miss in review but still wrong.

Minimal-fix philosophy applies here: prefer the smallest change that makes the claim
literally true (reword the label) unless the missing half of the feature is small and
genuinely in scope (e.g. the save-half already captures full state faithfully, so
building the restore-half is the honest fix rather than a scope violation).

## Category 8 — internal self-consistency

Two places in the same UI stating the same numeric fact (price, discount percentage,
count) must agree, including across tiers/variants/states — a static promotional pill
next to a toggle is easy to leave hardcoded to one tier's number while a computed
receipt/detail view elsewhere correctly varies by tier. When a percentage or price is
genuinely tier/state-dependent, either compute every display of it from the same source
function or delete the redundant static copy.

## Token pattern: darker-text variant for tinted surfaces

When a color passes non-text (3:1) contrast but narrowly fails text (4.5:1) contrast on
a *tinted/light* surface, introduce a companion darker-shade custom property (e.g.
`--status-success-text` alongside `--success`) rather than changing the base token
everywhere — the base token is often still correct at its original weight (icons,
borders, non-text uses). Important refinement: these darker-text variants are tuned for
light surfaces specifically. On a *dark* surface (e.g. a dark-mode log panel), the
original/lighter base token can pass where the darker "text" variant actually fails —
don't apply the light-surface variant reflexively; check contrast per surface.

## Process lesson

Categories a previous grading round called "clean" are not guaranteed to stay clean —
a fix in one round can introduce a new defect in a category that was fine before (a new
`restoreFromSnapshot()` feature introduced two of the patterns above in the same round
it was added). Always re-run the full 8-category rubric on every round, not just the
categories that previously had findings.
