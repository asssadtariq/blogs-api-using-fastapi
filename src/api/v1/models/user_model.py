"""
    This file has the User model
    its attributes, constraints, and relationships
"""

from sqlalchemy import UUID, Column, VARCHAR, DATE, Text, BOOLEAN, TIMESTAMP, func

from sqlalchemy.orm import relationship

from . import Base


class User(Base):
    """User Model
    This class represents the user in the app
    It contains information as user id, username, firstname
    """

    __tablename__ = "user"

    user_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    username = Column(VARCHAR(64), unique=True, nullable=False)
    email = Column(VARCHAR(64), unique=True, nullable=False)
    first_name = Column(VARCHAR(64), nullable=False)
    last_name = Column(VARCHAR(64), nullable=False)
    password = Column(VARCHAR(32))
    dob = Column(DATE, nullable=False)
    ver_key = Column(Text)
    is_verified = Column(BOOLEAN, default=False)
    is_active = Column(VARCHAR(32), default=True)
    created_on = Column(TIMESTAMP, server_default=func.now())
    last_modified = Column(TIMESTAMP, server_default=func.now())
    profile_img_path = Column(Text, nullable=True)

    user_blog = relationship("Blog", backref="user_blog")
