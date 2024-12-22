#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Use test cases, the docstring, and labels to describe this solution."""


def reverse_list(to_reverse: list) -> list:
    """
    Reverses the characters in a string.

    base case:     # if the len(to_reverse) == 0, return
        empty string(if the len(to_reverse))    ->  empty string (return [])
    recursive case: # if the len(to_reverse) > 0, return reverse_list(to_reverse[1:]) + [to_reverse[0]]
        non-empty str ->  ƒ(string without first char) + first char
    """
    if len(to_reverse) == 0:  # empty string    ->  empty string
        return []  # return case

    # Recursive call to reverse the list
    return reverse_list(to_reverse[1:]) + [to_reverse[0]]
    # break_down = to_reverse[1:] # must use argument(s)
    # recursion = reverse_string(break_down)
    # build_up = recursion + to_reverse[0] # must use recursion
    # return build_up


# --- call the traced function ---

print(reverse_list([]), "should be", [])
print(reverse_list([1, 2, 3]), "should be", [3, 2, 1])
print(reverse_list([1, 2, 1]), "should be", [1, 2, 1])
print(reverse_list(["", False, None, 0]), "should be", [0, None, False, ""])
