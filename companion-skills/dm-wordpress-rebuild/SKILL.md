---
name: dm-wordpress-rebuild
description: Rebuild an existing service-business website as an editable WordPress theme without losing URLs, backlinks or rankings. Use when migrating or redesigning a live site into a classic PHP theme - crawl and inventory, local WordPress import, redirects from Wayback data, no hotlinking, noindex static preview hosting, block patterns for non-developers, multilingual parity, QA audit harness and client taste rules.
license: MIT
---

# WordPress rebuild of a service-business site

Lessons from rebuilding a service-business site as a WordPress theme. Pair with `dm-seo` for titles, schema and launch checks.

## Workflow
1. Crawl the old site into an inventory (URL, type, title, h1, images, language, status). It becomes the parity checklist.
2. Import all content into a local WordPress with identical URLs. WordPress Playground CLI works (port 9400, mount the theme folder).
3. Build a classic PHP theme that reads the existing menu and content, keeps permalinks and custom post types, and adds no new required plugins.
4. Test locally against the inventory, then ship two things: the theme zip and a noindex static preview of the rendered pages.
5. Never touch the live site without the owner. The owner installs the zip and flips the switch.

## Backlink safety
- Recover archived URLs from the Wayback CDX API (`collapse=urlkey`, `filter=statuscode:200`).
- HEAD-check each one on the live site. Copy the live 301 targets into `redirects.csv` (old path, new path, status).
- Handle redirects in a `template_redirect` hook that reads the CSV. Anything 404 and not in the CSV goes to the report, not to the homepage.

## Do not hotlink the old domain
It will be removed. Rewrite absolute old-domain URLs to `home_url()` on output (`the_content`, `wp_get_attachment_url`, thumbnails, srcset). Mirror the uploads folder before the old site goes away and verify no request leaves the new host.

## Preview hosting gotchas
- A Cloudflare Pages upload of about 12,000 files and 1.2 GB failed repeatedly with EPIPE. About 3,500 files and 600 MB worked.
- Prune image size variants, strip `srcset` and `data-srcset`, keep only referenced files, recompress big PNG and JPG.
- Retry the deploy in a loop, logging to a file.
- Add `X-Robots-Tag: noindex` through `_headers`, a `robots.txt` with `Disallow: /`, and a canonical pointing at the preview host.

## Editable for employees
- `theme.json`: palette, font, button style, spacing.
- Block patterns in `/patterns`: hero, services, stats, features, principles, office gallery, partners, FAQ (core/details), CTA, latest posts.
- A seed function that fills the homepage from those patterns, plus a reset button under Appearance.
- CSS: one commented section per block, a per-block CSS split, and a computed-styles report (Playwright `getComputedStyle` per block) so another developer can merge it into an existing stylesheet.
- Pattern files may run PHP, but the pattern registry does not expose their content. Include the file with output buffering (`ob_start(); include $f; $c = ob_get_clean();`) to build the content string.

## Languages
- Separate language pages must not have different layouts. Seed each language homepage from the same patterns.
- Use one string table keyed by the English text (a helper like `t('English text')`) for patterns, header, footer, nav and chat.
- Output hreflang only when the twin page exists.

## Client taste rules learned
- No black text on orange buttons: white text on a deeper orange.
- Avoid near-black sections. Use brand colours and tints. Keep the client's body font.
- No dashes or em dashes in copy.
- Do not add an AI chatbot if the original has none. A keyword-matching helper with call, WhatsApp or book handoff is enough.
- No fixed bottom action bar on mobile. A small round chat button instead.
- Mega menus with more than about 12 links need a two-pane group list, not a wall of links.
- Use many distinct real photos on the landing page. Never repeat one image.
- Fix auto-capitalised acronyms (Seo to SEO).
- One h1 per page, tap targets at least 44px, titles about 60 characters.

## Audit harness
- Playwright at 360, 390, 768 and 1440: horizontal overflow, broken images, missing alt, exactly one h1, console errors, tap targets.
- A full parity run over every inventory URL. Run the same audit on the deployed preview.
- Gotchas:
  - `backdrop-filter` on a header makes it the containing block of fixed children and causes overflow.
  - Full-page screenshots miss scroll-reveal content: scroll first or force the revealed state.
  - Python multiprocessing scripts need an `if __name__ == "__main__"` guard.
  - macOS has no `timeout` or `setsid`.
  - Background jobs can be killed when the user interrupts: write logs to a file.

## Content fixer pattern
A WP-CLI `eval-file` script that fixes content in bulk. Dry run by default, `--apply` to write, a backup table written first, a `--restore` mode, and never a delete.

## Process
The owner or manager reviews the design, so deliver: a block list, per-block styles, a launch checklist, and a list flagging all new copy for review. Keep a request list with a status per item.
