#!/usr/bin/python3
"""This is the FileStorage module"""
import json
from models.base_model import BaseModel

	class FileStorage:
	"""This is the FileStorage class"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""This is the all method"""
		return FileStorage.__objects

	def new(self, obj):
		"""This is the new method"""
		dct = FileStorage.__objects
		cname = obj.__class__.__name__
		dct["{}.{}".format(cname, obj.id)] = obj

	def save(self):
		"""This is the save method"""
		dct = {}
		for i, o in FileStorage.__objects.items():
			dct[i] = o.to_dict()
		with open(FileStorage.__file_path, "w+") as f:
			json.dump(dct, f)

	def reload(self):
		"""This is the reload method"""
		try:
			o1 = []
			with open(FileStorage.__file_path) as f:
			dct = json.load(f)
			for i, o in dct.items():
				dct[i] = BaseModel(**o)
			FileStorage.__objects = dct
		except FileNotFoundError:
			return
