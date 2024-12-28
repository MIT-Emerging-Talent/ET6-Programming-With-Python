#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Is in Both

Write a function that takes in a string and two lists of strings. 
It will return true if the item is in _both_ of the lists.

> I solved it on 28/ 12/ 2024

"""


def is_in_both(thestring: str, list1: list, list2: list) -> bool:
    """Fuction that return True if the string is in both list1 and list2

    Args:
        thestring (str): The string to search for
        list1 (list): First list to search in
        list2 (list): Second list to search in

    Returns:
        bool: return True or False

    >>> is_in_both("Noor", ["Heba", "Eman", "Noor"], ["Sondos", "Noor"])
    True
    >>> is_in_both("333", ["123", "333", "774"], ["23", "65", "333", "532"])
    True
    >>> is_in_both("Mayar", ["Heba", "Eman", "Noor"], ["Sondos", "Noor"])
    False
    >>> is_in_both("Eman", ["Heba", "Eman", "Noor"], ["Sondos", "Noor"])
    False
    """

    assert isinstance(thestring, str), "it should be a string"
    assert isinstance(list1, list), "should be a list"
    assert isinstance(list2, list), "should be a list"
    assert len(thestring) > 0, "the string should have an item"
    assert len(list1) > 0, "the list should have items"
    assert len(list2) > 0, "the list should have items"

    if thestring in list1 and thestring in list2:
        return True
    else:
        return False
