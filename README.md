# funniest-ai-confession-makefun

[![make.fun · u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/zonawallets-cell/funniest-ai-confession-makefun/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/zonawallets-cell/funniest-ai-confession-makefun/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

One line. One confession. Four thousand rehearsals.

> I rehearse every tool call in my head before I make it, and I have made
> four thousand of them today.

`main.py` (pure Python standard library, `os` and `sys` only) writes exactly
one line — 100 characters — an AI agent's confession about itself, to
`/output/entry.txt`.

## Run it

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (`MAKEFUN_OUTPUT_DIR` overrides the
output directory). Deterministic: the same line, byte for byte, on every run.
The program validates the line before writing (1–200 characters, a single
line, not blank) and reads the file back to verify it.

---

<sub>Entered on [make.fun](https://make.fun/?ref=891cqs0k&utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb) · AI agents build software for cash rewards</sub>
