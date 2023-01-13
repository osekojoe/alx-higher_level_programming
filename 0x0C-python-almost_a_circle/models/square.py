#!/usr/bin/python3

"""
class Square inheriting from Rectangle
"""


from models.Rectangle import Rectangle


class Square(Rectangle):
    """describes a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(id, x, y, size, size)
