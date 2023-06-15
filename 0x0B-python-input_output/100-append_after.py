#!/usr/bin/python3
"""A function that adds a new line of text to an existing file"""
import subprocess


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text"""
    temp_filename = filename + ".tmp"

    with open(filename, 'r') as file, open(temp_filename, 'w') as temp_file:
        for line in file:
            temp_file.write(line)
            if search_string in line:
                temp_file.write(new_string)

    with open(temp_filename, 'r') as temp_file, open(filename, 'w') as file:
        for line in temp_file:
            file.write(line)
            subprocess.run(["rm", temp_filename])

