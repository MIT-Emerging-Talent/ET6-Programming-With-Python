#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""demo implementing recursive strategies"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from trace_recursion import trace_recursion


@trace_recursion
def reverse_list(to_reverse: list) -> list:
    """
    behavior description

    base case :
        argument description  ->  turn-around description
    recursive case:
        argument description  ->  ƒ(break-down description) build-up description 
    """
    base_case = _ # must use to_reverse
    if base_case:
        turn_around = _
        return turn_around

    break_down = _ # must use to_reverse
    recursion = reverse_list(break_down)
    build_up = _ # must use recursion
    
    return build_up

# ----- ----- test cases ----- -----


print(reverse_list([]), 'should be', [])
print(reverse_list([1]), 'should be', [1])
print(reverse_list(['a', 'b']), 'should be', ['a', 'b'])
print(reverse_list([1, 2, 3]), 'should be', [3, 2, 1])
print(reverse_list([3, 2, 1, 0, -1, -2, 3]), 'should be', [3, -2, -1, 0, 1, 2, 3])
