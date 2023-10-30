#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """represent a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() > rect_2.area()):
            return (rect_1)
        elif (rect_1.area() < rect_2.area()):
            return (rect_2)
        elif (rect_1.area() == rect_2.area()):
            return (rect_1)

    def __str__(self):
        """print the retangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ('')

        ret = []
        for i in range(self.__height):
            [ret.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                ret.append('\n')
        return ("".join(ret))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return (ret)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
