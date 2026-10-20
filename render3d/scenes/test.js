import { makeEnv, STUDIOS } from '../lib/studio.js';
export async function build({ THREE, scene, camera }) {
  scene.environment = scene.background = makeEnv(STUDIOS.soft);
  const m = new THREE.Mesh(new THREE.SphereGeometry(1.5, 128, 64),
    new THREE.MeshStandardMaterial({ color: '#7aa2ff', metalness: 0.2, roughness: 0.15 }));
  scene.add(m);
  const f = new THREE.Mesh(new THREE.PlaneGeometry(40, 40), new THREE.MeshStandardMaterial({ color: '#333', roughness: .5 }));
  f.rotation.x = -Math.PI / 2; f.position.y = -1.5; scene.add(f);
}
