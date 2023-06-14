#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_attribute(obj, attribute, value):
"""adds a new attribute to an object if it's possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

