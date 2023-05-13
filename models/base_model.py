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

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, d)
