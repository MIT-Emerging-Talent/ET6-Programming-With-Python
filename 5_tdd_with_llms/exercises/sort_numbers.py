#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Sort Numbers

Write a function that takes in a list of numbers and returns the list sorted in ascending order.

"""


def sort_numbers(numbers):
    """
    Sort a list of numbers in ascending order.

    Parameters:
    numbers (list): The list of numbers to sort.

    Returns:
    list: The sorted list of numbers.

    Examples:
    >>> sort_numbers([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> sort_numbers([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    >>> sort_numbers([10, -1, 2.5, 3, 0])
    [-1, 0, 2.5, 3, 10]
    >>> sort_numbers([1])
    [1]
    >>> sort_numbers([])
    []
    """

    # Type test
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be integers or floats")

    sorted_list = []

    while numbers:
        smallest = numbers[0]  # Assume the first number is the smallest

        # Go through the list to find the real smallest number
        for num in numbers:
            if num < smallest:
                smallest = num

        sorted_list.append(smallest)  # Add the smallest to the sorted list
        numbers.remove(
            smallest
        )  # Remove the smallest from the original list, test won't run without this line

    return sorted_list
