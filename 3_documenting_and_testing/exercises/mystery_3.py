#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_3(a, b):
    """
    Compares two values, `a` and `b`, and returns:
        - The smaller value if `a` is less than `b`.
        - The larger value if `a` is greater than `b`.
        - The sum of `a` and `b` if they are equal.

    Parameters:
        a (int or float): The first value to compare.
        b (int or float): The second value to compare.

    Returns:
        int or float:
            - The smaller value if `a` < `b`.
            - The larger value if `a` > `b`.
            - The sum of `a` and `b` if `a` == `b`.

    Examples:
        >>> mystery_3(2, 3)
        2
        >>> mystery_3(10, 5)
        5
        >>> mystery_3(4, 4)
        8
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
