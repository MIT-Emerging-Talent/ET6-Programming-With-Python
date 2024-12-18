#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 18/12/2024

@author: Evan Cole
@editor: Heba Shaheen
"""
# --- before documenting and testing ---
# def mystery_5(a, b=None):
#    if b is None:
#        b = []
#    while a:
#        c = min(a)
#        a.remove(c)
#        b.append(c)
#    return b

# --- after documenting and testing ---


def sort_list(alist: list, result=None):
    """Sort alist increasly
    Args:
        alist (list): the origin list
        result (None, optional): The list that will return. Defaults to None.

    Returns (list) -> A sorted list from lowest to highest
    """
    if result is None:
        result = []
    while alist:
        c = min(alist)
        alist.remove(c)
        result.append(c)
    return result
