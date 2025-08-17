"""Configuration for HuggingFace dataset creation."""

from pathlib import Path

# Go up 3 levels from hf_dataset/src/hf_dataset/config.py to get repo root
REPO_ROOT = Path(__file__).parents[3]
DATA_DIR = REPO_ROOT / "res_v0.2"
