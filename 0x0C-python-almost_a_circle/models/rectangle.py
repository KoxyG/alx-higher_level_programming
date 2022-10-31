#!/usr/bin/python3
"""
This module contains a rectangle class
"""


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes attributes of the object"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    #list for getter function
    @property
    def width(self):
        """Get the value for width"""
        return self.__width

    @property
    def height(self):
        """Get the value for height"""
        return self.__height

    @property
    def x(self):
        """Get the value for X"""
        return self__x

    @property
    def y(self):
        """Get the value for y"""
        return self__y

    #list for setter function
    @width.setter
    def width(self, value):
        """set the value for width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """set the value for height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """set the value for x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """set the value for y"""
        self.__y = value

