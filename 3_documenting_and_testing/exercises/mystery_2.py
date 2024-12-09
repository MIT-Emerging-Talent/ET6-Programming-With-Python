#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9/12/2024

@author: Evan Cole
"""


def mystery_2(a):
    """
    Returns the length of the input sequence if it is not empty.
    If it`s empty returns None, returns None.

    Parameters:
        a (sequence): The input sequence (could be a string, int, list)

    Returns-> int or None:
                - The length of the sequence if it is not empty.
                - None if the sequence is empty.

    Examples:
    >>> mystery_2([1, 2, 3, 4, 5])
    5
    >>> mystery_2("name")
    4
    >>> mystery_2("")
    None
    >>> mystery_2([])
    None
    """
    if len(a) == 0:
        return None

    return len(a)
