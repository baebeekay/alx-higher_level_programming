#!/usr/bin/python3
""" 10-student.py - module """


class Student:
    """
    Public instance attributes:
     first_name
     last_name
     age
    """
    def __init__(self, first_name, last_name, age):
        """
        defines the attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
         retrieves a dictionary representation of a Student instance.

         If attrs is a list of strings,
         only attribute names contained in this list must be retrieved.
         Otherwise, all attributes must be retrieved
        """
        new = {}
        if type(attrs) is list:
            for key, value in self.__dict__.items():
                if key in attrs:
                    new[key] = value
            return new
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        hat replaces all attributes of the Student instance
        """
        if not json:
            return
        self.__dict__ = json
