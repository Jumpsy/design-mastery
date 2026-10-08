---
name: dm-seo
description: WordPress-focused SEO build and audit skill. Use when building, migrating or auditing a WordPress site or theme for search - titles, meta, canonical, robots, JSON-LD schema graph, permalinks and 301 redirects, Core Web Vitals, internal linking, local SEO, AI-answer (GEO) readiness and the launch checklist. Includes audit.py, a Playwright page checker.
license: MIT
---

# dm-seo: WordPress SEO

Goal: a site search engines and AI answer engines can crawl, understand and trust, without breaking what already ranks. Verify every claim in a real page (view source, run `audit.py`), do not assume.

## 1. Technical checklist (themes)

- Theme declares `add_theme_support( 'title-tag' )`; never hard-code `<title>` in header.php.
- If Yoast, Rank Math, AIOSEO or SEOPress is active, the theme must NOT output its own title, description, canonical, robots, Open Graph or JSON-LD. Detect and yield:

```php
function dm_seo_plugin_active() {
	return defined( 'WPSEO_VERSION' ) || defined( 'RANK_MATH_VERSION' )
		|| defined( 'AIOSEO_VERSION' ) || defined( 'SEOPRESS_VERSION' );
}
```
- Fallback when no plugin: output one meta description (from excerpt, 120-160 chars), `rel=canonical` (WordPress core already prints it for singular posts via `rel_canonical`; do not duplicate), Open Graph and Twitter tags.
- Robots: use the core `wp_robots` filter, never a hand-written `<meta name="robots">`:

```php
add_filter( 'wp_robots', function ( $robots ) {
	if ( is_search() || is_404() ) { $robots['noindex'] = true; $robots['follow'] = true; }
	return $robots; // core adds max-image-preview:large by default
} );
```
- Exactly one `<h1>` per page, logical h2/h3 below it. Logo is not the h1 on inner pages.
- `<html lang>` via `language_attributes()`. Add `hreflang` only for real translations.
- Titles about 50-60 chars, unique, primary topic first. Descriptions 120-160 chars, unique, written for a click.
- Pagination: self-canonical per page; archives of thin content (tags, dates, authors on one-author sites) get noindex.
- Every image: meaningful `alt` (empty `alt=""` only for decoration), width/height attributes.
- `robots.txt`: allow assets (CSS/JS), disallow `/wp-admin/` except `admin-ajax.php`, link the sitemap. Core serves `wp-sitemap.xml`; if a plugin provides a sitemap, disable the other.
- HTTPS everywhere, one canonical host (www vs non-www), trailing-slash consistent.

## 2. JSON-LD as one @graph

Emit one `<script type="application/ld+json">` with a `@graph`, linked by `@id`. Skip entirely if an SEO plugin already outputs a graph (extend it through its filter instead, e.g. `wpseo_schema_graph_pieces`, `rank_math/json_ld`). Encode with `wp_json_encode( $data, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE )`.

Pieces:
- `Organization` (or `ProfessionalService` / `LocalBusiness` subtype for service firms): name, url, logo, sameAs, contactPoint; for local add address, telephone, openingHours, areaServed.
- `WebSite` with `potentialAction` `SearchAction` (`target` `{home}/?s={search_term_string}`, `query-input` `required name=search_term_string`). Only if site search works.
- `WebPage` (or `BlogPosting` for posts: headline, datePublished, dateModified, author, image, mainEntityOfPage) with `isPartOf` and `about`.
- `BreadcrumbList` matching visible breadcrumbs.
- `FAQPage` only when the Q&A is visible on the page, verbatim. Do not mark up hidden or invented FAQs.

Rules: no fake ratings or reviews, no markup for content not on the page, values match visible text (NAP, prices). Validate in the Rich Results Test and with `audit.py` (parse check).

## 3. Permalinks and 301 preservation

Never change URLs that rank without a mapped redirect.
1. Set permalinks to `/%postname%/` early; do not change after launch.
2. Before a rebuild, collect old URLs: Search Console pages report, server logs, sitemap, and the Wayback CDX API for the old domain:
   `https://web.archive.org/cdx/search/cdx?url=example.com/*&output=txt&fl=original&collapse=urlkey&filter=statuscode:200&filter=mimetype:text/html`
3. Normalise (strip query/fragment, lowercase host, dedupe) into `redirects.csv` with columns `old_path,new_path,status` (301). Map each to the closest equivalent page; never bulk-redirect everything to the homepage (soft 404).
4. Implement in the server or a redirect plugin (Redirection, or a small mu-plugin reading the CSV); server-level is fastest.
5. Status check every old URL: expect 301 then 200 in one hop, no chains, no loops.

```bash
while IFS=, read -r old new status; do
  printf '%s -> ' "$old"; curl -s -o /dev/null -L -w '%{http_code} %{num_redirects} %{url_effective}\n' "https://example.com$old"
done < <(tail -n +2 redirects.csv)
```
6. Keep the redirects for at least a year. Update internal links to point at new URLs directly.

## 4. Core Web Vitals

Targets (75th percentile): LCP <= 2.5 s, INP <= 200 ms, CLS <= 0.1.
- Fonts: self-host WOFF2, subset, `font-display: swap`, preload only the one or two critical files, no render-blocking Google Fonts requests.
- Images: serve WebP/AVIF, correct `srcset`/`sizes`, explicit width and height (prevents CLS).
- LCP image: do NOT lazy-load it; add `fetchpriority="high"` and a `<link rel="preload" as="image">` if it is a CSS background or late-discovered. WordPress core lazy-loads by default and skips the first image in many cases; verify.
- Below the fold: `loading="lazy"`, `decoding="async"`.
- Embeds (YouTube, Maps): facade pattern. Show a poster and load the iframe on click.
- JS: defer or delay third-party scripts (chat, analytics tags) until interaction; remove unused plugins and their assets; load page-builder CSS per page.
- Caching and server: page cache, Brotli/gzip, HTTP/2+, CDN for static assets, good TTFB.
- Measure with Lighthouse and field data (CrUX, Search Console Core Web Vitals report). Lab scores alone are not proof.

## 5. Internal linking

- Every important page reachable within 3 clicks and linked from at least 3 relevant pages.
- Descriptive anchors (not "click here"); link from body copy, not only menus.
- Hub and spoke: service or topic hub page links to detail pages and back.
- Orphan check: compare sitemap URLs to crawled-linked URLs. Fix broken internal links (no 404s, no redirected internal links).
- Breadcrumbs on inner pages, visible and in the schema graph.

## 6. Local SEO (NAP)

- Name, Address, Phone identical everywhere: site footer, contact page, schema, Google Business Profile, directories. Same formatting, same abbreviations.
- Click-to-call `tel:` links, embedded map (facade), opening hours as text and in schema.
- One landing page per location or service area with unique content, not doorway clones.
- Claim and complete the Google Business Profile; match categories to services; collect genuine reviews; do not self-review.

## 7. GEO: AI-answer readiness

- Answer first: each page leads with a 1-3 sentence direct answer, then detail. Use question-style h2/h3 and short self-contained paragraphs.
- Name entities consistently (business, people, places, products) and tie them with schema `sameAs` and an About page with real credentials.
- Facts with sources, dates and a visible "last updated". Prefer specifics (numbers, steps, comparisons) over adjectives.
- Tables and lists for comparisons and processes; real FAQ sections that match actual customer questions.
- Allow reputable AI crawlers in robots.txt unless you have a reason not to; ensure content renders without JS.
- `llms.txt` is optional and unproven: a plain-markdown file at `/llms.txt` summarising the site and key URLs. Cheap to add, do not expect ranking effects.

## 8. Launch checklist

- [ ] Staging is `noindex` (Settings > Reading "discourage" plus `X-Robots-Tag` or HTTP auth) and that flag is REMOVED at launch. Check source for `noindex` on production.
- [ ] robots.txt does not contain `Disallow: /`.
- [ ] Redirect map live and status-checked (section 3).
- [ ] One canonical host, HTTPS, no mixed content.
- [ ] Sitemap submitted in Search Console; domain property verified; request indexing for key pages.
- [ ] Analytics and conversion tracking firing once.
- [ ] `audit.py` passes on all key templates (home, service, post, contact, 404).
- [ ] Schema validates; titles/descriptions unique; no placeholder text or lorem ipsum.
- [ ] Core Web Vitals checked on mobile.
- [ ] Post-launch: watch Search Console Coverage and Crawl errors for 2-4 weeks; fix 404s with new redirects.

## audit.py

```bash
pip install playwright   # uses installed Google Chrome (channel chrome)
python3 companion-skills/dm-seo/audit.py https://example.com / /about/ /blog/
```
Checks per path: no horizontal overflow at 390px, exactly one h1, title (10-60 chars) and description (50-160) length, canonical present, JSON-LD parses, no broken images, no missing alt. Prints a pass/fail table; exit code 1 on any failure.

## Lessons from a WordPress rebuild
- Keep titles near 60 characters and descriptions under 160. Check every template, not just the homepage.
- Put a canonical on archive and paginated pages too, not only singles.
- Output hreflang only for real twins. A missing twin with an hreflang is an error.
- One h1 per page: demote any h1 inside body content to h2.
- Fix acronym case that auto-capitalisation breaks (Seo to SEO) in titles, headings and menus.
- Recover backlink URLs from the Wayback CDX API, HEAD-check them on the live site, and replicate its 301s in the theme.
- Keep any preview or staging copy noindex: `X-Robots-Tag`, `Disallow` robots.txt, canonical to the preview host.
- Emit one JSON-LD `@graph` with linked ids (Organization, WebSite, WebPage, breadcrumbs) instead of separate unconnected blocks.
See `dm-wordpress-rebuild` for the full workflow.
