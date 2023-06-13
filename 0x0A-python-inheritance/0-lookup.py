#!/usr/bin/python3
""" Creating a function"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    attributes = []
    for attr in dir(obj):
        if not attr.startswith("__"):
            attributes.append(attr)
    return attributes
