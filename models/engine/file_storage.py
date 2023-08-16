#!/usr/bin/python3
"""
module for file storage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """The file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id
        Args:
            obj: given object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {}
            for k, v in self.__objects.items():
                d[k] = v.to_dict()
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                d = json.load(f)
                for k, v in d.items():
                    if v["__class__"] == "BaseModel":
                        self.__objects[k] = BaseModel(**v)
                    elif v["__class__"] == "User":
                        self.__objects[k] = User(**v)
                    elif v["__class__"] == "State":
                        self.__objects[k] = State(**v)
                    elif v["__class__"] == "City":
                        self.__objects[k] = City(**v)
                    elif v["__class__"] == "Amenity":
                        self.__objects[k] = Amenity(**v)
                    elif v["__class__"] == "Place":
                        self.__objects[k] = Place(**v)
                    elif v["__class__"] == "Review":
                        self.__objects[k] = Review(**v)
        except FileNotFoundError:
            pass
