"""This file imports all routes and register it to our fast api app"""

from fastapi import FastAPI
from src.api.v1.routes.user_routes import router as user_router


def register_routes(app: FastAPI) -> None:
    """To register routes to our app"""

    app.include_router(router=user_router)
