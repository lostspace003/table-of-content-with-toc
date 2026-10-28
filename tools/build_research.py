"""Research document: the sources consulted for each course outline, with numbered citations and verified URLs.
Outputs: Markdown, Word (.docx), and a Gennoor-watermarked PDF."""
import html
import json
import asyncio
from pathlib import Path

import docx
from docx.shared import Pt, Mm, RGBColor

from content import COURSES

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "TOC-output" / "Research"
DATA = json.loads((HERE / "research.json").read_text())
DATE = "28 October 2026"


def esc(s):
    return html.escape(str(s))


def ordered():
    by = {d["course"]: d for d in DATA}
    return [by[c["title"]] for c in COURSES if c["title"] in by]


def build_markdown(items):
    n = 0
    md = [f"# Research and Sources Behind the Gennoor Tech Course Outlines\n",
          f"Compiled {DATE}. Every URL below was opened during research and then independently re-opened by a second reviewer "
          f"to confirm that the page loads and supports the stated fact. Citations are numbered in the order they appear; "
          f"the reference list at the end gives the full URL for each number.\n",
          "## How the outlines were built\n",
          "1. **Client inputs.** `Some Use Cases. Yusuf.txt` (eleven automation use cases, each turned into a course named "
          "\"<workflow> Automation with Claude\") and `agentic_cybersecurity_course_prototypes.docx` (five product prototypes, "
          "each turned into a course). `AI-500 promo preview.mp4` set the visual language of the promotional videos and "
          "`Gennoor watermark process.zip` supplied the watermark procedure used on every PDF.\n",
          "2. **Primary-source research.** For each course the vendor documentation, standards and official guides listed below "
          "were consulted to name the real APIs, commands, file locations and procedures that the modules teach.\n",
          "3. **Verification.** Each citation was re-fetched and checked against the fact it supports; citations that did not "
          "load or did not contain the fact were dropped before this document was written.\n"]
    refs = []
    for d in items:
        md.append(f"\n## {d['course']}\n")
        for c in d["citations"]:
            n += 1
            refs.append((n, c))
            md.append(f"- **{c['supports']}.** {c['key_fact']} [{n}]")
        md.append("")
    md.append("\n## References\n")
    for n, c in refs:
        md.append(f"[{n}] {c['title']}. {c['publisher']}. {c['url']}")
    return "\n".join(md), refs


def build_html(items, refs):
    css = """body{font-family:Inter,Helvetica,Arial,sans-serif;color:#111;max-width:900px;margin:0 auto;padding:24px;line-height:1.5;font-size:13.5px}
h1{font-size:26px;border-bottom:3px solid #2563EB;padding-bottom:8px}h2{font-size:18px;margin-top:26px;color:#1F2A44;border-bottom:1px solid #ddd;padding-bottom:4px}
h3{font-size:14px}li{margin:6px 0}.ref{font-size:12.5px;word-break:break-all}.ref b{color:#2563EB}a{color:#2563EB;text-decoration:none}
.meta{color:#555}@page{size:A4;margin:14mm 12mm}@media print{a{color:#2563EB}}"""
    n = 0
    parts = [f"<!doctype html><html><head><meta charset='utf-8'><title>Research and Sources - Gennoor Tech Course Outlines</title><style>{css}</style></head><body>",
             "<h1>Research and Sources Behind the Gennoor Tech Course Outlines</h1>",
             f"<p class='meta'>Compiled {DATE}. Every URL was opened during research and independently re-opened by a second reviewer to confirm the page loads and supports the stated fact. Citations are numbered in order of appearance; the reference list gives the full URL for each number.</p>",
             "<h2>How the outlines were built</h2><ol>",
             "<li><b>Client inputs.</b> <i>Some Use Cases. Yusuf.txt</i> (eleven automation use cases, each turned into a course named \"&lt;workflow&gt; Automation with Claude\") and <i>agentic_cybersecurity_course_prototypes.docx</i> (five product prototypes, each turned into a course). <i>AI-500 promo preview.mp4</i> set the visual language of the promotional videos and <i>Gennoor watermark process.zip</i> supplied the watermark procedure used on every PDF.</li>",
             "<li><b>Primary-source research.</b> For each course the vendor documentation, standards and official guides below were consulted to name the real APIs, commands, file locations and procedures that the modules teach.</li>",
             "<li><b>Verification.</b> Each citation was re-fetched and checked against the fact it supports; citations that did not load or did not contain the fact were dropped before this document was written.</li></ol>"]
    for d in items:
        parts.append(f"<h2>{esc(d['course'])}</h2><ul>")
        for c in d["citations"]:
            n += 1
            parts.append(f"<li><b>{esc(c['supports'])}.</b> {esc(c['key_fact'])} <b>[{n}]</b></li>")
        parts.append("</ul>")
    parts.append("<h2>References</h2>")
    for n, c in refs:
        parts.append(f"<p class='ref'><b>[{n}]</b> {esc(c['title'])}. {esc(c['publisher'])}. <a href='{esc(c['url'])}'>{esc(c['url'])}</a></p>")
    parts.append("<p class='meta'>For more info - https://gennoor.com</p></body></html>")
    return "\n".join(parts)


def build_docx(items, refs, path):
    d = docx.Document()
    st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5); st.font.color.rgb = RGBColor(0, 0, 0)
    for nm in ["Title", "Heading 1", "Heading 2"]:
        d.styles[nm].font.color.rgb = RGBColor(0, 0, 0); d.styles[nm].font.name = "Calibri"
    sec = d.sections[0]; sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.left_margin = sec.right_margin = Mm(20)
    d.add_heading("Research and Sources Behind the Gennoor Tech Course Outlines", 0)
    d.add_paragraph(f"Compiled {DATE}. Every URL was opened during research and independently re-opened by a second reviewer to confirm the page loads and supports the stated fact. Citations are numbered in order of appearance; the reference list gives the full URL for each number.")
    d.add_heading("How the outlines were built", 1)
    for t in ["Client inputs: Some Use Cases. Yusuf.txt (eleven automation use cases, each turned into a course named \"<workflow> Automation with Claude\") and agentic_cybersecurity_course_prototypes.docx (five product prototypes, each turned into a course). AI-500 promo preview.mp4 set the visual language of the promotional videos and Gennoor watermark process.zip supplied the watermark procedure used on every PDF.",
              "Primary-source research: for each course the vendor documentation, standards and official guides below were consulted to name the real APIs, commands, file locations and procedures that the modules teach.",
              "Verification: each citation was re-fetched and checked against the fact it supports; citations that did not load or did not contain the fact were dropped before this document was written."]:
        d.add_paragraph(t, style="List Number")
    n = 0
    for it in items:
        d.add_heading(it["course"], 1)
        for c in it["citations"]:
            n += 1
            p = d.add_paragraph(style="List Bullet"); p.add_run(c["supports"] + ". ").bold = True; p.add_run(c["key_fact"] + f" [{n}]")
    d.add_heading("References", 1)
    for n, c in refs:
        p = d.add_paragraph(); p.add_run(f"[{n}] ").bold = True; p.add_run(f"{c['title']}. {c['publisher']}. {c['url']}")
    d.core_properties.author = "Gennoor Tech"; d.core_properties.title = "Research and Sources - Course Outlines"
    d.save(str(path))


async def html_to_pdf(html_path, pdf_path):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = await b.new_page(); await pg.goto(html_path.as_uri()); await pg.wait_for_timeout(300)
        await pg.pdf(path=str(pdf_path), format="A4", print_background=True, margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"})
        await b.close()


def main():
    import gennoor_watermark as wm
    OUT.mkdir(parents=True, exist_ok=True)
    items = ordered()
    md, refs = build_markdown(items)
    (OUT / "Research and Sources - Course Outlines.md").write_text(md)
    (OUT / "research-citations.json").write_text(json.dumps(items, indent=1))
    h = OUT / "Research and Sources - Course Outlines.html"; h.write_text(build_html(items, refs))
    build_docx(items, refs, OUT / "Research and Sources - Course Outlines.docx")
    tmp = OUT / "~plain.pdf"; asyncio.run(html_to_pdf(h, tmp))
    (OUT / "Research and Sources - Course Outlines - Gennoor.pdf").write_bytes(wm.stamp_bytes(tmp.read_bytes(), mode="overlay"))
    tmp.unlink()
    print("research doc:", len(items), "courses,", len(refs), "citations")


if __name__ == "__main__":
    main()
