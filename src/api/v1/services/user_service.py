from sqlalchemy.orm import Session

from src.api.v1.models.user_model import User
from src.api.v1.validators.user_validators import InValidatorUserAdd


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add_user(
        self, user_details: InValidatorUserAdd, do_commit: bool = True
    ) -> User:
        user_obj: User = User(
            username=user_details.username,
            email=user_details.email,
            first_name=user_details.first_name,
            last_name=user_details.last_name,
            password=user_details.password,
            dob=user_details.dob,
            ver_key=user_details.ver_key,
        )

        # add data in the db
        self.db.add(user_obj)

        # commit changes
        if do_commit:
            self.db.commit()

        # refresh the data
        self.db.refresh(user_obj)

        return user_obj
