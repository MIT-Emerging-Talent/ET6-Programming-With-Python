#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 19/12/2024

@author: Evan Cole
@editor: Heba Shaheen
"""
# --- before documenting and testing ---


# def mystery_6(a, b):
#    if a == 0:
#        return []
#    c = []
#    while len(c) < a:
#        c.append(b)
#        b = b + 1
#    return c
# --- after documenting and testing ---
def make_list(length: int, start):
    """Make a list with specific length and it start from a number and add +1 everytime

    Args:
        length (int): The list length that we want
        start (Any number): a specific value to start the list with

    Returns(list) -> A list with spesific length and start value
    """
    if length == 0:
        return []

    c = []
    while len(c) < length:
        c.append(start)
        start = start + 1

    return c
