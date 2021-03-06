#!/usr/bin/python3
""" 9-student.py - module """


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

    def to_json(self):
        """
         retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
