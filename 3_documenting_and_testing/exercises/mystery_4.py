#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_4(a):
    """
    Generates a list of integers starting from 0 up to `a-1`.

    Parameters:
        a (int): The number to determine the length of the list.

    Returns-> list: A list of integers from 0 to `a-1`.

    Examples:
        >>> mystery_4(5)
        [0, 1, 2, 3, 4]
        >>> mystery_4(3)
        [0, 1, 2]
        >>> mystery_4(0)
        []
    """
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
