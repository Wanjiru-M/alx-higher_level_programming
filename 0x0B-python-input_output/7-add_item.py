#!/usr/bin/python3
"""Script to add command-line arguments to a Python list and save them to a file."""

import sys
import json
import os.path

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

file_name = 'add_item.json'

my_list = []

if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
my_list = load_from_json_file(file_name)

if len(sys.argv) > 1:
for elem in sys.argv[1:]:
my_list.append(elem)

save_to_json_file(my_list, file_name)
