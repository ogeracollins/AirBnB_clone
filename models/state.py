#!/usr/bin/python3
"""
States class deninition
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state class
    Attributes:
        name(str): Name of the state
    """

    name = ""
