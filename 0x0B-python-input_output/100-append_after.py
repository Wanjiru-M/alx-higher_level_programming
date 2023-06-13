#!/usr/bin/python3
"""A function that adds a new line of text to an existing file"""

import linecache
import tempfile
import shutil

def append_after(filename="", search_string="", new_string=""):
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    with open(filename, 'r') as file, temp_file:
        line_number = 0
        line = linecache.getline(filename, line_number)
        while line:
            temp_file.write(line)
            if search_string in line:
                temp_file.write(new_string)
            line_number += 1
            line = linecache.getline(filename, line_number)

    shutil.move(temp_file.name, filename)
