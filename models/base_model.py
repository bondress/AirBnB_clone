#!/usr/bin/python3
"""Defines BaseModel Class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """The BaseModel of the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize new BaseModel."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
	else:
		models.storage.new(self)

    def save(self):
        """Change updated_at to current datetime"""
        self.updated_at = datetime.now()
	models.storage.save()

    def to_dict(self):
        "Return the dictionary of the BaseModel instance"
        dct = self.__dict__.copy()
        dct["created_at"] = self.created_at.isoformat()
        dct["updated_at"] = self.updated_at.isoformat()
        dct["__class__"] = self.__class__.__name__
        return dct

    def __str__(self):
        """Return the str representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
