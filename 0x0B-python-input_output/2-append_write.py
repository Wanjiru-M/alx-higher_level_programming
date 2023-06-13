#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file and returns the number of characters appended."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
