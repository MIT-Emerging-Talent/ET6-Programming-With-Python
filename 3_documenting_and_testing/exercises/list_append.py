#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 18/12/2024

@author: Evan Cole
@editor: Heba Shaheen
"""
# --- before documenting and testing ---
# def mystery_4(a):
#    b = []

#    c = 0
#    while len(b) < a:
#        b.append(c)
#        c = c + 1

#    return b

# --- after documenting and testing ---


def list_append(input_list: list):
    """return list as the same input list length from 0 to len(a)-1

    Parameters:
        input_list (list): a list to count its length

    Returns ->  list start from 0 to length input_list -1
    """
    new_list = []

    c = 0
    while len(new_list) < len(input_list):  # len(a) not a
        new_list.append(c)
        c = c + 1

    return new_list
