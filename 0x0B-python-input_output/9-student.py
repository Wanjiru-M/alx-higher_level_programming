#!/usr/bin/python3
""" creating a student class """

#!/usr/bin/python3

class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the student instance"""
        json_dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith("__") and not callable(value):
                json_dict[key] = value
        return json_dict
