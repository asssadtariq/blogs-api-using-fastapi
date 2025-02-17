"""
This file has the User model
its attributes, constraints, and relationships
"""

import uuid
from sqlalchemy import UUID, Column, VARCHAR, DATE, Text, BOOLEAN, TIMESTAMP, func

from sqlalchemy.orm import relationship

from . import Base


class User(Base):
    """User Model
    This class represents the user in the app
    It contains information as user id, username, firstname
    """

    __tablename__ = "user"

    user_id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    username = Column(VARCHAR(64), unique=True, nullable=False)
    email = Column(VARCHAR(64), unique=True, nullable=False)
    first_name = Column(VARCHAR(64), nullable=False)
    last_name = Column(VARCHAR(64), nullable=False)
    password = Column(VARCHAR(64))
    dob = Column(DATE, nullable=False)
    ver_key = Column(Text)
    is_verified = Column(BOOLEAN, default=False)
    is_active = Column(BOOLEAN, default=True)
    created_on = Column(TIMESTAMP, server_default=func.now())
    last_modified = Column(TIMESTAMP, server_default=func.now())
    profile_img_path = Column(Text, nullable=True)

    user_blog = relationship("Blog", backref="user_blog")

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
            "ver_key": self.ver_key,
            "is_verified": self.is_verified,
            "is_active": self.is_active,
            "created_on": self.created_on,
            "last_modified": self.last_modified,
            "profile_img_path": self.profile_img_path,
        }
