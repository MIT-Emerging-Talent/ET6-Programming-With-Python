#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for a item that exist in 2 lists.

Parameters:
    item(str): String that will be checked in list1 and list2.
    list(str, list): contains a list of string
    list2(str, list): contains a list of string

Returns->
    item(str) -> bool: An Item that exist in list1 and list2

Created on 2024-12-13
Author: Aziz
"""


def is_in_both(item: str, list1: list, list2: list) -> bool:
    """is in Both

    A function that takes in two lists of strings and a string.
    It will return true if the item is in _both_ of the lists.

    doctest:
    >>> is_in_both("date", ["Aziz", "date"], ["cool", "date"])
    True
    >>> is_in_both("MIT", ["MIT", "best", "University"], ["study", "MIT", "student"])
    True
    >>> is_in_both("Aziz", ["Aziz", "date"], ["human", "time"])
    False
    >>> is_in_both(4, ["Blue", "Red"], ["Black", "Gray"])
    False
    >>> is_in_both("precious", [], ["cool", "time"])
    False
    >>> is_in_both("pizza", [], [])
    False
    """
    if not isinstance(item, str):
        return False

    return item in list1 and item in list2
