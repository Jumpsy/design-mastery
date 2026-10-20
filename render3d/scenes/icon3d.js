// 3D app-icon tile with an embossed symbol. params: color, symbol (circle|plus|bolt|heart|star), bg, studio
import { studio, mat, floor, lens, roundedBox } from '../lib/kit.js';
export async function build({ THREE, scene, camera, params }) {
  const { color = '#6366f1', symbol = 'star', symbolColor = '#ffffff', bg = null, studio: st = 'soft' } = params;
  studio(scene, { preset: st, bg });
  floor(scene, { y: -1.7, color: '#eef0f7', roughness: 0.3 });
  const tile = new THREE.Mesh(roundedBox(3.2, 3.2, 0.9, 0.42), mat.plastic(color)); tile.rotation.set(-0.25, 0.5, 0.08); scene.add(tile);
  const s = new THREE.Shape();
  if (symbol === 'circle') s.absarc(0, 0, 0.8, 0, Math.PI * 2);
  else if (symbol === 'plus') { const a = 0.25, b = 0.85; s.moveTo(-a, -b); s.lineTo(a, -b); s.lineTo(a, -a); s.lineTo(b, -a); s.lineTo(b, a); s.lineTo(a, a); s.lineTo(a, b); s.lineTo(-a, b); s.lineTo(-a, a); s.lineTo(-b, a); s.lineTo(-b, -a); s.lineTo(-a, -a); }
  else if (symbol === 'bolt') { [[0.2, 1], [-0.65, -0.1], [-0.05, -0.1], [-0.25, -1], [0.65, 0.15], [0.05, 0.15]].forEach(([x, y], i) => i ? s.lineTo(x, y) : s.moveTo(x, y)); }
  else if (symbol === 'heart') { s.moveTo(0, -0.9); s.bezierCurveTo(-1.4, 0.1, -0.7, 1.0, 0, 0.4); s.bezierCurveTo(0.7, 1.0, 1.4, 0.1, 0, -0.9); }
  else { for (let i = 0; i < 10; i++) { const r = i % 2 ? 0.38 : 0.95, a = Math.PI / 2 + i * Math.PI / 5; i ? s.lineTo(Math.cos(a) * r, Math.sin(a) * r) : s.moveTo(Math.cos(a) * r, Math.sin(a) * r); } }
  const g = new THREE.ExtrudeGeometry(s, { depth: 0.25, bevelEnabled: true, bevelThickness: 0.1, bevelSize: 0.1, bevelSegments: 10, curveSegments: 48 });
  const sym = new THREE.Mesh(g, mat.lacquer(symbolColor)); sym.position.z = 0.5; tile.add(sym);
  lens(camera, { pos: [0, 0.5, 11], look: [0, 0, 0], fov: 30 });
}
