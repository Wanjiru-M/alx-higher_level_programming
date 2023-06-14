#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""

class MetaBaseGeometry(type):
    """Using a metaclass to define an empty class"""
    pass

class BaseGeometry(metaclass=MetaBaseGeometry):
    pass
