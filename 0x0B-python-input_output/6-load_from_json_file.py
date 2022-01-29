#!/usr/bin/python3
""" 6-load_from_json_file.py - module """


import json
""" json module """


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    """
    with open(filename) as f:
        return json.load(f)
