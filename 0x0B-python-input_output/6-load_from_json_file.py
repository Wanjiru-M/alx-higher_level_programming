#!/usr/bin/python3
"""Function that constructs a Python object from a JSON file."""
import json

def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename) as file:
        json_str = file.read()
    data = eval(json_str)
    return data
