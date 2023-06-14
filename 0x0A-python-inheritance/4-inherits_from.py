#!/usr/bin/python3
""" Return Only sub class of a class """


def inherits_from(obj, a_class):
    """Traversing the object's class hierarchy"""
    current_class = type(obj)
    while current_class != object:
        if current_class == a_class:
            return True
        current_class = current_class.__base__
    return False
