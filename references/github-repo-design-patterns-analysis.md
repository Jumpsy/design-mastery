# GitHub website corpus: full-manifest metadata + expanded design-pattern sample

## What was and wasn't analyzed (read this before anything else)

Two genuinely different things happened here, at two genuinely different depths, and
they must not be conflated:

1. **Track A — full-manifest metadata analysis (all 14,425 repos).** This is a pure
   aggregate-statistics pass over the existing `github-website-corpus-manifest.csv`,
   computed directly with a Python script (no eyeballing, no sampling) — language, license,
   star, and creation-year distributions across every single row. Nothing was cloned for
   this track. The `license_spdx_api` field in particular is **unverified GitHub API
   metadata** for essentially all of these rows (GitHub's own license-detection heuristic,
   which can be wrong, "unknown," or "NOASSERTION" when no machine-readable LICENSE file
   was found) — it is a signal, not a legal determination, except for the small hand-verified
   samples noted below.

2. **Track B — deep design-pattern inspection of a 228-repo stratified sample**, newly
   added in this round on top of the 44 repos already covered in
   `github-website-corpus-analysis.md`. This is **228 out of 14,425** — a 1.6% sample,
   stratified across language, star tier, and creation year specifically to reduce
   survivorship bias (not just top-starred repos). It is a real, source-grounded sample,
   large enough to report percentages with some confidence, but it is **not** "all the
   repos" and none of its findings should be read as claims about the full 14,425.
   Combined with the prior round's 44, **272 total repos have now been cloned and
   design-inspected across both rounds** of this project.

Every clone in Track B was shallow (`git clone --depth 1`), inspected with grep/find-based
heuristics (not a manual read of every file — see methodology below), and **deleted
immediately after inspection**; no repo source remains in this skill's `references/`
directory, only this aggregate-count markdown and the manifest CSV.

---

## Track A: full-manifest statistics (14,425/14,425 repos, 100% coverage)

Computed with a one-off Python/csv script reading `github-website-corpus-manifest.csv`
directly — every row counted, no sampling.

### Language distribution (API-reported primary language, top languages)

| Language | Count | % of 14,425 |
|---|---|---|
| HTML | 3,458 | 23.97% |
| JavaScript | 2,666 | 18.48% |
| PHP | 2,274 | 15.76% |
| CSS | 2,161 | 14.98% |
| TypeScript | 1,155 | 8.01% |
| SCSS | 691 | 4.79% |
| (none reported) | 575 | 3.99% |
| Vue | 343 | 2.38% |
| Astro | 141 | 0.98% |
| Python | 131 | 0.91% |
| Shell | 84 | 0.58% |
| Ruby | 71 | 0.49% |
| Svelte | 66 | 0.46% |
| MDX | 60 | 0.42% |
| Nunjucks | 53 | 0.37% |
| Go | 49 | 0.34% |

80 distinct language values appear across the manifest; the long tail below Go includes
Dart, Pug, Jupyter Notebook, Java, HCL, EJS, Handlebars, Stylus, Sass, Dockerfile, TeX,
Rust, Blade, Liquid, and more, each under 0.25%. PHP's 15.76% share is notably higher than
its representation in the 44+228-repo deep sample (see Track B) — WordPress-theme-style
queries in the manifest's search strategy pull in a large PHP-primary population that the
Track B stratification deliberately capped rather than proportionally represented.

### License distribution (`license_spdx_api` field — unverified API metadata, all 14,425 rows)

| License (API-reported) | Count | % of 14,425 |
|---|---|---|
| MIT | 4,558 | 31.60% |
| unknown | 3,920 | 27.18% |
| (none/blank) | 3,091 | 21.43% |
| GPL-3.0 | 874 | 6.06% |
| GPL-2.0 | 605 | 4.19% |
| NOASSERTION | 574 | 3.98% |
| Apache-2.0 | 327 | 2.27% |
| AGPL-3.0 | 72 | 0.50% |
| 0BSD | 71 | 0.49% |
| CC0-1.0 | 64 | 0.44% |
| Unlicense | 60 | 0.42% |
| CC-BY-4.0 | 34 | 0.24% |
| BSD-3-Clause | 33 | 0.23% |

30 distinct license values total. **Important caveat, repeated from the prior analysis
file**: "unknown" + "(none/blank)" together account for 48.6% of the manifest — nearly
half of all rows have no machine-readable license GitHub could detect, which is common
for small personal-site forks. This is API metadata only; only 44 (round 1) + a subset
of round-2 licenses noted below were ever hand-verified by reading an actual LICENSE file.

### Stars distribution (all 14,425 rows)

| Bucket | Count | % |
|---|---|---|
| 0–10 | 9,967 | 69.10% |
| 10–100 | 3,226 | 22.36% |
| 100–1,000 | 1,023 | 7.09% |
| 1,000+ | 209 | 1.45% |

Max stars: 24,253. Long-tailed as expected for a topic-search corpus — the overwhelming
majority (69%) are small/low-visibility repos (personal forks, one-off variants), and only
1.45% are "famous" (1,000+ star) projects.

### Creation-year distribution (`created_at`, all 14,425 rows, capped at <2024-01-01 by manifest design)

| Year | Count |
|---|---|
| 2009 | 1 |
| 2010 | 7 |
| 2011 | 19 |
| 2012 | 52 |
| 2013 | 89 |
| 2014 | 192 |
| 2015 | 322 |
| 2016 | 572 |
| 2017 | 1,265 |
| 2018 | 1,345 |
| 2019 | 1,487 |
| 2020 | 2,075 |
| 2021 | 2,196 |
| 2022 | 2,417 |
| 2023 | 2,386 |

Repo creation is heavily weighted toward 2017–2023 (78% of the manifest), consistent with
GitHub's own overall growth curve and the rise of static-site generators / JAMstack
templates as a popular open-source category in that window. This creation-year skew is
the reason Track B's dark-mode finding (below) reads as a generational split rather than
noise — the sample is naturally dense in exactly the years where that convention emerged.

---

## Track B: expanded deep-inspection sample — 228 repos (new this round)

### Methodology

- Selection: stratified from the manifest by language bucket (HTML, JavaScript, PHP, CSS,
  TypeScript, SCSS, Vue, Astro, Svelte, Python), with **per-language star-tier quotas**
  (top/1000+, high/100-1000, mid/10-100, low/0-10) deliberately weighted toward mid/low
  tiers so the sample isn't just famous repos — final tier mix: 32 top, 54 high, 72 mid,
  70 low (of 228). Creation years span 2011–2023 (density matches the manifest's own
  2017–2023 skew).
- Every repo was shallow-cloned (`git clone --depth 1`) into a scratch directory,
  inspected with grep/find heuristics (file-extension presence, config-file presence,
  and text-pattern matches — not a manual line-by-line read), the flags recorded, and the
  clone **deleted immediately** before moving to the next repo. All 228 clone attempts
  succeeded (0 failures) after fixing an initial tooling issue (macOS's `bash` lacks a
  `timeout` binary; a manual poll/kill loop was substituted).
- This is heuristic pattern-matching, not a full manual design audit of every repo —
  e.g. "has Tailwind" means `tailwind.config.*` was found at the repo root, "has dark
  mode" means `prefers-color-scheme` or `data-theme` appeared in some source file, etc.
  Real counts, but a shallower read than the 44-repo round's manual analysis.
- Combined with the 44 repos from the prior round (which *were* read manually, including
  every LICENSE file), **272 total repos** have now been cloned and inspected across the
  project's two rounds — still 1.9% of the 14,425-repo manifest, reported honestly as a
  sample, not a census.

### CSS methodology (228 repos, multi-label — most repos exhibit more than one)

| Pattern | Count | % of 228 |
|---|---|---|
| Plain `.css` files present | 154 | 67.5% |
| CSS custom properties (`--var:`) present | 133 | 58.3% |
| SCSS/Sass files present | 82 | 36.0% |
| Bootstrap reference in `package.json`/manifest | 29 | 12.7% |
| Tailwind (`tailwind.config.*` at root) | 37 | 16.2% |
| CSS-in-JS (styled-components/Emotion reference) | 19 | 8.3% |
| LESS files present | 9 | 3.9% |

Tailwind adoption is heavily concentrated in the newer JS-framework cohort: TypeScript
repos hit 12/25 (48%) Tailwind and Astro 7/15 (47%), Svelte 6/10 (60%), while PHP (0/25)
and SCSS-primary repos (0/20) show zero Tailwind hits — confirming the prior round's
finding that utility-first CSS adoption tracks framework generation, not "website
template" category, now on a 5x larger sample. SCSS remains concentrated in
CSS-primary/SCSS-primary and JavaScript repos (SCSS: 20/20 in the SCSS-labeled bucket by
definition; 14/35 = 40% in JavaScript; 12/45 = 27% in HTML-primary), consistent with the
Jekyll/Hugo `_sass/` convention identified in the 44-repo round.

### Typography

| Pattern | Count | % of 228 |
|---|---|---|
| Google Fonts reference (`fonts.googleapis.com`) | 84 | 36.8% |
| `@font-face` (self-hosted/custom webfonts) | 78 | 34.2% |
| System-font stack (`system-ui`/`-apple-system`) | 66 | 28.9% |

These aren't mutually exclusive (a repo can offer a Google Fonts link as one theme option
and a system-font fallback elsewhere), but the three-way near-even split (37%/34%/29%) is
itself a finding: there is no single dominant typography strategy across this broad a
sample the way there was a dominant SSG choice in the narrower 44-repo round — webfonts
(Google-hosted or self-hosted) collectively outnumber pure system-font stacks roughly
2:1, but neither approach is closer to universal than the other 60%+ combined.

### Color/theming

| Pattern | Count | % of 228 |
|---|---|---|
| CSS custom properties present | 133 | 58.3% |
| Dark-mode marker (`prefers-color-scheme` or `data-theme`) | 48 | 21.1% |

By creation year, dark-mode presence: repos created 2022–2023 hit 31/79 (39%) vs. repos
created before 2020 at 7/68 (10%) — reproducing the 44-repo round's "generational split"
finding on a much larger base, with real numbers behind it this time rather than an
impression from a 44-repo sample.

### Layout

| Pattern | Count | % of 228 |
|---|---|---|
| `display: flex` present | 117 | 51.3% |
| `display: grid` present | 48 | 21.1% |

Flexbox usage is more than double grid usage in this sample — grid tends to appear
specifically in repos with more deliberate page-level layout systems (dashboards,
multi-column marketing pages), while flex is near-ubiquitous for smaller-scale
component-level alignment (nav bars, button groups, card rows) even in repos that also
use grid for their outer layout, which is why flex's count is higher rather than the two
being complementary halves of the sample.

### Component/folder structure

| Pattern | Count | % of 228 |
|---|---|---|
| Top-level or shallow `components/` directory | 102 | 44.7% |
| Top-level `src/` directory | 92 | 40.4% |

Consistent with the framework distribution of the sample (TypeScript/Vue/Astro/Svelte
together are ~48% of the 228) — the `src/`+`components/` convention tracks modern
JS-framework adoption, same underlying pattern the 44-repo round found for the
Astro/Next/SvelteKit cohort specifically, now visible at the aggregate level too.

### Accessibility markers (rough presence/absence, not an audit)

| Pattern | Count | % of 228 |
|---|---|---|
| Semantic landmark tags (`<main>`/`<nav>`/`<header>`) | 137 | 60.1% |
| `alt=` attribute present anywhere | 127 | 55.7% |
| `aria-*` attribute present anywhere | 88 | 38.6% |

Read honestly: "has at least one `alt=` somewhere in the codebase" is a very low bar —
this is presence, not coverage (a repo with one `alt=""` on a logo and zero alt text on
20 content images still counts as a "hit" here). The ordering itself is informative
though: semantic HTML (60%) > alt attributes (56%) > ARIA attributes (39%) is exactly the
expected accessibility maturity curve — semantic tags are close to a free default in any
modern template scaffold, alt text is the next-easiest habit, and explicit ARIA
annotation (which requires deliberate authoring, not just using the right tag) lags
furthest behind.

### License spot-check within the 228 (API field, not independently re-verified for most)

MIT 115 (50.4%), unknown 51 (22.4%), blank 20 (8.8%), GPL-3.0 17 (7.5%), Apache-2.0 8
(3.5%), NOASSERTION 4, CC0-1.0 4, GPL-2.0 3, Unlicense 2, CC-BY-4.0 2, LGPL-3.0 1, WTFPL
1. This 228-repo slice skews more MIT-heavy (50.4%) than the full manifest (31.6%)
because the underlying language-stratified sampling pulled disproportionately from
JS/TS/Astro/Svelte buckets, which the manifest-wide data (Track A) shows lean more
permissively-licensed than the PHP-heavy WordPress-theme population. These 228 licenses
were **not** individually re-verified by reading LICENSE files (unlike the 44 in the
prior round) — this is the API field only, reported as a signal consistent with the rest
of Track B's heuristic (not manual-read) methodology.

---

## Bottom line

Track A gives 100%-coverage, computed-not-eyeballed statistics on language, license,
stars, and creation year across the actual 14,425-repo manifest, with an explicit flag
that the license field is unverified API metadata for the overwhelming majority of rows.
Track B adds 228 newly cloned-and-heuristically-inspected repos (0 clone failures, all
deleted after inspection) to the project's existing 44-repo hand-analyzed sample, bringing
the two-round total to 272 repos genuinely design-inspected — a real, stratified,
star-tier-diversified, multi-year sample that surfaces reproducible findings (CSS-approach
tracks framework generation not template category, dark mode as a 2022+ generational
default, flex-over-grid at component scale, an accessibility-maturity ordering of semantic
HTML > alt text > ARIA) each backed by an actual count out of 228, not a vibe. 272 out of
14,425 (1.9%) is not "all the repos," and no claim in either track should be read as
covering the full manifest at design-inspection depth — only Track A's four metadata
fields have that coverage, and even those are reported with their real caveats.
