#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt:
     """Invert int operators == and !=."""
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """Override == opeartor with != behavior."""
        return self.value != other

    def __ne__(self, other):
         """Override != operator with == behavior."""
        return self.value == other
