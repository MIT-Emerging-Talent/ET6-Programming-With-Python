#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Fix the bug(s)! """

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from trace_recursion import trace_recursion


@trace_recursion
def f_s_n(numbers: list) -> int:
    """
    
    """
    if len(numbers) == 0:
        return None
    
    if len(numbers) == 1:
        return numbers[0]

    smallest_so_far = f_s_n(numbers[1:])
    if smallest_so_far > numbers[len(numbers) - 1]:
        return  numbers[0] 
    else: 
        return smallest_so_far


# --- call the traced function ---

print(f_s_n([]), 'should be', None)
print(f_s_n([1, 2, 3]), 'should be', 1)
print(f_s_n([1, 2, 1]), 'should be', 1)
print(f_s_n([0, -2, 1, 4, 8]), 'should be', -2)
print(f_s_n([3, 2, 1, 0, -1, -2, 3]), 'should be', -2)
