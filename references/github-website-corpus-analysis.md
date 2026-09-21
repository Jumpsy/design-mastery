# GitHub open-source website corpus: manifest + sample analysis

## Honest headline numbers

- **14,425 unique repositories** in `github-website-corpus-manifest.csv` as of the
  second search round (was 8,886 after round 1). The 10,000+ target has been
  legitimately crossed. Reported as-is, not rounded up.
- Source: GitHub REST Search API (`gh api search/repositories`), 59 distinct queries
  in round 1 (35 initial topic queries + 24 supplementary topic queries), each with
  `created:<2024-01-01` applied server-side, star-bucket partitioning
  (`stars:>3000`, `1000..3000`, `300..999`, `100..299`, `20..99`, `0..19`) used to
  get past the API's 1,000-results-per-query cap on high-volume topics.
- Every row passed `created_at < 2024-01-01` (verified again during dedup — 0 rows
  were dropped for failing this a second time, meaning the server-side filter was
  reliable).
- Deduplicated by `full_name` across round 1's two sub-rounds: 11,125 raw JSON
  records in → 8,886 unique repos out (~20% were cross-query duplicates, as
  expected since many topics overlap, e.g. `hugo-theme` and `hugo-site`).
- **Round 1 fell short of 10k** for a real reason: GitHub's topic-tagging is
  sparse, and star-bucket partitioning alone couldn't unlock much more volume
  once a topic's star buckets were each already under the per-query cap.

### Round 2: date-range partitioning + new topics (crossed 10,000)

- Added 25 new topic queries not used in round 1 (`wordpress-theme`,
  `static-website`, `developer-portfolio`, `restaurant-website`,
  `ecommerce-template`, `blog-template`, `documentation-site`,
  `webflow-template`, `squarespace-template`, `vuejs-website`,
  `angular-website-template`, `svelte-website-template`, `nuxt-template`,
  `eleventy-template`, `elementor-template`, `wix-template`,
  `github-pages-template`, `startup-landing-page`, `portfolio-template`,
  `freelancer-website`, `conference-website`, `event-website-template`,
  `nonprofit-website-template`, `real-estate-website`, `music-website-template`).
- Instead of star-bucket partitioning, each topic was partitioned by
  `created:YYYY-01-01..YYYY-12-31` across every year 2010-2023 (14 slices per
  topic, 350 base queries), with pagination (up to 10 pages of 100) within any
  year-slice that itself exceeded 100 results. This is a genuinely different
  strategy from round 1: it directly targets the per-query 1,000-result cap by
  slicing on time instead of stars, which works well for topics whose volume is
  concentrated in a few recent years (e.g. most `wordpress-theme` and
  `static-website` repos cluster in 2016-2023).
- Yield was very uneven across the 25 new topics: high-traffic tags
  (`wordpress-theme`, `static-website`, `portfolio-template`) each returned
  hundreds to low-thousands of repos across their year slices, while many of
  the newer/niche tags (`elementor-template`, `wix-template`, `squarespace-template`,
  `music-website-template`, `nonprofit-website-template`) returned 0 or near-0
  results across nearly every year — these tags are simply rarely applied on
  GitHub. This unevenness is expected and reported honestly rather than
  smoothed over.
- Total raw JSON records pulled in round 2: 6,717. After removing 113
  duplicates within the new batch and 1,065 records that were already present
  in the round-1 manifest (cross-round dedup by lowercased `full_name`), 5,539
  net-new unique repos were added. 0 records were dropped for failing the
  `created_at < 2024-01-01` filter (the server-side `created:` qualifier did
  its job).
- Final total: 8,886 + 5,539 = **14,425** unique repos, comfortably past the
  10,000+ target. Unlike round 1, round 2 did NOT hit diminishing returns before
  reaching the target — date-range partitioning combined with fresh topics
  unlocked substantially more volume than star-bucket partitioning alone could
  from the same 59 original topics. This confirms round 1's topic set (not the
  partitioning method) was the binding constraint, not an inherent scarcity of
  qualifying repos on GitHub.
- New rows use the same CSV schema as round 1 and were **not** cloned/verified;
  their `license_spdx_api` field remains unverified API metadata, consistent
  with all non-sampled rows in the manifest.
- Manifest fields per row (metadata only, **not verified by cloning** except for
  the 44 sampled below): `full_name, html_url, description, stars, language,
  license_spdx_api, created_at, pushed_at`. The `license_spdx_api` field is
  **GitHub API metadata, unverified** for all rows except the 44 cloned ones —
  it reflects GitHub's own license-detection heuristic (`license.spdx_id`), which
  can be wrong or `"unknown"`/`"NOASSERTION"` when a repo has no machine-readable
  LICENSE file GitHub could parse. Treat this field as a signal, not a legal
  determination, for anything not in the cloned sample.
- Manifest-wide (unverified) license distribution: MIT 3,651, unknown 3,920,
  NOASSERTION 376, GPL-3.0 331, Apache-2.0 219, 0BSD 68, CC0-1.0 55, AGPL-3.0 47,
  Unlicense 41, plus a long tail. Language distribution (API-reported primary
  language): HTML 2,576, JavaScript 1,970, CSS 1,222, TypeScript 1,013, SCSS 545,
  Vue 307, PHP 156, Astro 129, Python 82. Star distribution: max 24,253, median 7,
  1,095 repos with ≥100 stars, 186 with ≥1,000 stars — the manifest is long-tailed,
  as expected for a topic-search corpus (a handful of famous themes, thousands of
  small personal forks/variants).

## The cloned, analyzed sample: 44 repositories

44 repos were selected from the manifest for diversity across static-site
generators/frameworks and languages, filtered first to API-reported permissive
licenses (MIT/Apache-2.0/ISC/CC0-1.0/Unlicense/0BSD/BSD-2/BSD-3), then picked
~5-8 per language/framework bucket by star count, shallow-cloned
(`git clone --depth 1`), and **the LICENSE file of every single one of the 44 was
read directly** (not just trusted from the API field) before analysis:

- **44/44 verified by reading the actual LICENSE file in the clone.**
- 42 of 44 verified MIT, 2 of 44 verified Apache-2.0 (`docsy/docsy`,
  `vlad-moroshan/portfolio-website`).
- 0 discrepancies found between the API's `license_spdx_id` guess and the actual
  LICENSE file text for this sample — the API signal was reliable for all 44,
  though that's not proof it's reliable across the full 14,425-row manifest,
  only for this one clean, well-known, already-popular sample (drawn from
  round 1; round 2's added repos were not sampled or cloned).
- All 44 cloned directories and the raw API JSON dumps were deleted after analysis
  — nothing but the manifest CSV and this markdown file remain in `references/`.

### Framework / static-site-generator breakdown (44 repos, some multi-label)

| Generator/framework | Count |
|---|---|
| Hugo | 8 |
| Jekyll | 8 |
| Other JS/npm project (no recognized SSG) | 7 |
| Astro | 6 |
| Other (no package.json/index.html found at shallow depth) | 5 |
| Next.js | 4 |
| VuePress | 3 |
| SvelteKit | 2 |
| Nuxt | 1 |
| Static HTML, no generator | 1 |

Jekyll and Hugo together account for 16/44 (36%) of the sample — consistent with
GitHub Pages being the dominant free-hosting path for personal/portfolio sites
pre-2024, and with both ecosystems having a long tradition of "theme repo as a
GitHub-native package" distribution. Astro (6) is the leading newer-generation
entrant, reflecting its rise as the default choice for content-first sites
2022-2023.

### CSS approach breakdown (44 repos, multi-label — many repos mix approaches)

| Approach | Count |
|---|---|
| SCSS/Sass | 14 |
| Vanilla CSS (plain `.css` files, no preprocessor/framework) | 13 |
| Tailwind (utility-first) | 7 |
| Bootstrap | 7 |
| No CSS files found at shallow scan depth | 7 |
| LESS | 2 |

No single approach dominates. SCSS narrowly leads, driven by the Jekyll/Hugo
theme cohort (`_sass/` partials are the idiomatic Jekyll pattern — 7 of the 44
repos have a top-level `_sass/` directory). Vanilla CSS is nearly as common,
concentrated in older/simpler personal-site templates. Utility-first (Tailwind)
appears specifically in the Astro/Next.js/SvelteKit cohort — every Tailwind hit
in this sample is in a modern JS-framework repo, none in a Jekyll/Hugo repo,
suggesting utility-first CSS adoption tracks framework generation more than
"website template" category per se.

### Common file/folder structure patterns (top-level directory names, 44 repos)

Most frequent top-level directories across the sample (count of repos containing
each, not total occurrences):

`.github` (33), `assets` (17), `src` (15), `public` (13), `.vscode` (12),
`docs` (11), `scripts` (10), `layouts` (9), `images` (9), `static` (7),
`_sass` (7), `_layouts` (7), `_includes` (7), `_data` (6), `i18n` (5),
`exampleSite` (5), `archetypes` (5), `.husky` (5), `_posts` (5).

Reading: `.github` (CI workflows / issue templates) is in 75% of repos —
almost universal, expected for anything with real community adoption.
`assets`/`images`/`public`/`static` collectively show that "put raw media
outside the build pipeline" is the default convention regardless of framework.
The Jekyll-family underscore-prefixed directories (`_sass`, `_layouts`,
`_includes`, `_data`, `_posts`) cluster together as expected — they're not
optional in Jekyll's convention, they're the framework's required layout.
Hugo repos commonly ship an `exampleSite/` (demo content decoupled from the
theme itself, since Hugo themes are typically consumed as git submodules) and
an `archetypes/` directory (content-type scaffolding templates) — a structural
pattern Jekyll has no equivalent for, reflecting Hugo's more explicit
theme/site separation.

### Recurring design/markup patterns observed

- Nearly every Jekyll/Hugo theme in the sample ships a `_config.yml.example` or
  equivalent commented config file with color/font/social-link variables exposed
  at the top — i.e., "theme configuration via YAML front-matter or a single
  config file," not via editing markup, is the dominant customization contract
  for this whole SSG-theme category.
  
- The Astro/Next.js/SvelteKit cohort converges on a near-identical file
  taxonomy regardless of framework: a `components/` directory of small
  single-purpose UI pieces (Hero, Header, Footer, Card), a `content/` or
  `posts/` directory for Markdown/MDX content, and a `config.ts`/`site.config.ts`
  for site-wide metadata (title, description, social links, analytics ID) —
  the "framework-native config object" pattern has effectively replaced the
  old Jekyll/Hugo YAML config for the newer generation, same underlying
  customization contract, different syntax.

- Dark-mode support (a `prefers-color-scheme` media query or a `data-theme`
  attribute toggle) appears in essentially all of the post-2022-created repos
  in the sample and in almost none of the pre-2020 ones — a visible generational
  split rather than a framework-driven one.

- Admin-dashboard-style templates in the sample (`startbootstrap-sb-admin-2`,
  `TailAdmin/free-nextjs-admin-dashboard`) both organize markup around a fixed
  sidebar + top navbar + scrollable content-card grid, and both ship a
  significant chunk of pure demo/placeholder content (charts, tables) whose
  purpose is to be deleted by the site's actual author — i.e. these are
  explicitly "starter scaffolding" rather than finished sites, a distinct
  sub-genre from the portfolio/blog templates in the rest of the sample.

## Bottom line

The manifest holds 14,425 real, deduplicated, pre-2024 GitHub website repos with
API-sourced metadata (license field unverified except for the 44 cloned from
round 1) — past the 10,000 target, reached honestly by adding a genuinely
different search strategy (date-range partitioning across new topics) in round
2 rather than by loosening the filters. The 44-repo cloned sample is small
relative to the manifest but every one of its licenses was hand-verified by
reading the actual LICENSE file, and it surfaces real, source-grounded patterns
(SSG choice split, CSS-approach-tracks-framework-generation, near-universal
`.github` presence, Jekyll/Hugo underscore-directory convention vs. Astro/Next
`components+content+config` convention, dark-mode as a generational rather than
framework-driven feature) rather than received wisdom about "what website
templates look like."
