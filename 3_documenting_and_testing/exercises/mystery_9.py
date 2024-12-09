#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_9(a):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Parameters:
        a (list): The list to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Example:
        >>> mystery_9([4, 3, 1, 5, 2])
        [1, 2, 3, 4, 5]
        >>> mystery_9([10, 7, 8, 9, 1, 5])
        [1, 5, 7, 8, 9, 10]
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
