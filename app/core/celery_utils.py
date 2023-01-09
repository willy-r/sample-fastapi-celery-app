from celery import current_app as current_celery_app
from celery import Celery

from .settings import settings


def create_celery() -> Celery:
    celery_app = current_celery_app
    celery_app.config_from_object(settings, namespace="CELERY")

    return celery_app
