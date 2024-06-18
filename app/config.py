import os


class Config:
    DB_CONFIG = os.getenv(
        "DATABASE_URL",
        "",
    )
    RABBIT_URL = os.getenv(
        "RABBITMQ_URL",
        ""
    )


config = Config
