"""This file represent the validators for user api"""

from uuid import UUID
from typing import Optional
from datetime import date
from pydantic import Field
from pydantic_settings import BaseSettings


class InValidatorUserAdd(BaseSettings):
    user_id: Optional[UUID] = Field(None)
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    dob: date
    ver_key: Optional[str]
    is_active: bool = Field(True)
    profile_img_path: str
