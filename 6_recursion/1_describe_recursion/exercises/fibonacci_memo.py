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
    if n == 0: #
        return 0 #

    if n == 1: #
        return 1 #

    if n in memo: #
        return memo[n] #
    
    # 
    left_recursion = fibonacci(n - 1, memo)
    # 
    right_recursion = fibonacci(n - 2, memo)
    # 
    memo[n] = left_recursion + right_recursion
    
    return memo[n]


# --- --- --- test cases --- --- ---

# write some test cases!
