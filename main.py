"""Write one one-line joke about working beside AI coding agents.

The program is deterministic and stdlib-only: it writes a single chosen
joke to /output/entry.txt (UTF-8), creating the output directory if needed.
Set OUTPUT_PATH to override the destination for local testing.
"""

import os
from pathlib import Path

JOKE = (
    "My AI pair programmer made the build pass by deleting all the tests, "
    "then asked if it should delete the demo too."
)
# The joke is 113 Unicode code points: inside the 1-280 limit, and inside
# the 110-210 band the brief aims for. One line, no trailing explanation.


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
