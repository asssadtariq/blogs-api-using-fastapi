"""This file represent the routes for /user API"""

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from src.api.v1.db.session import get_db
from src.api.v1.core.security import validate_token
from src.api.v1.controllers.user_controller import UserController
from src.api.v1.validators.user_validators import InValidatorUserAdd

router = APIRouter(prefix="/user")


@router.post("/create_user", summary="")
def create_user(
    user_details: InValidatorUserAdd,
    db: Session = Depends(get_db),
):
    """To create a new user"""
    ## call the controller to add data
    response = UserController(db=db).add_new_user(user_details=user_details)

    ## return response
