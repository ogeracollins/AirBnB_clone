#!/usr/bin/python3
"""
User class definition
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Represents a user
    Attributes:
        email(str): User email
        password(str): User password
        first_name(str): First name
        last_name(str): Last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
