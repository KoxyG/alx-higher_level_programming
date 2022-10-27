#!/usr/bin/python3
"""This is module defines a file-writing function"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file
    """
    with open(filename, "w", encodinb="utf-8") as f:
        return f.write(text)
