#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its contents to stdout"""
    try:
        with open(filename, encoding="utf-8") as file:
            contents = file.read()
            print(contents, end="")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{filename}'.")
