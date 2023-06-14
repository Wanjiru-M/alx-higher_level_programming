#!/usr/bin/python3
""" A class that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
