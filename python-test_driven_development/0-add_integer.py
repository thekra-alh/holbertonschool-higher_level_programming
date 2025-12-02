#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after checking their type and converting floats to integers.

    Args:
        a (int or float): First number
        b (int or float, optional): Second number, defaults to 98

    Raises:
        TypeError: If a or b is not an int or float

    Returns:
        int: Sum of a and b as an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
