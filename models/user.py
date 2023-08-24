#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base  # import Base
from sqlalchemy import Column, String  # import necessary SQLAlchemy classes


class User(BaseModel, Base):  # make User inherit from Base
    """This class defines a user by various attributes"""
    __tablename__ = 'users'  # set table name
    email = Column(String(128), nullable=False)  # set email column
    password = Column(String(128), nullable=False)  # set password column
    first_name = Column(String(128), nullable=True)  # set first_name column
    last_name = Column(String(128), nullable=True)  # set last_name column
