"""Build the embeddable HTML TOC and the Gennoor-watermarked PDF for every course."""
import asyncio
import html
import sys
from pathlib import Path

from content import COURSES, COMMON_ASSESSMENT, SHARED_PRINCIPLES, INSTRUCTOR
from icons import icon_svg, gennoor_logo_svg, brand_color

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "TOC-output"


def esc(s):
    return html.escape(str(s))


CSS = """
:root{--gt-blue:#2563EB;--gt-amber:#F59E0B;--gt-ink:#1F2A44;--gt-ink2:#4A5568;--gt-muted:#6B7280;--gt-line:#E5E7EB;--gt-bg:#FFFFFF;--gt-soft:#F5F7FB;--gt-navy:#0E1538;}
*{box-sizing:border-box}
body{margin:0;background:var(--gt-bg);color:var(--gt-ink);font-family:Inter,"Segoe UI",Helvetica,Arial,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
.gt-toc{max-width:980px;margin:0 auto;padding:32px 24px 48px}
.gt-head{display:flex;justify-content:space-between;align-items:flex-start;gap:24px;border-bottom:3px solid var(--gt-blue);padding-bottom:20px}
.gt-head .gt-logo svg{display:block}
.gt-code{display:inline-block;background:var(--gt-amber);color:#1a1200;font-weight:800;font-size:12px;letter-spacing:.14em;text-transform:uppercase;padding:5px 10px;border-radius:6px}
h1.gt-title{font-size:34px;line-height:1.15;margin:12px 0 6px;font-weight:800;letter-spacing:-.02em}
.gt-tag{font-size:17px;color:var(--gt-ink2);margin:0 0 14px}
.gt-chips{display:flex;flex-wrap:wrap;gap:8px}
.gt-chip{display:inline-flex;align-items:center;gap:7px;background:var(--gt-soft);border:1px solid var(--gt-line);border-radius:999px;padding:6px 12px;font-size:13px;font-weight:600;color:var(--gt-ink2)}
.gt-chip svg{color:var(--gt-blue)}
.gt-instr{display:flex;align-items:center;gap:12px;margin-top:16px}
.gt-instr img{width:56px;height:56px;border-radius:50%;object-fit:cover;border:3px solid var(--gt-amber)}
.gt-instr b{display:block;font-size:15px}
.gt-instr span{font-size:13px;color:var(--gt-muted)}
h2.gt-h2{display:flex;align-items:center;gap:10px;font-size:20px;margin:34px 0 12px;padding-bottom:8px;border-bottom:1px solid var(--gt-line);letter-spacing:-.01em}
h2.gt-h2 svg{color:var(--gt-blue)}
.gt-grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media (max-width:700px){.gt-grid2{grid-template-columns:1fr}h1.gt-title{font-size:26px}}
.gt-card{background:var(--gt-soft);border:1px solid var(--gt-line);border-radius:12px;padding:16px 18px}
.gt-card h3{margin:0 0 8px;font-size:15px;display:flex;gap:8px;align-items:center}
.gt-card h3 svg{color:var(--gt-blue)}
.gt-card ul{margin:0;padding-left:18px;font-size:14px}
.gt-card li{margin:4px 0}
.gt-card p{margin:0;font-size:14px}
.gt-tools{display:flex;flex-wrap:wrap;gap:10px}
.gt-tool{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--gt-line);border-radius:10px;padding:8px 12px;font-size:13px;font-weight:600;background:#fff}
.gt-day{margin-top:26px}
.gt-dayhead{display:flex;align-items:center;gap:12px;margin:0 0 12px}
.gt-daynum{background:var(--gt-navy);color:#fff;font-weight:800;font-size:13px;letter-spacing:.12em;text-transform:uppercase;padding:6px 12px;border-radius:8px}
.gt-dayhead span{color:var(--gt-muted);font-size:14px}
.gt-mod{display:grid;grid-template-columns:56px 1fr;gap:14px;border:1px solid var(--gt-line);border-left:4px solid var(--gt-blue);border-radius:12px;padding:16px 18px 14px 14px;margin:10px 0;page-break-inside:avoid;break-inside:avoid;background:#fff}
.gt-modicon{width:56px;height:56px;border-radius:12px;background:var(--gt-soft);display:flex;align-items:center;justify-content:center}
.gt-mod h3{margin:0 0 6px;font-size:17px;letter-spacing:-.01em}
.gt-mod h3 small{display:block;color:var(--gt-muted);font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;margin-bottom:2px}
.gt-mod ul{margin:0 0 8px;padding-left:18px;font-size:14px;color:var(--gt-ink2)}
.gt-mod li{margin:3px 0}
.gt-lab{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:6px}
.gt-lab div{font-size:13px;background:var(--gt-soft);border-radius:8px;padding:8px 10px}
.gt-lab b{color:var(--gt-blue);font-size:11px;letter-spacing:.1em;text-transform:uppercase;display:block;margin-bottom:2px}
.gt-lab div:nth-child(2) b{color:#B45309}
@media (max-width:600px){.gt-lab{grid-template-columns:1fr}}
.gt-cap{background:linear-gradient(135deg,#0E1538,#1E3A8A);color:#fff;border-radius:14px;padding:22px 24px;display:grid;grid-template-columns:56px 1fr;gap:16px;align-items:start}
.gt-cap h3{margin:0 0 6px;font-size:18px}.gt-cap p{margin:0;font-size:15px;color:#DCE4F5}
table.gt-tab{width:100%;border-collapse:collapse;font-size:14px}
table.gt-tab th{text-align:left;background:var(--gt-navy);color:#fff;padding:9px 12px;font-weight:700}
table.gt-tab td{padding:9px 12px;border-bottom:1px solid var(--gt-line);vertical-align:top}
table.gt-tab td:nth-child(2){font-weight:700;color:var(--gt-blue);white-space:nowrap}
.gt-princ{margin:0;padding-left:20px;font-size:14px;color:var(--gt-ink2)}
.gt-princ li{margin:5px 0}
.gt-foot{margin-top:36px;border-top:1px solid var(--gt-line);padding-top:14px;display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--gt-muted);flex-wrap:wrap;gap:8px}
.gt-foot a{color:var(--gt-blue);font-weight:600;text-decoration:none}
@page{size:A4;margin:14mm 12mm}
@media print{body{-webkit-print-color-adjust:exact;print-color-adjust:exact}.gt-toc{max-width:none;padding:0}.gt-day{page-break-before:auto}}
"""


def module_block(i, m):
    topics = "".join(f"<li>{esc(t)}</li>" for t in m["topics"])
    return f"""
<div class="gt-mod">
  <div class="gt-modicon">{icon_svg(m['icon'], 30)}</div>
  <div>
    <h3><small>Module {i}</small>{esc(m['title'])}</h3>
    <ul>{topics}</ul>
    <div class="gt-lab">
      <div><b>Hands-on lab</b>{esc(m['lab'])}</div>
      <div><b>Deliverable</b>{esc(m['deliverable'])}</div>
    </div>
  </div>
</div>"""


def build_html(c, for_pdf=False):
    days = {}
    for m in c["modules"]:
        days.setdefault(m["day"], []).append(m)
    n = 0
    day_html = ""
    for d in sorted(days):
        blocks = ""
        for m in days[d]:
            n += 1
            blocks += module_block(n, m)
        day_html += f'<section class="gt-day"><div class="gt-dayhead"><span class="gt-daynum">Day {d}</span><span>{len(days[d])} modules</span></div>{blocks}</section>'

    tools = "".join(f'<span class="gt-tool">{icon_svg(s, 20)}{esc(label)}</span>' for s, label in c["tools"])
    outcomes = "".join(f"<li>{esc(o)}</li>" for o in c["outcomes"])
    prereqs = "".join(f"<li>{esc(p)}</li>" for p in c["prerequisites"])
    assess = "".join(f"<tr><td>{esc(a)}</td><td>{esc(w)}</td><td>{esc(e)}</td></tr>" for a, w, e in COMMON_ASSESSMENT)
    princ = "".join(f"<li>{esc(p)}</li>" for p in SHARED_PRINCIPLES)
    fonts = "" if for_pdf else '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">'
    days_word = f"{c['days']} days (8 hours per day)"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(c['title'])} - Course Outline | Gennoor Tech</title>
<meta name="description" content="{esc(c['tagline'])}. Course outline by Gennoor Tech.">
{fonts}<style>{CSS}</style></head>
<body><main class="gt-toc">
<header class="gt-head">
  <div>
    <span class="gt-code">Course outline</span>
    <h1 class="gt-title">{esc(c['title'])}</h1>
    <p class="gt-tag">{esc(c['tagline'])}</p>
    <div class="gt-chips">
      <span class="gt-chip">{icon_svg('generic:clock', 16)}{esc(days_word)}</span>
      <span class="gt-chip">{icon_svg('generic:level', 16)}{esc(c['level'])}</span>
      <span class="gt-chip">{icon_svg('generic:lab', 16)}Instructor-led, hands-on labs</span>
      <span class="gt-chip">{icon_svg('generic:capstone', 16)}Capstone project</span>
    </div>
  </div>
  <div class="gt-logo">{gennoor_logo_svg(44)}</div>
</header>

<h2 class="gt-h2">{icon_svg('generic:target', 20)}About this course</h2>
<div class="gt-grid2">
  <div class="gt-card"><h3>{icon_svg('generic:users', 18)}Who should attend</h3><p>{esc(c['audience'])}.</p></div>
  <div class="gt-card"><h3>{icon_svg('generic:book', 18)}Prerequisites</h3><ul>{prereqs}</ul></div>
</div>
<div class="gt-card" style="margin-top:14px"><h3>{icon_svg('generic:check', 18)}What you will be able to do</h3><ul>{outcomes}</ul></div>

<h2 class="gt-h2">{icon_svg('generic:shield', 20)}Tools and technologies</h2>
<div class="gt-tools">{tools}</div>

<h2 class="gt-h2">{icon_svg('generic:book', 20)}Table of contents</h2>
{day_html}

<h2 class="gt-h2">{icon_svg('generic:capstone', 20)}Capstone</h2>
<div class="gt-cap">{icon_svg('generic:capstone', 44, '#F59E0B')}<div><h3>Capstone project</h3><p>{esc(c['capstone'])}</p></div></div>

<h2 class="gt-h2">{icon_svg('generic:level', 20)}Assessment</h2>
<table class="gt-tab"><tr><th>Assessment area</th><th>Weight</th><th>Evidence</th></tr>{assess}</table>

<h2 class="gt-h2">{icon_svg('generic:shield', 20)}Engineering principles used throughout</h2>
<ul class="gt-princ">{princ}</ul>

<footer class="gt-foot"><span>&copy; Gennoor Tech &middot; Train. Innovate. Build.</span><a href="https://gennoor.com">For more info - https://gennoor.com</a></footer>
</main></body></html>"""


async def html_to_pdf(html_path, pdf_path):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = await b.new_page()
        await pg.goto(html_path.as_uri())
        await pg.wait_for_timeout(300)
        await pg.pdf(path=str(pdf_path), format="A4", print_background=True,
                     margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"})
        await b.close()


def main():
    import gennoor_watermark as wm
    for c in COURSES:
        d = OUT / c["folder"] / "TOC"
        d.mkdir(parents=True, exist_ok=True)
        base = f"{c['title']} - Course Outline"
        html_out = d / f"{base}.html"
        html_out.write_text(build_html(c))
        tmp_html = d / "~print.html"
        tmp_html.write_text(build_html(c, for_pdf=True))
        tmp_pdf = d / "~plain.pdf"
        asyncio.run(html_to_pdf(tmp_html, tmp_pdf))
        pdf_out = d / f"{base} - Gennoor.pdf"
        pdf_out.write_bytes(wm.stamp_bytes(tmp_pdf.read_bytes(), mode="flatten"))
        tmp_html.unlink(); tmp_pdf.unlink()
        print("built", html_out.name, "|", pdf_out.name)


if __name__ == "__main__":
    main()
