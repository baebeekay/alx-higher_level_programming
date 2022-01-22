#!/usr/bin/python3
""" 0-lookup.py  - module """
def lookup(obj):
    """
    returns the list of available attributes and methods of an obj
    """
    return dir(obj)
