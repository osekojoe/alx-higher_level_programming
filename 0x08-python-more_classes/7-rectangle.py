#!/usr/bin/python3
"""class Rectangle that defines a rectangle
"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instance initialization
        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method for getting width
        Returns:
            rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Method for defining width
        Args:
            value: rectangle width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width  is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method for getting height
        Returns:
            rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Method for defining heigth
        Args:
            value: rectangle height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method for rectangle area
        Returns:
            Area
        """
        return self.width * self.height

    def perimeter(self):
        """Method for rectangle perimeter
        Returns:
            Perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """method prints the rectangle with # character
        Returns:
            string
        """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method returns string representation of instance
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method prints message on instance deletion
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
