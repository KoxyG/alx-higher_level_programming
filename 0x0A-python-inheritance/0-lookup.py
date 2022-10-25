#!/usr/bin/python3
""" 
    This module returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """This function that looks for all the attributes and methods of an object"""
    return dir(obj)
