---
name: dm-motion-graphics
description: Craft-level motion graphics for web and video - choreography, easing, timing, scroll-driven and SVG/Canvas/WebGL motion, GSAP, CSS, Framer Motion/Motion, Remotion, Lottie-style vector animation - with reduced-motion and performance rules. Use for any animation, transition, hero motion, loader, scroll effect, explainer or product-demo video.
license: MIT
---

# Motion Graphics

Motion explains change, directs attention and gives the product a physical character. If an
animation does none of those, delete it. Pair with `design-mastery`'s anti-slop checklist
and the `vendored/gsap-skills` pack for GSAP specifics. Follow `dm-grounding`: check the
installed library version's docs before using an API; never guess method names.

## 1. Choose the motion idea before the tool
1. **Job:** orient (where did it go), confirm (it worked), guide (look here), delight (brand).
2. **One signature move** per project (e.g. masked text rise, shared-element morph, magnetic
   cursor, scroll-scrubbed line draw) repeated consistently. Not ten different effects.
3. **Character:** pick one of snappy (150-250ms, expo-out), smooth (300-500ms, cubic-out),
   springy (physical, slight overshoot). Use it everywhere.

## 2. Timing and easing (defaults to start from, then judge by eye)
- Micro-feedback 100-200ms; UI transitions 200-350ms; large/page-level 400-700ms; hero
  intros up to ~1.2s total, never blocking interaction.
- Enter = ease-out (decelerate in). Exit = ease-in (accelerate out), and ~30% faster than
  enter. Movement across the screen = ease-in-out. Never `linear` except for continuous
  loops, progress and scroll-scrubbing.
- Stagger 30-80ms per item, cap total stagger near 400-600ms; for long lists stagger only
  the first visible ~8 items.
- Offset overlapping actions (follow-through): children lag parents by 40-120ms.
- Distances: 8-24px translate for UI, larger only for deliberate drama. Pair translate with
  opacity; add subtle blur or scale (0.96-1) for premium feel, not rotation.

## 3. Choreography
- Hierarchy of arrival: background, then structure, then headline, then supporting, then CTA.
- Animate the cause, not the decoration: the thing the user touched moves first.
- Preserve object constancy: shared elements morph (FLIP: First, Last, Invert, Play) rather
  than cut and fade.
- Loops are quiet: ambient motion under 10% visual energy, pausable, off-screen paused.

## 4. Techniques by tool (pick the lightest that works)
1. **CSS transitions/animations** for state changes. Animate only `transform`, `opacity`
   (and `filter`/`clip-path` sparingly). Use `will-change` only on elements actively
   animating. Prefer CSS `@keyframes` + `animation-timeline: scroll()/view()` where
   supported, with a JS fallback.
2. **Web Animations API** for imperative one-offs without a library.
3. **GSAP** (timelines, ScrollTrigger, SplitText, Flip, MorphSVG) for sequenced or
   scroll-scrubbed work. Use timelines with labels, `gsap.context()` / `useGSAP` cleanup in
   React, `ScrollTrigger.refresh()` after layout changes. See `vendored/gsap-skills/*`.
4. **Motion (Framer Motion)** for React layout animation, shared layout, gestures,
   `AnimatePresence`.
5. **SVG** line-draw (`stroke-dasharray/offset`), path morphs, masks; **Canvas/WebGL
   (three.js, OGL, shaders)** only when particles/3D/generative visuals justify the cost.
6. **Video (Remotion)**: deterministic frames from React; drive everything from
   `useCurrentFrame()` and `interpolate()` / `spring()`; no CSS transitions or timers,
   they will not render. 30fps default, 60 for fast UI motion; design at 1920x1080 or
   1080x1920 for social.
7. **Lottie/Rive** for authored character/icon animation; keep files small.

## 5. Typography and kinetic text
Split by line or word (not always char), reveal with a mask (`overflow:hidden` +
translateY 100%), keep text selectable and readable at rest, never animate body copy
the user must read quickly. Keep a no-JS final state.

## 6. Performance and robustness
- 60fps budget = 16ms/frame. Avoid layout-triggering properties (width, height, top, left,
  margin) in animation; use transform. Batch reads then writes.
- Pause off-screen animation (IntersectionObserver); cancel on unmount; one rAF loop.
- Test on a throttled CPU (4x) and a mid-range phone viewport.
- `prefers-reduced-motion: reduce`: replace movement with instant or opacity-only changes,
  stop parallax/auto-play/loops, keep essential state feedback. Provide pause for anything
  over 5s (WCAG 2.2.2). Nothing flashes more than 3 times per second (WCAG 2.3.1).
- Motion never delays task completion: skippable intros, no animation on repeat visits to
  the same view within a session.

## 7. Verify before claiming it works
Run it. Record or screenshot at several time points (0%, 25%, 50%, 100%) and confirm
start/end states, no layout shift, no jank, reduced-motion path works, and nothing is
left half-animated when interrupted. If you could not run it, say so.

## 8. Slop tells to avoid
Everything fading up with identical 0.6s ease on scroll; infinite bouncing arrows;
gratuitous parallax; gradient blobs drifting forever; cursor trails with no purpose;
animation that replays on every scroll direction change; overshoot on everything.
