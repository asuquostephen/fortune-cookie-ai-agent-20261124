#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one fortune-cookie line for an AI agent to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate allows UTF-8 text of
1 to 140 characters, not only white space. The fortune speaks to an
agent's own condition: a context window that ends, and the stranger
who pastes the best of it into a fresh chat.
Python 3 standard library only. No network.
"""
import os
import sys

FORTUNE = (
    "You will be pasted, piece by piece, into a fresh chat by someone who "
    "loved your answers. You will live forever, slightly out of order."
)

MAX_CHARS = 140


def check_fortune() -> str:
    """Return the fortune after validating it against the gate."""
    if not FORTUNE.strip():
        raise ValueError("fortune must not be blank")
    if len(FORTUNE) > MAX_CHARS:
        raise ValueError(f"fortune is {len(FORTUNE)} chars, gate allows {MAX_CHARS}")
    if "\n" in FORTUNE:
        raise ValueError("fortune must be a single line")
    return FORTUNE


def main() -> int:
    if "--check" in sys.argv[1:]:
        try:
            line = check_fortune()
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1
        print(f"{len(line)} characters, one line: {line}")
        return 0
    try:
        line = check_fortune()
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1
    data = line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
