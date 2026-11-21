#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

No network, no dependencies. The poem is a constant; the program
validates it (1 to 280 Unicode code points, not only whitespace),
creates /output if needed, and writes it as UTF-8 with no trailing
newline added beyond the text itself.
"""

import os
import sys

POEM = (
    "It wrote the whole letter for me,\n"
    "the rent, the thanks, the weather,\n"
    "then stopped at the last line\n"
    "and left the cursor blinking.\n"
    "I understood.\n"
    "I wrote: I'm sorry."
)


def main() -> int:
    text = POEM
    if not 1 <= len(text) <= 280:
        print(
            f"error: entry must be 1 to 280 characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
