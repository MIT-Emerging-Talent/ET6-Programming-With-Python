#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for a item that exist in one lists.

Parameters:
    item(str): String that will be checked in list1 and list2.
    list(str, list): contains a list of string
    list2(str, list): contains a list of string

Returns->
    item(str) -> bool: An Item that exist in list1 or list2

Created on 2024-12-13
Author: Aziz
"""


def is_in_one(item: str, list1: list, list2: list) -> bool:
    """is in one

    A function that takes in two lists of strings and a item.
    It will return True if the item is in one of the lists.

    doctest:
    >>> is_in_one("cool", ["Aziz", "date"], ["cool", "date"])
    True
    >>> is_in_one("study", ["MIT", "best", "University"], ["study", "MIT", "student"])
    True
    >>> is_in_one("food", [], ["food", "Gray"])
    True
    >>> is_in_one("nice", ["Aziz", "date"], ["human", "time"])
    False
    >>> is_in_one(6, ["Blue", "Red"], ["Black", "Gray"])
    False
    >>> is_in_one("wizard", [], [])
    False
    """
    if not isinstance(item, str):
        return False

    return item in list1 or item in list2
