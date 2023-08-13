#!/usr/bin/python3
"""
City class deninition
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city class
    Attributes:
        state_id(str): Unique state identifier
        name(str): Name of the city
    """

    state_id = ""
    name = ""
