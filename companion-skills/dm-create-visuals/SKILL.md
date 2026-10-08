---
name: dm-create-visuals
description: How Claude CREATES the hero subject and its animation by itself (no Flow or image generator needed) instead of only laying out type - cars, products, scenes, icons, gauges. Method ladder: layered mirrored vector render, procedural three.js 3D, precise SVG/canvas, with working templates, honest limits, legal rules (no logos, no real people, no trademark-bearing output) and animation recipes. Use whenever a design needs a realistic or illustrated subject, a hero visual, or a looping/scroll-driven animation of one.
license: MIT
---

# Create visuals (subjects + animation)

Pick the method by how REAL the subject must look. Do not pretend a lower rung looks like a higher one.

## Works with Claude alone (no image generator, no Flow, no accounts)
Everything below is code Claude writes itself. External generators are an optional extra the
user may already have, never a requirement.

## Method ladder (pick by how real the subject must look; never oversell a rung)
1. **Layered vector render (best for a hero that must read as a real object, fastest to polish).**
   Template: `templates/supercar-front.html` (front-on generic supercar: mirrored half, gradient
   paint, glass canopy, LED headlights, mesh intakes, carbon splitter, dusk track backdrop, CSS
   motion). Method: draw ONE half of a symmetric subject and mirror it with `<use transform="translate(W 0) scale(-1 1)">`;
   build in layers (backdrop, contact shadow, tyres, body, form shading, glass, lights, intakes,
   trim); fake form with linear/radial gradients plus blurred highlight strokes (`feGaussianBlur`)
   along every crest and soft dark strokes in every crease; add reflections to glass; keep one
   consistent light direction; end with a moving specular sweep clipped to the body.
2. **Interactive stylized 3D:** `templates/supercar-3d.html` (three.js, lofted profile body, PBR
   clearcoat, studio env, scroll-driven orbit). Reads as a stylized concept car, not a real model.
3. **Precise 2D diagrams/gauges/abstract speed art:** exact SVG/canvas geometry from trig and measured
   points. Never freehand clip-art of a complex object; abstract instead.
4. **Video:** Remotion or CSS/SVG timelines; see `dm-motion-graphics`, `vendored/video-shotcraft`.
5. **Optional photoreal:** only if the user already has an image/video generator connected. Prompt as a
   photographer (subject, lens, angle, light, surface, palette) with "no logos, badges, text, plates,
   people"; ask before spending credits; strip any mark from results. Do not make the skill depend on it.

Honest limits: rungs 1-3 are original illustrations, not photographs. Say so, and push craft
(lighting, reflections, edge highlights, contact shadow) until it stops looking like clip-art.

## How to study a reference without copying it
Look at a photo of the kind of subject (a person's reference, a stock shot) to learn its ANATOMY:
proportions, silhouette, where highlights and creases fall, what is glossy vs matte. Then draw an
original, generic version from that understanding. Never trace or reproduce the photo, its badge or
a specific model's distinctive design; keep the result generic ("red mid-engine supercar").

## Procedural 3D checklist (three.js)
- Build from lofted shapes (`ExtrudeGeometry` of a side profile with bevel), then deform vertices (plan taper, shoulder tuck) and `computeVertexNormals()`.
- Materials: `MeshPhysicalMaterial` with `clearcoat`, `metalness` .5, low `roughness`; dark glass; separate glasshouse sitting ON the beltline (do not bury it inside the body).
- Lighting is 80% of "premium": a painted equirect studio env (softboxes) through `PMREMGenerator`, one key, one warm/colored rim, soft contact shadow, low-gloss floor, `ACESFilmic` tone mapping, `sRGB` output.
- Wheel proportions and ride height make or break it: tyre radius about 0.30-0.35 of body height ratio, small gaps, visible arch.
- Canvas `position:fixed`, drive the camera from scroll progress, pause when hidden, `prefers-reduced-motion` = one still angle.
- Debug with fixed angles (`?a=` in the template): check side, 3/4 and front before shipping.

## Animation recipes
- Scroll-scrubbed orbit/dolly: camera angle = base + progress * arc; ease with `lerp` toward target for inertia.
- Reveal: clip-path or mask wipe on the hero image, then 1.04 to 1 scale settle (long ease-out).
- Parallax depth: split foreground subject / midground light streaks / background, move at 0.2 / 0.5 / 1.0 of scroll.
- Frame sequence: export 60-120 frames, preload, draw to canvas by scroll progress.

## Verify and be honest
Render and OPEN screenshots from 3 angles/scroll points. State plainly which rung you used and its limit ("stylized procedural car, not photoreal"). Follow `dm-grounding`.

## Legal
No trademarks, logos, badges, real people or copyrighted images. A brand name may appear only as plain text on a clearly labelled unofficial concept. When mimicking a famous product's look, keep it generic and never claim it is the real thing.
