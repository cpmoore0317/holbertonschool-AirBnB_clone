#!/usr/bin/python3
""" Unit testing for base_model.py """
import unittest
from models.base_model import BaseModel
import pathlib
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Class for base_model testing """
    @classmethod
    def setUpClass(cls):
        """
        Method to set up BaseModel classes for use during testing.
        """
        cls.base1 = BaseModel()
        cls.base2 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """
        Method to tear down BaseModel classes for use during testing.
        """
        del cls.base1
        del cls.base2
        return super().tearDownClass()
    
    def test_init(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)