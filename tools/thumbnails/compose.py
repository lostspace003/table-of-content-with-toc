"""compose.py - 1280x720 course thumbnails: gpt-image-2 background + exact title + domain tag + the course's own tool icons + Gennoor logo.
usage: python compose.py <tocsrc dir> <bg dir> <out dir> [course index ...]      (HTML + Playwright, one page at a time)"""
import sys, os, base64, html, re
from pathlib import Path
SRC = Path(sys.argv[1]); BG = Path(sys.argv[2]); OUT = Path(sys.argv[3]); OUT.mkdir(parents=True, exist_ok=True)
only = set(int(x) for x in sys.argv[4:])
sys.path.insert(0, str(SRC))
import content as c
from icons import icon_svg

# supporting tooling that every course shares; the thumbnail shows what is specific to the course
SKIP = {'anthropic', 'pydantic', 'pytest', 'json', 'githubactions', 'python', 'generic:invoice', 'generic:cert', 'generic:key', 'generic:users'}
MAX_ICONS = 6
logo = "data:image/png;base64," + base64.b64encode((SRC / "logo-dark.png").read_bytes()).decode()


def icons_for(x):
    picked = [t for t in x['tools'] if t[0] not in SKIP][:MAX_ICONS]
    return picked


def fit_size(title):
    n = len(title)
    return 58 if n <= 30 else 51 if n <= 44 else 45 if n <= 56 else 40


def page(i, x):
    th = x['theme']
    domain = 'Agentic Cybersecurity' if x['title'].startswith('Agentic') else 'Automation with Claude'
    bg = "data:image/png;base64," + base64.b64encode((BG / f"bg_{i:02d}.png").read_bytes()).decode()
    chips = ''.join(
        f'<div class="chip"><div class="tile">{icon_svg(s, 44)}</div><span>{html.escape(l)}</span></div>' for s, l in icons_for(x))
    t = html.escape(x['title'])
    return f"""<!doctype html><meta charset=utf-8><style>
*{{box-sizing:border-box;margin:0}} html,body{{width:1280px;height:720px;overflow:hidden;background:{th['bg'][2]};font-family:'Segoe UI',Inter,Arial,sans-serif}}
.bg{{position:absolute;inset:0;background:url({bg}) center/cover no-repeat}}
.shade{{position:absolute;inset:0;background:linear-gradient(90deg,{th['bg'][2]}f2 0%,{th['bg'][2]}d9 38%,{th['bg'][2]}33 66%,transparent 100%)}}
.wrap{{position:absolute;left:64px;top:56px;bottom:56px;width:610px;display:flex;flex-direction:column}}
.logo{{height:44px;align-self:flex-start}}
.tag{{margin-top:44px;align-self:flex-start;padding:7px 16px;border-radius:999px;background:{th['accent']}26;border:1px solid {th['accent']}88;color:{th['accent2']};font-weight:700;font-size:17px;letter-spacing:.06em;text-transform:uppercase}}
h1{{margin-top:22px;color:#fff;font-weight:800;font-size:{fit_size(x['title'])}px;line-height:1.08;letter-spacing:-.02em;text-shadow:0 2px 24px rgba(0,0,0,.55)}}
.meta{{margin-top:20px;color:{th['accent2']};font-size:21px;font-weight:600}}
.chips{{margin-top:auto;display:flex;gap:16px;flex-wrap:nowrap}}
.chip{{display:flex;flex-direction:column;align-items:center;gap:8px;width:92px}}
.tile{{width:76px;height:76px;border-radius:18px;background:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 22px rgba(0,0,0,.4)}}
.chip span{{color:#dbe3f0;font-size:13px;font-weight:600;text-align:center;line-height:1.15}}
</style><div class=bg></div><div class=shade></div>
<div class=wrap><img class=logo src="{logo}"><div class=tag>{domain}</div><h1>{t}</h1><div class=meta>3 days &middot; 24 hours &middot; instructor-led training</div><div class=chips>{chips}</div></div>"""


def main():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--disable-gpu"])
        for i, x in enumerate(c.COURSES, 1):
            if only and i not in only: continue
            if not (BG / f"bg_{i:02d}.png").exists(): print("no bg", i); continue
            pg = b.new_page(viewport={"width": 1280, "height": 720})
            pg.set_content(page(i, x)); pg.wait_for_timeout(250)
            pg.screenshot(path=str(OUT / f"thumb_{i:02d}.png")); pg.close(); print("thumb", i, flush=True)
        b.close()


main()
