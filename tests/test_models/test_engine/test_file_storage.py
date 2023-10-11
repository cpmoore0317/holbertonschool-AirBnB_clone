#!/usr/bin/python3
""" Unit testing for file_storage.py """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage as FileStorage


class TestFileStorage(unittest.TestCase):
    """ Unit testing for file_storage.py """
    def setUp(cls):
        """
        Method to set up FileStorage classes for use during testing.
        """
        cls.filestorage1 = FileStorage()
        cls.filestorage2 = FileStorage()
        cls.basemodel1 = BaseModel()

    def tearDown(cls):
        """
        Method to tear down FileStorage classes for use during testing.
        """
        del cls.filestorage1
        del cls.filestorage2
        del cls.basemodel1
        return super().tearDown()

if __name__ == '__name__':
    unittest.main()