#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_6(a, b):
    """
    Generates a list of length `a`, where the list starts with `b`
    and increments the value of `b` by 1 for each subsequent element.

    Parameters:
        a (int): The number of elements in the output list.
        b (int): The starting value of the list.

    Returns:
        list: A list containing `a` elements, starting from `b` and
              incrementing by 1 for each element.

    Examples:
        >>> mystery_6(5, 1)
        [1, 2, 3, 4, 5]
        >>> mystery_6(3, 10)
        [10, 11, 12]
        >>> mystery_6(0, 7)
        []
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
