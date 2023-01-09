from fastapi import APIRouter

users_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

from . import models, tasks  # noqa
