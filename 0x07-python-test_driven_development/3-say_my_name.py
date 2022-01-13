#!/usr/bin/python3
"""  3-say_my_name - prints a statement """


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is <first name> <last name>
    first name and last name must be a string, otherwise
    RAISE a TypeError exception
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
