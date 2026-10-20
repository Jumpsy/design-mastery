// Hero orb: glossy sphere with orbiting ring on a soft studio floor. params: color, ring, bg, studio, glass(bool)
import { studio, mat, floor, lens } from '../lib/kit.js';
export async function build({ THREE, scene, camera, params }) {
  const { color = '#7aa2ff', ring = '#ffffff', bg = null, studio: st = 'soft', glass = false, floorColor = '#eef0f7' } = params;
  studio(scene, { preset: st, bg });
  floor(scene, { y: -1.6, color: floorColor, roughness: 0.25 });
  const orb = new THREE.Mesh(new THREE.SphereGeometry(1.6, 160, 96), glass ? mat.glass(color) : mat.lacquer(color));
  scene.add(orb);
  const torus = new THREE.Mesh(new THREE.TorusGeometry(2.4, 0.12, 48, 200), mat.metal(ring, 0.1));
  torus.rotation.set(1.2, 0.3, 0.2); scene.add(torus);
  const small = new THREE.Mesh(new THREE.SphereGeometry(0.35, 64, 48), mat.glow('#ffffff', 3));
  small.position.set(2.2, 1.4, 1); scene.add(small);
  lens(camera, { pos: [0, 0.6, 12], look: [0, -0.1, 0], fov: 30 });
}
