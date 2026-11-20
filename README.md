# 20 November 2026 — The World in One Image

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/mihawnk-nft/news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/mihawnk-nft/news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

An entry for the [make.fun](https://make.fun/c/news-image-20261120) bounty
"Sum up 20 November's world news in one image".

## The image

`entry.png` is one 1024×1024 picture of Friday 20 November 2026,
built from 28 reported stories of that day, from 7 regions — every story
first reported on 20 November, each checked against its source and its
date:

- **Cyclone Akvan makes landfall near Gopalpur, Odisha**, around noon IST;
  ~300,000 evacuated and 423 rescue teams deployed.
- **Trump puts the Iran decision off to 2027** — "We'll see what happens
  after January 1" — and warns Musk after "I'm not MAGA": "when people
  veer from it, they don't do very well."
- **Israel completes its Gaza ground raid** past the Yellow Line; the BBC
  reports from besieged Taiz, where a mother tells her son the shelling
  is "just fireworks".
- **Citi misbooked trades by ~$35bn**; **Nvidia falls a 6th straight day**,
  $669bn gone in six sessions; **Anthropic closes its first Nasdaq day at
  $97.17**, +17% on the $83 IPO — the biggest IPO ever.
- Plus: Phillips' 118 lifts New Zealand to 317-6, COP31's draft drops all
  fossil-fuel mention, and GTA 6 passes The Odyssey at an estimated $1.84bn.

A DATE CHECK box on the image names the big stories that are NOT 20 November's
news — the Shenzhen trilateral, the ICJ Rohingya ruling, the Riyadh PIF Tower
strike, the Kyiv embassy strikes — so nothing from 17–19 November is shown
as Friday's news.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. It needs no network and writes identical bytes on
every run:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
