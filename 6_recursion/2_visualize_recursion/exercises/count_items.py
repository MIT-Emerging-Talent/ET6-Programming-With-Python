#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing count_items

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
def count_items(to_count: list) -> int:
    """
    
    """
    if len(to_count) == 0:
        return 0

    break_down = to_count[1:]
    recursion = count_items(break_down)
    build_up = recursion + 1

    return  build_up


# --- call the traced function ---

print(count_items([]), 'should be', 0)
print(count_items([1, 2, 3]), 'should be', 3)
print(count_items([1, 2, 1]), 'should be', 3)
print(count_items(["", False, None, 0]), 'should be', 4)
print(count_items(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']), 'should be', 8)
