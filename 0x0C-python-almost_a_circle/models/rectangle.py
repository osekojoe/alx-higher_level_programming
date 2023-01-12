#!/usr/bin/python3

"""
class Rectangle that inherits from Base
"""


class Rectangle:
    """
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
    """ class constructor"""
    super().__init__(id)
    self.width = width
    self.height = height
    self.x = x
    self.y = y

    @property
    def width(self):
    """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
    """width setter"""
        self.__width == value

    @property
    def height(self):
    """heighter getter"""
        return self.__height

    @height.setter
    def height(self, value):
    """height setter"""
        self.__height = value

    @property
    def x(self):
    """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
    """x setter"""
        self.__x = value

    @property
    def y(self):
    """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
    """y setter"""
        self.__y = value
