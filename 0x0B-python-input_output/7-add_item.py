#!/usr/bin/python3
"""Incorporate all the command-line arguments into a Python list and persist the list by saving it to a file."""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    # Load existing data from the file
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

# Add arguments to the data list using a for loop
for arg in args:
    data.append(arg)

# Save the updated data to the file
save_to_json_file(data, filename)
