#!/usr/bin/python3
"5-square.py - prints a square"


class Square:
    """
    Class that defines the area a square
    If the size is not an integer raises a Type Error
    If the size is less than zero raises a Value error
    Args:
        Size (int): Private, Size of the square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                print("#" * self.size)
