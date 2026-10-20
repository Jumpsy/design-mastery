# render3d: free 3D-rendered images for websites and apps

Headless Chrome + three.js + a GPU path tracer. No Blender, no image generator, no credits.
Output is a real path-traced PNG (soft shadows, true reflections, global light) with denoise, bloom, grain and optional transparent background.

## Setup (once)
    cd render3d && npm install

## Render
    node render.mjs <scene> --out hero.png --w 2400 --h 1350 --samples 192
    node render.mjs shapes --params '{"palette":"midnight","finish":"lacquer","seed":3}'
    node render.mjs icon3d --transparent --params '{"color":"#6366f1","symbol":"bolt"}'

Flags: `--w --h --samples --bounces --transparent --exposure --params '<json>' --post '<json>' --verbose`
Post json: `bloom` (0.35), `vignette` (0), `grain` (0.025), `contrast`, `saturate`, `denoise` radius (2), `denoiseStrength` (28).

## Scenes (scenes/*.js)
| scene | use |
|---|---|
| `shapes` | floating soft shapes cluster, feature/illustration spots (palette, seed, count, finish) |
| `orb` | hero orb with ring (color, ring, glass) |
| `podium` | product podium with floating hero object (color, object) |
| `ribbon` | interlocked chrome/metal rings, dark hero art (finish, color) |
| `icon3d` | 3D app icon tile with symbol (color, symbol, symbolColor) |

Add a scene: copy one, export `async build({THREE, scene, camera, params})`. Use `lib/kit.js` (`studio`, `mat`, `roundedBox`, `floor`, `lens`, `palette`, `rng`).

## Timing (Apple M1)
1280x720 at 64 samples is about 15 s. 2400x1350 at 192 samples is a few minutes. Preview small, then final.

## Rules learned
- Use MeshStandardMaterial recipes in `mat` (lacquer, plastic, clay, metal, chrome). Glass/transmission can render black on some GPUs (see companion-skills/dm-visual-to-3d probe).
- The path tracer needs an equirect DataTexture environment (`lib/studio.js`), not a PMREM cube. The backdrop is a separate softbox-free gradient so lights never show.
- Chrome needs a bright environment; on dark studios it reads as black streaks.
- `--transparent` renders a matte pass; floors are excluded from alpha. Put a CSS shadow under the PNG.
- Long lens (fov 28-30), off-center framing, soft area light: that is what makes it read as a photo, not CG.
- Always LOOK at the PNG before shipping. Raise samples if grain shows. Never claim it matches a specific image generator; say it is a rendered 3D look.
