#!/usr/bin/python3

"""Retrieve from a file"""


def read_file(filename=""):
    """Reads text from a file and prints to stdoutput"""
    with open(filename) as file:
        text = file.read()
    print(text,end="")
