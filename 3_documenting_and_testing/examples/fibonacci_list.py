#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating lists of Fibonacci numbers

Module contents:
    - fibonacci_list: generates a list of n fibonacci numbers.

Created on XX XX XX
@author: Evan Cole
"""

# --- before documenting and testing ---


# def mystery_0(a):
#     if a == 0:
#         return []
#     if a == 1:
#         return [0]
#     if a == 2:
#         return [0, 1]

#     b = [0, 1]
#     for c in range(2, a):
#         b.append(b[-1] + b[-2])
#     return b


# --- after documenting and testing ---


def fibonacci_list(sequence_length: int) -> list[int]:
    """Generates a list containing the first n numbers of the Fibonacci sequence.

    Parameters:
        sequence_length: int, greater than or equal to zero

    Returns -> list[int] with the first n numbers of the Fibonacci sequence

    Raises:
        AssertionError: if the argument is not an integer
        AssertionError: if the argument is less than 0

    >>> fibonacci_list(0)
    []

    >>> fibonacci_list(4)
    [0, 1, 1, 2]

    >>> fibonacci_list(8)
    [0, 1, 1, 2, 3, 5, 8, 13]
    """

    # the sequence length should be an integer greater than 0
    assert isinstance(sequence_length, int), "sequence length is not an integer"
    assert sequence_length >= 0, "sequence length is less than 0"

    # 3 base cases if the list is too short
    # because this strategy reads back 2 indices in the list
    if sequence_length == 0:
        return []

    if sequence_length == 1:
        return [0]

    if sequence_length == 2:
        return [0, 1]

    # sum the previous two values and append them to the list
    #   until the list is long enough, then we have the solution
    sequence = [0, 1]
    while len(sequence) < sequence_length:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence
