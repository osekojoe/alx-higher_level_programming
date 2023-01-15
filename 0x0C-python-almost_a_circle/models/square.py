#!/usr/bin/python3

"""
class Square inheriting from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """describes a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """square initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Validating attributes"""
        if args is not None and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if args is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """overloading __str__ method should return
           [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
            self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
