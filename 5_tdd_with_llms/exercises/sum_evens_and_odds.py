#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sum Evens and Odds

Write a function that takes a list of numbers
and returns a dictionary with sums of the even and odd numbers in the list.

"""


def sum_even_and_odds(numbers):
    """
    Sum the even and odd numbers in a list of numbers.

    Parameters:
    numbers (list): The list of numbers to sum.

    Returns:
    sum: Sum of the even and odd numbers.

    Examples:
    >>> sum_even_and_odds([1, 2, 3, 4, 5, 6])
    {'evens': 12, 'odds': 9}
    >>> sum_even_and_odds([7, 6, 5, 4, 3, 2, 1])
    {'evens': 12, 'odds': 16}
    >>> sum_even_and_odds([1, 3, 5, 7, 9])
    {'evens': 0, 'odds': 25}
    >>> sum_even_and_odds([2, 4, 6, 8, 10])
    {'evens': 30, 'odds': 0}
    >>> sum_even_and_odds([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    {'evens': 12, 'odds': 32}
    >>> sum_even_and_odds([10, -1, 2.5, 3, 0])
    {'evens': 12.5, 'odds': 2}
    >>> sum_even_and_odds([12.6, 1, 2.4, 3, 0, 1.5])
    {'evens': 15.0, 'odds': 5.5}
    >>> sum_even_and_odds([1])
    {'evens': 0, 'odds': 1}
    >>> sum_even_and_odds([])
    {'evens': 0, 'odds': 0}
    >>> sum_even_and_odds([1, 'a', 2, 3])
    Traceback (most recent call last):
        ...
    TypeError: All elements in the list must be numbers (int or float).
    """
    evens = 0
    odds = 0

    # Check each number in the list if it's even or odd
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers (int or float).")

        int_part = int(num)  # Convert float to integer by cutting the decimal part
        if int_part % 2 == 0:
            evens += num
        elif isinstance(num, (int, float)):
            odds += num

    return {"evens": evens, "odds": odds}
