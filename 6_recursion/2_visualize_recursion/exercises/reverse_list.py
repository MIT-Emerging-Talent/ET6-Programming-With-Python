#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing reverse_list

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
    
    """
    if len(to_reverse) == 0:
        return []

    break_down = to_reverse[1:]
    recursion = reverse_list(break_down)
    build_up = recursion + [to_reverse[0]]

    return  build_up


# --- call the traced function ---

print(reverse_list([]), 'should be', [])
print(reverse_list([1, 2, 3]), 'should be', [3, 2, 1])
print(reverse_list([1, 2, 1]), 'should be', [1, 2, 1])
print(reverse_list(["", False, None, 0]), 'should be', [0, None, False, ""])
