#!/usr/bin/python3
'''
define review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    represents review class objects
    '''

    place_id = ""
    user_id = ""
    text = ""
