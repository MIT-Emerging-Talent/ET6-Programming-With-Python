#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Fix the bug(s)!"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from trace_recursion import trace_recursion


@trace_recursion
def fibonacci_memo(n: int, memo: dict = {}) -> int:
    """
    Calculates the nth Fibonacci number using memoization.

    base case 1: if n == 0, return 0

    base case 2: if n == 1, return 1

    base case 3: if n in memo, return memo[n]

    recursive case: return fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    """
    if n == 0:  # base case 1
        return 0  # return case 1

    if n == 1:  # base case 2
        return 1  # return case 2

    if n in memo:  # base case 3
        return memo[n]  # return case

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(
        n - 2, memo
    )  # recursive case
    return memo[n]


# --- call the traced function ---

print(fibonacci_memo(0), "should be", 0)
print(fibonacci_memo(1), "should be", 1)
print(fibonacci_memo(2), "should be", 1)
print(fibonacci_memo(3), "should be", 2)
print(fibonacci_memo(4), "should be", 3)
print(fibonacci_memo(6), "should be", 8)
print(fibonacci_memo(8), "should be", 21)
