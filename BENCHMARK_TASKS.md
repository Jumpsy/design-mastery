# Benchmark Tasks — for the next goal

25 frozen test prompts for evaluating `design-mastery` after V1. **These are not to be run
or optimized against during V1.** They exist so the next goal has a fixed, non-cherry-picked
evaluation set that was written before any attempt was scored against it.

Distinct from `references/benchmark-fixtures.json`, which re-verifies the 10 existing demo
builds still render correctly. These 25 are new, unbuilt prompts — a forward test, not a
regression check.

## Web / landing pages
1. Design a landing page hero for a developer-focused API product ("ship webhooks in
   minutes") — no purple-gradient-hero default.
2. Recreate a competitor's pricing page layout from a provided screenshot, matching type
   scale and spacing within a few px.
3. Design a waitlist landing page for a consumer AI voice app, using the "serif + italic
   accent word" hero formula as one option to consider (not mandatory).

## Product UI
4. Design a settings panel with 5 toggle groups and a danger-zone delete-account section.
5. Design an empty state for a project-management app's "no tasks yet" board column.
6. Design a multi-step onboarding flow (3 screens) for a B2B SaaS signup.

## Dashboards
7. Design an analytics dashboard for e-commerce: revenue, orders, conversion rate, top
   products table.
8. Design a system-status/uptime monitoring dashboard with incident timeline.
9. Design a personal finance dashboard: spending by category, monthly trend line, budget
   progress bars.

## Mobile UI
10. Design a mobile onboarding permission-request screen (notifications + location).
11. Design a mobile checkout flow screen with saved payment method and order summary.
12. Design a mobile app's dark-mode settings screen, 390x844 frame.

## Branding
13. Design a one-page brand guidelines sheet for a fictional boutique fitness studio.
14. Design a brand color/type system for a children's educational app (playful but not
    juvenile).
15. Design a rebrand direction (palette + type pairing only, no full build) for a legacy
    enterprise software company modernizing its identity.

## Logos
16. Design a wordmark logo for a specialty coffee roaster (should differ from the existing
    "Fieldnote" demo mark).
17. Design a monogram/lettermark logo for a two-person design studio.
18. Design an icon-based app logo for a meditation/sleep app.

## Editorial / posters
19. Design a magazine cover for a technology quarterly, feature story on AI and labor.
20. Design a concert poster for an indie band's album release show.
21. Design an editorial spread (2-page layout description) for a long-form essay on urban
    design.

## Packaging
22. Design product packaging for a skincare serum, minimalist pharmacy-adjacent aesthetic.
23. Design a shipping box interior/unboxing insert for a direct-to-consumer electronics
    product.

## Presentations
24. Design a 3-slide investor pitch sequence: problem, solution, traction (data-forward,
    no default PowerPoint gradients or clip art).

## Marketing creative
25. Design a 1080x1350 Instagram carousel first-slide for a SaaS product's feature launch
    announcement.

## Usage notes for the next goal

- Run each prompt once, unmodified, against the frozen skill at the commit this file was
  introduced in.
- Score against SKILL.md §2 (anti-slop checklist) and the matching category file's
  criteria — do not invent new pass criteria after seeing results.
- These prompts intentionally span difficulty (some single-artifact, some multi-screen) and
  intentionally avoid re-using the exact "Fieldnote" brand or the 10 existing demo briefs,
  so results reflect generalization, not memorized outputs.
