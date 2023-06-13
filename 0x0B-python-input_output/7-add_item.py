#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""

import sys
from os import path
from json import dump, load
from typing import List


def save_to_json_file(my_obj: List, filename: str):
    """Save object to JSON file"""
    with open(filename, 'w') as file:
        dump(my_obj, file)


def load_from_json_file(filename: str):
    """Load object from JSON file"""
    with open(filename, 'r') as file:
        return load(file)


def add_items_to_list(items: List):
    """Add items to list and save to file"""
    filename = "add_item.json"

    if path.exists(filename):
        my_list = load_from_json_file(filename)
        my_list.extend(items)
    else:
        my_list = items

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_items_to_list(args)
