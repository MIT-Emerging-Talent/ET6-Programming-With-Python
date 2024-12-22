#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Visualizing reverse_list

To visualize implementation,
- use your VSCode debugger
- copy-paste the code into PythonTutor

To visualize strategy:
- run the script and read the recursion trace
- comment @trace_recursion and debug the function
or copy the function into one of these sites:
- https://www.recursionvisualizer.com
- (https://recursion.vercel.app
- https://recursion-visualizer.vercel.app
- https://visualgo.net/en/recursion

"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from trace_recursion import trace_recursion


@trace_recursion
def reverse_list(to_reverse: list) -> list:
    """
    Reverses the order of a list.

    base case:
        empty list (if the len(to_reverse) == 0)    ->  [] (return [])

    recursive case: # if the len(to_reverse) > 0, return reverse_list(to_reverse[1:]) + [to_reverse[0]]
        non-empty list ->  ƒ(list without first item) + [first item]

    """
    if len(to_reverse) == 0:  # base case - empty list    ->  []
        return []  # return case

    break_down = to_reverse[1:]  # must use argument(s)
    recursion = reverse_list(break_down)  # must use recursion
    build_up = recursion + [to_reverse[0]]  # must use recursion

    return build_up


# --- call the traced function ---

print(reverse_list([]), "should be", [])
print(reverse_list([1, 2, 3]), "should be", [3, 2, 1])
print(reverse_list([1, 2, 1]), "should be", [1, 2, 1])
print(reverse_list(["", False, None, 0]), "should be", [0, None, False, ""])
