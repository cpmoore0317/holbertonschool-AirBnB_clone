#!/usr/bin/python3
'''
defines city class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    represent city class objects
    '''
    state_id = ""
    name = ""
