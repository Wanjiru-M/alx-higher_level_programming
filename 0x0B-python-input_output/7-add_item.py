#!/usr/bin/python3
"""Incorporate all the command-line arguments into a Python list and persist the list by saving it to a file."""
import sys


if name == "main":
save_to_json_file = import('5-save_to_json_file').save_to_json_file
load_from_json_file = import('6-load_from_json_file').load_from_json_file

try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

new_items = sys.argv[1:]

items = existing_items + new_items

save_to_json_file(items, "add_item.json")
