#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Fix the bug(s)!"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from trace_recursion import trace_recursion


@trace_recursion
def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number using recursion.

    base case 1: if n <= 0, return 0

    base case 2: if n == 1, return 1

    recursive case: return fibonacci(n + 1) - fibonacci(n + 2)

    """
    if n <= 0:  # base case 1
        return 0  # return case 1

    if n == 1:  # base case 2
        return 1  # return case 2

    return fibonacci(n - 1) + fibonacci(n - 2)  # recursive case


# --- call the traced function ---

print(fibonacci(0), "should be", 0)
print(fibonacci(1), "should be", 1)
print(fibonacci(2), "should be", 1)
print(fibonacci(3), "should be", 2)
print(fibonacci(4), "should be", 3)
print(fibonacci(6), "should be", 8)
print(fibonacci(8), "should be", 21)
