#!/usr/bin/python3
"""
This module defines the Rectangle class, representing a rectangle
with width and height properties, and methods for calculating
area and perimeter.
"""


class Rectangle:
    """Represents a rectangle with width and height properties."""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width property. Ensures width is an integer >= 0.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height property. Ensures height is an integer >= 0.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if either
                 width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
