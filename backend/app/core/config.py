import yaml
from pathlib import Path
from pydantic_settings import BaseSettings

# Points to 'backend' directory
# core -> app -> backend
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    """
    Application settings configuration.
    
    Attributes:
        app (dict): General application settings.
        database (dict): Database connection settings.
        security (dict): Security settings (e.g., secret keys).
    """
    app: dict
    database: dict
    security: dict

def load_settings() -> Settings:
    """
    Loads application settings from a YAML file.

    Returns:
        Settings: An instance of the Settings class populated with data from 'settings.yaml'.

    Raises:
        FileNotFoundError: If 'settings.yaml' is not found in the project directory.
    """
    config_path = PROJECT_DIR / "settings.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")
    
    with open(config_path) as f:
        config_data = yaml.safe_load(f) or {}
    
    return Settings(**config_data)

settings = load_settings()