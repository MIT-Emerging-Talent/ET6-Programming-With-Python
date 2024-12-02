#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing Fibonacci

To visualize implementation, 
- use your VSCode debugger
- copy-paste the code into PythonTutor

To visualize strategy:
- uncomment @trace_calls and run the script
or copy the code into one of these sites:
- https://www.recursionvisualizer.com
- (https://recursion.vercel.app
- https://recursion-visualizer.vercel.app
- https://visualgo.net/en/recursion

"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


# @trace_calls
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# --- call the traced function ---

fibonacci(0)
fibonacci(1)
fibonacci(2)
fibonacci(4)
fibonacci(6)
fibonacci(8)
