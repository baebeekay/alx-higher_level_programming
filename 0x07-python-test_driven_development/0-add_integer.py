#!/usr/bin/python3
""" 0-add_integer.py - adds two integers """


def add_integer(a, b=98):
    """
    function that adds two integers
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
