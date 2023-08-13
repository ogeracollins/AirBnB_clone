#!/usr/bin/python3
"""
FileStorage serialization and deserialization of JSON
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
    __file_path = "file.json"
    __objects = {}
    air_dict = {
        "BaseModel": BaseModel, "User": User, "Place": Place,
        "Amenity": Amenity, "City": City, "Review": Review, "State": State
    }

    def all(self):
        """
        Returns dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key id
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to JSON fole in __file_path
        """
        with open(self.__file_path, 'w+')as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.air_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
