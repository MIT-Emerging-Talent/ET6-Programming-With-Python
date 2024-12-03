#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Use test cases, the docstring, and labels to describe this solution. """


def fibonacci(n: int, memo: dict = {}) -> int:
    """


    base case 1:

    base case 2:

    base case 3:

    recursive case:

    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# --- --- --- test cases --- --- ---

# write some test cases!
