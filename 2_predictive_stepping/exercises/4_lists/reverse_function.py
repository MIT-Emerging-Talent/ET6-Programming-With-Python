#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Testing Functions with Lists

Assertion tests to understand the function's behavior.

"""

# --- declare function ---


def reverse_list(items: list) -> list:
    """Creates a reversed copy of a list"""
    backwards = []
    for item in items:
        backwards.insert(0, item)
    return backwards


# --- test function ---

_1_arg = ["x", "y", "z"]
_1_returned = reverse_list(_1_arg)
assert _1_returned == ["z", "y", "x"], "Test 1"

_2_arg = [True, False]
_2_returned = reverse_list(_2_arg)
assert _2_returned == [False, True], "Test 2"

_3_arg = [1729]
_3_returned = reverse_list(_3_arg)
assert _3_returned == [1729], "Test 3"

_4_arg = []
_4_returned = reverse_list(_4_arg)
assert _4_returned == [], "Test 4"
