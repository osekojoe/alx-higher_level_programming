#!/usr/bin/python3

"""
Class Base:
 private class attribute __nb_objects = 0
"""


import json
from os import path
import csv

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """dictionary to instance"""
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """file to instances"""
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())

            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    column_names = ["id", "width", "height", "x", "y"]
                else:
                    column_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=column_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV
        Has the same behavior as the JSON serialization/deserialization
        """
        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    column_names = ["id", "width", "height", "x", "y"]
                else:
                    column_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=column_names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                            for d in list_dicts]

                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
