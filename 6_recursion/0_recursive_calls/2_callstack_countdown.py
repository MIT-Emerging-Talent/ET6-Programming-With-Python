#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Callstack Countdown

This recursive function calls itself a specific number of times, then returns 0.

Using a conditional statement, you can stop the recursion before there is an error.

"""


def callstack_countdown(depth: int) -> int:
    """Recursively calls itself until the callstack depth is reached.
        Each call prints the callstack countdown, then print...

    Parameters:
        depth: int, greater than or equal to zero

    Returns -> 0, when the callstack depth is reached
    """

    if depth == 0:
        print("done!")
        return depth

    print(depth)
    return callstack_countdown(depth - 1)


callstack_countdown(3)
callstack_countdown(2)
callstack_countdown(1)
callstack_countdown(0)
