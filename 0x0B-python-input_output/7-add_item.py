#!/usr/bin/python3
"""Incorporate all the command-line arguments into a Python list and persist the list by saving it to a file."""
import sys


from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []
for arg in args:
    data.append(arg)
save_to_json_file(data, filename)
