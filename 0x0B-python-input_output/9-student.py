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

    def to_json(self):
        """to dictionary representation"""
        return self.__dict__
