#!/usr/bin/python3

"""
class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """heighter getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout the Rectangle instance with the char #"""
        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method so that it returns
            [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        _str = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height)
        return _str

    def update(self, *args, **kwargs):
        """assigns an argument (1,2,3,4,5) to each attribute respectively
        > attribs: id, width, height, x, y"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
             for key, value in kwargs.items():
                 if key == "id":
                     self.id = value
                 if key == "width":
                     self.width = value
                 if key == "height":
                     self.height = value
                 if key == "x":
                     self.x = value
                 if key == "y":
                     self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rect_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                    'height': self.__height, 'width': self.__width}
        return rect_dict
