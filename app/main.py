from .core import create_app

from dotenv import load_dotenv

load_dotenv()

app = create_app()
celery = app.celery_app
