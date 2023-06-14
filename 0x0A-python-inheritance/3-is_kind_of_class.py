#!/usr/bin/python3
"""Defines a class and inherited function."""


def is_kind_of_class(obj, a_class):
    """Traversing the object's class hierarchy"""
    current_class = type(obj)
    while current_class != object:
        if current_class == a_class:
            return True
        current_class = current_class.__base__
    return False
