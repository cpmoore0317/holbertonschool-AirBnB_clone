#!/usr/bin/python3
""" Module for FileStorage class. """
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
    __file_path:  string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        dict_obj = FileStorage.__objects
        serialized_dict = {obj: dict_obj[obj].to_dict() for obj in dict_obj.keys()}
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized_dict, json_file)

    def reload(self):
        """ Deserializes the JSON file to __objects if the JSON file
        exists ; otherwise, nothing. """
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                dict_obj = json.load(json_file)
                for value in dict_obj.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
