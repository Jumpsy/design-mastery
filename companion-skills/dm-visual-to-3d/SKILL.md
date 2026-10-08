---
name: dm-visual-to-3d
description: Turn any visual (photo, sketch, screenshot, description) into a 3D model and render it as 4K (3840x2160) path-traced stills and animation that read as photographs, using only a web browser - no Blender, no installs, no image generator. Reference-driven modelling with measurable compare loops, mesh QA gates, physically based lighting, photographic post, in-browser 4K WebM turntables, and honest limits. Use when a design needs a 3D hero object, product shot, turntable or camera-move animation.
license: MIT
---

# Visual to 3D to 4K (browser only)

Everything runs in a normal browser (Chrome/Edge; Safari for stills): three.js + a WebGL path tracer loaded
from a CDN. Claude writes the model as code; the page renders it with real light transport (soft shadows,
true reflections, depth of field) and encodes video in-browser (WebCodecs). No Blender, no ffmpeg.

## Honest scope: what "perfect" means here
"No mistakes" cannot be promised for a model Claude builds from code. What this skill GUARANTEES is a
verified process: every model passes the QA gates below, is compared to the reference numerically and
visually, and the report states what still differs. Two limits to say out loud:
- **Rendering can be photographic; procedural modelling is the bottleneck.** A parametric car looks like a
  toy even at 4K (measured: see `templates/pathtraced-car.html`). Light and resolution cannot hide simple geometry.
- **To reach "doesn't look 3D", model fidelity must be high.** Either invest in many refinement passes
  (bevels, panel gaps, thickness, correct curvature), or load a properly licensed glTF/GLB made by an artist
  (`?model=file.glb`) and let this pipeline light, camera, render and animate it at 4K.

## Pipeline (follow in order; do not skip the gates)
1. **Analyse the reference.** List the object's measured proportions (length:width:height, wheelbase, overhangs,
   key curvature, material list: paint/glass/rubber/metal). Use only what you can see; mark guesses as guesses
   (`dm-grounding`). Study the photo for anatomy; never trace or reproduce a protected design, badge or logo.
2. **Blockout** in `templates/pathtraced-car.html` style: lofted cross-sections (`loft()`), primitives, CSG.
   Get silhouette and scale right first, details last.
3. **QA gates (all must pass before any slow render):**
   - Closed mesh: every edge shared by exactly 2 faces (`watertight()` -> 0 open edges).
   - Outward faces: positive signed volume (`volume()`; `orient()` fixes it). Required for CSG booleans.
   - Normals outward (spot-check), correct real-world scale (metres), object sits on the floor, nothing floating.
   - Raster check views (`?view=normals`, side/front/top via `&az=&el=`): 1 second each, catches 90% of errors.
   - Isolate parts (`?only=hull`, swap in a plain diffuse material) when something looks wrong.
4. **Compare to the reference** with `tools/compare.html` (blend, difference, edge overlap IoU) from a matching
   camera angle. Fix the largest error first; repeat until the edge IoU stops improving. Report the final number.
5. **Materials** (see recipe below), then **lighting + camera**, then a **low-res path-traced preview**
   (960x540, 64 samples, ~10 s) and open it. Iterate here, never at 4K.
6. **Final render:** `renderStill({w:3840,h:2160,samples:256})` or the "Save 4K PNG" button. Verify the file is
   really 3840x2160 and look at a 100% crop for noise, fireflies, banding.
7. **Animate** if asked (below), previewing at 1080p first.
8. **Report** honestly: resolution, samples, render time, what still reads as CG, what you could not verify.

## "Doesn't look like a 3D model" recipe
- **Geometry:** bevel every hard edge (real objects have radii), panel gaps/thickness, no perfectly flat large
  faces, asymmetry in small details, correct wheel/arch/clearance relationships.
- **Materials:** physically plausible values; add micro-variation to roughness (noise), subtle fingerprints/dust on
  glass, anisotropy on brushed metal. Dark rubber is dark (albedo ~0.03), never grey.
- **Light:** large soft area lights (softboxes/strips) so reflections have shape; a gradient strip down the flank;
  a warm rim light; low fill so shadows are not dead black; a contact shadow under every object.
- **Camera:** long lens (70-120 mm equivalent), low angle, shallow depth of field focused on the key feature,
  slight imperfection in framing. Wide lenses scream "CG".
- **Post (applied to the final pixels):** subtle bloom on highlights, vignette, tiny chromatic fringe, film grain,
  filmic tone mapping. Implemented in `post()`.

## Hard-won rules (from building the template; each cost real debugging time)
- `MeshPhysicalMaterial` with `clearcoat` rendered BLACK in this path tracer build. Use `MeshStandardMaterial`
  (metalness ~0.6, roughness ~0.2) for car paint; fake gloss with low roughness. Test any new material feature on a
  sphere first.
- Environment maps lit horizontal faces poorly in testing (floor and roof lit, sides black). Drive the look with explicit
  `RectAreaLight` softboxes (sampled directly, predictable) and keep the env as faint fill.
- Power: area light intensities of 5-12 are plenty for a ~9 m camera distance; start low and raise.
- CSG (`three-bvh-csg`) needs closed, outward-wound meshes WITH a `uv` attribute.
- `loft(len, keys, options)`: station arrays go in `keys`; `x0`/`x1` range goes in `options` (mixing them stretched
  a cabin along the whole car).
- A path tracer must accumulate samples across animation frames (`renderSample()` in a rAF loop until
  `samples >= N`); a single call only shows a raster preview.
- Glass: keep it opaque, glossy and dark (roughness 0.04) unless you need see-through; transmission is slow and noisy.

## Timing (measured on an Apple M4, Chrome/Metal; scale by your hardware)
- 1280x720, 128 samples: ~20 s. 3840x2160 (8.3 MP), 256 samples: ~4 min per still.
- Video cost = frames x per-frame time. 4K at 96 samples is ~1.5 min/frame; 48 frames ~ 70 min. Always say the
  estimate before starting and offer 1080p. In-browser encoding: `renderTurntable({w,h,frames,fps,samples,arc})`
  returns a VP9 WebM Blob (level selected automatically for 4K); tested decoding at 640x360.
- Keep the tab visible and the machine awake during long renders.

## Animation recipes
- Turntable / camera arc: `renderTurntable` (ease in-out). Add dolly by changing `dist`, tilt by `el`.
- Cheaper "4K look" motion: render one 4K still plus a depth pass, then do small parallax moves in WebGL.
- Object motion (rolling wheels, opening doors): keyframe transforms per frame before `pt.reset()`.
- Always render motion blur-free frames at a fixed shutter-less look unless you accumulate sub-frame samples.

## Legal and safety
Original models only, or glTF with a licence that permits your use (check and record it). No trademarks/logos/badges,
no real people, no copying a protected design. Label concept work as unofficial. Never present a procedural stand-in as the real product.

Files: `templates/pathtraced-car.html` (scene, loft, CSG, QA gates, studio, camera, post, 4K still, WebM turntable,
glTF loader), `tools/compare.html` (reference vs render).
