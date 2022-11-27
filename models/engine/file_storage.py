#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 2022

@authors: Godday Okoduwa
          Ingrid Koumayeb
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class for serializing and deserializing objects into and from
    files.
    """
    __file_path = 'file.json'
    __objects = dict()

    def __init__(self):
        """
        init method for FileStorage class
        """
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Attributes:
            obj (Python object): The object to set
        """
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file_stor:
            json.dump(dictionary, file_stor)

    def reload(self):
        """
        deserializes the JSON file to __objects ONLY if the JSON file
        exists, otherwise, do nothing. If the file doesn't exist,
        raise no exception
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file1:
                loaded_json = json.load(file1)
            for k, v in loaded_json.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except Exception:
            pass
