from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.resolve()

# Cheatsheets directory (relative to BASE_DIR)
CHEATSHEETS_DIR = BASE_DIR / "cheatsheets"

# Allowed file extensions
ALLOWED_EXTENSIONS = {".md", ".php", ".js", ".sh", ".s", ".py", ".html"}  # Add needed extensions

# Security settings
MAX_SEARCH_LENGTH = 200
ALLOWED_SEARCH_CHARS = set(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
)

# Ripgrep command (ensure rg is installed and put its location here)
RIPGREP_CMD = "/usr/bin/rg"
