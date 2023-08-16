#!/usr/bin/env python3
"""class review from base model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    attributes:
        place_id: empty
        user_id: empty
        text: empty
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if there're values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
