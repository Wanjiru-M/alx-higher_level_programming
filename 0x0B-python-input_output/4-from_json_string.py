#!/usr/bin/python3
"""An object represented by a JSON string"""

import json


def from_json_string(my_str):
    """Converts a JSON string into a Python data structure"""
    return json.loads(my_str)
