#!/usr/bin/python3
class Square:
    """Square class that defines a square"""

    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if not self._Square__size:
            print("")
        for i in range(self._Square__size):
            print("#" * self._Square__size)
