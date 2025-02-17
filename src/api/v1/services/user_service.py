from typing import List
from sqlalchemy.orm import Session

from src.api.v1.models.user_model import User
from src.api.v1.validators.user_validators import (
    InValidatorUserAdd,
    InValidatorGetUsers,
)


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

    def get_users(self, user_conditions: InValidatorGetUsers) -> List[User]:
        users = self.db.query(User)

        if user_conditions.user_id:
            users = users.filter(User.user_id == user_conditions.user_id)

        # if user_conditions.username:
        #     users = users.filter(User.username == user_conditions.username)

        if user_conditions.email:
            users = users.filter(User.email == user_conditions.email)

        if user_conditions.first_name:
            users = users.filter(User.first_name == user_conditions.first_name)

        if user_conditions.last_name:
            users = users.filter(User.last_name == user_conditions.last_name)

        if user_conditions.is_active is not None:
            users = users.filter(User.is_active == user_conditions.is_active)

        if user_conditions.page_size:
            users = users.limit(limit=user_conditions.page_size)

        if user_conditions.page_number:
            users = users.offset(offset=user_conditions.page_number)

        print(users)

        users = users.all()

        print(users)


        return users
