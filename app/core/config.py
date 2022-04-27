from pathlib import Path
from pydantic import BaseModel, BaseSettings, Field
from typing import Optional

APP_ROOT = Path(__file__).parent.parent


class AppSettings(BaseModel):
    """
    Configuration settings specific to FastAPI
    Will be accessed qs  'more_settings' within app
    """


class GlobalSettings(BaseSettings):
    """
    Inherits 'BaseSettings' from pydantic
    """
    APP_DIR: Path = APP_ROOT
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    MONGO_SCHEME: Optional[str] = None
    MONGO_HOST: Optional[str] = None
    MONGO_PORT: Optional[str] = None
    MONGO_USER: Optional[str] = None
    MONGO_PASSWORD: Optional[str] = None
    MONGO_DB: Optional[str] = None

    FAVORITE_SONG: Optional[str] = None

    class Config:
        env_file = APP_ROOT.parent / ".env"


class DevSettings(GlobalSettings):
    """
    Dev Environment
    """

    class Config:
        env_prefix: str = "DEV_"


class ProdSettings(GlobalSettings):
    """
    Prod Environment
    """

    class Config:
        env_prefix: str = "PRD_"


class FactorySettings:
    """Callable class that loads Dev or Prod settings
    based on `ENV_STATE` defined in .env file.
    """

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevSettings()
        elif self.env_state == "prd":
            return ProdSettings()
        else:
            raise ValueError(
                f"Invalid ENV_STATE: {self.env_state}"
            )
