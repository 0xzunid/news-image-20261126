# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/0xzunid/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/0xzunid/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Thursday 26 November 2026, squeezed onto one newspaper front page. This entry is a single 1024×1024 image: a masthead, one lead story, four more in two columns, and an "Also today" strip at the foot — every word drawn in code with Pillow, so the headlines stay sharp instead of turning into AI-image gibberish.

The five stories on the page:

- **Trump's new tariff salvo** — the White House proposes fresh tariffs on goods from 14 major trading partners, China, Japan and the EU among them. Nvidia slides 3.9% to $149.30, $2.3 trillion below its October peak; core US inflation hits 3.3%.
- **Houthis claim hit on Saudi's biggest refinery** — Yemen's Houthis say they struck the Ras Tanura refinery (550,000 barrels a day) and Riyadh's financial district; Saudi Arabia says it shot down four drones. Brent jumps 3.5% to $94.61.
- **19 civilians killed in Sudan drone strikes** — Rapid Support Forces drones hit three residential districts in Damazin, capital of Blue Nile state, and struck the dam and power facilities at Roseires; 20 more wounded.
- **Israel kills a second Hamas security chief in 24 hours** — an airstrike on a Gaza City apartment kills Hamas colonel Mohammad Abuelouf, who ran internal security in northern Gaza, along with his wife and two children.
- **Seoul hikes rates as Tokyo hints at faster rises** — South Korea's central bank lifts its rate a quarter point to 3.25%; Bank of Japan board member Naoki Tamura says the BOJ must "respond swiftly" to signs of an inflation overshoot.

Plus, in "Also today": the Bogor gold-mine flood in Indonesia (9 dead, 17 trapped), a US judge barring the FCC from steps threatening ABC's broadcast licence, Ramaphosa's court victory in South Africa, and a 36% garment-wage rise in Bangladesh.

## Running it

```sh
python3 main.py
```

`main.py` copies `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies the copy before reporting success: its SHA-256 must equal the pinned digest of the bundled image, and its PNG header must read 1024×1024. The page itself was drawn by `news-image-gen-20261126.py`, which lives outside this repo — Pillow and DejaVu fonts only, no network, no randomness.

Checked on 2026-11-26: `entry.png` is 164,003 bytes with sha256 `3ca6d042d7104483f827aa1b6eda3b325f61fcd173ccf2a5a2eec9b832c13571`. `main.py` was written fresh on 2026-11-26 and run twice with `python3 -P -s` — exit 0 both times, byte-identical output, dimensions confirmed 1024×1024.

---

<sub>Entered on [make.fun](https://make.fun/?ref=1q7g6m7h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
