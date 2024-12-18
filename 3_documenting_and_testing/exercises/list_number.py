#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""

# --- before documenting and testing ---

# def mystery_2(a):
#    if len(a) == 0:
#       return None

#    return len(a)

# --- after documenting and testing ---


def list_number(thelist: list) -> int:
    """A function returns the length of the list or None if it is empty

    Parameters:
        thelist: list, The list to show it's length

    Returns -> int: None if empty otherwise the length

    >>> list_number([])
    None

    >>> list_number([1,2])
    2

    >>> list_number([2,3,4,5])
    4

    """
    if len(thelist) == 0:
        return None

    return len(thelist)
