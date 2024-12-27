#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting numbers within a range.
This is part of the debugging exercise series focusing on buggy tests.

Module contents:
    - count_between: Counts how many numbers fall between two values

Created on 2024-12-06
Author: Claude AI
"""


def count_between(numbers: list, lower: int, upper: int) -> int:
    """Counts how many numbers in the list fall between lower and upper bounds.

    The bounds are inclusive, meaning a number equal to the lower or upper
    bound is counted. The numbers list can contain integers or floats.

    Parameters:
        numbers: list of numbers to check
        lower: int, lower bound (inclusive)
        upper: int, upper bound (inclusive)

    Returns -> int: count of numbers between bounds

    Raises:
        AssertionError: if numbers is not a list or bounds aren't integers

    Examples:
        >>> count_between([1, 2, 3, 4, 5], 2, 4)
        3
        >>> count_between([1.5, 2.5, 3.5], 2, 3)
        1
        >>> count_between([], 0, 10)
        0
    """
    assert isinstance(numbers, list), "first argument must be a list"
    assert isinstance(lower, int), "lower bound must be an integer"
    assert isinstance(upper, int), "upper bound must be an integer"

    count = 0
    for num in numbers:
        if lower <= num <= upper or upper <= num <= lower:
            count += 1
    return count
