// Interlocked chrome/metal rings, abstract hero art. params: color, finish (chrome|metal|plastic), bg, studio
import { studio, mat, lens } from '../lib/kit.js';
export async function build({ THREE, scene, camera, params }) {
  const { color = '#7aa2ff', finish = 'chrome', bg = '#0b0c12', studio: st = 'soft' } = params;
  studio(scene, { preset: st, bg, ambient: 1 });
  const n = 4;
  for (let i = 0; i < n; i++) {
    const m = finish === 'chrome' ? mat.chrome() : finish === 'plastic' ? mat.plastic(color) : mat.metal(color, 0.1);
    const t = new THREE.Mesh(new THREE.TorusGeometry(2.1, 0.32, 64, 200), m);
    t.rotation.set(i * Math.PI / n, i * 0.5, i * 0.3);
    scene.add(t);
  }
  lens(camera, { pos: [0, 0, 13], look: [0, 0, 0], fov: 30 });
}
