"""Create HuggingFace dataset from JSON conversation data."""

from pathlib import Path

import polars as pl
from pydantic import DirectoryPath, validate_call

from .config import DATA_DIR, REPO_ROOT


@validate_call
def create_hf_dataset(
    repo_root: DirectoryPath = REPO_ROOT, data_dir: DirectoryPath = DATA_DIR
):
    """Main function to create the HuggingFace dataset."""
    print(f"Repository root: {repo_root}")
    print(f"Data directory: {data_dir}")
