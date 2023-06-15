#!/usr/bin/python3
    """Defines a function that adds attributes to objects."""

def add_attribute(obj, attribute, value):
    """adds a new attribute to an object if it's possible"""
    if isinstance(obj, dict):
    obj[attribute] = value
    else:
    setattr(obj, attribute, value)
