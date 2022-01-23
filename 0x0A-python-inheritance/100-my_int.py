#!/usr/bin/python3
"""  100-my_int.py - module """


class MyInt(int):
    """
    a class MyList that inherits from int
    """

    def __eq__(self, int):
        """
        true returns false
        """
        return False

    def __ne__(self, int):
        """
        false returns true
        """
        return True
