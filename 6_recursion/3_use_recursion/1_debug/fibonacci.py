#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Fix the bug(s)! """

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from trace_recursion import trace_recursion


@trace_recursion
def fibonacci(n: int) -> int:
    """
    
    """
    if n < 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n + 1) - fibonacci( n + 2)


# --- call the traced function ---

print(fibonacci(0), 'should be', 0)
print(fibonacci(1), 'should be', 1)
print(fibonacci(2), 'should be', 1)
print(fibonacci(4), 'should be', 3)
print(fibonacci(6), 'should be', 8)
print(fibonacci(8), 'should be', 21)
