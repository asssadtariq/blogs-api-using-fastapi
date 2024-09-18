"""
    To keep Declarative Base
    and all other models which needs to be added in DB 
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .user_model import User
from .blog_category_model import BlogCategory
from .blog_model import Blog
