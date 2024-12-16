#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Repeat Character

Write a function that takes in a string, a single character, and a number.
The function returns a string with each occurrence of the character repeated n times.

"""


def repeat_character(text: str, repeat_char: str, n: int) -> str:
    """
    Repeat each occurrence of the character in the string n times.

    Parameters:
    s (str): The input string.
    char (str): The character to repeat.
    n (int): The number of times to repeat the character.

    Returns:
    str: The modified string with each occurrence of the character repeated n times.

    Examples:
    >>> repeat_character("Aziz", "z", 3)
    'Azzzizzz'
    >>> repeat_character("Gray", "r", 5)
    'Grrrrray'
    >>> repeat_character("Time", "e", 7)
    'Timeeeeeee'
    >>> repeat_character("Hand", "D", 3)
    'Handdd'
    >>> repeat_character("Goat", "d", 20)
    'Goat'
    >>> repeat_character(123, "a", 3)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
    >>> repeat_character("Earth", "t", "g")
    Traceback (most recent call last):
    ...
    TypeError: n must be an integer
    >>> repeat_character("text", 4, 6)
    Traceback (most recent call last):
    ...
    TypeError: repeat_char must be a string
    """

    # Type test
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if not isinstance(repeat_char, str):
        raise TypeError("repeat_char must be a string")
    # Convert the input string to lowercase
    text = text.lower()
    repeat_char = repeat_char.lower()

    # Initialize an empty result string
    result = ""

    # Iterate through each character in the input string
    for char in text:
        # If the current character matches the character to repeat
        if char == repeat_char:
            # Add the character repeated n times to the result
            result += char * n
        else:
            # Otherwise, just add the current character to the result
            result += char

    # Return the final result string and capitalize the first letter of the result string
    return result[0].upper() + result[1:]
