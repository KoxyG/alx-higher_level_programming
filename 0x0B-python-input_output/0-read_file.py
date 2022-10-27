#!/usr/bin/python3
def read_file(filename=""):
    """This module defines a text file-reading function"""


    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
