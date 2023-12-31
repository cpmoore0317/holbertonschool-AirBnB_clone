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
    
    def test_class_attrs(self):
        self.assertEqual(self.p1.city_id, "")
        self.assertEqual(self.p1.user_id, "")
        self.assertEqual(self.p1.name, "")
        self.assertEqual(self.p1.description, "")
        self.assertEqual(self.p1.number_rooms, 0)
        self.assertEqual(self.p1.number_bathrooms, 0)
        self.assertEqual(self.p1.max_guest, 0)
        self.assertEqual(self.p1.price_by_night, 0)
        self.assertEqual(self.p1.latitude, 0.0)
        self.assertEqual(self.p1.longitude, 0.0)
        self.assertEqual(self.p1.amenity_ids, [])
        self.assertIn('id', self.p1.to_dict())
        self.assertIn('created_at', self.p1.to_dict())
        self.assertIn('updated_at', self.p1.to_dict())
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)

    def test_instance_attrs(self):
        self.p1.city_id = "Eurika Springs"
        self.p1.user_id = "1124"
        self.p1.name = "Lofty Lookout"
        self.p1.description = ""
        self.p1.number_rooms = 32
        self.p1.number_bathrooms = 1
        self.p1.max_guests = 137
        self.p1.price_by_night = 3
        self.p1.latitude = 36
        self.p1.longitude = 37
        self.p1.amenity_ids = ["Hot tub", "Wifi"]
        self.assertEqual(self.p1.city_id, "Eurika Springs")
        self.assertEqual(self.p1.user_id, "1124")
        self.assertEqual(self.p1.name, "Lofty Lookout")
        self.assertEqual(self.p1.description, "")
        self.assertEqual(self.p1.number_rooms, 32)
        self.assertEqual(self.p1.number_bathrooms, 1)
        self.assertEqual(self.p1.max_guests, 137)
        self.assertEqual(self.p1.price_by_night, 3)
        self.assertEqual(self.p1.latitude, 36)
        self.assertEqual(self.p1.longitude, 37)
        self.assertIsInstance(self.p1.amenity_ids, list)