#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry(7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create subclass Rectangle from class BaseGeometry"""
    def __init__(self, width, height):
        """
        Create and validate instances
        weight and height: must be private & positive integer
        Args:
            width: width
            height: height
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
