#!/usr/bin/python3
"""
Unit testing for place class
"""
import unittest
from models.place import Place


class PlaceTests(unittest.TestCase):
    """
    Class for place unit testing
    """
    @classmethod
    def setUp(cls):
        """
        Method to set up Place classes for use during testing
        """
        cls.p1 = Place()

    @classmethod
    def tearDown(cls):
        """
        Method to tear down State classes for use during testing
        """
        del cls.p1
        return super().tearDownClass()