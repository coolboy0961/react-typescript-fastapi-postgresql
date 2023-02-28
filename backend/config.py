from functools import lru_cache
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str
    base_url: str
    database_url: str

    class Config:
        env_file = f"env/{os.getenv('ENVIRONMENT', 'unit-test')}.env"
        env_file_encoding = 'utf-8'

@lru_cache()
def get_settings():
    settings = Settings()
    print(f"load environment file: {settings.Config.env_file}")
    return settings