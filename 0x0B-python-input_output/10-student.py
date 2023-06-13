#!/usr/bin/python3
""" Creating Student class """

class Student:
    """ Definition of the Student class """
    def init(self, first_name, last_name, age):
    """ Initializes the Student instance """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

def to_json(self, attributes=None):
    """ Retrieves a dictionary representation of the Student instance """
    if isinstance(attributes, list) and all(isinstance(attr, str) for attr in attributes):
        return {attr: getattr(self, attr) for attr in attributes if hasattr(self, attr)}
    else:
        return self.__dict__

