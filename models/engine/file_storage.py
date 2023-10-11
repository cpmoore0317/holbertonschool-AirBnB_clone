#!/usr/bin/python3
""" Module for FileStorage class. """
import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

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

    def classes(self):
        """
        Return a dictionary of all the supported classes for serialization.
        You can add more classes as needed.
        """
        return {
            'BaseModel': BaseModel,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        This includes all the supported classes.
        """
        dict_obj = FileStorage.__objects
        serialized_dict = {
            key: obj.to_dict()
            for key, obj in dict_obj.items()
        }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(serialized_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the JSON file exists.
        This handles all the supported classes.
        """
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                dict_obj = json.load(json_file)
                for key, value in dict_obj.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    obj_class = self.classes().get(class_name)
                    if obj_class:
                        self.new(obj_class(**value))
        except FileNotFoundError:
            pass
