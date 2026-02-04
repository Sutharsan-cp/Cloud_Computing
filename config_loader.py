import os
import yaml
from pathlib import Path
from typing import Any, Dict
from models import Config
from pydantic import ValidationError

CONFIG_PATH = os.getenv("CONFIG_PATH", "config.yaml")

def load_yaml(path: str = CONFIG_PATH) -> Dict[str, Any]:
    text = Path(path).read_text()
    return yaml.safe_load(text) or {}

def load_config(path: str = CONFIG_PATH) -> Config:
    raw = load_yaml(path)
    # environment overrides
    if os.getenv("DB_HOST"):
        raw.setdefault("database", {})["host"] = os.getenv("DB_HOST")
    if os.getenv("APP_MODE"):
        raw.setdefault("app", {})["mode"] = os.getenv("APP_MODE")
    try:
        return Config(**raw)
    except ValidationError as e:
        raise RuntimeError(f"Config validation error: {e}")

def save_config(data: Dict[str, Any], path: str = CONFIG_PATH) -> None:
    Path(path).write_text(yaml.safe_dump(data, sort_keys=False))
