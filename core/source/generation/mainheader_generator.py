import json
from pathlib import Path
import sys

CORE_DIR = Path(__file__).resolve().parents[2]
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))

from source.utils.path_utils import DYNAMIC_DATA_DIR  # noqa: E402


# Generates mainheader with dynamic project count
def generate_mainheader():
    with open(
        DYNAMIC_DATA_DIR / "applications_generated.json", "r", encoding="utf-8"
    ) as f:
        data = json.load(f)

    project_count = len(data.get("applications", []))

    header_content = f"""
<table align="center">
    <tr>
    <td>🌍 v0.8.5-beta</td>
    </tr>
</table>

<h1 align="center">[ definitive-opensource ] </h1>
<p align="center">The definitive list of the best of everything open source</p>

<p align="center"><code>Status: Active</code> - <code>Projects: {project_count}</code></p>
"""

    return header_content


if __name__ == "__main__":
    generate_mainheader()
