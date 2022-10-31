#!/usr/bin/python3
"""
This module contains a class to serves as base for other classes
"""


class Base:
    """Represents base of all classes created"""

    __nb_objects = 0


    def __init__(self, id=None):
        """ """
        if id == None:
            self.id = None
        else:
            Base.__nb_objects += 1
            Base.__nb_objects = self.id
