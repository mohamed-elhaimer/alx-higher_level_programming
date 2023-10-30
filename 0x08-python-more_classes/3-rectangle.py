#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """retuen the area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimetre of Rectangle"""
        if self.__width and self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """print the retangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ('')

        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += '#'
            if i < self.__height - 1:
                ret += '\n'
        return (ret)
