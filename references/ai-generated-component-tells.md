# AI-generated component tells

A catalog of specific UI *components* (not just colors/fonts) that LLM-generated
designs default to, why each one reads as fake/AI-made even when the color palette
and typography are otherwise fine, and what the real-world version actually does
differently. Anti-slop checklists (SKILL.md §2, the design-critique reel analyzed
in this session) mostly name surface traits — gradients, shadows, fonts. This file
goes one level deeper: the *component itself* is often the tell, independent of
how it's styled, because the default implementation is a plausible-looking mockup
of the real thing rather than the real thing.

Read this alongside `references/interaction-bug-patterns.md` (behavioral tells)
and SKILL.md §2 (visual/token tells). This file is about *structural* tells: what
the component contains, how it's built, and what real instances of it actually do
that the generic version fakes or omits.

## Fake terminal / code window

**Default AI version:** three colored dots (red/yellow/orange/green) top-left,
rounded-corner card, a monospace block with 3-5 lines of made-up command output,
often a blinking-cursor `<span>` at the end that never actually types anything,
no scrollback, no prompt structure (`$`, `>`, or a real shell prompt with cwd/user).
Frequently uses a *sans-serif or semi-monospace* font (Space Grotesque, Inter) or a
monospace font at the wrong line-height/letter-spacing for a real terminal, which
reads as "text styled to look techy" rather than an actual terminal render.

**What's actually wrong:** real terminals have a real prompt syntax (`user@host
~/project $`, or a zsh git-branch segment, or a language REPL's own prompt like
`>>>`), monospace font at ~1.2-1.4 line-height with no letter-spacing, a cursor
that's a solid block or underscore (not a thin blinking `|`), ANSI color codes
used sparingly and consistently (not rainbow), and output that's *plausible
program output* — real file paths, real error formats, real timestamps — not
generic placeholder strings like `Initializing...` / `Done!` / `Success ✓`.

**Fix:** if a terminal is genuinely necessary (dev-tool marketing, CLI product),
either screenshot a real terminal running the real command, or hand-author output
that matches the actual tool's real CLI format byte-for-byte (check the tool's
actual help/output text, don't invent it). If it's decorative, don't use a
terminal motif at all — it's one of the most over-used "this looks technical"
crutches in AI output and reads as fake unless the content is real.

## Chat / message bubbles for a "demo"

**Default AI version:** two-tone bubble pairs (accent-colored right-aligned "user"
bubble, gray left-aligned "assistant" bubble), generic avatar circles, a typing
indicator of exactly three bouncing dots, timestamps that are either absent or a
suspiciously round "2 min ago" / "Just now."

**What's actually wrong:** real chat products have inconsistent message lengths,
occasional multi-message bursts from one sender (no bubble on every line), read
receipts/delivery states that map to real product behavior, and copy that sounds
like two specific people, not "Hi! How can I help you today? 😊" generic assistant
tone. The three-dot typing indicator specifically is instantly recognizable as a
stock component when the rest of the UI isn't otherwise trying to look like a
specific real messaging product.

## "3 feature cards in a row" / icon-circle-title-description grid

Already in SKILL.md §2, but the component-level tell beyond "colored circle behind
every icon": the three descriptions are always near-identical sentence length and
near-identical level of vagueness ("Powerful analytics to help you make better
decisions" / "Seamless integrations with your favorite tools" / "Enterprise-grade
security you can trust") — real feature copy varies in length and gets specific
(a number, a named integration, a named compliance standard) because real features
aren't equally important or equally described.

## Fake browser chrome / device mockup

**Default AI version:** a rounded rectangle with three dots or a URL bar showing
`example.com` or `yourapp.com`, containing a screenshot-shaped placeholder (often
just more UI in the same generated style, i.e. the app "screenshotted" inside its
own marketing page was never actually run).

**What's actually wrong:** the URL bar text is fake, the "screenshot" is
obviously the same synthetic design system as the marketing chrome around it
(no visual discontinuity you'd expect between a marketing site's design and an
actual product's UI, which are almost always stylistically distinct even within
one company), and the browser chrome itself is often the wrong OS/browser
combination for no reason (macOS traffic-light dots next to a Windows-style
scrollbar).

**Fix:** use a real screenshot of the real product, in a real device frame if
needed. If the product doesn't exist yet, don't fake a "real" URL/browser chrome
around it — that specific combination (real-looking chrome + fabricated content)
is what reads as deceptive rather than just placeholder.

## Bento grid with mismatched cell content

**Default AI version:** asymmetric grid of cards (one 2x2, a few 1x1, one wide
1x2) each containing an icon+headline, sized by grid aesthetics rather than by
what the content actually needs — a one-sentence feature gets the same 2x2 cell
as a data-dense stat block, or vice versa, so the layout looks deliberate but the
cell-size-to-content-density ratio is arbitrary.

**What's actually wrong:** in real bento layouts (the pattern's namesake — Apple's
product pages, e.g.), cell size is driven by actual content weight — a cell with
a live chart or a multi-line stat block is large because it needs the space, not
because the grid needed a large cell there. Fix: size cells from content, not the
other way around; if every cell has equally light content, use a uniform grid
instead of bento (bento on uniform content is itself a tell).

## Testimonial cards with fabricated attribution

Already covered under "dishonesty/fake-state" in the interaction-bug-patterns
reference for *functional* fakery; the component-level visual tell is a stock
avatar (generic gradient circle with initials, or worse, an obviously-stock
headshot), a title that's suspiciously perfectly matched to the product ("Head of
Growth" for a growth-analytics tool, always), and 1-2 sentence quotes that praise
in generic superlatives ("This tool changed how we work") rather than citing a
specific outcome, number, or workflow.

## Pricing table with three tiers, middle "highlighted"

The 3-tier/middle-highlighted layout itself isn't inherently fake (real SaaS
pricing legitimately often has 3 tiers), but the AI-default version has: perfectly
round numbers with no psychological pricing (or over-uses .99 pricing
reflexively), identical feature-list length per tier with only checkmarks toggled
on/off (real tiers usually gate *different* things, not a strict superset), and a
"Most Popular" badge on the middle tier by pure convention rather than because
that reflects real usage data for this specific product.

## Skeleton/loading states that don't match final content shape

**Default AI version:** generic gray pulsing rectangles/circles, either absent
entirely (content just pops in) or present but sized independently of the real
content's actual dimensions (a skeleton line block where the real content will be
a short badge, or vice versa).

**What's actually wrong:** real skeleton loaders are shaped to closely preview
the actual content's layout (line lengths approximate real text line lengths,
avatar-circle skeleton matches the real avatar size) so there's no layout shift
on load. A skeleton that doesn't match final content geometry both looks fake and
causes real CLS.

## Empty states with a centered illustration + single CTA

Not inherently wrong, but the AI-default illustration is almost always an
abstract blob/character in the brand's accent color holding or looking at a
generic object (a magnifying glass, an empty box, a folder) with no relationship
to what's actually empty. Real empty states from products with a strong design
system reuse the product's own iconography/illustration system rather than a
one-off generic illustration commissioned just for this screen.

## Stat/metric counters with suspiciously clean numbers

`10,000+ users`, `99.9% uptime`, `4.9/5 rating`, `24/7 support` — each individually
plausible, but appearing together as a row of 4 stat cards is a strong tell
because real products rarely have every headline metric be a round, unfalsifiable
number simultaneously. Fix: if the numbers are real, cite them with enough
specificity to be checkable (a date range, a source); if they're placeholder,
don't present them as a "stats bar" at all — that framing implies verified fact.

## Toggle/switch controls with no real second state behavior

A billing-period toggle, dark-mode toggle, or feature toggle that's wired to
change a number or class but has no realistic secondary consequences (a discount
toggle that doesn't change any other visible pricing math elsewhere on the page,
a dark-mode toggle in a screenshot/demo that doesn't actually re-render — see the
interaction-bug-patterns reference's Category 5/8 for the functional version of
this same tell).

## Process notes

- Every pattern above was named because it's a *structural* shortcut — the
  component fakes having a specific real-world counterpart's content/behavior
  while only replicating its visual shell. The fix is almost never "restyle it,"
  it's "either make the content/behavior real, or don't use that component."
- This list is not exhaustive by construction — extend it opportunistically
  whenever a fresh cold-read grader or an external source (like the design-critique
  reel analyzed this session) names a specific component-level tell not yet
  captured here, rather than only the visual/token-level tells SKILL.md §2 already
  covers.
