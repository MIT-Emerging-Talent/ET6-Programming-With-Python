#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing Fibonacci

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

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from trace_recursion import trace_recursion


@trace_recursion
def fibonacci(n: int) -> int:
    """
    
    """
    if n <= 0:
        return 0

    if n == 1:
        return 1

    left_break_down = n - 1
    right_break_down = n - 2

    left_recursion = fibonacci(left_break_down)
    right_recursion = fibonacci(right_break_down)

    build_up = left_recursion + right_recursion
    
    return build_up


# --- call the traced function ---

print(fibonacci(0), 'should be', 0)
print(fibonacci(1), 'should be', 1)
print(fibonacci(2), 'should be', 1)
print(fibonacci(4), 'should be', 3)
print(fibonacci(6), 'should be', 8)
print(fibonacci(8), 'should be', 21)
