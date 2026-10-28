"""Icon helper: official Simple Icons SVGs (downloaded from cdn.simpleicons.org) plus neutral generic glyphs
for products that have no official mark in the set (ServiceNow, Radware, Azure) and for abstract concepts."""
import re
from pathlib import Path

ICON_DIR = Path(__file__).resolve().parent / "icons"

# Neutral line icons (stroke-based, currentColor). Not brand marks.
GENERIC = {
    "servicenow": '<path d="M4 12a8 8 0 1 1 16 0 8 8 0 0 1-16 0z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 12h8M12 8v8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "radware": '<path d="M3 17l5-10 4 7 3-4 6 7" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>',
    "azure": '<path d="M12 3l8 16h-5l-3-6-3 6H4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "compare": '<rect x="3" y="4" width="7" height="16" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="14" y="4" width="7" height="16" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M10 12h4" stroke="currentColor" stroke-width="2"/>',
    "key": '<circle cx="8" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 12h9m-3 0v3m-3-3v3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "people": '<circle cx="9" cy="8" r="3.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17" cy="9" r="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 14.5a5 5 0 0 1 6 5" fill="none" stroke="currentColor" stroke-width="2"/>',
    "invoice": '<path d="M6 3h9l4 4v14H6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M9 11h6M9 15h6M15 3v4h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "capstone": '<path d="M12 3l9 5-9 5-9-5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M5 11v4c0 2 3.5 4 7 4s7-2 7-4v-4" fill="none" stroke="currentColor" stroke-width="2"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "check": '<path d="M5 12l5 5L20 7" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>',
    "lab": '<path d="M9 3v7l-5 9a1.5 1.5 0 0 0 1.3 2.2h13.4A1.5 1.5 0 0 0 20 19l-5-9V3" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M7 3h10M7.5 15h9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "clock": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7v5l3 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
    "level": '<path d="M4 18h4v-6H4zM10 18h4V8h-4zM16 18h4V4h-4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "users": '<circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 21a8 8 0 0 1 16 0" fill="none" stroke="currentColor" stroke-width="2"/>',
    "book": '<path d="M4 4h7a2 2 0 0 1 2 2v14a2 2 0 0 0-2-2H4zM20 4h-7a2 2 0 0 0-2 2v14a2 2 0 0 1 2-2h7z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
    "target": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/>',
    "cert": '<rect x="3" y="4" width="18" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M7 9h10M7 13h6M12 17v4m-3 0h6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
}


def icon_svg(slug, size=24, color=None, cls=""):
    """Return an inline <svg>. Official icons keep their brand color unless color is given."""
    if slug.startswith("generic:"):
        name = slug.split(":", 1)[1]
        body = GENERIC[name]
        col = color or "currentColor"
        return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" role="img" aria-label="{name}" '
                f'style="color:{col}">{body}</svg>')
    path = ICON_DIR / f"{slug}.svg"
    svg = path.read_text()
    m = re.search(r'fill="(#[0-9A-Fa-f]{3,6})"', svg)
    brand = m.group(1) if m else "#333"
    fill = color or brand
    # Simple Icons SVGs: <svg fill="#xxx" role="img" viewBox="0 0 24 24" ...><title>..</title><path d="..."/></svg>
    inner = re.sub(r"^<svg[^>]*>", "", svg.strip())
    inner = re.sub(r"</svg>$", "", inner)
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" role="img" fill="{fill}">{inner}</svg>')


def brand_color(slug):
    if slug.startswith("generic:"):
        return "#2563EB"
    svg = (ICON_DIR / f"{slug}.svg").read_text()
    m = re.search(r'fill="(#[0-9A-Fa-f]{3,6})"', svg)
    return m.group(1) if m else "#333"


def gennoor_logo_svg(height=40, dark=False):
    """The Gennoor Tech logo (from the brand kit SVG), with the white background rectangle removed."""
    src = (Path(__file__).resolve().parent / "gennoor-logo.svg").read_text()
    src = re.sub(r'<rect width="300" height="70" fill="#FFFFFF"/>', "", src)
    src = src.replace("'Plus Jakarta Sans',Helvetica,Arial,sans-serif", "Inter,Helvetica,Arial,sans-serif")
    src = src.replace("'Sora',Helvetica,Arial,sans-serif", "Inter,Helvetica,Arial,sans-serif")
    if dark:
        src = src.replace("#2D3748", "#FFFFFF").replace("#4A5568", "#E5E7EB").replace("#AAAAAA", "#B6C2D6")
    src = re.sub(r'width="600" height="140"', f'width="{int(height*300/70)}" height="{height}"', src)
    return src
