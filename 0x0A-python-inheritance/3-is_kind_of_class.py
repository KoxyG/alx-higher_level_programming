#!/usr/bin/python3
"""checks if object is an instance of a class
of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """returns True if object ia an instance of a class
    or False if it is a class that it inherits from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
