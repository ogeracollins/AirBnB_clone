#!/usr/bin/python3
"""
Review class deninition
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review class
    Attributes:
        place_id = Id of the place in review
        user_id - Id of reviewer
        text (str): Name of the state
    """

    place_id = 0
    user_id = 0
    text = ""
