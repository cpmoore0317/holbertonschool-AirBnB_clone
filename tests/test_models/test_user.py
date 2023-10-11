#!/usr/bin/python3
"""
Unit testing class User
"""

import unittest
from models import user
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class User"""

    @classmethod
    def setUpClass(self):
        self.my_model = User()

    def setUp(self):
        self.dict = self.my_model.to_dict()

    def test_docmodule(self):
        self.assertIsNotNone(user.__doc__)

    def test_docclass(self):
        self.assertIsNotNone(User.__doc__)

    def test_create_base(self):
        self.assertIsInstance(self.my_model, User)

    def test_attr(self):
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)
        self.assertEqual(self.my_model.email, "")
        self.assertEqual(self.my_model.password, "")
        self.assertEqual(self.my_model.first_name, "")
        self.assertEqual(self.my_model.last_name, "")

    def test_create_kwargs(self):
        self.kwargs = User(self.dict)
        self.assertIsInstance(self.kwargs, User)

    def test_update(self):
        update_old = self.my_model.updated_at
        self.my_model.save()
        update_new = self.my_model.updated_at
        self.assertTrue(update_old != update_new)

    def test_class(self):
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))