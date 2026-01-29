import yaml
from pathlib import Path
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


PROJECT_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    app: dict
    database: dict
    security: dict

    @classmethod
    def settings_customize_sources(cls, settings_cls, init_settings, env_settings, dotenv_settings, file_secret_settings):
        def yaml_config_settings_source(settings: BaseSettings) -> dict:
            return yaml.safe_load(open(PROJECT_DIR / "settings.yaml"))
        return (init_settings, env_settings, yaml_config_settings_source)

settings = Settings()