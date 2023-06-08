#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.set_width(width)
        self.set_height(height)

    @classmethod
    def validate_value(cls, value, name):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    def get_width(self):
        return self.__width

    def set_width(self, value):
        self.validate_value(value, "width")
        self.__width = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        self.validate_value(value, "height")
        self.__height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)
