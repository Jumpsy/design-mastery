// Shared building blocks for scenes: materials, rounded shapes, floor, camera, studio.
import * as THREE from 'three';
import { makeEnv, STUDIOS } from './studio.js';

export function studio(scene, { preset = 'soft', bg = null, ...over } = {}) {
  const env = makeEnv({ ...STUDIOS[preset], ...over });
  scene.environment = env;
  // Backdrop is a separate softbox-free gradient so lights never show in frame.
  scene.background = bg ? new THREE.Color(bg) : makeEnv({ ...STUDIOS[preset], ...over, boxes: [], w: 128, h: 64 });
  scene.environmentIntensity = 1;
  return env;
}

// Material recipes tuned for the path tracer (MeshStandard only: clearcoat/transmission are unreliable on some GPUs)
export const mat = {
  clay: (c) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.55, metalness: 0 }),
  plastic: (c) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.18, metalness: 0 }),
  lacquer: (c) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.06, metalness: 0.35 }),
  metal: (c = '#d9dbe0', r = 0.12) => new THREE.MeshStandardMaterial({ color: c, roughness: r, metalness: 1 }),
  chrome: () => new THREE.MeshStandardMaterial({ color: '#ffffff', roughness: 0.02, metalness: 1 }),
  glow: (c, i = 4) => new THREE.MeshStandardMaterial({ color: '#000', emissive: c, emissiveIntensity: i }),
  glass: (c = '#ffffff', ior = 1.45) => new THREE.MeshPhysicalMaterial({ color: c, roughness: 0.02, metalness: 0, transmission: 1, ior, thickness: 0.8 }),
  floor: (c = '#e9ebf2', r = 0.35) => new THREE.MeshStandardMaterial({ color: c, roughness: r, metalness: 0 }),
};

export function roundedBox(w, h, d, r = 0.12, seg = 8) {
  const s = new THREE.Shape(), x = -w / 2, y = -h / 2;
  s.moveTo(x + r, y); s.lineTo(x + w - r, y); s.quadraticCurveTo(x + w, y, x + w, y + r);
  s.lineTo(x + w, y + h - r); s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y);
  const g = new THREE.ExtrudeGeometry(s, { depth: d - 2 * r, bevelEnabled: true, bevelThickness: r, bevelSize: r, bevelSegments: seg, curveSegments: 16 });
  g.translate(0, 0, -(d - 2 * r) / 2);
  g.computeVertexNormals();
  return g;
}

export function floor(scene, { y = 0, color = '#eceef5', roughness = 0.35, size = 80 } = {}) {
  const m = new THREE.Mesh(new THREE.PlaneGeometry(size, size), mat.floor(color, roughness));
  m.rotation.x = -Math.PI / 2; m.position.y = y; m.userData.noMatte = true; scene.add(m); return m;
}

// Mulberry32: deterministic layouts so a seed reproduces an image
export function rng(seed = 1) { let a = seed >>> 0; return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }

// 35-100mm look: set a long lens and aim; returns focal for reference
export function lens(camera, { pos = [0, 1, 9], look = [0, 0, 0], fov = 28 } = {}) {
  camera.fov = fov; camera.position.set(...pos); camera.lookAt(new THREE.Vector3(...look)); camera.updateProjectionMatrix();
}

export const PALETTES = {
  candy: ['#ff6b9d', '#ffb86b', '#6bd5ff', '#a78bfa', '#ffffff'],
  midnight: ['#7aa2ff', '#a78bfa', '#22d3ee', '#f472b6', '#e6e9f5'],
  sunset: ['#ff7a45', '#ffb347', '#ff4d6d', '#7b2cbf', '#fff1e0'],
  mint: ['#34d399', '#a7f3d0', '#60a5fa', '#fde68a', '#ffffff'],
  mono: ['#111111', '#444444', '#888888', '#cccccc', '#ffffff'],
};
export function palette(p) { return Array.isArray(p) ? p : (PALETTES[p] || PALETTES.candy); }
