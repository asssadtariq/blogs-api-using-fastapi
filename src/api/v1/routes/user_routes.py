"""This file represent the routes for /user API"""

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from src.api.v1.validators.user_validators import InValidatorUserAdd
from src.api.v1.db.session import get_db

router = APIRouter(prefix="/")


@router.post("/create_user", summary="")
def create_user(user_detail: InValidatorUserAdd, db: Session = Depends(get_db)):
    """To create a new user"""
    print("creating new user")
