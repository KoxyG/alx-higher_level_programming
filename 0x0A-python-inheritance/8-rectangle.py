#!/usr/bin/python3
"""inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
