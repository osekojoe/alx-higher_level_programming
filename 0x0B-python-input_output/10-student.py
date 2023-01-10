#!/usr/bin/python3

"""
a class Student that defines a student
"""


class Student:
    """define a student"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to dictionary representation
        attrs: attributes
        - if attrs is list of strings: return attribute names
        else: return all attributes
        """
        my_dict = dict()
        if type(attrs) is list and all(type(i) is str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    my_dict.update({i: self.__dict__[i]})
            return my_dict
        return self.__dict__.copy()
