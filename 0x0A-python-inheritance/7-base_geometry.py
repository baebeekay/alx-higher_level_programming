#!/usr/bin/python3
""" 7-base_geometry.py  - module """


class BaseGeometry:
    """
    geometry class
    """
    def area(self):
        """
        Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that Validates that value is an integer
        greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
