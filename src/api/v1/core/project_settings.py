"""
It keeps project's constants variables 
variables imported from environment
"""

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

## load env variables
load_dotenv()


class Settings(BaseSettings):
    pass
