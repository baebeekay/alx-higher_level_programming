#!/usr/bin/python3
""" 2-rectangle.py - defines a rectangle   """


class Rectangle:
    """
    Class that defines the a rectangle
    by width and height
    return area and perimeter
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        perimeter = 0
        if self.__width == 0 or self.__height == 0:
            return perimeter
        else:
            perimeter = (self.__width + self.__height) * 2
            return perimeter
