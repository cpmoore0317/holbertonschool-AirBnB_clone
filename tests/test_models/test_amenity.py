#!/usr/bin/python3
"""Unittest class for Amenity and all its functions"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestBase(unittest.TestCase):
    """ Test cases for amenity.py """

    def testSet(self):
        """Check if you can generate an instance"""
        self.C = Amenity()
    
    def testExist(self):
        """A test that check if the attributes exists in the class"""
        amenity1 = Amenity()
        self.assertTrue(hasattr(amenity1, "id"))
        self.assertTrue(hasattr(amenity1, "created_at"))
        self.assertTrue(hasattr(amenity1, "updated_at"))
        self.assertTrue(hasattr(amenity1, "name"))
    
    def testUser(self):
        """A test to check if all values are the correct type"""
        amenity2 = Amenity()
        self.assertIsInstance(amenity2.id, str)
        self.assertIsInstance(amenity2.created_at, datetime)
        self.assertIsInstance(amenity2.updated_at, datetime)
        self.assertIsInstance(amenity2.name, str)