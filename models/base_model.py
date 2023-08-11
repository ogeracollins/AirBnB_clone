#!/usr/bin/python3
"""
Parent class for entire project
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """"
    Base class containing common attributes/methods
    Attributes:
        id(str): Unique identifier for each model
        created_at: Time instance is created
        updated_at: Time instance is changed/created

    Methods:
        __str__: Prints class name, id and dictionary
        save(self): Updates updated_at with current time
        to_dict(self): Returns dict containing keys, values
    """

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
    """
    Returns class name, id and dictionary
    """
    return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
    """
    Updated updated_at to current time
    """
    self.updated_at = datetime.now()

    def to_dict(self):
    """
    Return dictionary of all keys/values
    """
    dict_cp = self.__dict__.copy()
    dict_cp["created_at"] = self.created_at.isoformat()
    dict_cp["updated_at"] = self.updated_at.isoformat()
    dict_cp["__class__"] = self.__class__.__name__

    return dict_cp
