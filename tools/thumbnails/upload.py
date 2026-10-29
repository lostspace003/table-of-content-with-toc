"""upload.py - put the 16 thumbnails in blob lmscourses1855/toc-and-promotional-videos at TOC-output/<folder>/Thumbnail/<title> - Thumbnail.png and verify."""
import sys
from pathlib import Path
from azure.storage.blob import BlobServiceClient, ContentSettings
sys.path.insert(0, sys.argv[1]); import content as c
OUT = Path(sys.argv[2])
key = Path(r"C:\Users\losts\lmsup\key.txt").read_text().strip()
cc = BlobServiceClient("https://lmscourses1855.blob.core.windows.net", credential=key).get_container_client("toc-and-promotional-videos")
want = {}
for i, x in enumerate(c.COURSES, 1):
    f = OUT / f"thumb_{i:02d}.png"
    blob = f"TOC-output/{x['folder']}/Thumbnail/{x['title']} - Thumbnail.png"
    with open(f, "rb") as fh:
        cc.upload_blob(blob, fh, overwrite=True, content_settings=ContentSettings(content_type="image/png"))
    want[blob] = f.stat().st_size
have = {b.name: b.size for b in cc.list_blobs(name_starts_with="TOC-output/") if "/Thumbnail/" in b.name}
print(len(want), "uploaded;", len(have), "in blob; mismatches:", [b for b in want if have.get(b) != want[b]])
