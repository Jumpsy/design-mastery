# Convergence loop (SKILL.md §5.5)

8-category material-defect rubric, no numeric scores. Clean-pass counter starts at 0.

## Convergence round 1 (fix)

Independent cold-read grader found 7 defect groups (categories 1, 2, 4, 5, 6, 7 — categories
3 and 8 fully clean):

1. **Cat 1**: `rgb(5, 150, 105)` used as *text* color reached only 3.27–3.77:1 against the
   light surfaces it sat on in several places (fails 4.5:1) — named instances: `.subdomain-status`,
   `.copy-confirm-text`, `.discount-pill`, and the JS-set `subdomainFeedback` inline color,
   plus the inline `<p style="...">` provisioning-confirmation banner text.
   Fix: introduced `--status-success-text: #047857` (verified 4.75–5.48:1 against every light
   background it's used on — white, the 10% tint `.ready-banner-box`, the 12% tint
   `.discount-pill`) and swapped all named text uses to it, plus the same identical
   text-on-tinted-background pattern on `.manifest-status-chip.live` (not explicitly named by
   the grader but the same failure) and the second JS occurrence in the `#btn-save-exit`
   handler. Left every non-text use of the original `rgb(5, 150, 105)` untouched since those
   already pass the 3:1 non-text threshold or sit on the dark `--ink` background where the
   original color already passes (4.74:1): `.step-item.is-complete .step-badge` icon+tint,
   `.status-indicator-dot`, `.benefit-icon`, `.manifest-status-chip.live .pulse-dot`,
   `.log-entry.success`.
2. **Cat 2**: five interactive-component boundaries used `var(--line)` (1.23:1 vs `--surface`)
   as their only idle-state border, with no other idle-state affordance: `.input-field`,
   `.radio-segment-btn`, `.btn-secondary`, `.plan-tier-card`, `.btn-icon-remove`.
   Fix: introduced `--border-control: #64748b` (verified 4.76:1 vs white) and applied it to all
   five. Left purely decorative `--line` uses (dividers, the `.manifest-identity-card` container
   border) untouched.
3. **Cat 4**: `goToStep()` called `nextField.focus()` on the incoming stage's first field
   *before* the `setTimeout` callback that adds `.is-visible` (removing `display: none`) had
   run — focusing a still-hidden, unfocusable element silently no-ops, breaking keyboard users'
   expected focus landing on step change.
   Fix: moved the focus-acquisition logic inside the existing 30ms `setTimeout` callback, after
   `.is-visible` is added.
4. **Cat 2 (non-text)**: `.switch-control`'s off-state track used `rgba(15, 23, 42, 0.48)`... —
   actually reported at ~1.37:1 (0.15 alpha) against the white card, with no other idle-state
   cue distinguishing on/off.
   Fix: raised the alpha to 0.48, verified ≈3.21:1.
5. **Cat 5**: the "✓ Configuration cached locally" status message shown after clicking
   "Save & Exit" made a factual persistence claim with no actual persistence — `state` was
   never written anywhere.
   Fix: added a real `localStorage.setItem('onboarding-snapshot', JSON.stringify(state))` call
   (wrapped in try/catch for private-browsing/quota edge cases) immediately before the message
   is shown, making the claim literally true. Deliberately did not add a restore-on-load
   feature — that would exceed the scope of the flagged claim, which is only about whether the
   save happened, not whether it's later restored.
6. **Cat 5**: `.pulse-dot` (used live inside `.manifest-status-chip.live`) and
   `.deployment-spinner-icon` (the provisioning-screen spinner) both used animation-implying
   names/shapes (a "pulse" dot, an SVG arc-plus-track spinner glyph) but had no actual
   `animation` — static fake-motion affordances.
   Fix: added `@keyframes pulse-dot-beat` (opacity pulse, 1.6s ease-in-out infinite) to the live
   pulse dot, and `@keyframes deployment-spinner-rotate` (360° rotation, 1s linear infinite) to
   the spinner icon. Both animations are safely covered by the file's existing global
   `prefers-reduced-motion: reduce` override, which disables all `animation`/`transition`.
7. **Cat 6/7**: the literal `font-family: 'Inter', -apple-system, BlinkMacSystemFont,
   sans-serif;` and `font-family: 'JetBrains Mono', monospace;` strings were hardcoded at ~18
   call sites each, duplicating the already-declared `--font-ui`/`--font-mono` tokens verbatim
   (a de facto dead-token situation, since the tokens existed but were never referenced).
   Fix: batch-replaced every occurrence outside the `:root` token declarations themselves with
   `var(--font-ui)` / `var(--font-mono)`; verified via grep that zero literal occurrences remain
   outside `:root`.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (201/201, 101/101),
extracted script parses cleanly via `node -e "new Function(...)"`, and all new/changed contrast
values recomputed via the standard WCAG relative-luminance script (success text 4.75–5.48:1
across its three background contexts, border-control 4.76:1, switch off-state 3.21:1).

Rounds 2 and 3 must both come back clean before this artifact is considered converged.

## Convergence round 2 (fix)

Independent cold-read grader (fresh subagent, did not read this file) found 7 defect groups
across categories 1, 2, 4, 5, 7, 8, with category 3 flagged as borderline/defensible and
categories 3-partial/6 otherwise clean:

1. **Cat 1**: `.input-field::placeholder` at `rgba(71, 85, 105, 0.6)` reached only ~2.88:1
   against `--surface` (white), below the 4.5:1 text minimum.
   Fix: raised alpha to 0.8, verified 4.54:1.
2. **Cat 1**: `.benefit-icon` renders a visible `✓` text glyph (not a decorative SVG), so it
   is bound by the 4.5:1 text threshold, not the 3:1 non-text threshold — its original green
   only cleared the lower bar.
   Fix: switched to `--status-success-text` (already introduced in round 1), verified
   5.48:1 vs white.
3. **Cat 2**: `.input-subdomain-group` and `.copy-link-input` still used `var(--line)`
   (1.23:1) as their sole idle-state border, missed in round 1's border-token sweep.
   Fix: switched both to `--border-control` (round 1's token), verified 4.76:1.
4. **Cat 4**: the team-size segmented control and plan-tier cards were single-select
   radiogroups (`role="radio"`/`role="radiogroup"`) with click-only handlers — no arrow-key
   navigation, no roving `tabindex`, so keyboard users could not operate them per the ARIA
   APG radiogroup pattern.
   Fix: added a shared `wireRadioGroup(buttons, onSelect)` helper implementing roving
   `tabindex` (0 on checked, -1 on others) plus Left/Right/Up/Down (wrapping) and Home/End,
   wired to both groups in place of the old click-only listeners.
5. **Cat 4/8**: a state-clobbering bug — the subdomain field was silently overwritten by
   the org-name auto-slug logic on every keystroke in the org-name field, even after the
   user had manually edited the subdomain themselves.
   Fix: added a `subdomainManuallyEdited` flag set `true` on the first manual subdomain
   edit, gating the auto-derivation so it only applies before the user has diverged.
6. **Cat 4**: `#form-error-banner` had both `role="alert"` and `aria-live="polite"` — the
   explicit `polite` setting contradicts/downgrades the assertive live-region semantics
   `role="alert"` already implies.
   Fix: removed the redundant `aria-live="polite"`, leaving `role="alert"` alone.
7. **Cat 5**: the subdomain-availability feedback claimed "Available · Reserved for your
   organization" (both in static markup and the JS-driven update) with no actual
   uniqueness check ever performed — a fabricated claim of a real backend guarantee.
   Fix: reworded to "Looks available" in both the static markup and the JS string,
   removing the false "reserved" claim without building an unrequested real/fake backend
   check — smallest change that makes the copy stop asserting something untrue.
8. **Cat 7 (self-identified during fix, not explicitly named by the grader as a literal
   duplicate)**: `rgba(15, 23, 42, X)` / `rgba(37, 99, 235, X)` / `rgba(185, 28, 28, X)` and
   a bare `rgb(185, 28, 28)` were re-typed as raw RGB triplets at multiple alpha levels
   across the file, duplicating the already-declared `--ink` / `--accent` hex tokens (and,
   for the red, a color used ~4+ times with no token backing it at all — a Cat 8 internal-
   consistency gap since no token existed yet to duplicate literally).
   Fix: added `--ink-rgb`, `--accent-rgb`, and a new `--danger`/`--danger-rgb` pair to
   `:root`, then batch-converted every literal RGB-triplet occurrence to
   `rgba(var(--*-rgb), X)` / `var(--danger)`. Verified via grep: zero old-format literals
   remain outside the `:root` declarations themselves.
9. **Cat 5**: `updateLiveManifest()` built an invitee chip via string-concatenated
   `innerHTML` including the invitee's self-entered email local-part — an injection risk
   from unescaped user input, independent of whether this specific app is a mock.
   Fix: replaced with `createElement`/`textContent`/`Node.append(...)` safe DOM
   construction.

Disclosed, not fixed (out of material scope for this round, logged per protocol rather
than silently left):

- **Cat 3 (borderline/defensible)**: `.pulse-dot` (the 8px "live" status indicator) has no
  on-page pause/hide control, so it does not independently satisfy WCAG 2.2.2 beyond the
  file's existing global `prefers-reduced-motion: reduce` override (which stops the
  animation at the OS level but is not itself a page-level Pause/Stop/Hide mechanism).
  Treating this as a defensible exemption rather than a required fix: it is a small,
  `aria-hidden` decorative accompaniment to text that already states "Live" elsewhere in
  the same chip, not the sole conveyor of the status, and is under the width/duration
  profile 2.2.2 exempts for essential, non-distracting status indicators. Not implementing
  a bespoke pause control for an 8px dot; flagging this explicitly rather than silently
  passing over it.
- **Cat 7 (unfixable via token)**: the `select.input-field` background-image is an inline
  SVG `data:` URI containing a literal `stroke='%23475569'` (URL-encoded `#475569`, matching
  `--muted`). CSS custom properties cannot be interpolated inside a `data:` URI string, so
  this literal cannot be converted to `var(--muted)` without either duplicating the whole
  SVG per theme variant or switching to an inline `<svg>`/mask-based icon — both out of
  scope for this round's fixes. Logged as a known, structurally-unavoidable duplication
  rather than silently left unmentioned.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (201/201,
103/103), extracted script parses cleanly via `node -e "new Function(...)"`, and all
new/changed contrast values recomputed via the standard WCAG relative-luminance script
(placeholder 4.54:1, `.benefit-icon` 5.48:1, `.input-subdomain-group`/`.copy-link-input`
border 4.76:1 — all vs. white).

Rounds 3 and 4 must both come back clean before this artifact is considered converged.

## Convergence round 3 (fix)

Independent cold-read grader (fresh subagent, did not read this file) found defect groups
across categories 1, 2, 4 (five separate issues), 5 (four separate issues), 7 (two issues,
one self-identified by the grader as not a real defect), and 8, with category 6 confirmed
fully clean and category 3 re-flagged as the same borderline `.pulse-dot` case already
disclosed in round 2 (no new Pause/Stop/Hide issue).

1. **Cat 1**: the subdomain input (`.subdomain-input`) has a different class than
   `.input-field` and was silently missing the documented 4.5:1-safe placeholder color
   from round 2's fix — it still rendered at the pre-round-2 ~2.88:1 alpha.
   Fix: extended the `.input-field::placeholder` selector to also cover
   `.subdomain-input::placeholder`, so both share the 0.8-alpha (4.54:1) color.
2. **Cat 8**: `.step-badge`'s idle border still used `var(--line)` (1.23:1), missed by
   round 1's border-token sweep despite matching the file's own documented rule (every
   interactive/component border should use `--border-control`).
   Fix: switched to `var(--border-control)`.
3. **Cat 7**: `rgb(5, 150, 105)` / `rgba(5, 150, 105, X)` was re-typed as a raw literal at
   7+ call sites (`.step-item.is-complete .step-badge`, `.status-indicator-dot`,
   `.discount-pill`, `.manifest-status-chip.live .pulse-dot`, `.log-entry.success`,
   `.ready-banner-box`) with no token backing it, unlike `--ink-rgb`/`--accent-rgb`/
   `--danger-rgb`, which already existed for the identical purpose.
   Fix: added `--success: #059669;` / `--success-rgb: 5, 150, 105;` to `:root` (next to
   `--danger`/`--danger-rgb`), then batch-converted every non-`:root`, non-comment literal
   occurrence to `var(--success)` / `rgba(var(--success-rgb), X)`. Verified via grep: zero
   remaining literal `5, 150, 105` occurrences outside the `:root` declaration; the
   explanatory contrast comment at line 25 was preserved untouched since its factual claim
   about the raw value's contrast ratio is still accurate.
4. **Cat 5**: the plan-tier cards' displayed prices (`#card-pro-rate`, `#card-ent-rate`)
   were static markup that never updated when the billing-cadence toggle switched between
   monthly/annual, contradicting the receipt/summary panel below which did update —
   two elements derived from the same state disagreeing.
   Fix: added `cardProRate`/`cardEntRate` to the `els` cache and updated both inside
   `updatePricingCalculations()` alongside the existing receipt calculation. Verified the
   static default markup already matched the default state (`annual`/`pro`) so no
   additional init-time call was needed for correctness at first paint.
5. **Cat 4**: `goToStep()`'s step-transition animation never visibly animated — the
   `setTimeout` callback mutated both the `display`/`opacity` state and the offset-
   transform state synchronously in the same tick, giving the browser no intermediate
   paintable frame to interpolate the CSS transition from.
   Fix: rewrote the transition to set inline `display`/`opacity`/`transform` styles first
   (establishing the pre-transition state via inline-specificity override), force a
   synchronous reflow via `void nextStage.offsetHeight` inside the `setTimeout` callback,
   then toggle the classes and clear the inline overrides — guaranteeing a real "before"
   frame exists for the transition to animate from.
6. **Cat 4**: `.input-field:focus` and `.input-field.has-error` are same-specificity
   selectors that can both apply to a focused, invalid field simultaneously; source order
   alone decided which "won," producing a mixed red-border/blue-ring visual state that
   matched neither design intent.
   Fix: added an explicit `.input-field.has-error:focus` rule with the intentionally-
   designed combined styling (red border + red-tinted focus ring), rather than relying on
   accidental cascade order.
7. **Cat 4/8**: both `.step-connector` elements were `<div>`s used as direct children of
   `<ol class="step-track">`, which per spec may only contain `<li>` children — invalid
   markup subject to unpredictable browser parser repair.
   Fix: changed both wrapper tags to `<li class="step-connector">`; verified safe against
   visible bullet markers via the existing global `ul, ol { list-style: none; }` reset,
   and confirmed no CSS selector in the file targets the tag (all target the class).
8. **Cat 5/8**: the invite counter (`refreshRosterFromDOM()`) counted
   `state.invites.length` (all rows, including blank-email ones), while
   `updateLiveManifest()`'s roster-chip rendering filtered out blank-email rows — the two
   UI elements could visibly disagree about how many invites existed.
   Fix: changed the counter to `state.invites.filter(inv => inv.email.trim()).length`,
   matching the same filter predicate the chip rendering already used.
9. **Cat 5**: the "Save & Exit" button never actually exits or navigates anywhere — it
   only persists to `localStorage` and updates a status label — so its label claimed
   behavior it doesn't perform.
   Fix: renamed the button to "Save Progress" (copy-only change), consistent with the
   established minimal-fix philosophy from rounds 1 and 2 (reword the claim to match
   actual behavior rather than build unrequested exit/navigation functionality).
10. **Cat 5**: the `#btn-save-exit` click handler wrapped the actual save (a synchronous,
    instant `localStorage.setItem` call) in an artificial 400ms `setTimeout`, showing a
    "Saving snapshot..." interstitial that manufactured the appearance of server-side or
    otherwise asynchronous work that doesn't exist.
    Fix: removed the `setTimeout` wrapper and the fake interstitial message; the handler
    now performs the save and updates the status text synchronously, since the operation
    genuinely is instant. Also added a `catch` branch (previously the try/catch had no
    catch clause reachable after the timeout was removed) so a `localStorage` quota/
    private-browsing failure now surfaces an honest "Could not save locally" message
    instead of silently claiming success.

Disclosed, not fixed (out of material scope for this round, logged per protocol rather
than silently left):

- **Cat 7 (self-identified by the grader as not a real defect)**: the raw-black
  `box-shadow: rgba(0, 0, 0, 0.15)` / `rgba(0, 0, 0, 0.2)` literals on the switch thumb
  and range thumb are not exact-value duplicates of `--ink` (which is a dark navy, not
  pure black) — the grader itself flagged this only as a possible pattern-consistency
  question, not a literal token duplication. Not converting these to `--ink-rgb`, since
  doing so would change the rendered shadow color rather than just referencing an
  existing equivalent value.
- **Cat 5 (re-affirming round 2's decision)**: the subdomain-availability feedback was
  re-flagged as still implying a real uniqueness check. Round 2 already softened the copy
  from "Available · Reserved for your organization" to "Looks available" specifically to
  remove the false "reserved" guarantee while keeping a plausible, hedged UI string for a
  client-only demo with no backend to check against. Re-affirming that fix as sufficient
  rather than re-fixing or further hedging the copy, since "Looks available" no longer
  asserts a real guarantee.
- **Cat 5 (accepted demo limitation)**: the deployment/provisioning sequence (fixed
  `setTimeout` timings, no real backend, ending in a static "LIVE & HEALTHY" state) is
  fully simulated. Treating this as a defensible, disclosed limitation of a client-only
  static demo rather than building a real or more elaborately faked backend simulation,
  which would be out of scope for this artifact.
- **Cat 5 (accepted demo limitation)**: "Launch Workspace Console" uses `alert()` instead
  of real navigation, since there is no real console destination for this demo to link
  to. Disclosing rather than fixing, consistent with the file being a static prototype.
- **Cat 3 (re-flagged, same as round 2)**: `.pulse-dot` still has no on-page Pause/Stop/
  Hide control beyond the global `prefers-reduced-motion` override. No new information
  this round beyond round 2's disclosure; re-affirming the same defensible-exemption
  reasoning (small `aria-hidden` decorative accompaniment to text that already states
  "Live" elsewhere in the same chip).

Verification after all fixes: `<style>`/`<script>` brace counts balanced (202/202,
100/100), extracted script parses cleanly via `node -e "new Function(...)"`, and all
new/changed contrast values recomputed via the standard WCAG relative-luminance script
(subdomain placeholder 4.54:1, `.step-badge` border 4.76:1 — both vs. white/surface).

Rounds 4 and 5 must both come back clean before this artifact is considered converged.

## Convergence round 4 (fix)

Independent cold-read grader (fresh subagent, did not read this file) found categories 6
and 7 fully clean, categories 1/2/3 clean or explicitly borderline/defensible (not
asserted as definite violations), and three concrete, non-borderline defects in
categories 4/5/8 (overlapping across categories, reported once each below).

1. **Cat 4/5**: the Team Access step's static instructional copy read "...anyone with an
   verified @acme.com corporate email..." and never updated, while the live manifest
   aside's `#manifest-sso-val` *does* dynamically compute the domain from the current
   subdomain — so renaming the org made two parts of the same wizard contradict each
   other about state the app itself proves it tracks.
   Fix: wrapped the domain text in a new `<span id="sso-domain-text">acme.com</span>`,
   added it to the `els` cache, and set its `textContent` alongside
   `manifestSSOVal` inside `updateLiveManifest()`'s existing domain-computation line, so
   both elements now derive from the same `domain` variable and stay in sync.
2. **Cat 4/5**: the Developer-tier plan claimed a "(max 2)" seat cap in
   `updatePricingCalculations()`'s receipt text, but nothing enforced it — the seat
   slider's `max="50"` was never adjusted, so a user could select 8+ seats on the
   supposedly 2-seat-max free tier and see self-contradictory text like "8 seats (max 2)".
   Fix: in the plan-tier-card selection handler, when the selected tier is `developer`
   the slider's `max` attribute (and `aria-valuemax`) is now set to `2` and any seats
   value above 2 is clamped down to 2; switching to a paid tier restores `max="50"`. This
   makes the "(max 2)" claim actually enforced by the control itself, not just asserted
   in text.
3. **Cat 4 (self-identified while fixing #2, not explicitly named by the grader)**: the
   seat slider's `input` handler and the plan-tier-card selection handler both called
   `updatePricingCalculations()` but neither called `updateLiveManifest()` — so
   `#manifest-seat-count-val` in the live-manifest aside never updated when the user
   dragged the seat slider or switched plan tiers, silently freezing at its initial "8
   Seats" markup value regardless of actual state. This is the same class of two-elements-
   derived-from-one-state-disagreeing bug fixed for the invite counter in round 3.
   Fix: added `updateLiveManifest()` calls to both handlers, alongside the newly-added
   seat-cap clamping logic in the tier handler.
4. **Cat 5**: `#live-save-status` defaulted to the static markup text "Draft saved
   locally" on page load, before the user had ever clicked "Save Progress" and before any
   `localStorage.setItem` call had executed — claiming a save had already happened when
   it had not.
   Fix: changed the default text to "Not saved yet", an honest statement of the actual
   initial state; the real "✓ Configuration cached locally" message (added in round 1,
   made synchronous in round 3) still fires only after an actual save occurs.

Disclosed, not fixed (grader explicitly flagged these as borderline/defensible or
out-of-scope simplifications rather than clear violations, and I'm re-affirming that
framing rather than fixing or re-litigating):

- **Cat 1 (borderline)**: `.plan-badge-rec` / `.role-badge-tag` (`--accent` #2563eb at
  12px/700 on a 10%-tint `--accent` background) computes to ≈4.50:1 — right at the 4.5:1
  line, not a clear fail. Not adjusting the color for a threshold-line case the grader
  itself declined to assert as a definite violation.
- **Cat 3 (re-flagged, same as rounds 2 and 3)**: `.pulse-dot`'s indefinite animation with
  no page-level pause control, again described by this round's grader as "reasonably
  exempt" under WCAG's own small-essential-status-indicator guidance. No new information;
  re-affirming the same defensible-exemption reasoning already logged twice.
- **Cat 5 (re-affirming round 3's decision)**: the subdomain-availability "Looks
  available" status was re-flagged as reusing the status-check convention for a check
  that isn't real, but the grader itself called this "a common and largely expected
  simplification in a self-contained demo" and declined to count it as a hard violation.
  Re-affirming round 2/3's softened copy as sufficient.
- **Cat 7**: the raw-black `rgba(0, 0, 0, 0.15)` / `rgba(0, 0, 0, 0.2)` drop-shadow
  literals were checked again and confirmed to have no declared shadow-color token to
  duplicate — consistent with round 3's disclosure of the same items.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (202/202,
103/103), extracted script parses cleanly via `node -e "new Function(...)"`.

Rounds 5 and 6 must both come back clean before this artifact is considered converged.

## Convergence round 5 (fix)

Independent grader (agent `ae0b5cc060faea866`) found 6 concrete defects across categories
4, 5, and 8, plus 2 non-violation/defensible notes.

1. **Cat 5 (dishonesty/fake-state)**: `els.manifestStatusLabel.textContent = 'LIVE &amp;
   HEALTHY';` — `textContent` does not decode HTML entities, so the label rendered the
   literal string `LIVE &amp; HEALTHY` instead of `LIVE & HEALTHY`. Fixed by using a real
   `&` character in the JS string literal.
2. **Cat 4 (state-integrity bug)**: the two static invite rows' `aria-label`s ("Remove
   first teammate" / "Remove second teammate", and matching ordinal labels on the email/
   role fields) went stale once rows were added or removed, since nothing recomputed them
   after the DOM changed. Fixed by having `refreshRosterFromDOM()` — which already runs on
   every roster `input`/`change`/add/remove event — reassign `aria-label` on each row's
   email input, role select, and remove button to a 1-based index derived from the row's
   current DOM position, so labels always reflect actual order.
3. **Cat 8 (rule-consistency break)**: the step-2→step-3 "Continue to Infrastructure"
   button label didn't match step 3's own declared names (stepper nav: "Plan & Deploy";
   `h2#heading-step-3`: "Deployment Tier & Plan"). Fixed by renaming the button label to
   "Continue to Plan & Deploy" to match the stepper nav's own title for that step.
4. **Cat 4 (state-integrity bug)**: `.status-indicator-dot` had a hardcoded
   `background-color: var(--success)` with no error variant, so it stayed green even when
   the adjacent subdomain-feedback text turned red for an invalid (too-short) subdomain —
   the dot's own color claim silently disagreed with the real validation state. Fixed by
   adding a `.status-indicator-dot.is-error { background-color: var(--danger); }` rule and
   toggling that class in the existing `input-subdomain` handler alongside the text color
   change, so the dot and text always agree.
5. **Cat 4 (state-integrity bug, recurrence of round 3's roster-counter fix)**: the
   deployment-sequence's final log line used unfiltered `state.invites.length` for the
   "Invitation tokens broadcast to N engineers" count, while the roster counter (fixed in
   round 3) already uses `state.invites.filter(inv => inv.email.trim()).length` to exclude
   blank rows. Fixed by reusing the same filtered-count predicate in the deployment log
   line so both places agree on what counts as a real invite.
6. **Cat 8 (rule-consistency break, self-discovered while checking the pricing-token
   fix below)**: the static default pricing markup (`receipt-discount-amount`,
   `receipt-total-price`, the billing note, `manifest-cost-val`) baked in a mistaken
   double-20%-discount rather than what `updatePricingCalculations()` actually computes
   for the true default state (pro tier, annual, 8 seats). Correct default values:
   monthly-equivalent total `$192.00/mo` (8 seats × $24/seat annual rate), discount
   `-$48.00/mo` (8 seats × ($30 − $24)), annual billed `$2,304.00/year`. Fixed all four
   static values to match.
7. **Cat 8 (self-discovered, adjacent to the round-5 grader's findings)**:
   `.log-entry.success` used `var(--success)` directly for log-line text color, breaking
   the file's own declared text-vs-non-text token split (`--success` for non-text
   elements, `--status-success-text` for text) even though it still passed contrast at
   ≈4.73:1. Fixed by switching it to `var(--status-success-text)` (#047857, darker than
   `--success`'s #059669, so contrast only improves).

Disclosed, not fixed (grader-flagged as non-violations or already-logged):
- **Cat 1 (non-violation note)**: the grader confirmed no new contrast failure this round;
  flagged as a note only, not a finding.
- **Cat 7 (re-confirmed, same as rounds 3 and 4)**: the data-URI `stroke='%23475569'`
  literal inside the `select.input-field` background-image SVG was checked again and
  confirmed necessary — SVG data URIs can't reference CSS custom properties, so this
  remains a disclosed, unavoidable duplication.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (203/203,
103/103), extracted script parses cleanly via `node -e "new Function(...)"`.

Rounds 6 and 7 must both come back clean before this artifact is considered converged.

## Convergence round 6 (fix)

Independent cold-read grader found 12 defects across categories 1, 2, 3, 4, 5, 7, and 8:

1. **Cat 1**: `--accent` (#2563eb) as text color on its own 10%-tint background
   (`.plan-badge-rec`, `.role-badge-tag`) reached only ≈4.497:1, a hair under the 4.5:1
   text minimum. Fixed via the same darker-text-variant pattern as `--status-success-text`:
   added `--accent-text: #1d4ed8;` and swapped both usages to it.
2. **Cat 2**: `.continuous-range-input` slider track used `background-color: var(--line)`
   against `--canvas`, ≈1.18:1 (fails 3:1 non-text minimum). Fixed by reusing the existing
   `--border-control` token (established in an earlier round for idle-state 3:1 component
   boundaries), now ≈4.02:1.
3. **Cat 3**: `.pulse-dot`'s `pulse-dot-beat` animation runs infinitely with no on-page
   pause/stop/hide control. Disclosed, not fixed — same disposition as prior rounds'
   equivalent findings (a status indicator's ambient pulse is treated as essential
   live-state signaling, not decorative motion requiring a pause control, consistent with
   WCAG 2.2.2's own carve-out for essential indicators).
4. **Cat 4 (interaction bug)**: the subdomain-input handler unconditionally reassigned
   `input.value` on every keystroke, resetting the caret to the end of the field. Fixed by
   only reassigning `.value` when the slugified value actually differs from the raw input,
   and restoring the caret position via `setSelectionRange`.
5. **Cat 4 (state-integrity bug)**: the stepper nav allowed bypassing step-2 email
   validation — `els.navStep1`'s click handler jumped to step 1 with no validation, and
   `els.navStep3`'s handler validated only `state.currentStep` (whichever step happened to
   be active), so a user could leave an invalid email on step 2, nav-click back to step 1
   (no validation fires), then nav-click to step 3 (validates step 1, which is already
   valid, and skips step 2 entirely). Fixed by splitting `validateCurrentStep()` into a
   `validateStep(stepNum)` taking an explicit step number, and having the nav-step-2 and
   nav-step-3 handlers explicitly validate every step being passed through (step 1 for a
   step-2 jump; steps 1 and 2 for a step-3 jump) rather than only whichever step is
   "current" at click time.
6. **Cat 4 (redundant live regions)**: `#deployment-screen` (`role="status"`, an implicit
   live region) contained a child `#provisioning-log-box` with its own explicit
   `aria-live="polite"`, risking duplicate screen-reader announcements of the same log
   content. Fixed by removing the redundant explicit `aria-live` from the child.
7. **Cat 5**: `#btn-launch-console` ("Launch Workspace Console") fired only a placeholder
   `alert()` claiming to launch a real dashboard — a dishonest control. Fixed with the
   minimal change of rewording the alert text to honestly state this is a prototype and the
   console isn't available, rather than claiming it "launched" anything.
8. **Cat 7**: the `.input-field::placeholder` rule hardcoded `rgba(71, 85, 105, 0.8)`,
   duplicating the already-declared `--muted: #475569` token's color at non-1.0 alpha.
   Fixed via the same RGB-triplet companion-token pattern used for `--success-rgb`: added
   `--muted-rgb: 71, 85, 105;` and converted the literal to `rgba(var(--muted-rgb), 0.8)`.
9. **Cat 8 (rule-consistency break)**: `#subdomain-feedback-text` and
   `#manifest-status-label` update dynamically (validation state, deployment status) but
   have no live-region markup, unlike `#copy-feedback-msg` (`role="status"`) and the
   deployment log (`aria-live="polite"`) elsewhere in the same file. Flagged by the grader
   with lower confidence; disclosed rather than fixed this round — both elements sit
   immediately adjacent to, or inside, their own already-live-region ancestor context
   during the interactions that change them (the subdomain feedback is read alongside the
   input's own state on the active step; the manifest status label is inside the
   `manifest-aside`, which is not currently marked live at all), so adding live-region
   markup piecemeal here risks the exact redundant-announcement problem fixed in item 6
   without a clear net accessibility benefit — needs a deliberate pass across the whole
   manifest aside, not a one-off patch, so it's logged for a future round rather than
   patched now.
10. **Cat 8 (label mismatch)**: the nav-stepper's step-1 label ("Workspace Details") and
    the step-1 panel heading ("Organization & Workspace") described the same step with
    different emphasis; likewise step-3's nav label ("Plan & Deploy") vs. panel heading
    ("Deployment Tier & Plan") used the same two phrases in swapped order. Fixed by
    renaming both panel headings (`#heading-step-1`, `#heading-step-3`) to match their
    corresponding nav-stepper labels exactly.
11. **Cat 8 (content mismatch)**: the static `#receipt-billing-note` HTML text and what
    `updatePricingCalculations()`'s annual branch overwrites it with on page load differed
    in both content (the static version had an extra "Cancel or scale seats anytime"
    clause) and sentence order. Fixed by making the static markup match the JS-generated
    string exactly.
12. **Cat 8 (discount-math mismatch)**: the receipt's "Annual Commitment Discount (20%)"
    label was a static literal — exact for the Pro tier (24 vs. 30 = 20%) but wrong for
    Enterprise (64 vs. 79 ≈ 18.99%). Fixed by making the percentage dynamic: wrapped it in
    a `#receipt-discount-pct` span and computed it in `updatePricingCalculations()` from
    the actual monthly/annual rate difference for the selected tier.

Disclosed, not fixed:
- **Cat 3**: `.pulse-dot` infinite animation (see item 3 above) — essential live-state
  indicator, not decorative motion.
- **Cat 7 (re-confirmed, same as rounds 3, 4, and 5)**: the data-URI `stroke='%23475569'`
  literal inside the `select.input-field` background-image SVG remains necessary — SVG
  data URIs can't reference CSS custom properties.
- **Cat 8 (partial, item 9 above)**: `#subdomain-feedback-text` / `#manifest-status-label`
  live-region gap — logged for a future deliberate pass rather than patched piecemeal.
- **Cat 8 (lower-confidence, not acted on)**: the toggle-level "Save 20%" discount pill
  (`.discount-pill` in the billing-cadence toggle, not the per-tier receipt) is a general
  marketing label describing the default/recommended Pro tier's exact discount, not a
  per-tier computed value like the receipt row fixed in item 12 — left as a static
  headline claim rather than made tier-reactive, since it sits next to the toggle itself
  (not inside the tier-specific receipt) and is accurate for the page's actual default
  state (Pro, annual).

Verification after all fixes: `<style>`/`<script>` brace counts balanced (0/0 net),
extracted script parses cleanly via `node -e "new Function(...)"`.

## Convergence round 7 (fix)

Independent grader found 7 defects (not a clean pass).

1. **Cat 1**: `.log-entry.success` text on `.provisioning-log-card`'s dark `--ink`
   background used `--status-success-text` (#047857), which only reaches ~3.26:1 there —
   that token is tuned for light surfaces, not this dark card. Verified computationally
   (WCAG relative-luminance/contrast script) that the base `--success` (#059669) already
   clears 4.5:1 against `--ink` (~4.74:1), so switched `.log-entry.success` to `--success`
   directly rather than introducing a third green-text token, with a comment explaining
   why the usual darker-text-variant pattern doesn't apply here.
2. **Cat 1 / Cat 8**: `.radio-segment-btn.is-selected` used plain `--accent` text on the
   `rgba(var(--accent-rgb), 0.1)` tint background (~4.49:1, fails 4.5:1) and broke the
   file's own established darker-text-variant convention that `.plan-badge-rec` and
   `.role-badge-tag` already follow for this exact background pattern. Fixed by switching
   its `color` to `--accent-text`.
3. Cat 2: clean, no defects.
4. **Cat 3 (re-confirmed)**: `.manifest-status-chip.live .pulse-dot`'s infinite pulse
   animation has no page-level pause/stop/hide control beyond OS-level
   `prefers-reduced-motion`. Logged as disclosed, not fixed (see below) — same
   essential-live-state-indicator reasoning as prior rounds' `.pulse-dot` finding.
5. **Cat 4**: `validateStep(stepNum)`'s second branch still read
   `else if (state.currentStep === 2)` instead of `else if (stepNum === 2)` — a residual
   incomplete-refactor bug from round 6's `validateCurrentStep()` → `validateStep(stepNum)`
   change. This meant `els.navStep3`'s `validateStep(1) && validateStep(2)` call would
   silently skip real email validation when the user was still on step 1 and clicked
   directly to the step-3 nav dot. Fixed by changing the branch condition to `stepNum === 2`.
6. **Cat 4**: `els.btnCopyLink` and `els.btnCopyToken` both called
   `navigator.clipboard.writeText(...).then(...)` with no `.catch()`, so a clipboard-write
   rejection (permission denied, non-secure context) failed silently with no user-visible
   feedback. Fixed by adding a `.catch()` to each that surfaces a failure message through
   the same feedback-element pattern already used for the success path.
7. **Cat 5**: `#btn-save-exit` ("Save Progress") wrote the full `state` object to
   `localStorage` and showed a success message, but nothing ever read `onboarding-snapshot`
   back out — the control implied resumable save-and-continue-later behavior it could never
   actually deliver. Since the underlying data was already being saved faithfully, fixed by
   implementing a real `restoreFromSnapshot()` function that runs on load: it repopulates
   the org name/subdomain inputs, region select, team-size segmented control, invite roster
   (rebuilt from saved data via the existing row-template + `refreshRosterFromDOM()`), SSO
   switch, billing-cadence switch, plan-tier card, seat slider, and environment checkboxes
   — reusing each control's own existing event handler by setting its value/checked state
   and dispatching a native `input`/`change`/`click` event, rather than duplicating their
   state-sync logic — then calls the existing `goToStep()`/`updateLiveManifest()` to land on
   the saved step and refresh all derived UI. The save handler's behavior was already honest
   (it does cache locally); only the missing read-half needed implementing.
8. Cat 6: clean — all 18 `:root` tokens referenced at least once.
9. **Cat 7 (re-confirmed, same as rounds 3-6)**: `select.input-field`'s data-URI
   `stroke='%23475569'` still duplicates `--muted`'s value — grader itself noted this is
   largely unavoidable since SVG data-URIs can't reference CSS custom properties, but named
   it per audit criteria anyway.

Disclosed, not fixed:
- **Cat 3**: `.pulse-dot` infinite animation — essential live-state indicator, not
  decorative motion (re-confirmed, same reasoning as rounds 3-6).
- **Cat 7 (re-confirmed)**: `select.input-field`'s `stroke='%23475569'` data-URI literal —
  unavoidable, SVG data-URIs can't reference CSS custom properties.
- **Soft observation, not counted as a defect by the grader**: the `.pulse-dot` "live"
  heartbeat continues even on the static final deployment-complete screen; not flagged
  because the prototype nature of that screen is already honestly disclosed via the
  `btn-launch-console` alert text.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (0/0 net),
extracted script parses cleanly via `node -e "new Function(...)"`.

## Convergence round 8 (fix)

Independent grader (agent `a6bc9a33237b7cc13`) found 8 defects requiring fixes — not a
clean pass. Notably, several of these were newly-introduced by round 7's own fixes (the
`restoreFromSnapshot()` feature), confirming the value of re-grading after every fix
round rather than assuming previously-clean categories stay clean.

1. Cat 1: clean (verified numerically).
2. Cat 2: clean.
3. **Cat 3 (re-confirmed, same as rounds 3-7)**: `.pulse-dot` infinite animation, no
   pause/stop/hide affordance.
4. **Cat 4 (round-7 regression)**: `goToStep()`'s autofocus selector
   `'input:not([disabled]), select, button[role="radio"]'` used a bare comma-list, which
   `querySelector` matches in DOM order, not selection-state order — so on a step whose
   first focusable control is a `button[role="radio"]` group, autofocus always landed on
   the *first* radio button regardless of which one was actually selected/tab-stop
   (`tabindex="0"`). Fixed by qualifying the selector to
   `'input:not([disabled]), select, button[role="radio"][tabindex="0"]'`, reusing the
   file's existing roving-tabindex convention so the selector only matches the group's
   single real tab-stop.
5. **Cat 4 (round-7 regression)**: `restoreFromSnapshot()`'s roster-row rebuild loop
   didn't preserve the first invite row's `disabled` remove-button state, so restoring a
   saved snapshot silently let the first (undeletable-by-design) row become removable.
   Fixed by re-adding the `disabled` attribute and the distinct "Remove first teammate"
   `aria-label` for `i === 0` in the rebuilt row markup, matching the original static
   markup's behavior.
6. **Cat 4 (round-7 regression)**: the subdomain input handler unconditionally sets
   `subdomainManuallyEdited = true` on every `input` event, including the synthetic
   `input` event `restoreFromSnapshot()` dispatches to reuse that handler's state-sync
   logic — so restoring a snapshot always corrupted this flag to `true`, even for a
   subdomain that had never been manually edited before saving. Fixed by persisting
   `subdomainManuallyEdited` as a sibling of `state` in the saved snapshot
   (`JSON.stringify({ state, subdomainManuallyEdited })`) and explicitly restoring the
   real saved value immediately after the synthetic dispatch, overriding its side effect.
7. **Cat 5**: "Restart Onboarding Flow" (`#btn-restart-flow`) called `location.reload()`
   without clearing `onboarding-snapshot` from `localStorage` first, so a restart silently
   re-restored the old saved progress instead of actually resetting — contradicting its
   own label. Fixed by adding `localStorage.removeItem('onboarding-snapshot')` (guarded by
   try/catch) before the reload.
8. **Cat 5**: `#log-line-1`'s deployment-log first line hardcoded
   "Provisioning dedicated telemetry cluster in us-east-1..." regardless of the actual
   selected region, visible for ~500ms at the start of the deploy sequence — dishonest for
   any org that picked a different region. Fixed by setting `els.logLine1`'s text from
   `state.region` at the start of `startDeploymentSequence()` instead of relying on static
   markup.
9. Cat 6: clean — all 18 `:root` tokens referenced.
10. **Cat 7 (re-confirmed, same as rounds 3-7)**: `select.input-field`'s data-URI
    `stroke='%23475569'` still duplicates `--muted`'s value — unavoidable, SVG data-URIs
    can't reference CSS custom properties.
11. **Cat 8**: the static `<span class="discount-pill">Save 20%</span>` next to the
    "Annual Billing" toggle label was accurate for the Pro tier (20%) but wrong for
    Enterprise ($79→$64/seat = 18.99%, which the receipt itself correctly rendered as
    "19.0%") — selecting Enterprise put a contradicting "20%" pill and "19.0%" receipt line
    on screen simultaneously. Fixed by making the pill dynamic: it now computes the
    current tier's actual annual-vs-monthly discount percentage
    (`((RATES[tier].monthly - RATES[tier].annual) / RATES[tier].monthly) * 100`) in
    `updatePricingCalculations()` on every tier/cadence/seat change (mirroring the
    existing `#receipt-discount-pct` pattern), and hides itself entirely for the
    Developer tier (free, no annual discount to advertise).

Disclosed, not fixed:
- **Cat 3**: `.pulse-dot` infinite animation — essential live-state indicator, not
  decorative motion (re-confirmed, same reasoning as rounds 3-7).
- **Cat 7 (re-confirmed)**: `select.input-field`'s `stroke='%23475569'` data-URI literal —
  unavoidable, SVG data-URIs can't reference CSS custom properties.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (0/0 net),
extracted script parses cleanly via `node -e "new Function(...)"`.

## Convergence round 9 (grade — NOT clean, 7 findings)

Independent grader (fresh instance, did not read this file) findings:

1. **Cat 2 (regression)**: `.switch-control` off-state `rgba(ink,0.48)` was tuned/verified
   only against a pure-white background; `#switch-billing-cadence` actually sits inside
   `.billing-toggle-container` (`rgba(ink,0.04)` tint), a slightly darker composited
   background where the grader computed ~2.96:1 (below 3:1). Independently re-verified via
   a Node script using the real WCAG relative-luminance formula (not eyeballed): at 0.48
   alpha the true figures are white ~3.21:1, tinted ~3.16:1 — both technically pass, but
   with very little margin and the grader's own computation landed under 3:1, so treating
   this as real and fixing with margin rather than disputing a borderline number.
2. **Cat 3**: `.pulse-dot` infinite animation has no on-page pause/stop/hide control;
   `prefers-reduced-motion` support is a different SC's technique, not a substitute for a
   WCAG 2.2.2 on-page mechanism. Previously disclosed as "essential live-state indicator"
   across rounds 3-8, but re-flagged independently a second time — treating this as
   material rather than continuing to dispute it.
3. **Cat 4**: `validateStep(2)` adds `.has-error` to bad email fields but never calls
   `.focus()` on the first one, unlike `validateStep(1)`'s established convention.
4. **Cat 4**: `#btn-skip-step`'s click handler jumped straight to step 3 with zero call to
   `validateStep(2)`, letting a malformed (but non-empty) email ride into `state.invites`,
   the manifest roster, and the deployment "invitations broadcast" count without ever being
   validated.
5. **Cat 4**: removing a teammate row via the roster's delegated click handler left focus
   stranded on `<body>` with no redirection to an adjacent control.
6. **Cat 5**: `#subdomain-status-row`'s "Looks available" text implies a real
   backend uniqueness check; the actual logic is a pure client-side `length > 2` check with
   no verification the subdomain is actually unregistered.
7. **Cat 7 (re-confirmed)**: `select.input-field`'s data-URI `stroke='%23475569'` still
   duplicates `--muted` — unavoidable, disclosed again.

Fixes applied:

1. Bumped `.switch-control` off-state alpha from 0.48 to 0.54, re-verified via the same
   Node relative-luminance script against both real-world container backgrounds this
   component is deployed on (white ~3.86:1, tinted ~3.78:1) — now passes both with real
   margin instead of a borderline number, and the code comment was updated to document
   both backgrounds explicitly instead of only the one it was originally tuned against.
2. Added a real on-page pause/stop control instead of continuing to argue the "essential"
   exception a third time: a `⏸`/`▶` icon button (`#btn-pulse-pause`, `aria-pressed`,
   dynamic `aria-label`) appears next to the manifest status chip once deployment starts
   (`startDeploymentSequence()`), toggling a `.pulse-paused` class on `.manifest-header`
   that sets `animation-play-state: paused` on the dot via CSS.
3. `validateStep(2)` now tracks `firstInvalidInput` while looping the email fields and
   calls `.focus()` on it before returning `false`, matching `validateStep(1)`'s pattern.
4. `#btn-skip-step`'s handler now calls `validateStep(2)` and returns early if it fails,
   exactly like the "Continue" path — skip still works for the legitimate case (no
   invites entered at all, since `validateStep(2)` only blocks on non-empty-but-invalid
   emails, not empty rows).
5. The roster remove handler now records the removed row's index before removing it, then
   focuses the remove button of the row that slides into that same position (or the last
   remaining row, or `#btn-add-teammate` if the roster is now empty) after
   `refreshRosterFromDOM()` runs.
6. Reworded "Looks available" → "Valid format" (both the static markup and the JS that
   sets it dynamically) — this is the minimal-fix path per the honesty principle: the
   check genuinely only validates format/length, so the label now says exactly that
   instead of implying a real availability lookup that doesn't exist.

Disclosed, not fixed:
- **Cat 7 (re-confirmed)**: `select.input-field`'s `stroke='%23475569'` data-URI literal —
  unavoidable, SVG data-URIs can't reference CSS custom properties.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (0/0 net),
extracted script parses cleanly via `node -e "new Function(...)"`. Switch-control
contrast independently re-verified via a Node WCAG-luminance script (not eyeballed).

## Convergence round 10 (grade — NOT clean, 4 findings + 1 lower-priority)

Independent cold-read grader (fresh, no access to this file) audited the full 2835-line
file. Explicitly confirmed CLEAN this round: WCAG 1.4.3 text contrast (re-verified every
color pair including the round-9 fixes), WCAG 1.4.11 non-text/UI contrast (re-verified
`.switch-control`'s 0.54-alpha fix on both real backgrounds), WCAG 2.2.2 (confirmed the
new pulse-pause control is correctly implemented — first round to pass this category),
dead CSS custom properties, and initial-state/JS pricing-math consistency.

Findings:
1. **Cat 4 (validation bypass)**: `validateStep(1)`'s subdomain regex checked charset but
   never enforced the length ≥3 rule that the live `#subdomain-feedback-text` indicator
   displays and visually blocks on — a 1–2 character subdomain could pass the gate while
   still showing a red "invalid" state.
2. **Cat 4 (accessibility)**: `goToStep()` swaps completed step badges to an
   `aria-hidden="true"` checkmark SVG, wiping the numeral's accessible text with nothing
   replacing it — completion state was visual-only, invisible to assistive tech.
3. **Cat 4 (accessibility)**: the API-token copy button (`#btn-copy-token`) had no ARIA
   live-region announcement on success/failure, unlike the join-link copy button
   (`#copy-feedback-msg`, `role="status"`) which does the same job correctly.
4. **Cat 7 (re-confirmed, now documented)**: `select.input-field`'s hardcoded
   `stroke='%23475569'` duplicates `--muted` with no sync mechanism.
5. **Lower priority**: `goToStep()`'s 30ms `setTimeout` for post-transition focus had no
   debounce/cancellation — a narrow race window on rapid repeated navigation.

Fixes applied:
1. Added a `subVal.length < 3` check to `validateStep(1)`, matching the live-feedback
   copy exactly ("Workspace Subdomain must be at least 3 characters.").
2. `goToStep()` now sets `aria-label="Step N complete"` on the badge when swapping to the
   checkmark SVG, and removes it when reverting to the plain numeral.
3. Added a `role="status"` `.sr-only` span (`#copy-token-feedback`) next to the button,
   referenced via `aria-describedby`, and the click handler now sets/clears its text
   alongside the existing button-label swap — same pattern as the join-link copy flow.
4. Added a one-line CSS comment documenting that the data-URI's hex literal is `--muted`
   inlined and must be kept in sync by hand (data-URIs can't reference custom
   properties, so this is the honest minimal fix, not a functional one).
5. Added a module-scope `pendingStageFocusTimeout` variable; `goToStep()` now clears any
   pending timeout before scheduling a new one, closing the race window.

Verification after all fixes: `<style>`/`<script>` brace counts balanced (0/0 net),
extracted script parses cleanly via `node -e "new Function(...)"`.

Disclosed, not fixed (grader explicitly flagged these as non-material and omitted them
from its verdict, so leaving as-is per the minimal-fix philosophy):
- Hover-state border contrast (~1.5:1) on `.radio-segment-btn:hover`/`.plan-tier-card:hover`
  — supplementary embellishment only; idle-state border and label text remain legible.
- Region/seat/SSO/org facts triple-duplicated across `state`, form markup, and manifest
  markup — currently consistent because `updateLiveManifest()` unconditionally
  overwrites all three on load; fragile but not currently broken.
- Fake API token (`vkt_live_...`) and dead footer anchor links — self-disclosed prototype
  (Launch Console button alerts this is a prototype).
- Literal black box-shadows (`rgba(0,0,0,0.15)`/`0.2)`) instead of `--ink-rgb` — no
  declared token equals pure black, so not a true token-duplicate violation.

## Convergence round 11 (grade — NOT clean, 3 findings)

Categories confirmed clean this round: WCAG 2.2.2 pause/stop/hide, dead CSS custom
properties (18/18 referenced), pricing-math cross-check (RATES.pro/enterprise vs.
hardcoded initial markup consistent at default state).

Findings:
1. **WCAG 1.4.3 — `.discount-pill` fails in its actual nested context.** The pill's
   `--status-success-text` on 12%-alpha success tint clears 4.5:1 against a plain
   white/`--surface` background (4.74:1, matches the code comment's own math), but
   `.discount-pill` is deployed inside `.billing-toggle-container`, which has its own
   `rgba(--ink-rgb, 0.04)` tint. Composited on top of that tint instead of white, real
   contrast drops to ~4.40:1 — under threshold for 12px/600-weight text. The token
   comment justified the pair against one background; the component actually renders on
   a doubly-tinted one.
2. **Category 4 — stale `.has-error` state.** `.has-error` on `#input-org-name` /
   `#input-subdomain` is only added/removed inside `validateStep(1)`; the `input`
   handlers never clear it, so fixing an invalid value by typing leaves the red
   border/background showing on an already-valid field until the next full-step
   validation run. Same gap in `refreshRosterFromDOM` for roster email inputs (only
   `validateStep(2)` cleared it, not the live `input`/`change` handler).
3. **Category 4 — missing live-region wiring for subdomain feedback.** `#subdomain-
   status-row`/`#subdomain-feedback-text` update on every keystroke but had no
   `role="status"`, and `input-subdomain`'s `aria-describedby` only pointed at the
   static `#subdomain-desc` help text — screen-reader users got no announcement of
   subdomain validity changing while typing, inconsistent with `#copy-feedback-msg`/
   `#copy-token-feedback` elsewhere in the same file, which both correctly use
   `role="status"`.

Fixes applied:
1. Lowered `.discount-pill`'s background alpha from 0.12 to 0.08 (computed: ~4.62:1
   against the doubly-tinted `.billing-toggle-container` background, ~4.98:1 against
   plain white — passes both contexts with margin instead of failing one at exactly
   the boundary). Documented the reasoning inline since the alpha value now looks
   arbitrary without it.
2. Added `els.inputOrgName.classList.remove('has-error')` (guarded on non-empty value)
   to its `input` handler; added the equivalent `remove('has-error')` guarded on
   `state.subdomain.length > 2` to `#input-subdomain`'s `input` handler; added a
   regex-guarded `classList.remove('has-error')` to `refreshRosterFromDOM` for each
   roster email input.
3. Added `role="status"` to `#subdomain-status-row` and extended `input-subdomain`'s
   `aria-describedby` to `"subdomain-desc subdomain-feedback-text"` so live validity
   changes are announced alongside the static help text.

Verification: `<style>`/`<script>` brace balance both 0, script parses via
`new Function(...)`.

Disclosed, not fixed (grader-confirmed non-material):
- `.radio-segment-btn:hover`/`.plan-tier-card:hover` border contrast (~1.5:1, ~2.2:1) —
  transient hover layered on an already-3:1-compliant idle border; WCAG 1.4.11 doesn't
  require the hover treatment itself to pass.
- Enter key doesn't submit/advance the wizard (no `type="submit"` button) — keyboard
  friction, not a hard failure; flow stays fully Tab-completable.
- Hardcoded `#deployed-api-key` value — the only non-reactive field in an otherwise
  fully-reactive "deployed workspace" summary; not filed as deceptive since the flow
  self-discloses as a prototype on the Launch Console click.
- Minor UI-polish items: re-triggered transition when clicking the already-active
  nav-stepper button; ~30ms tabbable-but-invisible window during stage transition;
  roster row ARIA-label drift from "First/Second teammate email" to "Teammate N email"
  on first edit.

## Convergence round 12 (grade — NOT clean, 1 material + 1 minor finding)

**Clean categories:** WCAG 1.4.3 text contrast (every pair re-verified including doubly-tinted discount-pill at 4.617:1, dark-terminal `.log-entry.success` at 4.738:1, placeholder text at 4.543:1 — thin margin but passes), WCAG 1.4.11 non-text contrast (borders, switch fill, slider thumb via its white ring, focus rings), WCAG 2.2.2 (pulse-dot pause control present for animation's full lifetime + global `prefers-reduced-motion` kill-switch), keyboard/state-integrity (roving tabindex, synthetic-event snapshot-restore ordering, clipboard promise rejections handled), dishonesty/fake-state (prototype disclosure honest), dead CSS custom properties (all 18 used), hardcoded literals (only the documented data-URI chevron `#475569` tradeoff, already disclosed in-code).

**Findings:**
1. **Material (internal self-consistency), line 2300** — `els.manifestCadenceVal.textContent` hardcoded `'Annual (-20%)'` regardless of plan tier, while the billing-toggle discount pill and pricing receipt discount row both compute the real per-tier percentage dynamically. Invisible for Team Pro (30→24 = exactly 20%) but wrong for Enterprise (79→64 = 18.99%, shown elsewhere as "19.0%") and wrong for Developer (free tier, 0% discount, but manifest still claimed "-20%"). Reachable in two clicks (select Enterprise or Developer tier with Annual billing, the default cadence).
2. **Minor (interaction honesty), line ~1950/2733** — "Skip team invites for now" button still called `validateStep(2)`, which blocked navigation on malformed-but-typed emails — contradicting the button's own label, which implies bypassing the section entirely.
3. **Cosmetic/theoretical, lines 418-422** — placeholder text contrast passes at 4.543:1 but with almost no margin above the 4.5 WCAG minimum. Not a fail; noted for awareness only, no fix applied (real value, no rendering-time risk beyond sub-pixel AA variance).

**Fixes applied:**
- Line ~2298-2305: replaced the hardcoded `'Annual (-20%)'` literal with a per-tier computed percentage matching the same formula already used for the toggle pill and receipt row (`(RATES[tier].monthly - RATES[tier].annual) / RATES[tier].monthly * 100`), falling back to plain `'Annual'` (no percentage claim) for the Developer free tier where there is no discount to state.
- `els.btnSkip` click handler: now clears all roster email inputs' values and `has-error` state, empties `state.invites`, and clears the error banner before advancing to step 3 — genuinely skips the section rather than being gated by the same validation the primary "Continue" path uses.

**Verification:** `<style>`/`<script>` brace balance both 0; script parses via `new Function(...)`.

**Disclosed, not fixed (unchanged from round 11):** hover-state border contrast, Enter-key-doesn't-submit, hardcoded API key self-disclosed as prototype (round 12 additionally names it a "fake credential" structural tell — mild, low materiality given the adjacent prototype disclosure, not fixed), nav-stepper re-trigger flicker, 30ms tabbable-invisible window, roster ARIA-label drift, placeholder-text contrast thin margin (item 3 above).

## Convergence round 13 (grade — NOT clean, 4 material + 4 minor + 2 cosmetic findings)

**Clean categories:** WCAG 2.2.2 (unchanged, still compliant), keyboard/tab-order integrity, dead CSS custom properties, dishonesty/fake-state framing (prototype self-discloses), structural component tells (no new fake-terminal/bento/fabricated-testimonial patterns introduced).

**Findings:**
1. **Material (WCAG 1.4.3), `.btn-primary:hover`** — `background-color: rgba(var(--accent-rgb), 0.9)` composited over the white page lightens the effective color (L .1067 → .1921 when layered), dropping the white button label from 6.70:1 to 4.34:1, failing the 4.5:1 minimum for normal-size text. Independently recomputed the sRGB relative-luminance math by hand and it matched the grader's own L=.1067 value.
2. **Material (state consistency), subdomain "Valid format" indicator** — editing org name after the subdomain had already shown "Valid format" (via the auto-slug path) didn't re-run the validation/feedback update, so a manual edit to org name that changed the auto-slugged subdomain could leave a stale "Valid format" message showing for a subdomain that hadn't actually been re-validated.
3. **Material (regression introduced by round 12's own fix), `els.btnSkip` handler** — round 12 changed the Skip handler to clear `state.invites` directly instead of calling the existing `refreshRosterFromDOM()` helper, which left the "N invites queued" counter and live manifest stale after clicking Skip (counter kept showing the pre-skip count). This is a bug round 13's grader caught that round 12's own fix introduced, not a pre-existing defect — worth naming explicitly since it demonstrates the convergence loop catching its own regressions, not just legacy ones.
4. **Material (internal self-consistency), default state**  — `state.subdomain` defaulted to `'acme'` while `state.orgName` defaulted to `'Acme Corp'`; `slugify('Acme Corp')` produces `'acme-corp'`, not `'acme'`, so the form loaded with an org name and subdomain that visibly disagreed with the tool's own auto-slug logic (an attentive user retyping their own org name would see the subdomain silently change out from under an apparently-already-filled field).
5. **Minor (WCAG 1.4.11), `.step-item.is-complete .step-badge`** — fill (`rgba(var(--success-rgb), 0.12)`) and border (`rgba(var(--success-rgb), 0.25)`) both computed under 3:1 against the white page background (~1.16:1 / ~1.36:1); only mitigated by a redundant checkmark glyph + aria-label, not a real contrast pass.
6. **Minor (WCAG 1.4.11), `.pulse-pause-btn` idle border** — `1px solid var(--line)` computed ~1.23:1 against white, missed when `--border-control` was substituted for `--line` on other interactive control boundaries earlier in the file.
7. **Minor (disclosed, not fixed)** — hardcoded `#deployed-api-key` "live"-looking secret key is only disclosed as a prototype value after the fact (on Launch Console click), same finding round 12 named; still not fixed, same reasoning as round 12 (adjacent prototype disclosure keeps materiality low).
8. **Minor (disclosed, not fixed)** — a <30ms window where rapid double-navigation could theoretically race the stage transition; automation-timescale only, not reachable via normal human interaction.
9-10. **Cosmetic** — no material impact, not itemized separately for fixing.

**Fixes applied:**
- `.btn-primary:hover`: swapped `rgba(var(--accent-rgb), 0.9)` for solid `var(--accent-text)` (#1d4ed8, 6.70:1 against white) — same solid-token-over-translucent-overlay pattern used repeatedly in earlier rounds for this exact compositing pitfall.
- Extracted subdomain-feedback logic into a shared `refreshSubdomainFeedback()` function, called from both the org-name input handler's auto-slug branch and the subdomain input handler directly, so any path that changes `state.subdomain` re-validates and re-renders the feedback text/color/dot state.
- `els.btnSkip` handler: replaced the manual `state.invites = []` with a call to the existing `refreshRosterFromDOM()` helper (which also updates the queued-invites counter and live manifest), after clearing the roster inputs' values/error state.
- Default-state consistency: changed `state.subdomain` default from `'acme'` to `'acme-corp'` and the static HTML subdomain input's `placeholder`/`value` from `"acme"` to `"acme-corp"`, keeping `subdomainManuallyEdited` at its original `false` default (an earlier attempt flipped that flag to `true` instead, which would have silently disabled the live auto-slug demo behavior for all fresh sessions — rejected as over-broad once recognized, reverted before finalizing). `updateLiveManifest()` already runs once at script init and recomputes the manifest endpoint, SSO domain text, and invite-link fields from `state.subdomain`, so those derived displays self-correct with no separate edits needed. The seeded invite emails (`elena.rostova@acme.com`, `devon.chen@acme.com`) are left unchanged — they represent already-existing teammates' real email addresses, not values derived from the newly-chosen workspace subdomain.
- `.step-item.is-complete .step-badge`: changed `border-color` from `rgba(var(--success-rgb), 0.25)` to solid `var(--success)` (3.90:1 against white, comfortably clears the 3:1 non-text minimum); fill left as the translucent tint since only the boundary is the relevant graphical-object contrast per 1.4.11.
- `.pulse-pause-btn`: changed idle border from `var(--line)` to `var(--border-control)`, matching the token already used for every other interactive control boundary in the file (~5.10:1 against white).

**Verification:** `<style>`/`<script>` brace balance both 0; script parses via `new Function(...)`.

**Disclosed, not fixed (unchanged additions from round 12, plus items 7-8 above):** hover-state border contrast (pre-existing note, unrelated control), Enter-key-doesn't-submit, hardcoded API key self-disclosed as prototype, nav-stepper re-trigger flicker, 30ms tabbable-invisible window, roster ARIA-label drift, placeholder-text contrast thin margin, <30ms double-navigation race (item 8 above).

## Convergence round 14 (grade — NOT clean, 1 material + 1 minor-moderate + several cosmetic findings)

**Clean categories:** all 18 declared CSS custom properties used (no dead tokens), every text/background contrast pair independently re-verified as passing (including hover/disabled/dark-surface/doubly-tinted backgrounds), WCAG 2.2.2 (pulse-dot pause control present and correctly wired), keyboard/focus handling (radiogroup nav, stepper focus, remove-teammate refocus, debounced transitions), pricing math internally consistent across every tier/cadence/seat combination traced, no fabricated stats/testimonials, no generic-checkmark-superset pricing tiers, no fake terminal/bento/chat-bubble/browser-chrome structural tells.

**Findings:**
1. **Material (categories 4 + 8, stale state), lines 1880-1884 / 2671-2687** — seat-slider tick-row labels ("1 Seat" / "25 Seats" / "50 Seats") were static HTML never updated by the plan-tier radio-group handler, which does set `seatSlider.max = 2` for the Developer tier. Selecting Developer collapsed the slider's real range to 1-2 while the tick row kept displaying now-impossible "25 Seats" / "50 Seats" labels — a genuine displayed-value-disagrees-with-state defect.
2. **Minor-moderate (category 5, dishonesty), lines 1975-1994 / 2489-2517** — the provisioning sequence (three hardcoded `setTimeout` log lines, none reflecting real work) culminates in a fake but plausible-looking secret (`vkt_live_9f81a7b42e09c811`) presented with a working Copy button, with the only "this is a prototype" disclosure gated behind an `alert()` that only fires if the user clicks "Launch Workspace Console" afterward — a user who copies the key and never clicks that button never learns it's fabricated.
3. **Cosmetic (structural tell)** — the provisioning-log-card is a soft variant of the "fake terminal" AI tell (canned status lines, fixed timers, no real backend correlation), compounded by finding 2's undisclosed fake credential; same code addressed by finding 2's fix.
4. **Cosmetic (category 8, source-level only, not visually reachable)**, lines 1782 / 2015 / 2046 — static HTML placeholders (`acme.vektor.io`, `acme.com` ×2) disagreed with the `state.subdomain = 'acme-corp'` default established in round 13; `updateLiveManifest()` already overwrites all three at script init before first paint, so this was never visually observable, but the source itself disagreed with its own state model.
5. **Cosmetic (category 2, inverted-but-non-failing hover affordance)** — `.plan-tier-card:hover`, `.radio-segment-btn:hover`, `.btn-secondary:hover` all weaken border contrast on hover rather than strengthening it (idle already clears 3:1; hover isn't the sole means of conveying selection/focus, so not a compliance failure) — noted, not fixed, consistent with the same disclosed-not-fixed hover-contrast item from rounds 11-13.
6. **Cosmetic (category 7, self-disclosed, unfixable without JS-generated CSS)** — line 505 `<select>` chevron data-URI hardcodes `#475569` (duplicates `--muted`); already documented in-code as an unavoidable data-URI constraint since round history predates this log. Unchanged.

**Fixes applied:**
- Added `id="slider-tick-mid"` / `id="slider-tick-max"` to the two variable tick labels; registered `els.sliderTickMid` / `els.sliderTickMax`; the plan-tier `wireRadioGroup` callback now sets the mid label to `'2 Seats'` and hides the max label when `state.planTier === 'developer'`, and restores `'25 Seats'` / visible when any other tier is selected — tick row now always agrees with the slider's actual `max`.
- Added a persistent, always-visible disclosure line directly under the API token box ("This is a prototype flow — the provisioning sequence and key above are simulated, not a real deployment.") using the existing `--muted` token, so the fabrication is disclosed at the moment the fake key is shown and copyable, not gated behind a later button click.
- Static HTML placeholders at lines 1782, 2015, 2046 updated from `acme`/`acme.com` to `acme-corp`/`acme-corp.com` to match the round-13 `state.subdomain` default, closing the source-level (pre-paint) inconsistency even though it was never visually reachable.

**Not fixed (disclosed, low materiality, consistent with rounds 11-13 precedent):** inverted hover-border contrast (item 5), hardcoded chevron hex (item 6).

**Verification:** `<style>`/`<script>` brace balance both 0; script parses via `new Function(...)`.

## Convergence round 15

Independent cold-read grader (never-self), full 8-category rubric + AI-tells checklist, with independent sRGB contrast math and full click-through state tracing.

**Clean categories:** WCAG 1.4.3/1.4.11 contrast (broad independently-recomputed sample, all pass, including several the file self-justifies via inline comment, all corroborated), WCAG 2.2.2 (only continuous animation is the ~1.5s deployment spinner, well under pause-control thresholds, plus global `prefers-reduced-motion`), dishonesty/fake-state (simulated deployment sequence and fake API key both explicitly disclosed in-UI), dead CSS custom properties (all 18 `:root` tokens have ≥1 consumer), hardcoded literals (only the unavoidable, explicitly-commented SVG data-URI chevron hex), AI-tells checklist (only a disclosed/mitigated fake-terminal-adjacent structural note, not counted as a violation).

**1 material finding — same-step nav-pill self-transition flicker + involuntary focus steal.**
- `els.navStep1`'s click handler unconditionally called `goToStep(1, true)` with no check against the current step; `els.navStep2`'s guard only covered `currentStep > 2`, falling through to call `goToStep(2, false)` on itself when already on step 2; `els.navStep3`'s handler always re-validated and called `goToStep(3, false)` regardless of current step.
- When `currentStage === nextStage`, `goToStep` removed `is-visible` (dropping the stage to its base hidden/faded/offset state for one frame), then re-applied `is-visible` after a 30ms timeout — a visible flicker — and unconditionally called `.focus()` on the stage's first focusable field, yanking focus away from whatever the user currently had focus in on that same stage.
- Reachable via an entirely ordinary action: clicking the nav pill for the step already being viewed.

**1 minor finding — inert `teamSize` field.**
- "Engineering Team Size" segmented control (`state.teamSize`) was fully wired for selection (correct roving-tabindex/ARIA) but never read anywhere downstream — not in pricing, not in the manifest, not in validation.

**Fixes applied:**
- Added an `if (targetStep === state.currentStep) return;` guard at the top of each of the three nav-pill click handlers (`navStep1`/`navStep2`/`navStep3`), preventing any same-step call into `goToStep`.
- Gave `teamSize` a real downstream consequence instead of removing the control: added a "Company Size" row to the manifest aside's "Team Access Roster" section (`#manifest-team-size-val`), wired it into `updateLiveManifest()` (`state.teamSize + ' employees'`), and added `updateLiveManifest()` to the `wireRadioGroup(els.teamSizeBtns, ...)` selection callback so the manifest updates live on selection. `restoreFromSnapshot()` already re-clicks the saved team-size button, which now flows through the same callback and keeps the manifest in sync after a reload.

**Verification:** style brace balance 0, script brace balance 0, script parses via `new Function()`.

**Disclosed-not-fixed (unchanged from round 14, still low-materiality, consistent with rounds 11-14 precedent):** the inverted hover-border contrast nuance and the hardcoded SVG chevron hex (the latter is unavoidable in a data URI and is explicitly comment-flagged in the source).

Round 16's independent grader dispatched next to seek a second consecutive clean round for convergence per SKILL.md §5.5.

## Convergence round 16 — first clean pass

Independent cold-read grader (never-self), full 8-category rubric + AI-tells checklist, with independent sRGB contrast recomputation and full state-space tracing.

**No material findings in any category.** All 8 categories clean, including the two categories most prone to regressions across this file's history (1.4.3/1.4.11 contrast — independently recomputed every text/UI pair, including the translucent-over-tint cases previously fixed in rounds 12-13; interaction/state-integrity — walked re-click-active-nav, roving-tabindex, save/restore round-trip, seat-clamp/unclamp, all held up including the round-15 nav self-click fix).

**Minor/cosmetic notes only (not acted on — genuinely low materiality, no fix applied this round):**
- Switching plan tier to Developer (clamps seats to 2) then back to Pro/Enterprise does not restore the pre-clamp seat count. Plausible intentional product behavior, not a correctness bug — no false/stale data is displayed at any point.
- "Copy Link" (share-invite) and "Copy" (API token) use slightly different visual feedback micro-patterns (status line vs. label swap to "Copied!"). Cosmetic inconsistency, not a functional defect.
- Two `box-shadow` literals (slider-thumb shadows) use plain `rgba(0,0,0,...)` instead of `rgba(var(--ink-rgb),...)` — stylistic nit, not a duplicated-token violation (black ≠ ink).
- Placeholder text contrast (~4.545:1) passes 4.5:1 with near-zero margin — flagged only as a rendering-variance risk, not a failure as authored.
- Select-arrow SVG data-URI hex (line 505) duplicating `--muted` — already justified/disclosed via adjacent comment (data URIs can't reference custom properties), same item logged in prior rounds.

This is convergence round 16 of 1 required clean pass; SKILL.md §5.5 requires **two consecutive clean rounds** before declaring convergence. Round 17's independent grader dispatched next to seek the second.

## Convergence round 17 — second consecutive clean pass — CONVERGED

Independent cold-read grader (never-self), full 8-category rubric + AI-tells checklist, with independent sRGB contrast recomputation and full state-space tracing.

**No material or minor findings in any category.** All 8 categories clean under adversarial re-verification, including every composited-rgba 1.4.11 case explicitly re-checked for false passes, the round-15 nav self-click fix confirmed still holding (no flicker on re-click), the round-14 fake-key disclosure and round-16-flagged seat-count/copy-feedback items reviewed with nothing new surfaced, and the full pricing/manifest state-consistency trace repeated end-to-end with no divergence found.

**Cosmetic-only notes (unchanged from round 16, not acted on):**
- Placeholder text contrast (~4.544:1) passes 4.5:1 with near-zero margin.
- Data-URI select-chevron hex duplicating `--muted` — disclosed/unavoidable, same item logged since round 13.

**Convergence achieved: rounds 16 and 17 are two consecutive clean passes per SKILL.md §5.5.** `06-product-onboarding` is DONE at 17 total convergence rounds (13-17 completed and logged this window; 1-12 logged in earlier windows). Proceeding to the next benchmark artifact in `outputs_v4_validation/`.
