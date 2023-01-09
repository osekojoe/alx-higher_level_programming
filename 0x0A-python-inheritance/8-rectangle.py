#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry(7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create subclass Rectangle from class BaseGeometry"""
    def __init__(self, width, height):
        """
        width and height: must be private + integer
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
