import yaml
from pathlib import Path
from pydantic_settings import BaseSettings

# Points to 'backend' directory
# core -> app -> backend
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    app: dict
    database: dict
    security: dict

def load_settings() -> Settings:
    config_path = PROJECT_DIR / "settings.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path) as f:
        config_data = yaml.safe_load(f) or {}
    
    return Settings(**config_data)

settings = load_settings()