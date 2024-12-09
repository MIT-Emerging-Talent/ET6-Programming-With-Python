#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_8(a, b):
    """
    Filters a sequence of elements by checking if each element contains the value `b`.

    This function iterates through the given sequence `a`, checking if `b` is present
    in each element. It appends the element to a new list `c` if `b` is found in it.

    Parameters:
        a (iterable): A sequence (such as a list) of elements to be checked.
        b (any): The value to check for within each element of `a`.

    Returns:
        list: A new list containing elements from `a` that contain `b`.

    Examples:
        >>> mystery_8(["apple", "banana", "cherry"], "a")
        ['apple', 'banana']
        >>> mystery_8(["apple", "banana", "cherry"], "z")
        []
        >>> mystery_8([1, 2, 3, 4, 5], 3)
        [3]
        >>> mystery_8([], 0)
        []
    """
    c = []
    for item in a:
        if b in str(
            item
        ):  # Ensuring b and item are treated as strings for compatibility
            c.append(item)
    return c
