#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole + Chat GPT
"""


def even_odd(numbers):
    """
    Separate_even_odd takes in a list of integers and separates
        the values into a dictionary of two lists:
            one list contains all evens
            the other list contains all odds

    Input: list[int]

    Return: dict { even: [int], odd: [int] }
        both lists are present even when empty

    >>> separate_even_odd([1, 2, 3])
    { even: [2], odd: [1, 3] }

    >>> separate_even_odd([1, 3, 5])
    { even: [], odd: [1, 3, 5] }

    >>> separate_even_odd([])
    { even: [], odd: [] }

    >>> separate_even_odd([-2, -4, 3, 0])
    { even: [-2, -4, 0], odd: [3] }

    >>> separate_even_odd([1, 1, 4, 2, 5])
    { even: [4, 2], odd: [1, 1, 5] }

    >>> separate_even_odd([2, 4, 8])
    { even: [2, 4, 8], odd: [] }

    >>> separate_even_odd([-1, -3, -5])
    { even: [], odd: [-1, -3, -5] }"""

    # Check if numbers is a list
    assert isinstance(numbers, list), "Input should be a list"

    # Check if all elements in the list are integers
    assert all(
        isinstance(num, int) for num in numbers
    ), "All elements in the list should be integers"

    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return {"even": even_numbers, "odd": odd_numbers}
