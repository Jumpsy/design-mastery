# Web / landing pages

**Layout**: hero (headline + subhead + 1 CTA + proof element) → social proof strip →
3–5 feature sections alternating text-left/text-right → pricing or single strong CTA →
footer. Max content width 1200–1280px; hero can break out full-bleed.

**Hero image options** (pick one, justify by product type):
- Interface-as-hero: real, live-looking product UI cropped tight, no device frame
  (OpenAI, Linear, Wispr Flow). Best for products where the UI itself is the pitch.
- Annotated product mockup over gradient mesh (Stripe). Best for infra/API products
  needing to show multiple surfaces at once.
- Pure typography, no image (OpenAI editorial mode). Best when the copy is the product.
- Illustration/doodle (StudyFetch). Best for consumer/edtech needing warmth.
Never: abstract blob + two pill buttons + centered headline with no other information.

**Typography**: one display face for headlines, one workhorse for body/UI. Modular
scale 1.25 or 1.333. Serif+italic-accent-word formula (Wispr Flow/StudyFetch) signals
warm/consumer; tight sans + monochrome signals technical/infra.

**Motion**: entrance fades only on hero + 1–2 proof moments, 40–80ms stagger. Section
transitions 150–300ms ease-out, linear/flat (not bouncy) per measured Stripe data.
Cursor-glow hero accent used sparingly (Linear, Vercel), one per page max.

**Anti-patterns**: purple/blue gradient default, 3-icon feature grid with colored
circles, colored left-border accent strip on cards (single most-cited AI tell),
Inter+default Tailwind spacing with no typographic point of view.

**Sources**: live devtools inspection of stripe.com, openai.com, linear.app,
wisprflow.ai, studyfetch.com (this session); 74-brand `design-md/` teardown library.
