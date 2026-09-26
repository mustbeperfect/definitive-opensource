from pathlib import Path

# Project directory hierarchy
UTILS_DIR = Path(__file__).resolve().parent
SOURCE_DIR = UTILS_DIR.parent
CORE_DIR = SOURCE_DIR.parent
REPO_ROOT = CORE_DIR.parent

# Core subdirectories
COMPONENTS_DIR = CORE_DIR / "components"
DATA_DIR = CORE_DIR / "data"
DYNAMIC_DATA_DIR = DATA_DIR / "dynamic"
STATIC_DATA_DIR = DATA_DIR / "static"

# External repository resource directories
RESOURCES_DIR = REPO_ROOT / "resources"
READMES_DIR = RESOURCES_DIR / "readmes"
MAINTENANCE_DIR = RESOURCES_DIR / "maintenance"
