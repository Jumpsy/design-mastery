# Locally installed UI libraries (this machine)

Real inventory, found by scanning `node_modules` across `~/projects/` and
`~/agent-workspace/` on 2026-09-19 — not a wishlist, not the frozen 42-repo clone list a
prior stray paste suggested. Use these when a task's target stack already matches one of
these projects, or when the user asks to build with "shadcn," "Radix," or "Tailwind"
without specifying version — check here first instead of guessing a version.

| Library | Version(s) found | Where | Role |
|---|---|---|---|
| Tailwind CSS | 4.3.2 (jumpnote) | jumpnote, lumen-shell, jumpstudy-ai, .local-excalidraw, tzura | Utility-class styling — the dominant styling approach across this machine's projects. |
| Radix UI (primitives) | unversioned scoped packages, current as of install | jumpnote (`react-accordion`, `react-dialog`, `react-dropdown-menu`, `react-popover`, `react-select`, `react-tabs`, `react-progress`, `react-menu`, `react-label`, `react-collapsible`, + shared internals), `.local-excalidraw` (`react-popover` + shared internals) | Unstyled, accessible interaction primitives — jumpnote uses the broader set (menus/tabs/accordion/dialog), excalidraw only needs popover. |
| shadcn/ui | 0.9.5 | jumpnote | Copy-in component layer built on Radix + Tailwind — confirms jumpnote follows the shadcn pattern (owns its component source, not an npm-black-box dependency). |
| lucide-react | 1.47.0 (lumen-shell), 1.31.0 (.local-excalidraw, tzura) | lumen-shell, .local-excalidraw, tzura | Icon set — matches the icon-corpus guidance in `github-design-corpus-analysis.md` (Lucide is one of the 8 corpora already analyzed there). |
| tailwind-merge | present | jumpnote, .local-excalidraw, tzura | Utility for resolving conflicting Tailwind classes — near-universal companion to Tailwind, not a design signal on its own. |

## What this tells you

- This machine's real projects converge on **Tailwind + Radix primitives + shadcn/ui +
  lucide-react** as the default React stack — not Chakra, MUI, Ant Design, Mantine, or
  any of the ~40 other component libraries from the earlier stray GitHub-clone list
  (those were never actually installed anywhere on this machine; don't treat that old
  pasted list as this machine's real stack).
- When building a React component for one of these projects, match its actual installed
  set rather than introducing a new UI library — check the project's own
  `package.json`/`node_modules` first, this file is a fast index, not a substitute for
  that check if the project may have changed since 2026-09-19.
- shadcn/ui's pattern (generate/copy component source into the repo, style with Tailwind,
  wire behavior through Radix) is the concrete architecture `human-centric-frontend`'s
  "define a token system, don't hardcode" guidance should target by default on this
  machine's projects — it's what's already there, not a hypothetical.
