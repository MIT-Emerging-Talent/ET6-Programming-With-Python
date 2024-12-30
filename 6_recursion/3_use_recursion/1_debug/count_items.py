#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Fix the bug(s)! """

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from trace_recursion import trace_recursion


@trace_recursion
def count_items(to_count: list) -> int:
    """
    
    """
    if len(to_count) == 0:
        return 0

    return  count_items(to_count[1:])


# --- call the traced function ---

print(count_items([]), 'should be', 0)
print(count_items([1, 2, 3]), 'should be', 3)
print(count_items([1, 2, 1]), 'should be', 3)
print(count_items(["", False, None, 0]), 'should be', 4)
print(count_items(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']), 'should be', 8)
