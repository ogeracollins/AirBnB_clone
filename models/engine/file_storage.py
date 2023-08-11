#!/usr/bin/python3
"""
FileStorage serialization and deserialization of JSON
"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

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
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f.read())
                for value in new_dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except FileNotFoundError:
            pass


