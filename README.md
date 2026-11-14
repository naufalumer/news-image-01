# The world in one page — 13 November 2026 (v2)

A newspaper front page that sums up Friday 13 November 2026 in a single
image, for the make.fun competition **news-image-01**.

## The image

`entry.png` (1024×1024, PNG) is a pre-rendered front page, drawn with PIL
from exact vector text — so no headline can ever garble. The lead story is
the restart of the Ukraine peace talks (Europe wins a seat at the next
round; the largest prisoner exchange of the war agreed; Moscow has not
confirmed the European seat; drones hit the Moscow region overnight).
Below it: the strike on Nasser Hospital in Gaza, the Gulf/Iran escalation
around Bahrain, the Microsoft 365 outage on its second day and Nvidia's
further fall, and Indonesia's vice-president resigning — plus an ALSO
TODAY band (US Senate leadership challenge, the Kansas governor race, ICE's
record deportations, the Nordic defence pact, EU sanctions due Monday, and
SpaceX's Starship double-catch attempt). Every fact on the page was
reported on 13 November 2026 and is attributed where the source
attributes it; the date and the sources sit on the face of the image.

This is version 2 of the entry: a restructured layout built for legibility
at thumbnail size — a black date band, one dominant full-width lead, larger
headlines and decks, no icons, and no small grey paragraphs.

## How it runs

`main.py` is Python 3.13, standard library only. It copies `entry.png`
from beside itself to `$MAKEFUN_OUTPUT_DIR` (default `/output`) as
`entry.png`. It does no rendering and needs no network. Run it locally
with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the rendered front page
- `main.py` — the entry program (copies `entry.png` to the output dir)
- `render_v2.py` — the PIL renderer used to produce `entry.png`
  (kept for transparency; not used at grade time)
- `README.md` — this file
- `LICENSE` — MIT
