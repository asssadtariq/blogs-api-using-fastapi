"""This file represent the routes for /user API"""

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from src.api.v1.db.session import get_db
from src.api.v1.validators.user_validators import InValidatorUserAdd
from src.api.v1.core.security import validate_token

router = APIRouter(prefix="/user")


@router.post("/create_user", summary="")
def create_user(
    user_detail: InValidatorUserAdd,
    db: Session = Depends(get_db),
    # _=Depends(validate_token),
):
    """To create a new user"""
    print("Creating new user /user")

    ## call the controller to add data
    

    ## return response
