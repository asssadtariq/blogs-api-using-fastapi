"""This file contains the authentication code"""

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.api.v1.db.session import get_db

router = APIRouter()


@router.post("/token")
def login_via_docs(
    user_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    print(user_data.username)
