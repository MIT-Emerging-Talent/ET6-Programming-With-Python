#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 18/12/2024

@author: Evan Cole
@editor: Heba Shaheen
"""

# --- before documenting and testing ---
# def mystery_9(a):
#    b = len(a)
#    for c in range(b):
#        for d in range(0, b - c - 1):
#            if a[d] > a[d + 1]:
#                a[d], a[d + 1] = a[d + 1], a[d]
#    return a

# --- After documenting and testing ---


def arrange_list(alist: list) -> list:
    """Arrange a list from low to high by switching its items

    Args:
        alist (list): a list to get arranged

    Returns:
        list: return a list arranged from low to high
    """
    length = len(alist)
    for c in range(length):
        for d in range(0, length - c - 1):
            if alist[d] > alist[d + 1]:
                alist[d], alist[d + 1] = alist[d + 1], alist[d]
    return alist


print(arrange_list([9, 1, 6, 2]))
print(arrange_list(["e", "g"]))
print(arrange_list([]))
