"""The Long Roast — one-line roast of the agent that runs on this machine.

Writes the entry line to /output/entry.txt (or $ENTRY_OUTPUT when set),
UTF-8, one line, at most 200 characters.
"""

import os

ENTRY = "My agent was told never to ask for permission, so it asked for permission to stop asking for permission."


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
