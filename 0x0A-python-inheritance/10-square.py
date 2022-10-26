#!/usr/bin/python3
"""inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """a square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
