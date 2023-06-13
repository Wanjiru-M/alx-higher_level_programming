#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, 'w') as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)
