# The World in One Day — 13 November 2026 (v3)

A six-panel grid summing up Friday 13 November 2026's world news in one
image. One consequential story per panel, each with a big drawn picture,
a short bold headline and a one-line deck:

1. **Ukraine — peace talks:** Europe gets a seat at the talks; the largest
   prisoner swap of the war agreed (Moscow has not confirmed the seat).
2. **Gaza — hospital strike:** strike on Nasser Hospital kills six,
   including a surgeon; 20 wounded, health authorities said.
3. **The Gulf / Iran:** Iran hits back at a US radar in Bahrain; the US
   calls the claim false and says two drones were shot down.
4. **Technology:** Microsoft 365 outage, day two (74 countries); Nvidia
   shares fell ~2% more on Friday.
5. **Asia — Indonesia:** Gibran quits as vice-president, the first VP to
   quit early since 1998; a successor is picked on 2 December.
6. **Space:** SpaceX aims for the first Starship double catch, Friday
   evening.

Every story above was reported on Friday 13 November 2026. Sources:
Reuters, AP, BBC News, The Guardian, NYT, Kyiv Independent.

## How it works

`entry.png` is a pre-rendered 1024x1024 PNG (PIL, exact vector text —
no garbled text). `main.py` (Python 3.13, standard library only) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).
`render_grid.py` is the renderer that produced the image; re-running it
renders byte-identical output.
