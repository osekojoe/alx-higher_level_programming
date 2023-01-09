#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiate and validate size"""
    def __init__(self, size):
        """create and validate size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """print rectangle width/height"""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)

    def area(self):
        """Area method"""
        return self.__size ** 2
