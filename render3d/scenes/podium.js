// Product podium: stacked cylinders with a hero object floating above. params: color, object (sphere|torusknot|cube|capsule), bg, studio
import { studio, mat, floor, lens, roundedBox } from '../lib/kit.js';
export async function build({ THREE, scene, camera, params }) {
  const { color = '#ff6b9d', object = 'torusknot', bg = null, studio: st = 'soft', podium = '#f4f4f8' } = params;
  studio(scene, { preset: st, bg });
  floor(scene, { y: 0, color: podium, roughness: 0.4 });
  const base = new THREE.Mesh(new THREE.CylinderGeometry(2.4, 2.5, 0.35, 160), mat.clay(podium)); base.position.y = 0.175; scene.add(base);
  const top = new THREE.Mesh(new THREE.CylinderGeometry(1.7, 1.75, 0.5, 160), mat.plastic('#ffffff')); top.position.y = 0.6; scene.add(top);
  const g = { sphere: () => new THREE.SphereGeometry(1, 128, 96), torusknot: () => new THREE.TorusKnotGeometry(0.8, 0.28, 300, 48), cube: () => roundedBox(1.6, 1.6, 1.6, 0.3), capsule: () => new THREE.CapsuleGeometry(0.6, 1.2, 48, 96) }[object]();
  const o = new THREE.Mesh(g, mat.lacquer(color)); o.position.y = 2.5; o.rotation.set(0.4, 0.6, 0.1); scene.add(o);
  lens(camera, { pos: [0, 2.2, 13], look: [0, 1.6, 0], fov: 28 });
}
