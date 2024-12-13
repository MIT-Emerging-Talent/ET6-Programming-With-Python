#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the longest item in a list.
This is part of the debugging exercise series focusing on buggy implementations.

Module contents:
    - find_longest: Finds the longest string in a list

Created on 2024-12-06
Author: Claude AI
"""


def find_longest(items: list) -> str:
    """Returns the longest string from a list of strings.

    If multiple strings tie for longest length, returns the first one found.
    Empty strings are valid candidates for longest string.

    Parameters:
        items: list of strings to search

    Returns -> str: the longest string found

    Raises:
        AssertionError: if input is not a list or contains non-strings
        ValueError: if list is empty

    Examples:
        >>> find_longest(['a', 'bb', 'ccc'])
        'ccc'
        >>> find_longest(['hello', 'hi', 'hey'])
        'hello'
        >>> find_longest(['', 'a'])
        'a'
    """
    assert isinstance(items, list), "input must be a list"
    if not items:
        raise ValueError("list cannot be empty")

    longest = items[0]
    for item in items:
        if len(item) > len(longest):
            longest = item
    return longest
