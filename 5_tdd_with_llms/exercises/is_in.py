#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for a item that exist in one lists.

Parameters:
    list(str, list): contains a list of string
    list2(str, list): contains a list of string

Returns->
    item(str) -> bool: An Item that exist in list1 or list2

Created on 2024-12-13
Author: Aziz
"""


def is_in(item: str, list1: str, list2: str):
    """is_in
    A function that takes in a string and two lists of strings.
    It will return true if the item is in _at least one_ of the lists.

    Parameters:
    item (str): The string to check.
    list1 (list of str): The first list of strings.
    list2 (list of str): The second list of strings.

    Returns:
    bool: it is True if the item is in at least one of the lists, otherwise False.

    doctest:

    >>> is_in("cool", ["zizi", "date"], ["cool", "short"])
    True
    >>> is_in("study", ["MIT", "high", "University"], ["study", "jelly", "student"])
    True
    >>> is_in("Gray", [], ["food", "Gray"])
    True
    >>> is_in("", [], [])
    False
    >>> is_in("", [""], [])
    True
    >>> is_in(None, [], [])
    False
    >>> is_in("human", ["zip", "gig"], ["ring", "time"])
    False
    >>> is_in(7, ["Blue", "Red"], ["Black", "Gray"])
    False
    >>> is_in("wizard", [], [])
    False
    """

    if not isinstance(item, str):
        return False

    return item in list1 or item in list2
