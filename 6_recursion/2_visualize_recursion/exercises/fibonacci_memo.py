#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing fibonacci_memo

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
def fibonacci_memo(n: int, memo: dict = {}) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# --- call the traced function ---

fibonacci_memo(0)
fibonacci_memo(1)
fibonacci_memo(8)
fibonacci_memo(4)
fibonacci_memo(6)
fibonacci_memo(10)
