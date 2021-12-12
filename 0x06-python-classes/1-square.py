#!/usr/bin/python3
"1-square.py - defines a square with a private attribute"


class Square:
    """
    Class that defines a square with size
    Args:
        Size : Private, Size of the square
    """
    def __init__(self, size):
        self.__size = size
