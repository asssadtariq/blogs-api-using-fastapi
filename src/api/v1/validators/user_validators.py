"""This file represent the validators for user api"""

from uuid import UUID
from typing import Optional
from datetime import date
from pydantic import Field
from pydantic_settings import BaseSettings


class InValidatorUserAdd(BaseSettings):
    """
    InValidatorUserAdd is a Pydantic model used for validating user input data when adding a new user.
    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        password (str): The password for the user's account.
        dob (date): The date of birth of the user.
        ver_key (Optional[str]): An optional verification key for the user.
        is_active (bool): A flag indicating whether the user is active. Defaults to True.
        profile_img_path (str): The file path to the user's profile image.
    """

    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    dob: date
    ver_key: Optional[str] = None
    is_active: bool = Field(True)
    profile_img_path: Optional[str] = None

class InValidatorGetUsers(BaseSettings):
    """
    Validator for retrieving users with optional filters.
    Attributes:
        user_id (Optional[UUID]): The unique identifier of the user.
        username (Optional[str]): The username of the user.
        email (Optional[str]): The email address of the user.
        first_name (Optional[str]): The first name of the user.
        last_name (Optional[str]): The last name of the user.
        is_active (Optional[bool]): The active status of the user.
        page_size (int): The number of users to retrieve per page. Default is 10.
        page_number (int): The page number to retrieve. Default is -1.
    """

    user_id: Optional[UUID] = Field(None)
    username: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    is_active: Optional[bool]  = Field(None)
    page_size: int = Field(10)
    page_number: int = Field(default=0, ge=0)
