#!/usr/bin/python3
""" Unit testing for file_storage.py """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models

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

    def test_doc_module(self):
        """Checking doc module"""
        self.assertIsNotNone(models.__doc__)

    def test_doc_class(self):
        """Checking doc class"""
        self.assertIsNotNone(models.FileStorage.__doc__)

    def test_json_file(self):
        """Check if file.json is not empty"""
        with open("file.json") as json_file:
            self.assertGreater(len(json_file.read()), 0)

    def test_reload_from_json(self):
        """Test reloading objects from JSON"""
        self.my_model.name = "My_first_model"
        self.my_model.my_number = 89
        class_name = self.my_model.__class__.__name__
        key = f"{class_name}.{self.my_model.id}"
        self.my_model.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIsNotNone(objects[key])
        reloaded_obj = objects[key]
        self.assertTrue(self.my_model.__dict__ == reloaded_obj.__dict__)
        self.assertTrue(self.my_model is not reloaded_obj)
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.name, "My_first_model")

    def test_instance(self):
        """Test FileStorage instance"""
        file_storage = models.FileStorage()
        self.assertEqual(file_storage.path(), "file.json")
        base_model = models.BaseModel()
        file_storage.new(base_model)
        self.assertGreater(len(file_storage.all()), 0)

if __name__ == '__name__':
    unittest.main()