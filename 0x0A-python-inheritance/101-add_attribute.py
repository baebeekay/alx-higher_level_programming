#!/usr/bin/python3
""" 101-add_attribute.py """


def add_attribute(object, name, value):
    """
    a function that adds a new
    attribute to an object if it’s possible
    """
    if not hasattr(object, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(object, name, value)
