#!/usr/bin/python3
""" Module for FileStorage class. """
import json
import models


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
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ Deserializes the JSON file to __objects if the JSON file
        exists ; otherwise, nothing. """
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = models[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
