from fastapi import FastAPI

from .celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    # Before loading routes.
    app.celery_app = create_celery()

    # Routes.
    from ..users import users_router
    app.include_router(users_router) 

    @app.get("/", include_in_schema=False)
    async def root():
        return {"message": "Hello, World!"}

    return app
