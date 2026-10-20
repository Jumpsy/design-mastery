// Stage: loads a scene module, path-traces it, optional transparent matte + photographic post,
// stores the final PNG data URL in window.__result for render.mjs.
import * as THREE from 'three';
import { WebGLPathTracer } from 'three-gpu-pathtracer';

const q = new URLSearchParams(location.search);
const W = +q.get('w'), H = +q.get('h'), SAMPLES = +q.get('samples') || 128;
const BOUNCES = +q.get('bounces') || 8;
const transparent = q.get('transparent') === '1';
const post = JSON.parse(q.get('post') || '{}');
window.__log = [];
const log = (m) => { window.__log.push(String(m)); console.log(m); };

async function trace(renderer, scene, camera, samples, tag) {
  const pt = new WebGLPathTracer(renderer);
  Object.assign(pt, { renderToCanvas: true, rasterizeScene: false, dynamicLowRes: false, minSamples: 0, fadeDuration: 0, renderDelay: 0 });
  pt.bounces = BOUNCES; pt.transmissiveBounces = Math.max(8, BOUNCES); pt.filterGlossyFactor = 0.5; pt.tiles.set(2, 2);
  pt.setScene(scene, camera);
  const t0 = performance.now();
  while (pt.samples < samples) { pt.renderSample(); await new Promise(r => requestAnimationFrame(r)); }
  log(`${tag}: ${pt.samples} samples ${((performance.now() - t0) / 1000).toFixed(1)}s`);
  const c = document.createElement('canvas'); c.width = W; c.height = H;
  const x = c.getContext('2d', { willReadFrequently: true }); x.drawImage(renderer.domElement, 0, 0);
  return c;
}

// Edge-preserving denoise (bilateral). radius r, color sigma sc. Runs on RGBA, leaves alpha.
function denoise(c, r, sc) {
  if (!r) return c;
  const x = c.getContext('2d', { willReadFrequently: true }), id = x.getImageData(0, 0, W, H), s = id.data, o = new Uint8ClampedArray(s.length);
  const inv = 1 / (2 * sc * sc), sp = []; for (let j = -r; j <= r; j++) for (let i = -r; i <= r; i++) sp.push([i, j, Math.exp(-(i * i + j * j) / (2 * (r * 0.6) ** 2))]);
  for (let y = 0; y < H; y++) for (let xx = 0; xx < W; xx++) {
    const k = (y * W + xx) * 4; let R = 0, G = 0, B = 0, ws = 0;
    for (const [i, j, w0] of sp) {
      const X = xx + i, Y = y + j; if (X < 0 || Y < 0 || X >= W || Y >= H) continue;
      const m = (Y * W + X) * 4, dr = s[m] - s[k], dg = s[m + 1] - s[k + 1], db = s[m + 2] - s[k + 2];
      const w = w0 * Math.exp(-(dr * dr + dg * dg + db * db) * inv); R += s[m] * w; G += s[m + 1] * w; B += s[m + 2] * w; ws += w;
    }
    o[k] = R / ws; o[k + 1] = G / ws; o[k + 2] = B / ws; o[k + 3] = s[k + 3];
  }
  id.data.set(o); x.putImageData(id, 0, 0); return c;
}

// Photographic finishing on the 2D canvas: bloom, vignette, grain, contrast.
function finish(c, p) {
  const bloom = p.bloom ?? 0.35, vig = p.vignette ?? 0.0, grain = p.grain ?? 0.025, contrast = p.contrast ?? 1.04, sat = p.saturate ?? 1.06;
  const out = document.createElement('canvas'); out.width = W; out.height = H;
  const x = out.getContext('2d', { willReadFrequently: true });
  x.filter = `contrast(${contrast}) saturate(${sat})`; x.drawImage(c, 0, 0); x.filter = 'none';
  if (bloom > 0) {
    const b = document.createElement('canvas'); b.width = W; b.height = H; const bx = b.getContext('2d');
    bx.filter = `brightness(0.9) contrast(2.2) blur(${Math.round(W / 90)}px)`; bx.drawImage(out, 0, 0);
    x.globalCompositeOperation = 'screen'; x.globalAlpha = bloom; x.drawImage(b, 0, 0); x.globalAlpha = 1; x.globalCompositeOperation = 'source-over';
  }
  if (vig > 0) { const g = x.createRadialGradient(W / 2, H / 2, Math.min(W, H) * 0.35, W / 2, H / 2, Math.hypot(W, H) * 0.55); g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, `rgba(0,0,0,${vig})`); x.fillStyle = g; x.fillRect(0, 0, W, H); }
  if (grain > 0) { const id = x.getImageData(0, 0, W, H), d = id.data; for (let i = 0; i < d.length; i += 4) { const n = (Math.random() - 0.5) * 255 * grain; d[i] += n; d[i + 1] += n; d[i + 2] += n; } x.putImageData(id, 0, 0); }
  return out;
}

try {
  const renderer = new THREE.WebGLRenderer({ antialias: false, alpha: true, preserveDrawingBuffer: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(1); renderer.setSize(W, H);
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = +(q.get('exposure') || 1);
  document.body.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, W / H, 0.1, 200);
  camera.position.set(0, 0, 8);
  const mod = await import(`/scenes/${q.get('scene')}.js`);
  const params = JSON.parse(q.get('params') || '{}');
  await mod.build({ THREE, scene, camera, renderer, W, H, params, transparent });
  camera.aspect = W / H; camera.updateProjectionMatrix();

  let beauty = await trace(renderer, scene, camera, SAMPLES, 'beauty');
  beauty = denoise(beauty, post.denoise ?? 2, post.denoiseStrength ?? 28);
  let final = finish(beauty, post);

  if (transparent) {
    // Matte pass: every mesh becomes flat white emissive, background black, no tone mapping.
    const white = new THREE.MeshBasicMaterial({ color: '#ffffff' });
    const hide = []; // floor-like helpers can opt out with userData.noMatte
    scene.traverse(o => { if (o.isMesh) { if (o.userData.noMatte) { o.visible = false; hide.push(o); } else o.material = new THREE.MeshStandardMaterial({ color: '#000', emissive: '#fff', emissiveIntensity: 1 }); } });
    scene.environment = null; scene.background = new THREE.Color('#000');
    renderer.toneMapping = THREE.NoToneMapping;
    const mask = await trace(renderer, scene, camera, Math.min(64, SAMPLES), 'matte');
    const m = mask.getContext('2d').getImageData(0, 0, W, H).data;
    const fx = final.getContext('2d'), id = fx.getImageData(0, 0, W, H), d = id.data;
    for (let i = 0; i < d.length; i += 4) d[i + 3] = m[i];
    fx.putImageData(id, 0, 0);
  }
  window.__result = final.toDataURL('image/png');
  window.__done = true;
} catch (e) {
  window.__error = String(e && e.stack || e);
  console.error(window.__error);
}
