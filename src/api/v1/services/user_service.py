from sqlalchemy.orm import Session

from src.api.v1.models.user_model import User
from src.api.v1.validators.user_validators import InValidatorUserAdd


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add_user(self, user_details: InValidatorUserAdd) -> User:
        user_obj: User = User(
            username=user_details.user_id,
            email=user_details.email,
            first_name=user_details.first_name,
            last_name=user_details.last_name,
            password=user_details.password,
            dob=user_details.dob,
            ver_key=user_details.ver_key,
        )
