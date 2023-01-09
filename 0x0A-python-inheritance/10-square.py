#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """calculate size and validate with integer validator"""
    def __init__(self, size):
        """find size and validate it as well"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
