#!/usr/bin/python3
"""
module for base model class
"""
import uuid
from datetime import datetime
import models  # ensures the models module __init__.py is run


class BaseModel:
    """The is the Base model class"""
    def __init__(self, *args, **kwargs):
        """Constructor for the base model class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != "__class__":
                    setattr(self, k, v)
        models.storage.new(self)

    def __str__(self):
        """Return a string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the class"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
