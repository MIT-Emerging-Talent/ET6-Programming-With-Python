#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23/12/2024

@author: Evan Cole
@editor: Heba Shaheen
"""
# --- before documenting and testing ---

# def mystery_7(a, b):
#    c = []
#    for d in a:
#        if b in d:
#            c.append(d)
#    return c

# --- After documenting and testing ---


# This makes errors
def lists_same_items(first_list: list, second_list: list) -> list:
    """Give the items that include in the two lists

    Args:
        first_list (list): The first list
        second_list (list): The Second list

    Returns:
        list: return a list have the items that included it the first and second lists
    """
    result = []
    for item in first_list:
        if item in second_list:  # (d in b) not (b in d)
            result.append(item)
    return result


print(lists_same_items([1, 3, 4, 5], [3, 4, 5, 9, 11]))
print(lists_same_items(["He", "ew", "aa", "a"], ["aa", "qqwdd", "He"]))
