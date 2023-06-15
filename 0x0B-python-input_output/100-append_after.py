#!/usr/bin/python3
"""A function that adds a new line of text to an existing file"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text"""
    temp_filename = filename + ".tmp"

    with open(filename, 'r') as file, open(temp_filename, 'w') as temp_file:
        for line in file:
            temp_file.write(line)
            if search_string in line:
                temp_file.write(new_string)

    os.replace(temp_filename, filename)
