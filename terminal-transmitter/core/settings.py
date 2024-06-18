import logging

from pydantic_settings import BaseSettings, SettingsConfigDict

from project_root import PROJECT_ROOT


class Settings(BaseSettings):
    """Настроечки микросевриса"""
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT / '.env')

    SERVER_HOST: str
    SERVER_PORT: int
    ROOT_PATH: str

    TOKEN_UPDATE_TIME: int

    LOG_LEVEL: int = logging.INFO
    DIRECTORY_OF_LOGS: str = PROJECT_ROOT / "logs"
    LOG_FORMAT: str = "%(asctime)s: %(name)s - %(" "levelname)s  | %(message)s"
    LOG_FORMAT_REDIS: str = "%(asctime)s: %(name)s - %(" "levelname)s  | %(message)s"
    VERSION: str = "0.0.1"

    @property
    def db_url(self):
        return ""

    @property
    def redis_url(self):
        return f""

    @property
    def rabbitmq_url(self):
        return ""



settings = Settings()
