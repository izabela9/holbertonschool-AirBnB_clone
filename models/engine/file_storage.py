#!/usr/bin/python3
'''
Module for file storage
'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''
    Class for file storage
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        function that returns the dict of objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        function to set obj in objects
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''
        function to serialize objects to the json file
        '''
        obj_dictionary = {}
        for key, value in FileStorage.__objects.items():
            obj_dictionary[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dictionary, f)

    def reload(self):
        '''
        functiont to deserialize json files to objects
        '''
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    obj = eval(cls_name)(**value)
                    self.new(obj)
        except Exception as e:
            pass
