"""
Centralized project paths for PingSense.
All modules should import paths from here instead of hardcoding directories.
"""

from pathlib import Path

# --------------------------------------------------
# Project Root
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]

# --------------------------------------------------
# Data Directories
# --------------------------------------------------

DATA_DIR = ROOT_DIR / "data"

RAW_DATA = DATA_DIR / "raw"

PROCESSED_DATA = DATA_DIR / "processed"

CACHE_DATA = DATA_DIR / "cache"

# --------------------------------------------------
# Media Directories
# --------------------------------------------------

IMAGES_DIR = RAW_DATA / "images"

AUDIO_DIR = RAW_DATA / "audio"

VIDEOS_DIR = RAW_DATA / "videos"

# --------------------------------------------------
# Cache Directories
# --------------------------------------------------

OCR_CACHE = CACHE_DATA / "ocr"

TRANSCRIPT_CACHE = CACHE_DATA / "transcripts"

EMBEDDING_CACHE = CACHE_DATA / "embeddings"

LLM_CACHE = CACHE_DATA / "llm"

# --------------------------------------------------
# Output Directory
# --------------------------------------------------

OUTPUT_DIR = ROOT_DIR / "outputs"

LOGS_DIR = OUTPUT_DIR / "logs"

# --------------------------------------------------
# Config Directory
# --------------------------------------------------

CONFIG_DIR = ROOT_DIR / "configs"

PROMPTS_DIR = CONFIG_DIR / "prompts"

# --------------------------------------------------
# Documentation
# --------------------------------------------------

DOCS_DIR = ROOT_DIR / "docs"

# --------------------------------------------------
# Test Directory
# --------------------------------------------------

TESTS_DIR = ROOT_DIR / "tests"

# --------------------------------------------------
# Notebooks
# --------------------------------------------------

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"

# --------------------------------------------------
# Ensure Required Directories Exist
# --------------------------------------------------

DIRECTORIES = [
    PROCESSED_DATA,
    CACHE_DATA,
    OCR_CACHE,
    TRANSCRIPT_CACHE,
    EMBEDDING_CACHE,
    LLM_CACHE,
    OUTPUT_DIR,
    LOGS_DIR,
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)