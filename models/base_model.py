#!/usr/python3
"""
Class BaseModel that defines attributes and methods for all other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The 'BaseModel' class serves as the foundation for all common attributes/methods 
    Attributes:
    
    """

    def __init__(self, id=None):
        """
        Initializes an instance of the 'BaseModel' class

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
