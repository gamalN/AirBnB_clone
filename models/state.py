#!/usr/bin/env python3
"""stete to manage state entity"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    attributes:
        name: empty
    """
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if there're values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
