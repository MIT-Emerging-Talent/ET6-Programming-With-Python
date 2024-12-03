#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Testing Functions with Strings

Assertion tests to understand the function's behavior.

"""

# --- declare function ---


def reverse_string(text: str) -> str:
    """Creates a reversed copy of a string"""
    backwards = ""
    for char in text:
        backwards = char + backwards
    return backwards


# --- test function ---

_1_arg = "xyz"
_1_returned = reverse_string(_1_arg)
assert _1_returned == "zyx", "Test 1"

_2_arg = "Malayalam"
_2_returned = reverse_string(_2_arg)
assert _2_returned == "malayalaM", "Test 2"

_3_arg = "1729"
_3_returned = reverse_string(_3_arg)
assert _3_returned == "9271", "Test 3"

_4_arg = ""
_4_returned = reverse_string(_4_arg)
assert _4_returned == "", "Test 4"
