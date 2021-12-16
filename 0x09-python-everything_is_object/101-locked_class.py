#!/usr/bin/python3
""" 101-locked_class.py - locked class module """


class LockedClass:
    """
    instannce attribute called first name
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        self.first_name = first_name
