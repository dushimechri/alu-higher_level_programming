#!/usr/bin/python3
"""
This module defines the Rectangle class with width and height properties,
area and perimeter methods, __str__ and __repr__ for string representations,
and a class attribute to count instances.
"""


class Rectangle:
    """Represents a rectangle with width, height, and instance counter."""

    number_of_instances = 0  # Class attribute to track number of instances

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance counter

    @property
    def width(self):
        """Getter for the width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width property."""
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
        """Setter for the height property."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string depicting the rectangle with '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Returns a string  that can recreate the rectangle instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message and decrements the instance counter on deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instance counter
