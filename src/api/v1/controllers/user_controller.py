from sqlalchemy.orm import Session

from src.api.v1.models.user_model import User
from src.api.v1.services.user_service import UserService
from src.api.v1.helper.helpers import generate_random_string
from src.api.v1.validators.user_validators import InValidatorUserAdd
from src.api.v1.core.security import get_password_hash


class UserController:
    def __init__(self, db: Session):
        self.db = db

    def add_new_user(self, user_details: InValidatorUserAdd) -> User:
        # transform the user details, hash the password, get random string for verification key
        verification_key = generate_random_string(text_length=10)
        password_hash = get_password_hash(user_details.password)

        print(password_hash)
        return True
