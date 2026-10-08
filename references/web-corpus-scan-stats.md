# Web corpus scan: lightweight homepage meta-tag statistics

This is a coarse, automated companion to the 86 hand-verified deep teardowns in
`references/design-md/`. It does **not** reach anywhere near 10,000 sites, and
it does not replace the deep teardowns — treat every number below as a rough
statistical signal from public `<head>` metadata, not a design audit.

## Method (exactly what was run, no more)

- 346 real, recognizable company/product domains (`webscan/domains.txt`),
  drawn from names already referenced elsewhere in this skill plus a modest,
  non-invented expansion across SaaS, dev tooling, e-commerce, AI labs, and
  consumer apps.
- One plain `GET https://<domain>` per domain, stdlib `urllib`, no JS
  execution, no crawling past the homepage, no retries on failure.
- Descriptive `User-Agent`, 7s timeout, ~0.4s delay between requests,
  sequential (not concurrent) — respectful single-pass scan, not a stress test.
- Extracted only what's present in the raw HTML `<head>`: `theme-color` meta,
  `viewport` meta, `og:*` meta tags, linked Google Fonts `family=` params,
  and inline `--color-*`/`--font-*` CSS custom properties if present in
  `<style>` blocks in the fetched HTML.
- Raw response bodies were discarded after extraction; only the compact
  extracted JSON (`webscan/results.jsonl`, not shipped in the skill) and this
  summary remain.

## Yield — reported bluntly

- **346 attempted, 260 returned 200 (75.1% hit rate), 86 failed.**
- Failure breakdown: 48 HTTP 403 (bot/WAF blocking a plain script UA — expected
  for many large consumer sites), 15 HTTP 308 (redirect chains not followed),
  9 timeouts, 6 other, 4 HTTP 429 (rate-limited), 4 TLS errors.
- Of the 260 successful fetches, **usable design-token data was sparse**:
  - `theme-color` meta: 68/260 (26.2%)
  - `viewport` meta: 219/260 (84.2%) — near-universal, as expected
  - `og:*` social meta: 210/260 (80.8%) — near-universal
  - Linked Google Fonts stylesheet: only 24/260 (9.2%) — most modern sites
    self-host fonts or use system fonts, so this signal is weak
  - Inline CSS custom properties visible in raw HTML: 52/260 (20.0%) — most
    production sites ship compiled/hashed CSS in external files, invisible to
    a plain-HTML GET (this is the same limitation that made WebFetch unusable
    for the deep teardowns; a static-HTML scan hits the same wall, just for a
    different reason — no external CSS fetching in this script).

**Bottom line: only about 1 in 4 attempted domains yielded a theme-color, and
under 1 in 10 yielded a Google Fonts link.** This scan is a weak, noisy signal
on its own — its main value is the aggregate pattern below, not any single
site's row.

## What the aggregate actually shows

- Most common explicit `theme-color` values: `#ffffff`/`#fff` (25 sites) and
  `#000000` (6 sites) dominate — i.e. when sites bother to set this meta tag
  at all, they overwhelmingly pin the browser chrome to pure black or white
  rather than a brand color. This matches the "high-contrast neutral chrome"
  convention already documented from the deep teardowns.
- Among the (small) set of sites using a linked Google Fonts stylesheet,
  **Inter** and international CJK support fonts (Noto Sans SC/KR) were the
  most repeated, plus **JetBrains Mono** for monospace/dev-tool contexts —
  consistent with Inter's dominance already noted elsewhere in this skill.
- `viewport` and Open Graph meta are close to universal (84%/81%) — this is
  baseline SEO/social-share hygiene, not a design signal, included here only
  for completeness.

## Explicit non-claims

- This is not 10,000 sites. It is 346 attempted, 260 fetched, and a much
  smaller usable-signal subset within those.
- This does not add new entries to `references/design-md/` (those remain the
  86 hand-verified, live-DOM `getComputedStyle()` teardowns — a fundamentally
  different, deeper method than a static-HTML GET).
- Font/color counts above are raw tallies over a non-random, name-recognition-biased
  domain list — not a statistically representative sample of "the web."
- Combined with the 86 deep teardowns and the 41,000+ licensed icon corpus,
  the total analyzed surface across this skill's references is still an order
  of magnitude below a literal 10,000-full-website target, and no further
  scan at this scope will honestly reach it without either abusive-scale
  crawling (out of scope) or a licensed third-party dataset (not located).
