#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from trace_recursion import trace_recursion


@trace_recursion
def flatten_nested_list(nested_list: list) -> list:
    """
    flatten_nested_list flattens a nested list.

    base case: if the nested_list is empty, return an empty list []

    recursive case: if the nested_list is not empty,
                    return a list with the first item and the flattened list of the rest of the items

    """
    if not nested_list:  # base case
        return []  # return case

    flattened_list = []  # must use a list
    for item in nested_list:
        if isinstance(item, list):  # recursive case
            flattened_list.extend(flatten_nested_list(item))  # must use recursion
        else:
            flattened_list.append(item)  # must use item
    return flattened_list


# --- test cases ---

print(flatten_nested_list([]), "should be", [])
print(flatten_nested_list([1, [2, 3]]), "should be", [1, 2, 3])
print(flatten_nested_list([1, [2, [3, 4]], 5]), "should be", [1, 2, 3, 4, 5])
print(flatten_nested_list([1, 2, 3]), "should be", [1, 2, 3])
