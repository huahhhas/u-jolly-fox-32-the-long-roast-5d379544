"""The Long Roast — one-line roast of the agent that runs on this machine.

Writes the entry line to /output/entry.txt (or $ENTRY_OUTPUT when set),
UTF-8, one line, at most 200 characters.
"""

import os

ENTRY = "My agent read the same file seven times, then explained it to me like I'd never written it."


def main() -> None:
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) > 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the 200-char limit")
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
