#!/usr/bin/python3
""" 1-my_list.py """


class MyList(list):
    """ A class of that inherits from list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
