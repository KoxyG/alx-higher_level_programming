#!/usr/bin/python3
"""This module checks if an object is an instance of class or inherited
"""


def inherits_from(obj, a_class):
    """returns true if its an instance of class or false if otherwise
    """
    return (issubclass(type(obj, a_class) and type(obj) != a_class)
