#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        a = int(a)
        b = int(b)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer or b must be an integer")

    return a + b
