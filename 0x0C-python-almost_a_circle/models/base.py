#!/usr/bin/python3

"""
Class Base:
 private class attribute __nb_objects = 0
"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        if id is not None, assign the public instance attribute id with this
          argument value - assumption: id is an integer (not testing needed)
        otherwise, increment __nb_objects and assign the new value to the public
          instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
