#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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

    # 3 base cases if the array is too short
    # because this strategy reads back 2 indices in the array
    if sequence_length == 0:
        return []

    if sequence_length == 1:
        return [0]

    if sequence_length == 2:
        return [0, 1]

    # sum the previous two values and append them to the list
    sequence = [0, 1]
    for _ in range(2, sequence_length):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
