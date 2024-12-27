#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the words in a string.
This is part of the debugging exercise series focusing on buggy implementations.

Module contents:
    - count_words: Counts the number of words in a string

Created on 2024-12-06
Author: Claude AI
"""


def count_words(text: str) -> int:
    """Counts the number of words in a string.
    Words are separated by spaces.

    Parameters:
        text: str, the input string

    Returns -> int: number of words in the text

    >>> count_words("hello world")
    2
    >>> count_words("one")
    1
    >>> count_words("")
    0
    """
    assert isinstance(text, str), "input must be a string"

    # return len(text.split(" ")) -> this should be .split() not .split(" ")
    thestring = text.split()
    return len(thestring)
