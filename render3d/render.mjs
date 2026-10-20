#!/usr/bin/env node
// Usage: node render.mjs <scene> [--out file.png] [--w 1920] [--h 1080] [--samples 128]
//        [--bounces 8] [--transparent] [--params '{"color":"#fff"}']
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const root = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf('--' + k); return i < 0 ? d : args[i + 1]; };
const flag = (k) => args.includes('--' + k);
const scene = args.find(a => !a.startsWith('--') && !args[args.indexOf(a) - 1]?.startsWith('--'));
if (!scene) { console.error('usage: node render.mjs <scene> [--out f.png --w --h --samples --transparent --params json]'); process.exit(1); }
const W = +opt('w', 1920), H = +opt('h', 1080), samples = +opt('samples', 128);
const out = path.resolve(opt('out', `${scene}.png`));

let chromium;
for (const p of [path.join(process.env.HOME, 'mcp/google-flow-browser-mcp/node_modules/playwright-core'), 'playwright-core', 'playwright']) {
  try { chromium = createRequire(import.meta.url)(p).chromium; break; } catch {}
}
if (!chromium) { console.error('Need playwright-core: run `npm i playwright-core` in render3d/'); process.exit(1); }

const types = { '.js': 'text/javascript', '.mjs': 'text/javascript', '.html': 'text/html', '.json': 'application/json', '.hdr': 'application/octet-stream', '.glb': 'model/gltf-binary' };
const server = http.createServer((req, res) => {
  const u = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  const f = path.join(root, u === '/' ? 'stage.html' : u);
  if (!f.startsWith(root) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
}).listen(0);
const port = server.address().port;

const browser = await chromium.launch({
  channel: 'chrome', headless: true,
  args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist', '--enable-unsafe-webgpu', '--disable-web-security'],
});
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
page.on('console', m => { if (flag('verbose')) console.log('[page]', m.text()); });
page.on('pageerror', e => console.error('[pageerror]', e.message));
const qs = new URLSearchParams({ scene, w: W, h: H, samples, bounces: opt('bounces', 8), transparent: flag('transparent') ? 1 : 0, params: opt('params', '{}'), post: opt('post', '{}'), exposure: opt('exposure', 1) });
await page.goto(`http://localhost:${port}/?${qs}`);
await page.waitForFunction(() => window.__done || window.__error, null, { timeout: +opt('timeout', 900000), polling: 500 });
const err = await page.evaluate(() => window.__error);
if (err) { console.error(err); await browser.close(); server.close(); process.exit(1); }
const data = await page.evaluate(() => window.__result);
fs.writeFileSync(out, Buffer.from(data.split(',')[1], 'base64'));
console.log('wrote', out);
await browser.close(); server.close();
