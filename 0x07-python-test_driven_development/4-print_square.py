#!/usr/bin/python3
""" 4-print_square - print square module """


def print_square(size):
    """
    a function that prints a square with the character #.
    Parameter: size is the size length of the square
    Raises:
    TypeError: if size is a float and is less than 0
    size is not an integer
    ValueError: size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return None
    else:
        for i in range(size):
            print("#" * size, end="")
            print()
