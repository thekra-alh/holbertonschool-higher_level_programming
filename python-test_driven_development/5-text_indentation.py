#!/usr/bin/python3
'''prints a text with 2 new lines after each
of these characters: ., ? and :'''


def text_indentation(text):
    '''prints a text with 2 new lines after each
    of these characters: ., ? and :'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    new_line = False  # flag to add leading space

    for char in text:
        if new_line and char != " ":
            print(" ", end="")  # add leading space exactly once
            new_line = False

        print(char, end="")

        if char in ".?:":
            print("\n\n", end="")
            new_line = True
