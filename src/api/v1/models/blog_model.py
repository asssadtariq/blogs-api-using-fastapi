"""This file represent blog model"""

from sqlalchemy import (
    Column,
    func,
    UUID,
    VARCHAR,
    BOOLEAN,
    TEXT,
    INTEGER,
    TIMESTAMP,
    ForeignKey,
)

from . import Base


class Blog(Base):
    """This class represents the blog model"""

    __tablename__ = "blog"

    blog_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(VARCHAR(256), nullable=False)
    content = Column(TEXT, nullable=False)
    likes = Column(INTEGER, default=0)
    view = Column(INTEGER, default=0)
    created_on = Column(TIMESTAMP, server_default=func.now())
    last_modified = Column(
        TIMESTAMP, server_default=func.now(), server_onupdate=func.now()
    )
    is_active = Column(BOOLEAN, default=True)

    blog_catg_id = Column(UUID(as_uuid=True), ForeignKey("blog_category.blog_catg_id"))
