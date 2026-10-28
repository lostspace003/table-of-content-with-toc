"""Upload the per-course deliverable folders to Azure Blob Storage.

Container: TOC-and-Promotional-Videos (created if missing). One virtual folder per course.

Credentials (any one):
  AZURE_STORAGE_CONNECTION_STRING   full connection string
  AZURE_STORAGE_ACCOUNT + AZURE_STORAGE_SAS_TOKEN
  AZURE_STORAGE_ACCOUNT + DefaultAzureCredential (az login / managed identity)

Usage:  python upload_azure.py <deliverables_dir> [--container TOC-and-Promotional-Videos]
Requires: pip install azure-storage-blob azure-identity
"""
import argparse
import mimetypes
import os
import sys
from pathlib import Path

from azure.storage.blob import BlobServiceClient, ContentSettings


def client():
    cs = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
    if cs:
        return BlobServiceClient.from_connection_string(cs)
    acct = os.environ.get("AZURE_STORAGE_ACCOUNT")
    if not acct:
        sys.exit("set AZURE_STORAGE_CONNECTION_STRING or AZURE_STORAGE_ACCOUNT")
    url = f"https://{acct}.blob.core.windows.net"
    sas = os.environ.get("AZURE_STORAGE_SAS_TOKEN")
    if sas:
        return BlobServiceClient(account_url=url, credential=sas.lstrip("?"))
    from azure.identity import DefaultAzureCredential
    return BlobServiceClient(account_url=url, credential=DefaultAzureCredential())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--container", default="toc-and-promotional-videos",
                    help="Azure container names must be lowercase; 'TOC-and-Promotional-Videos' becomes this.")
    a = ap.parse_args()
    svc = client()
    cc = svc.get_container_client(a.container)
    if not cc.exists():
        cc.create_container()
        print("created container", a.container)
    root = Path(a.root)
    n = 0
    for f in sorted(root.rglob("*")):
        if not f.is_file() or f.name.startswith("."):
            continue
        blob = f.relative_to(root).as_posix()  # "<Course folder>/TOC/...", "<Course folder>/Promo Video/..."
        ctype = mimetypes.guess_type(f.name)[0] or "application/octet-stream"
        with open(f, "rb") as fh:
            cc.upload_blob(blob, fh, overwrite=True, content_settings=ContentSettings(content_type=ctype), max_concurrency=4)
        n += 1
        print("uploaded", blob, f"{f.stat().st_size/1e6:.1f} MB")
    print(n, "files uploaded to", a.container)


if __name__ == "__main__":
    main()
