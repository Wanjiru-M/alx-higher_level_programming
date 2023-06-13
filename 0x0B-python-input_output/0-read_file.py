#!/usr/bin/python3

"""Retrieve content from a file"""

def read_file(filename=""):
"""Outputs the text content of a file to the standard output"""
with open(filename) as file:
text = file.read()
print(text, end="")
