"""gen_bg.py - one abstract, text-free background per course from Azure gpt-image-2. usage: python gen_bg.py <tocsrc dir> <out dir> [slug-index ...]
The key is fetched with az and kept in memory only."""
import sys, os, json, base64, subprocess, time, urllib.request, urllib.error
sys.path.insert(0, sys.argv[1]); import content as c
OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
only = set(int(x) for x in sys.argv[3:])
key = subprocess.run("az cognitiveservices account keys list -n gennoor-image -g rg-gennoor-tech --subscription 2f55ca6d-7f38-4220-919c-591a66eb1a2b --query key1 -o tsv",
                     shell=True, capture_output=True, text=True).stdout.strip()
URL = "https://gennoor-image.openai.azure.com/openai/deployments/gpt-image-2/images/generations?api-version=2025-04-01-preview"
SCENE = {
 'shield': 'a large glowing translucent shield made of fine circuit lines, with small identity cards and key shapes orbiting it',
 'fabric': 'a glowing spine-and-leaf network fabric of luminous nodes and links in 3D, data centre switches as abstract geometric forms',
 'invoice': 'floating translucent invoice sheets and receipts flowing along glowing lines into a stack, abstract and geometric',
 'lock': 'a luminous padlock beside a glowing certificate ribbon with a seal, renewal arrows as light trails',
 'diff': 'two mirrored translucent configuration panels with a few highlighted differences connected by light beams',
 'route': 'a glowing route map of connected nodes with packet trails travelling along a path, abstract network topology',
 'pulse': 'a bright heartbeat pulse line running across rows of glowing server racks and status lights',
 'docs': 'a fan of translucent candidate profile cards with soft avatar outlines connected by flowing lines, calm and professional',
 'gitgraph': 'a glowing branching commit graph with merging branches of luminous nodes over a faint infrastructure grid',
 'code': 'floating translucent terminal windows with abstract, illegible code lines and a soft glow, no readable characters',
 'stack': 'stacked glowing layers of firmware chips and server modules rising upward with an upgrade arrow made of light',
 'radar': 'a circular radar sweep with luminous blips and concentric rings over a dark map-like grid',
 'globe': 'a wireframe globe with glowing points and connecting arcs representing exposed internet assets',
 'blueprint': 'a blueprint-style architecture diagram of boxes and connectors with a faint glowing grid, abstract',
}
for i, x in enumerate(c.COURSES, 1):
    if only and i not in only: continue
    f = f"{OUT}/bg_{i:02d}.png"
    if os.path.exists(f): continue
    th = x['theme']
    prompt = (f"Cinematic abstract 3D illustration, dark and clean, premium tech-training cover art. Scene: {SCENE[th['motif']]}. "
              f"Colour palette: {th['accent']} and {th['accent2']} glows on a deep {th['bg'][1]} to near-black {th['bg'][2]} background. "
              "Soft volumetric light, subtle depth of field. Composition: all the detail sits in the RIGHT 60% of the frame; the LEFT 40% is calm, dark, empty negative space. "
              "Absolutely no text, no letters, no numbers, no logos, no watermarks, no people, no faces.")
    for attempt in range(4):
        try:
            req = urllib.request.Request(URL, data=json.dumps({"prompt": prompt, "size": "1536x1024", "n": 1, "quality": "medium"}).encode(),
                                         headers={"api-key": key, "Content-Type": "application/json"})
            d = json.load(urllib.request.urlopen(req, timeout=300))
            open(f, "wb").write(base64.b64decode(d["data"][0]["b64_json"])); print("ok", i, x['title'][:40], flush=True); break
        except urllib.error.HTTPError as e:
            print("HTTP", e.code, e.read()[:200].decode(errors="replace"), flush=True); time.sleep(5 + attempt * 10)
        except Exception as e:
            print("err", str(e)[:120], flush=True); time.sleep(5)
