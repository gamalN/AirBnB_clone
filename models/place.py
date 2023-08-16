#!/usr/bin/env python3
"""place module from base module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    attributes:
        city_id: empty
        user_id: empty
        name: empty
        description: empty
        number_rooms: 0
        number_bathrooms: 0
        max_guest: 0
        price_by_night: 0
        latitude: 0.0
        longitude: 0.0
        amenity_ids (list): empty string list
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if there're values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
