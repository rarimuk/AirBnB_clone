#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines the BaseModel class of AirBnB project"""

    def __init__(self, *args, **kwargs):
        """INitializes a new BaseModel

        Args:
            *args (any): unused
            **kwargs (dict): the key/value of attributes
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for ke, val in kwargs.items():
                if ke == "created_at" or ke == "updated_at":
                    self.__dict__[ke] = datetime.strptime(val, tform)
                else:
                    self.__dict__[ke] = val
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
