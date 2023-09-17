#!/usr/bin/python3
"""This is the FileStorage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This is the FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This is the all method"""
        return FileStorage.__objects

    def new(self, obj):
        """This is the new method"""
        objclsnm = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objclsnm, obj.id)] = obj

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
                for o in obdct.values():
                    clsnm = o["__class__"]
                    del o["__class__"]
                    self.new(eval(clsnm)(**o))
        except FileNotFoundError:
            return
