""" This file creates FAST API app and register items like Middleware, Routes etc"""

from fastapi import FastAPI
from src.routes import register_routes


def create_app() -> FastAPI:
    """To create and return FastAPI app and register it to items like middleware, routes etc"""

    ## init fastapi app
    app = FastAPI()

    ## register middleware

    ## register routes
    register_routes(app)

    return app
