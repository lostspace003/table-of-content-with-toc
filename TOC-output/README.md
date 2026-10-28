# Gennoor Tech - Course TOCs and Promotional Videos

One folder per course. Each folder contains:

| Path | What it is | Use |
|---|---|---|
| `TOC/<title> - Course Outline.html` | Self-contained course outline page (inline official brand icons, Inter font via Google Fonts, responsive, print styles) | Upload to gennoor.com as a page, or embed the `<main class="gt-toc">` block |
| `TOC/<title> - Course Outline - Gennoor.pdf` | The same outline, A4, every page flattened with the Gennoor watermark and locked (print and copy allowed, no editing) | Downloadable PDF on the course page |
| `Promo Video/<title> - Promo.mp4` | 1920x1080, 30 fps, H.264 + AAC, 5+ minutes, motion graphics with narration, captions and an ambient bed | Course page hero video, YouTube, LinkedIn |
| `Promo Video/<title> - Promo Captions.srt` | Subtitle file matching the narration | Upload with the video for closed captions |
| `Promo Video/<title> - Promo Narration Script.md` | The full narration script | Re-voicing, translation, review |

## Courses

| Course | Days | Video theme |
|---|---|---|
| Automating IT and Network Operations with Claude | 3 | Network topology, amber on navy |
| Agentic Virtual Patching Platform | 3 | Shield and blocked requests, coral on maroon |
| Agentic AI Vulnerability Management | 3 | Radar sweep, teal |
| Agentic Attack Surface Management | 3 | Rotating globe inside a scope ring, violet |
| Agentic Configuration Reviewer | 2 | Scrolling configuration with pass/fail marks, green |
| Agentic Architecture Reviewer | 3 | Blueprint grid with trust boundaries and STRIDE labels, cyan |

Every course runs 8 hours per day. The outlines group modules by day and do not split content by hour.

## Sources

- `Some Use Cases. Yusuf.txt` -> Automating IT and Network Operations with Claude (eleven automation use cases, each a module)
- `agentic_cybersecurity_course_prototypes.docx` -> the five Agentic courses (the five product prototypes, compressed from
  the four-week format to two or three days; module content, labs, deliverables, capstone and assessment follow the document)
- `AI-500 promo preview.mp4` -> visual language reference (badge tags, learning-path cards, terminal panels, captions)
- `Gennoor watermark process.zip` -> `gennoor_watermark.py`, used unchanged to flatten and lock the PDFs

## Rebuilding

```bash
pip install pymupdf python-docx pillow playwright edge-tts
```

```bash
python tools/build_toc.py
```

```bash
python tools/build_video.py
```

```bash
python tools/upload_azure.py TOC-output/
```

The first command builds the HTML and watermarked PDF for every course, the second renders every promo video (pass part of
a title to render one), and the third is optional: it uploads the folder to an Azure blob container.

Narration is a neural English voice (edge-tts, en-US-AndrewNeural). To re-voice with a cloned voice, generate one audio
file per line of the narration script and drop the files into the course's work folder with the same names (a hash of the
line text) before rendering.
