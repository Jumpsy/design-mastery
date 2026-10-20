// Floating soft 3D shapes cluster (the "Stripe/Linear/Notion illustration" look). params: palette, seed, count, finish (clay|plastic|lacquer|metal), bg, studio
import { studio, mat, roundedBox, rng, lens, palette } from '../lib/kit.js';
export async function build({ THREE, scene, camera, params }) {
  const { palette: pal = 'candy', seed = 7, count = 9, finish = 'plastic', bg = null, studio: st = 'soft' } = params;
  studio(scene, { preset: st, bg });
  const cols = palette(pal), R = rng(seed);
  const geos = [
    () => new THREE.SphereGeometry(0.8, 96, 64),
    () => new THREE.TorusGeometry(0.7, 0.3, 64, 128),
    () => roundedBox(1.3, 1.3, 1.3, 0.28),
    () => new THREE.CapsuleGeometry(0.4, 0.9, 32, 64),
    () => new THREE.CylinderGeometry(0.6, 0.6, 0.6, 96).translate(0, 0, 0),
    () => new THREE.TorusKnotGeometry(0.55, 0.2, 200, 32),
  ];
  for (let i = 0; i < count; i++) {
    const g = geos[Math.floor(R() * geos.length)]();
    const c = cols[i % cols.length];
    const m = new THREE.Mesh(g, finish === 'metal' ? mat.metal(c, 0.18) : (mat[finish] || mat.plastic)(c));
    const a = (i / count) * Math.PI * 2 + R();
    const rad = 1.2 + R() * 2.4;
    m.position.set(Math.cos(a) * rad * 1.4, (R() - 0.5) * 3.2, Math.sin(a) * rad * 0.8 - 1);
    m.rotation.set(R() * 6, R() * 6, R() * 6);
    m.scale.setScalar(0.55 + R() * 0.8);
    scene.add(m);
  }
  lens(camera, { pos: [0, 0.3, 14], look: [0, 0, -1], fov: 30 });
}
