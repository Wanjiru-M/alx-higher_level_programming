#!/usr/bin/python3
""" Return Only sub class of a class """


def inherits_from(obj, a_class):
    """Traversing the object's class hierarchy"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
