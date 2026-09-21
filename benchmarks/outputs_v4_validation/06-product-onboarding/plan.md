# Plan Gate: Benchmark 06 — B2B SaaS Multi-Step Onboarding Flow

## 1. Product Context & Overview
- **Product**: **Vektor Cloud** — an enterprise telemetry, observability, and workflow orchestration platform for high-velocity software engineering teams.
- **Goal**: Guide a new organization lead from sign-up to a fully configured, collaborative workspace ready for workload ingestion in 3 distinct, high-signal steps.
- **Audience**: Staff engineers, VP of Engineering, and Platform Team Leads evaluating and deploying enterprise infrastructure.
- **Tone**: Focused, authoritative, engineering-grade, calm, and responsive. Zero marketing fluff; pure task velocity and clarity.

---

## 2. Layout Structure
- **Overall Shell**: A structured application frame with:
  1. **Top Navigation Landmark (`<header>`)**: Minimal brand logo, workspace breadcrumb, active step badge (`Step X of 3`), and a live "Save & Exit" link that confirms drafts are cached locally.
  2. **Step Tracker (`<nav>`)**: A top progressive stepper with three connected segments:
     - `1. Workspace Details`
     - `2. Team Access & Roles`
     - `3. Infrastructure & Plan`
     Featuring completed checkmarks, current active step indicator, and forward step states with clear accessible labeling (`aria-current="step"`).
  3. **Main Workspace Split (`<main>` + `<aside>`)**:
     - **Active Step Container (`<section>` within `<form>`)**: Left/primary panel (60% width on desktop) housing the active step form controls with strict single-column vertical rhythm.
     - **Live Workspace Manifest (`<aside>`)**: Right auxiliary panel (40% width on desktop) acting as a live-reactive, read-only configuration manifest. As the user types their organization name, selects their cloud region, adds teammates with roles, and adjusts their seat tier/slider, this telemetry card reflects their live provisioned state in real time.
  4. **Action Footer Bar (`<footer>`)**: Persistent bottom actions with primary "Continue / Next" on the right, secondary "Back" on the left, and optional "Skip" where appropriate.
  5. **Completion State**: A dedicated provisioning celebration modal / deployment state with simulated infrastructure spinning up (DNS, IAM policies, environment keys) and a direct entry point into the workspace dashboard.

---

## 3. The 3 Screens / Steps in Detail
1. **Screen 1: Organization & Work Details**
   - **Form Fields**:
     - Organization Name (`<input id="org-name">`, required, with auto-generation of avatar token and subdomain slug).
     - Workspace Subdomain (`<div class="slug-input">` with live validation, status badge "Available", prefix `https://`, suffix `.vektor.io`).
     - Primary Workload Region (`<select>` or custom segmented radio selector: `US-East (N. Virginia)`, `EU-Central (Frankfurt)`, `AP-Southeast (Tokyo)`).
     - Organization Size (Segmented radio group: `1–10 engineers`, `11–50 engineers`, `51–250 engineers`, `250+ enterprise`).
   - **Interactive Validation**: Required field checking, slug regex validation, error helper text, auto-focus management.

2. **Screen 2: Team Roster & Role Permissions**
   - **Form Fields**:
     - Dynamic Teammate Invites list: each row has an Email input, Role selector (`Admin`, `Member`, `Observer/Read-only`), and Remove button.
     - "Add Teammate" action (`<button type="button">`) that inserts a new row dynamically.
     - Quick Team Invite Link generator with one-click "Copy Link" feedback.
     - Domain Auto-join toggle (`role="switch"`, `aria-checked`): "Allow anyone with @yourdomain to automatically request workspace access".
   - **Interactive Validation**: Valid email formatting, duplicate email detection, graceful zero-invite empty state ("Skip this step" affordance).

3. **Screen 3: Infrastructure Tier & Launch**
   - **Form Fields**:
     - Tier Selector cards: `Developer` (Free / $0), `Team Pro` ($24/seat/mo), `Enterprise Scale` (Custom).
     - Billing Cadence Switch (`role="switch"`): Monthly vs. Annual (with "Save 20%" badge).
     - Continuous Quantity Seat Estimator: Real `<input type="range">` slider from 1 to 50 seats with exact live mathematical total readout (`Seats × Base Price × Annual Discount`), satisfying §2.5 Continuous-Quantity requirement!
     - Initial Environment Checkboxes: `Production` (default locked), `Staging` (checked), `Local/Preview` (checked).
   - **Launch Action**: "Deploy Workspace" CTA that triggers deployment sequence with real state change into the final active workspace view.

---

## 4. One Signature Motif
- **The Live Workspace Manifest**: Rather than standard disconnected wizard cards, the right-hand container functions as an architectural blueprint / deployment manifest that reactively updates on every keystroke and selection:
  - Generates a custom SVG geometric workspace monogram from the organization initials.
  - Formats the full verified URL endpoint `https://[slug].vektor.io`.
  - Dynamically lists invited members with color-coded role tags.
  - Dynamically displays the live cost model ($0/mo or $X/mo) with active seat count from the slider.
  - Shows deployment region latency ping indicator.
  This gives the user an immediate sense of building real production infrastructure as they complete each step.

---

## 5. Palette, Typography, and Spacing Direction
- **Typography System**:
  - Modular Scale (1.25x ratio): 12.8px (caption/meta), 16px (body/inputs), 20px (card headers/subheads), 25px (step titles), 31.25px (single primary H1).
  - Primary Font: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`.
  - Monospace Font: `'JetBrains Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace` for slugs, domains, telemetry, and calculations.
  - Strict Heading Order: Exactly one `<h1>` (e.g. `Vektor Workspace Setup`), `<h2>` for each active step title, `<h3>` for sub-sections. No heading level gaps.
- **Disciplined Palette (6 core tokens)**:
  - Canvas / Background: `#f8fafc` (neutral slate-50)
  - Surface / Panels: `#ffffff` (pure white)
  - Ink / Primary Text: `#0f172a` (slate-900, AA/AAA contrast >= 14:1)
  - Muted / Secondary Text: `#475569` (slate-600, WCAG AAA contrast 7.0:1 on white)
  - Line / Border: `#e2e8f0` (slate-200)
  - Accent / Primary CTA: `#2563eb` (electric royal blue, 4.6:1 contrast on white; white text on blue passes WCAG AA at 4.56:1)
  - Success / Live: `#059669` (emerald-600)
- **Strict 4px/8px Spacing Grid**:
  - All margins, paddings, and gaps are multiples of 4px: 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px.
  - Zero ad-hoc values (no 13px, 17px, 23px).

---

## 6. Motion & Transitions Specification (per Motion Notes)
- **Step Transitions**:
  - Forward transition: Current step slides out left (-16px) and fades out (180ms ease-in), Next step slides in from right (+16px) and fades in (280ms cubic-bezier(0.16, 1, 0.3, 1)).
  - Backward transition: Reverse direction (slides from left to right) so spatial orientation is preserved.
  - Duration: 260ms total.
- **Interactive Feedback**:
  - Button hover/active: 100ms ease.
  - Slider scrub: instant reactive calculation (0ms latency).
  - Progress bar width: 280ms ease-out.
- **Accessibility / Reduced Motion**:
  - `@media (prefers-reduced-motion: reduce)` completely disables transform slides and reduces transitions to instant state swaps.

---

## 7. Anti-Slop & Gate Checklist Pass (§3 & §5.5)
- [x] **No Card Soup**: The form is an open, unified single-surface workspace; steps transition cleanly without nested Russian-doll cards.
- [x] **No Generic Marketing Hero**: This is an authentic in-app onboarding setup flow, not a landing page with hero text and abstract illustrations.
- [x] **No Gratuitous Gradients or Glassmorphism**: Clean opaque surfaces with 1px border lines and calibrated ambient elevation.
- [x] **No Over-animation**: Staggered motion limited to the step change and progress bar.
- [x] **No Pill Overuse**: Pills reserved solely for semantic role tags (`Admin`, `Member`) and plan badges.
- [x] **Continuous Controls Satisfied**: Step 3 features a working continuous seat allocation range slider (`role="slider"`) and a live toggle switch (`role="switch"`).
- [x] **Form State Persistence**: Full back-and-forth navigation retains all input values across all steps.
- [x] **Real Accessibility**: Native `<button>`, `<input>`, `<select>`, `<label for="...">`, ARIA live region for validation status, keyboard navigable, 44px+ touch targets.

## 8. Gate Question Check
- **"Will the user say wow?"**: Yes — the tactile, reactive workspace manifest on the right updates instantaneously with every keystroke, seat slider scrub, and team member addition, feeling like a high-end enterprise tool on par with Stripe, Vercel, and Linear.
- **"Would this read as vibe-coded?"**: No — it is grounded in real B2B engineering constraints, genuine enterprise copy, actual validation logic, and authentic product workflows.
- **Verdict**: **PASSED. Proceed to implementation.**
