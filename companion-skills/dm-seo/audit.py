#!/usr/bin/env python3
"""Basic on-page SEO audit. Usage: audit.py BASE_URL PATH [PATH ...]
Requires: pip install playwright (uses installed Google Chrome)."""
import json
import sys
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright

JS = """() => {
  const q = s => document.querySelector(s);
  const meta = q('meta[name="description"]');
  const imgs = [...document.images];
  return {
    overflow: document.documentElement.scrollWidth > window.innerWidth + 1,
    h1: document.querySelectorAll('h1').length,
    title: document.title || '',
    desc: meta ? (meta.content || '') : '',
    canonical: (q('link[rel="canonical"]') || {}).href || '',
    ld: [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => s.textContent),
    broken: imgs.filter(i => i.complete && i.naturalWidth === 0 && i.currentSrc).map(i => i.currentSrc),
    noalt: imgs.filter(i => !i.hasAttribute('alt')).map(i => i.currentSrc || i.src),
  };
}"""


def check(page, url):
    r = {}
    resp = page.goto(url, wait_until="networkidle", timeout=45000)
    status = resp.status if resp else 0
    # force lazy images to load before checking
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(800)
    page.evaluate("window.scrollTo(0, 0)")
    d = page.evaluate(JS)
    ld_ok, ld_err = True, ""
    for raw in d["ld"]:
        try:
            json.loads(raw)
        except Exception as e:
            ld_ok, ld_err = False, str(e)[:40]
    r["status 200"] = (status == 200, str(status))
    r["no overflow 390px"] = (not d["overflow"], "")
    r["one h1"] = (d["h1"] == 1, str(d["h1"]))
    r["title 10-60"] = (10 <= len(d["title"]) <= 60, str(len(d["title"])))
    r["desc 50-160"] = (50 <= len(d["desc"]) <= 160, str(len(d["desc"])))
    r["canonical"] = (bool(d["canonical"]), d["canonical"][-30:])
    r["json-ld valid"] = (ld_ok, ld_err or f"{len(d['ld'])} block(s)")
    r["no broken img"] = (not d["broken"], str(len(d["broken"])))
    r["alt present"] = (not d["noalt"], str(len(d["noalt"])))
    return r


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    base, paths = sys.argv[1], sys.argv[2:]
    failed = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        ctx = browser.new_context(viewport={"width": 390, "height": 844})
        page = ctx.new_page()
        for path in paths:
            url = urljoin(base if base.endswith("/") else base + "/", path.lstrip("/"))
            print(f"\n{url}")
            try:
                res = check(page, url)
            except Exception as e:
                print(f"  ERROR {str(e)[:100]}")
                failed += 1
                continue
            for name, (ok, note) in res.items():
                failed += not ok
                print(f"  {'PASS' if ok else 'FAIL'}  {name:<20} {note}")
        browser.close()
    print(f"\n{failed} failure(s)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
