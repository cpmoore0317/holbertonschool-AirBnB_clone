#!/usr/python3
"""
Class BaseModel that defines attributes and methods for all other classes
"""
from uuid import uuid4
from datetime import datetime


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

    def __init__(self):
        """
        Initializes an instance of the 'BaseModel' class.

        Args:

        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        '''
        updates public instance attribute
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        returns dictionary containing all keys/values
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['uodated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        _summary_

        Returns:
            _type_: _description_
        """
        return "{}".format(self.__dict__)
