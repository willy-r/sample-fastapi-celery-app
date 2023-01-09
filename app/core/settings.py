import os
import pathlib
from typing import Any
from functools import lru_cache


class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")
    DATABASE_CONNECT_DICT: dict[str, Any] = {}

    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")
    CELERY_BEAT_SCHEDULE: dict[str, Any] = {
        "divide-every-30-seconds": {
            "task": "app.users.tasks.divide_periodically",
            "schedule": 30.0,  # Seconds.
            "args": (1, 2),
        }
    }


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    DATABASE_CONNECT_DICT = {
        "check_same_thread": False,  # For SQLite3
    }


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }

    config_name = os.getenv("ENVIRONMENT", "development").lower()
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
