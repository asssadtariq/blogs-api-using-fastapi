"""This class represent the Blog category model"""

from sqlalchemy import Column, UUID, VARCHAR, TIMESTAMP, func, BOOLEAN
from sqlalchemy.orm import relationship

from . import Base


class BlogCategory(Base):
    """This class represents the Blog Category Model"""

    __tablename__ = "blog_category"

    blog_catg_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    blog_catg_name = Column(VARCHAR(128), nullable=False)
    created_on = Column(TIMESTAMP, server_default=func.now())
    last_modified = Column(
        TIMESTAMP, server_default=func.now(), server_onupdate=func.now()
    )
    is_active = Column(BOOLEAN, default=True)

    blog = relationship("Blog", backref="category")
