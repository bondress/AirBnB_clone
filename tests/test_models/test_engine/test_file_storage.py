#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test__FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test__FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(1)

    def test__FileStorage_file_path_is_private_attribute(self):
        with self.assertRaises(AttributeError):
            fs = FileStorage()
            print(fs.__file_name)

    def test__FileStorage_objects_is_private_attribute(self):
        with self.assertRaises(AttributeError):
            fs = FileStorage()
            print(fs.__objects)

    def test__storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):

        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test__all(self):
        objs = models.storage.all()
        self.assertEqual(type(objs), dict)
        self.assertEqual(str, type(list(objs.keys())[0]))
        self.assertIsInstance(list(objs.values())[0], BaseModel)

    def test__all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(1)

    def test__new(self):
        bsmd = BaseModel(id="123")
        models.storage.new(bsmd)
        self.assertIn("BaseModel.123", models.storage.all().keys())
        self.assertIn(bsmd, models.storage.all().values())

    def test__new_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(1)

    def test__save(self):
        bsmd = BaseModel()
        models.storage.new(bsmd)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bsmd.id, save_text)

    def test__save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(1)

    def test__reload(self):
        bsmd = BaseModel()
        with open("file.json", "w") as f:
            json.dump({"BaseModel." + bsmd.id: bsmd.to_dict()}, f)
        models.storage.reload()
        self.assertIn("BaseModel." + bsmd.id, models.storage.all().keys())

    def test__reload_no_file(self):
        objs = models.storage.all()
        models.storage.reload()
        self.assertEqual(objs, models.storage.all())

    def test__reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(1)


if __name__ == "__main__":
    unittest.main()
