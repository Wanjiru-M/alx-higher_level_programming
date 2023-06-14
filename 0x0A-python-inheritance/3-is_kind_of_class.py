#!/usr/bin/python3
"""Defines a class and inherited function."""


def is_kind_of_class(obj, a_class):
    """Traversing the object's class hierarchy"""
     return issubclass(type(obj), a_class)
