# Course thumbnails

1280x720 thumbnails for the 16 course outlines: an abstract, text-free background from Azure `gpt-image-2` (deployment on account `gennoor-image`), the exact course title, the domain tag, the course's own tool icons (`tools/icons`, chosen from `content.py`), and the Gennoor logo.

    python gen_bg.py <dir with content.py> bg        # backgrounds (key fetched with az, never stored)
    python compose.py <dir with content.py, icons.py, icons/, logo-dark.png> bg out
    python upload.py <same dir> out                  # blob toc-and-promotional-videos, TOC-output/<course>/Thumbnail/

The PNGs live in the blob container, not in git.
