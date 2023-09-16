#!/usr/bin/python3
"""This is the FileStorage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """This is the FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This is the all method"""
        return FileStorage.__objects

    def new(self, obj):
        """This is the new method"""
        dct = FileStorage.__objects
        objclsnm = obj.__class__.__name__
        dct["{}.{}".format(objclsnm, obj.id)] = obj

    def save(self):
        """This is the save method"""
        obdct = FileStorage.__objects
        objdct = {obj: obdct[obj].to_dict() for obj in obdct.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdct, f)

    def reload(self):
        """This is the reload method"""
        try:
            with open(FileStorage.__file_path) as f:
                obdct = json.load(f)
                for i, o in obdct.items():
                    self.new(BaseModel(**o))
        except FileNotFoundError:
            return
