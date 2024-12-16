#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing find_smallest_number

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
def find_smallest_number(numbers: list) -> int:
    """
    
    """
    if len(numbers) == 0:
        return None
    
    if len(numbers) == 1:
        return numbers[0]

    break_down = numbers[1:]
    recursion = find_smallest_number(break_down)
    build_up = numbers[0] if numbers[0] < recursion else recursion
    
    return  build_up


# --- call the traced function ---

print(find_smallest_number([]), 'should be', None)
print(find_smallest_number([1, 2, 3]), 'should be', 1)
print(find_smallest_number([1, 2, 1]), 'should be', 1)
print(find_smallest_number([0, -2, 1, 4, 8]), 'should be', -2)
print(find_smallest_number([3, 2, 1, 0, -1, -2]), 'should be', -2)
