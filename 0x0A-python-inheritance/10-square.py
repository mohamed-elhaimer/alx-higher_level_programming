#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square"""
    def __init__(self, size):
        """initialize a square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """return the area of square"""
        return (self.__size * self.__size)
