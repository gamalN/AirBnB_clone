#!/usr/bin/env python3
"""for class user from from basemodel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    attributes:
        email: empty
        password: empty
        first_name: empty
        last_name: empty
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if there're values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
