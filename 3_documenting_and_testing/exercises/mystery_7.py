#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_7(a, b):
    """
    Filters a sequence of elements by checking if each element contains the value `b`.

    This function iterates through the given sequence `a` and appends to a new list
    all elements that contain the value `b`.

    Parameters:
        a (iterable): A sequence (such as a list) of elements to be checked.
        b (any): The value to check for within each element of `a`.

    Returns:
        list: A new list containing elements from `a` that contain `b`.

    Examples:
        >>> mystery_7(["apple", "banana", "cherry"], "a")
        ['apple', 'banana']
        >>> mystery_7(["apple", "banana", "cherry"], "z")
        []
        >>> mystery_7([1, 2, 3, 4, 5], 3)
        [3]
        >>> mystery_7([], 0)
        []
    """
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
