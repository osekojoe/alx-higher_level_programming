#!/usr/bin/python3

"""
class Square inheriting from Rectangle
"""


from models.Rectangle import Rectangle


class Square(Rectangle):
    """describes a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """square initialization"""
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        """get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
