#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:
    """
    This class defines a Rectangle with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes instance of Rectangle. Width and height are
        optional and default to 0.
        """
        self.width = width
        self.height = height

    def width(self):
        """
        Returns the width of the Rectangle.
        """
        return self.__width

    def width(self, value):
        """
        Sets the width of the Rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """
        Returns the height of the Rectangle.
        """
        return self.__height

    def height(self, value):
        """
        Sets the height of the Rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
