#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Tree Recursion

Tree recursion is a recursive function calls itself more than once in the body.

The names "Linear" and "Tree" recursion will make sense after the next chapter:
    2. Visualizing Recursion

This is a recursive function with two base cases and two recursive calls.

"""


def fibonacci(n: int) -> int:
    """
    Calculates the n'th number in the Fibonacci Sequence.

    base case 1:
        0               ->   0
    base case 2:
        1                ->   1
    recursive case:
        n > 1          ->   ƒ(n - 1) + ƒ(n - 2)
    """
    if n <= 0:  # base case 1
        return 0  # turn-around 1

    if n == 1:  # base case 2
        return 1  # turn-around 2

    #            rec. 1   | bd 1 |       rec. 2  | bd 2 |
    return fibonacci(n - 1) + fibonacci(n - 2)
    #                            | build-up |


# --- --- --- test cases --- --- ---

print(fibonacci(0) , 'should be ', 0)
print(fibonacci(1) , 'should be ', 1)
print(fibonacci(2) , 'should be ', 1)
print(fibonacci(3) , 'should be ', 2)
print(fibonacci(4) , 'should be ', 3)
print(fibonacci(5) , 'should be ', 5)
print(fibonacci(6) , 'should be ', 8)
print(fibonacci(7) , 'should be ', 13)
# print(fibonacci(33) , 'should be ', 3524578)  # a slow line!
