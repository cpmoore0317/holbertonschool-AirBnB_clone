#!/usr/bin/python3
"""
Class BaseModel that defines attributes and methods for all other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    The 'BaseModel' class serves as the foundation for all common
    attributes/methods for other classes.

    Attributes:
    id(str): A public instance attribute representing the unique identifier
    of an instance.

    created_at(datetime):

    updated_at(datetime):
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the 'BaseModel' class.

        Args:

        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        updates the attribute updated_at with the current datetime
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates public instance attribute
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        returns dictionary containing all keys/values
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
