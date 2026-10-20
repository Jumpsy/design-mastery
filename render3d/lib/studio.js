// Procedural studio environment: float equirect map with gradient + soft boxes.
// The path tracer needs an equirect DataTexture (not a PMREM cube).
import * as THREE from 'three';

// boxes: [{az, el, size (deg), color, intensity}] az/el in degrees, 0 az = toward camera (+z)
export function makeEnv({ top = '#202838', bottom = '#0a0b10', horizon = null, boxes = [], w = 512, h = 256, ambient = 1 } = {}) {
  const data = new Float32Array(w * h * 4);
  const ct = new THREE.Color(top), cb = new THREE.Color(bottom), ch = new THREE.Color(horizon || top).lerp(cb, 0.5);
  const c = new THREE.Color();
  const bx = boxes.map(b => ({ ...b, c: new THREE.Color(b.color || '#fff'), az: THREE.MathUtils.degToRad(b.az), el: THREE.MathUtils.degToRad(b.el), s: THREE.MathUtils.degToRad(b.size || 30) }));
  for (let y = 0; y < h; y++) {
    const el = (0.5 - (y + 0.5) / h) * Math.PI;
    const t = (el / (Math.PI / 2));
    for (let x = 0; x < w; x++) {
      const az = ((x + 0.5) / w - 0.5) * Math.PI * 2;
      if (t >= 0) c.copy(ch).lerp(ct, Math.pow(t, 0.7)); else c.copy(ch).lerp(cb, Math.pow(-t, 0.7));
      c.multiplyScalar(ambient);
      for (const b of bx) {
        let da = Math.abs(az - b.az); if (da > Math.PI) da = 2 * Math.PI - da;
        const de = Math.abs(el - b.el);
        const k = Math.max(da / (b.s * (b.aspect || 1)), de / b.s);
        const f = k < 1 ? Math.min(1, (1 - k) * 4) : 0; // soft edge
        if (f > 0) c.r += b.c.r * b.intensity * f, c.g += b.c.g * b.intensity * f, c.b += b.c.b * b.intensity * f;
      }
      const i = (y * w + x) * 4; data[i] = c.r; data[i + 1] = c.g; data[i + 2] = c.b; data[i + 3] = 1;
    }
  }
  const tex = new THREE.DataTexture(data, w, h, THREE.RGBAFormat, THREE.FloatType);
  tex.mapping = THREE.EquirectangularReflectionMapping;
  tex.magFilter = tex.minFilter = THREE.LinearFilter;
  tex.generateMipmaps = false;
  tex.needsUpdate = true;
  return tex;
}

export const STUDIOS = {
  soft: { top: '#d8e0ff', bottom: '#1a1a22', boxes: [{ az: -40, el: 30, size: 28, intensity: 14 }, { az: 60, el: 10, size: 14, intensity: 8, color: '#ffd9b0' }, { az: 180, el: 25, size: 20, intensity: 10, color: '#a8c4ff' }] },
  dark: { top: '#10131c', bottom: '#050507', boxes: [{ az: -50, el: 25, size: 22, intensity: 18 }, { az: 80, el: 5, size: 8, intensity: 14, color: '#7aa2ff' }, { az: 170, el: 20, size: 16, intensity: 12, color: '#ff9ad0' }] },
  light: { top: '#ffffff', bottom: '#d9dce6', ambient: 1.1, boxes: [{ az: -35, el: 40, size: 35, intensity: 9 }, { az: 70, el: 10, size: 20, intensity: 5 }] },
};
