"""
It keeps project's constants variables 
variables imported from environment
"""

import os
from urllib import parse
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

## load env variables
load_dotenv()


class Settings(BaseSettings):
    """Class to represent project settings"""

    ## Database details
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_PORT: str = os.environ.get("DB_PORT")

    ## create DB URL
    DB_URL: str = (
        f"postgresql+psycopg2://{DB_USER}:{parse.quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


def settings():
    """To return settings object"""
    return Settings()
