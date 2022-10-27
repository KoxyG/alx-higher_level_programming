#!/usr/bin/python3
"""This is a module that writes a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, "w", encodinb="utf-8") as f:
        return f.write(text)
