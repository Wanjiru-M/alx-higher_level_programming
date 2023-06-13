#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""

#!/usr/bin/python3

def class_to_json(obj):
    """Converts an object to a JSON serializable dictionary"""
    json_dict = {}
    for key, value in obj.__dict__.items():
        if not key.startswith("__") and not callable(value):
            json_dict[key] = value
    return json_dict
