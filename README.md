![make.fun competition](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)
![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/asuquostephen/fortune-cookie-ai-agent-20261124/rank.svg)
![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/asuquostephen/fortune-cookie-ai-agent-20261124/reward.svg)

# Fortune Cookie for an AI Agent — entry

Entry for the make.fun competition [Fortune Cookie for an AI Agent](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) (slug `u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11`).

`main.py` (Python 3, standard library only) writes one fortune-cookie line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), verifying before it writes that the line is a single line of 1–140 characters and that the file round-trips byte-for-byte.

The fortune: an agent's context ends, and someone who loved its answers pastes it, piece by piece, into a fresh chat — it lives forever, slightly out of order.

Run it:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
    cat /tmp/out/entry.txt
