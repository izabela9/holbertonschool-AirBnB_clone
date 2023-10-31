#!/usr/bin/python3
'''
Module for base model
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    Class for base objects
    '''

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        updates updated_at with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        returns a dictionary with all
        keys/values of __dict__ of the instance
        '''
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
