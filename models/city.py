#!/usr/bin/env python3
"""class city from basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    attributes:
        state_id: empty
        name: string - empty
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if there're values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
