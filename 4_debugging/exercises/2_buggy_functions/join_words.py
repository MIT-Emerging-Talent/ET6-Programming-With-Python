#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for string joining operations.
This is part of the debugging exercise series focusing on buggy implementations.

Module contents:
    - join_words: Combines a list of words with a separator

Created on 2024-12-06
Author: Claude AI
"""


def join_words(words: list, separator: str) -> str:
    """Joins a list of words using the given separator.

    Takes a list of words and combines them into a single string, placing
    the separator between each word. Does not add separator at start or end.

    Parameters:
        words: list of strings to join
        separator: str, the separator to place between words

    Returns -> str: the joined string

    Raises:
        AssertionError: if words is not a list or separator is not a string

    Examples:
        >>> join_words(['hello', 'world'], ' ')
        'hello world'
        >>> join_words(['a', 'b', 'c'], ',')
        'a,b,c'
        >>> join_words([], '-')
        ''
    """
    assert isinstance(words, list), "first argument must be a list"
    assert isinstance(separator, str), "separator must be a string"
    for word in words:
        assert isinstance(word, str), "all elements in list must be strings"
    return separator.join(words)
