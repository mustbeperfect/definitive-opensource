from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.generation.header_generator import (  # noqa: E402
    generate_header,
    generate_navbar,
    generate_top_header,
)

__all__ = [
    "generate_header",
    "generate_navbar",
    "generate_top_header",
    "generate_mainheader",
]


def generate_mainheader(platform="all"):
    """Backward-compatible wrapper for generating top header or full header."""
    return generate_top_header(platform)


if __name__ == "__main__":
    print(generate_mainheader())
