from pathlib import Path
import os

import yaml
from dotenv import load_dotenv

# Project root
ROOT_DIR = Path(__file__).resolve().parents[2]

# Load environment variables
load_dotenv(ROOT_DIR / ".env")

# Load YAML configuration
with open(ROOT_DIR / "configs" / "config.yaml", "r") as file:
    CONFIG = yaml.safe_load(file)

# API Keys
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")