#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Use test cases, the docstring, and labels to describe this solution.
> I did it in 29/12/2024
"""


def fibonacci(n: int, memo: dict = {}) -> int:
    """
    Calculates the n'th number in the Fibonacci Sequence. using memory

    base case 1:  n = 0      -> 0

    base case 2:  n = 1      -> 1

    base case 3:  n in memo  -> memo[n]

    recursive case: n > 1    -> ƒ(n - 1) + ƒ(n - 2)

    """
    if n == 0:  # base case 1
        return 0  # turn-around 1

    if n == 1:  # base case 2
        return 1  # turn-around 2

    if n in memo:  # base case 3
        return memo[n]  # turn-around 3

    #            rec. 1   | bd 1 |       rec. 2  | bd 2 |
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    #                           | build-up |

    return memo[n]


# --- --- --- test cases --- --- ---

# write some test cases!
assert fibonacci(0) == 0, "0 -> 0"
assert fibonacci(1) == 1, "1 -> 1"
assert fibonacci(2) == 1, "2 -> 1"
assert fibonacci(3) == 2, "3 -> 2"
assert fibonacci(4) == 3, "4 -> 3"
assert fibonacci(5) == 5, "5 -> 5"
assert fibonacci(6) == 8, "6 -> 8"
assert fibonacci(7) == 13, "7 -> 13"
assert fibonacci(11) == 89, "11 -> 89 "
