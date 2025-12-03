#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    start_new_line = False  # controls leading space

    for char in text:
        if char in ".?:":
            result += char + "\n\n"
            start_new_line = True  # next line must start with a space
        else:
            if start_new_line and char != " ":
                result += " "  # add EXACTLY one leading space
                start_new_line = False
            result += char

    print(result, end="")
