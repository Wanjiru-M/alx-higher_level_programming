#!/usr/bin/python3
def read_file(fname=""):
    with open(fname, encoding="utf-8") as f:
        print(f.read(), end="")
