"""Render a motion-graphics promo video for one course: TTS narration -> timeline -> frames via Playwright -> ffmpeg."""
import asyncio
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from content import COURSES, INSTRUCTOR, SHARED_PRINCIPLES
from icons import icon_svg

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "TOC-output"
WORK = HERE.parent / "vwork"
FPS = 30
W, H = 1920, 1080
MIN_SECONDS = 5 * 60 + 8
VOICE = "Jalal (cloned course voice)"
VOICE_DIR = Path(os.environ.get("VOICE_DIR", HERE.parent.parent / "out" / "_work"))
LESSONS = json.loads(Path(os.environ.get("VOICE_LESSONS", HERE.parent.parent / "lessons.json")).read_text(encoding="utf-8"))
GAP = 0.75  # pause between narration segments


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def dur(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]).stdout.strip()
    return float(out)


async def tts_all(course, wdir):
    """Generate one mp3 per narration segment (cached)."""
    files = []
    lesson = LESSONS[course["folder"]]
    for i, (scene, text) in enumerate(course["video"]["narration"]):
        f = VOICE_DIR / lesson / "voice" / f"s{i:02d}.wav"   # owner's voice, voiced on Kaggle (toc_kaggle.py)
        if not f.exists() or f.stat().st_size == 0:
            raise FileNotFoundError(f)
        files.append(f)
    return files


def split_captions(text, start, length):
    """Split narration into caption chunks of ~9 words, timed proportionally by character count."""
    words = text.split()
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= 9 or (len(cur) >= 5 and re.search(r"[.!?,;:]$", w)):
            chunks.append(" ".join(cur)); cur = []
    if cur:
        chunks.append(" ".join(cur))
    total = sum(len(c) for c in chunks) or 1
    out, t = [], start
    for c in chunks:
        d = length * len(c) / total
        out.append({"s": round(t, 3), "e": round(t + d, 3), "text": c})
        t += d
    return out


def build_timeline(course, seg_durs, gap=GAP):
    """Scene order follows narration scene tags; each scene lasts the sum of its segments + gaps."""
    GAP = gap
    nar = course["video"]["narration"]
    order = []
    for scene, _ in nar:
        if scene not in order:
            order.append(scene)
    # audio placement
    t = 1.2  # intro silence
    seg_start = []
    for d in seg_durs:
        seg_start.append(t)
        t += d + GAP
    end_audio = t
    # scene spans
    timeline, captions = [], []
    for sc in order:
        idx = [i for i, (s, _) in enumerate(nar) if s == sc]
        start = seg_start[idx[0]] - (0.6 if sc != order[0] else 1.2)
        end = seg_start[idx[-1]] + seg_durs[idx[-1]] + GAP - 0.6
        entry = {"id": sc, "start": round(start, 3), "end": round(end, 3)}
        # cue points: second segment start relative to scene start (hook question, instructor course card, cta url)
        if len(idx) > 1:
            entry["cue"] = round(seg_start[idx[1]] - start, 3)
        if sc.startswith("path"):
            n_items = len(course["video"]["paths"][int(sc[4:])]["items"])
            entry["itemGap"] = round(max(1.0, (end - start - 3) / (n_items + 1)), 3)
            lines = course["video"]["paths"][int(sc[4:])]["panel_lines"]
            chars = sum(len(l) + 18 for l in lines)
            entry["cps"] = round(max(35, chars / max(4, (end - start - 3))), 1)
        if sc == "stats":
            entry["itemGap"] = round(max(1.0, (end - start - 3) / (len(course["video"]["stats"]) + 1)), 3)
        timeline.append(entry)
        for i in idx:
            captions += split_captions(nar[i][1], seg_start[i], seg_durs[i])
    # insert the modules sweep scene after 'labs' if present: steal time by extending? Instead place it before 'stats' using a dedicated pause.
    return timeline, captions, end_audio, seg_start


def insert_mods_scene(timeline, captions, seg_start, seg_durs, course, hold=None):
    """Add a silent 'mods' scene (table of contents sweep) between labs and stats, shifting everything after it."""
    n_pages = -(-len(course["modules"]) // 8)
    hold = hold or (2.0 + n_pages * 7.0)
    ids = [s["id"] for s in timeline]
    if "stats" not in ids:
        return timeline, captions, seg_start, 0
    k = ids.index("stats")
    at = timeline[k]["start"]
    for s in timeline[k:]:
        s["start"] = round(s["start"] + hold, 3); s["end"] = round(s["end"] + hold, 3)
    for c in captions:
        if c["s"] >= at:
            c["s"] = round(c["s"] + hold, 3); c["e"] = round(c["e"] + hold, 3)
    seg_start = [ss + hold if ss >= at else ss for ss in seg_start]
    timeline.insert(k, {"id": "mods", "start": round(at, 3), "end": round(at + hold, 3)})
    return timeline, captions, seg_start, hold


def make_audio(wdir, seg_files, seg_start, total, out_path, bed_freq=110):
    """Mix narration at its start times over a soft synthesized ambient bed."""
    inputs, filters, labels = [], [], []
    for i, (f, st) in enumerate(zip(seg_files, seg_start)):
        inputs += ["-i", str(f)]
        filters.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={int(st*1000)}|{int(st*1000)}[a{i}]")
        labels.append(f"[a{i}]")
    n = len(seg_files)
    # ambient bed: two detuned low sines + slow tremolo, very quiet, with fade in/out
    f0 = bed_freq
    bed = (f"sine=frequency={f0:.1f}:sample_rate=48000:duration={total:.2f}[s1];"
           f"sine=frequency={f0*1.498:.1f}:sample_rate=48000:duration={total:.2f}[s2];"
           f"sine=frequency={f0*2.004:.1f}:sample_rate=48000:duration={total:.2f}[s3];"
           f"[s1][s2][s3]amix=inputs=3:normalize=0,tremolo=f=0.11:d=0.5,lowpass=f=600,volume=0.035,"
           f"aformat=channel_layouts=stereo,afade=t=in:d=3,afade=t=out:st={total-5:.2f}:d=5[bed]")
    fc = ";".join(filters) + ";" + bed + ";" + "".join(labels) + f"[bed]amix=inputs={n+1}:normalize=0:duration=longest,loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.95[out]"
    cmd = ["ffmpeg", "-y", "-v", "error"] + inputs + ["-filter_complex", fc, "-map", "[out]", "-t", f"{total:.2f}",
           "-c:a", "aac", "-b:a", "192k", str(out_path)]
    run(cmd)


async def render_frames(html_path, total, video_tmp):
    from playwright.async_api import async_playwright
    n_frames = int(total * FPS)
    ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-r", str(FPS), str(video_tmp)],
                          stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--disable-gpu", "--hide-scrollbars"])
        pg = await b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        await pg.goto(html_path.as_uri())
        await pg.wait_for_timeout(500)
        await pg.evaluate("document.fonts.ready")
        cdp = await pg.context.new_cdp_session(pg)
        t0 = time.time()
        for i in range(n_frames):
            t = i / FPS
            await pg.evaluate(f"seek({t:.4f})")
            res = await cdp.send("Page.captureScreenshot", {"format": "jpeg", "quality": 90, "captureBeyondViewport": False})
            import base64
            ff.stdin.write(base64.b64decode(res["data"]))
            if i % 600 == 0:
                print(f"  frame {i}/{n_frames}  {time.time()-t0:.0f}s", flush=True)
        await b.close()
    ff.stdin.close(); ff.wait()
    if ff.returncode != 0:
        raise RuntimeError("ffmpeg encode failed")


def course_data(c, timeline, captions):
    v = c["video"]
    icons = {"claude": icon_svg("claude", 24, "#fff"), "capstone": icon_svg("generic:capstone", 24, "#fff")}
    mods = [{"title": m["title"], "day": m["day"], "icon": icon_svg(m["icon"], 40)} for m in c["modules"]]
    tools = [(icon_svg(s, 44), label) for s, label in c["tools"]]
    aud = c["audience"]
    return {
        "seed": sum(map(ord, c["title"])), "code": c["code"], "title": c["title"], "days": c["days"],
        "hook_title": v["hook_title"], "hook_sub": v["hook_sub"], "hook_q": v["hook_q"],
        "story_big": v["story_big"], "story_num": v["story_num"], "story_num_label": v["story_num_label"], "story_sub": v["story_sub"],
        "paths": v["paths"], "stats": v["stats"], "cta": v["cta"], "tagline": c["tagline"],
        "audience_short": aud, "prereq_short": "Prerequisites: " + "; ".join(c["prerequisites"][:3]) + ".",
        "tools": tools, "modules": mods, "principles": PRINCIPLES_SHORT, "icons": icons, "timeline": timeline, "captions": captions, "theme": c["theme"],
    }


PRINCIPLES_SHORT = [
    ("Model output is a proposal", "validated by deterministic checks and tests"),
    ("Authorization outside the model", "enforced by code, scoped credentials and policy"),
    ("Humans approve consequential actions", "deployments, config changes, credential rotation"),
    ("Everything is logged", "decisions, evidence, versions, approvals, outcomes"),
    ("Provider-agnostic by design", "model adapter and tool adapter layers"),
    ("Quality is measured", "false positives, false negatives, cost, safe failure"),
]
PRINCIPLES_NARRATION = ("Every build in this course follows six engineering principles. Model output is a proposal, never a fact. "
    "Authorization lives outside the model. A human approves every consequential action. Decisions and evidence are logged. "
    "The stack stays provider-agnostic. And quality is measured, not assumed.")

def words(n):
    return {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}.get(n, str(n))

def mods_narration(c):
    days = {}
    for m in c["modules"]:
        days.setdefault(m["day"], []).append(m["title"])
    parts = [f"Here is the full table of contents, {len(c['modules'])} modules over {words(c['days'])} days."]
    for d in sorted(days):
        titles = days[d]
        parts.append(f"Day {words(d)}: " + "; ".join(titles[:-1]) + ("; and " if len(titles) > 1 else "") + titles[-1] + ".")
    return " ".join(parts)

def full_narration(c):
    nar = list(c["video"]["narration"])
    k = [i for i, (s, _) in enumerate(nar) if s == "labs"]
    at = k[0] + 1 if k else len(nar) - 3
    nar[at:at] = [("mods", mods_narration(c)), ("princ", PRINCIPLES_NARRATION)]
    return nar


async def build(c):
    wdir = WORK / c["folder"].replace(" ", "_"); wdir.mkdir(parents=True, exist_ok=True)
    c = dict(c); c["video"] = dict(c["video"]); c["video"]["narration"] = full_narration(c)
    print("==", c["title"], "TTS", flush=True)
    seg_files = await tts_all(c, wdir)
    seg_durs = [dur(f) for f in seg_files]
    natural = 1.2 + sum(seg_durs) + GAP * len(seg_durs) + 5.0
    gap = GAP if natural >= MIN_SECONDS else min(3.0, GAP + (MIN_SECONDS - natural) / len(seg_durs))
    timeline, captions, end_audio, seg_start = build_timeline(c, seg_durs, gap)
    for e in timeline:
        if e["id"] == "princ":
            e["itemGap"] = round(max(1.0, (e["end"] - e["start"] - 3) / 7), 3)
    total = end_audio + 5.0  # outro hold
    if total < MIN_SECONDS:
        total = MIN_SECONDS
    print(f"   segment gap {gap:.2f}s")
    timeline[-1]["end"] = round(total, 3)
    print(f"   narration {sum(seg_durs):.0f}s, video {total:.0f}s ({total/60:.2f} min)", flush=True)
    data = course_data(c, timeline, captions)
    html = (HERE / "video_template.html").read_text().replace("__DATA__", json.dumps(data))
    html_path = wdir / "scene.html"; html_path.write_text(html)
    for a in ["logo-dark.png"]:
        tgt = wdir / a
        if not tgt.exists():
            import shutil; shutil.copy2(HERE / a, tgt)
    if os.environ.get("PREPARE_ONLY"):
        print("   prepared", html_path); return None
    audio = wdir / "audio.m4a"; make_audio(wdir, seg_files, seg_start, total, audio, c["theme"]["bed"])
    video_tmp = wdir / "video_noaudio.mp4"
    print("   rendering frames", flush=True)
    await render_frames(html_path, total, video_tmp)
    outdir = OUT / c["folder"] / "Promo Video"; outdir.mkdir(parents=True, exist_ok=True)
    final = outdir / f"{c['title']} - Promo.mp4"
    run(["ffmpeg", "-y", "-v", "error", "-i", str(video_tmp), "-i", str(audio), "-c:v", "copy", "-c:a", "copy", "-shortest",
         "-movflags", "+faststart", "-metadata", f"title={c['title']} - Gennoor Tech", "-metadata", "artist=Gennoor Tech", str(final)])
    # narration script + captions for the website / subtitles
    (outdir / f"{c['title']} - Promo Narration Script.md").write_text(
        f"# {c['title']} - promo narration\n\nVoice: the presenter's own cloned voice. Duration: {total/60:.1f} min.\n\n" +
        "\n\n".join(f"**[{s}]** {t}" for s, t in c["video"]["narration"]))
    srt = []
    for i, k in enumerate(captions, 1):
        def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")
        srt.append(f"{i}\n{ts(k['s'])} --> {ts(k['e'])}\n{k['text']}\n")
    (outdir / f"{c['title']} - Promo Captions.srt").write_text("\n".join(srt))
    print("   done", final.name, f"{final.stat().st_size/1e6:.1f} MB", flush=True)
    return final


if __name__ == "__main__":
    want = sys.argv[1:]
    for c in COURSES:
        if not want or any(w.lower() in c["title"].lower() for w in want):
            asyncio.run(build(c))
