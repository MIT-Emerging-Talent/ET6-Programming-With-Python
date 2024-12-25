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


def sort_list(alist: list, result=None) -> list:
    # result have a default value 'None' we can put a value to it or not (just None or list)

    """it sort a list of either strings or numbers from low to high.then adds
        those values to the end of another list>
        string: sorted by UNICODE value
        numbers: sorted low to high
    Args:
        alist (list): the origin list
        result (None, optional): The list that will return. Defaults to None.

    Returns (list) -> sort alist and append it to result list if it empty or not

    >>>
    """
    # We should write assertions to check the input types
    # Make sure there is a list to fill
    if result is None:
        result = []
    # moves items from one list to another in sorted order
    while alist:
        # find the lowest item in the first
        c = min(alist)
        # move it to the second list
        alist.remove(c)
        result.append(c)
    return result


print(sort_list([7, 9, 1, 6]))

print(sort_list(["n", "a", "m", "e"]))
print(sort_list(["one", "apple", "", "123", "heba"]))
