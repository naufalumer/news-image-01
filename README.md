# The world in one page — 13 November 2026

Entry for make.fun competition **news-image-01**: "Sum up 13 November's
world news in one image".

The image is a newspaper front page, rendered with PIL from the verified
facts of Friday 13 November 2026: the Ukraine peace talks (Europe wins a
seat, largest prisoner exchange of the war agreed), the strike on Nasser
Hospital in Gaza, Iran's strike on a US radar in Bahrain, the Microsoft 365
outage and Nvidia's fall, Indonesia's vice-president resigning, plus an
"Also today" strip of nine more stories from the day.

## How it works

- `entry.png` — the pre-rendered front page (1024×1024 PNG, under 1 MiB).
  It was drawn with Pillow at build time; no image generation happens at
  grade time.
- `main.py` — the entry program. Python 3.13, standard library only. It
  copies `entry.png` sitting beside it to `$MAKEFUN_OUTPUT_DIR`
  (default `/output`) as `entry.png`. That is all it does, so it runs in a
  fresh container with no network and nothing installed.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png, byte-identical to entry.png
```

## Sources

Every story on the page was reported on Friday 13 November 2026. Sources:
Reuters, AP, BBC News, The Guardian, NYT, Kyiv Independent. Attributed
claims ("health authorities said", "the IRGC said", "US forces said") are
worded exactly as reported.
