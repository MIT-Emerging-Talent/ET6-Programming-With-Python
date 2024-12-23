#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 18/12/2024

@author: Evan Cole
@editor: Heba Shaheen
"""
# --- before documenting and testing ---

# def mystery_8(a, b):
#    c = []
#    while a:
#        if b in a[0]:
#            c.append(a[0])
#        a = a[1:]
#    return c

# --- After documenting and testing ---


# I changed the code a little bit as it was not working and giving error
def list_intersection(first_list: list, second_list: list) -> list:
    """A function takes two lists and gives the intersection between them
    Parameters:
    first_list (list): the first list
    Second_list (list): the second list
    Returns:
        (list): a list have the items that in the two lists
    """
    final_list = []
    for item in first_list:
        if item in second_list:  # it was b in a[0] that gives error
            final_list.append(first_list[0])
        first_list = first_list[1:]
    return final_list


# print(list_intersection([4, 2, 3], [0, 4, 55, 9]))
