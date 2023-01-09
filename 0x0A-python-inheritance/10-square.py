#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiate and validate size"""
    def __init__(self, size):
        """create and validate size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
