#!/usr/bin/python3

"""define a class Rectangle"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return (self._width)

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return (self._height)

    @width.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
