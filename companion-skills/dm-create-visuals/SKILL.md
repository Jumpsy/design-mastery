---
name: dm-create-visuals
description: How to CREATE the hero subject and its animation instead of only laying out type - cars, products, characters, scenes, icons, gauges. A method ladder from photoreal AI image/video (Google Flow or other generators) down to procedural 3D (three.js) and precise SVG/canvas, with honest limits, legal rules (no logos, no real people, no trademark-bearing output) and animation recipes. Use whenever a design needs a realistic or illustrated subject, a hero visual, or a looping/scroll-driven animation of one.
license: MIT
---

# Create visuals (subjects + animation)

Pick the method by how REAL the subject must look. Do not pretend a lower rung looks like a higher one.

## Method ladder
1. **Photoreal subject (a real-looking car, product, place, person-free scene):** use an image/video generator. Check what is connected: Google Flow tools (`flow_list_accounts` first; if not connected, ask the user to click Connect Flow in the Login Bridge extension and wait), otherwise any image-generation MCP/CLI the user has. Generate 2-4 variants, pick one, then animate (generator video, or parallax / 2.5D depth split in CSS/WebGL, or a scroll-scrubbed frame sequence).
   - Prompt like a photographer: subject, camera (lens, height, angle), light (key/rim/softbox, time of day), surface/reflections, palette, mood, aspect ratio, and an explicit negative: "no logos, no badges, no text, no license plate, no watermark, no people".
   - Describe the subject generically ("red Italian mid-engine supercar") never as a trademarked model name; strip every badge/logo from results before use. Never generate a real person's likeness.
   - Require the user's explicit OK before spending generation credits.
2. **Stylized 3D, interactive (turntable, scroll-orbit):** procedural three.js. See `templates/supercar-3d.html` (generic supercar built from lofted profiles, PBR clearcoat paint, studio env, scroll-driven camera, reduced-motion still). Honest limit: this reads as a stylized concept car, never as a specific real model. Use it when interactivity beats realism, or as a fallback.
3. **Precise 2D (gauges, icons, diagrams, abstract speed art):** hand-written SVG/canvas with exact geometry (tick marks from trig, strokes via `stroke-dasharray`, paths from measured points). Never freehand clip-art of a complex object (cars, faces, animals): it always reads amateur. Prefer abstraction (light streaks, rotor, track line) over a bad literal drawing.
4. **Video/motion piece:** Remotion (React frames) or generator video; see `dm-motion-graphics` and `vendored/video-shotcraft`.

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
