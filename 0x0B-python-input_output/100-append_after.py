#!/usr/bin/python3
"""A function that adds a new line of text to an existing file"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text"""
     lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
