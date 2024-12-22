#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Use test cases, the docstring, and labels to describe this solution."""


def fibonacci(n: int, memo: dict = {}) -> int:
    """
    Calculate the nth Fibonacci number using memoization.

    base case 1: if n is 0, return 0

    base case 2: if n is 1, return 1

    base case 3: if n is in memo, return memo[n]

    recursive case: if n > 1, return fibonacci(n - 1) + fibonacci(n - 2)

    """
    if n == 0:  # base case 1
        return 0  # return case 1

    if n == 1:  # base case 2
        return 1  # return case 2

    if n in memo:  # base case 3
        return memo[n]  # return case 3

    # Recursive call to calculate the Fibonacci number for n - 1
    left_recursion = fibonacci(n - 1, memo)
    # Recursive call to calculate the Fibonacci number for n - 2
    right_recursion = fibonacci(n - 2, memo)
    # Store the result in the memo dictionary
    memo[n] = left_recursion + right_recursion

    return memo[n]


# --- --- --- test cases --- --- ---

print(fibonacci(2), "should be", 1)
print(fibonacci(3), "should be", 2)
print(fibonacci(5), "should be", 5)
print(fibonacci(8), "should be", 21)
print(fibonacci(10), "should be", 55)
