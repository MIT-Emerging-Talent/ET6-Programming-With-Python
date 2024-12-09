#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_5(a, b=None):
    """
    Generates a list of integers starting from 0 up to `a-1`.

    Parameters:
        a (int): The number to determine the length of the list.

    Returns-> list: A list of integers from 0 to `a-1`.

    Examples:
        >>> mystery_5(5)
        [0, 1, 2, 3, 4]
        >>> mystery_5(3)
        [0, 1, 2]
        >>> mystery_5(0)
        []
    """
    if b is None:
        b = []
    for i in range(a):
        b.append(i)
    return b
