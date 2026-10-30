# Gennoor course outlines and promos

16 course outlines in two domains. Each course folder in `TOC-output/` has `TOC/` (HTML view, PDF for learners, DOCX for editing), `Promo Video/` (captions, narration script) and `Research/` (research and module-by-module content plan for building the course; index in `TOC-output/Research/README.md`).

- **Automation with Claude** (11): Bill Creation, Certificate Renewal, Cisco ACI Upgrade, Configuration Comparison, Credential and Access Management, Device Health Monitoring, Device Upgrade, HR Hiring Flow, Terraform and GitHub, Traffic and Flow Diagram, Troubleshooting.
- **Agentic Cybersecurity** (5): Vulnerability Management, Architecture Reviewer, Attack Surface Management, Configuration Reviewer, Virtual Patching Platform.

`courses.json` indexes every course (domain, days, hours, modules, file paths).

## Promo videos
The promo videos are served from Azure Blob Storage, not from git. The `.mp4` files kept in this repo are the earlier versions; the current ones (presenter's own voice) are in the blob container `toc-and-promotional-videos`, same paths as in `courses.json`.

## Layout
- `TOC-output/` outlines, captions, narration scripts, per-course research plans
- `tools/` build code (`build_toc.py`, `build_docx.py`, `build_video.py`, `build_research.py`, `content.py`, `specs/`, `research/`)
- `assets/` logo photo and watermark process, `notes/` source notes and prototypes

Duration rule: 1 day = 8 hours.
