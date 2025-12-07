#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a new square with a private size attribute.

        Args:
            size: The size of the square (no validation required yet).
        """
        self.__size = size
