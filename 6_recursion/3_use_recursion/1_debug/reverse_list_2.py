#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Fix the bug(s)!"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from trace_recursion import trace_recursion


@trace_recursion
def reverse_list(to_reverse: list) -> list:
    """
    reverses a list.

    base case:  empty list (if the len(to_reverse) == 0)    ->  [] (return [])

    recursive case:
        non-empty list (if the len(to_reverse) > 0)    ->
            reverse_list(list without last item) + [last item]

    """
    if len(to_reverse) == 0:  # empty list    ->  []
        return []  # return case

    length = len(to_reverse)  # must use argument(s)
    return reverse_list(to_reverse[: length - 1]) + [
        to_reverse[length - 1]
    ]  # must use recursion


# --- call the traced function ---

print(reverse_list([]), "should be", [])
print(reverse_list([1, 2, 3]), "should be", [3, 2, 1])
print(reverse_list([1, 2, 1]), "should be", [1, 2, 1])
print(reverse_list(["", False, None, 0]), "should be", [0, None, False, ""])
