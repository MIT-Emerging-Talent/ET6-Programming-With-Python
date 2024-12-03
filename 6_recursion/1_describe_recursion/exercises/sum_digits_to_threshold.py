#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Describe this solution by filling in the docstring and labeling each part. """


def sum_digits_to_threshold(n, threshold):
    """


    base case 1:

    base case 2:

    recursive case:

    """
    if n < 10:  #
        return n  #

    #                          |
    digit_sum = sum(int(digit) for digit in str(n))

    if digit_sum > threshold:  #
        return threshold  #

    #
    return sum_digits_to_threshold(digit_sum, threshold)


# --- --- --- test cases --- --- ---

assert sum_digits_to_threshold(123, 7) == 6, "Test 1"
assert sum_digits_to_threshold(123, 5) == 5, "Test 2"
assert sum_digits_to_threshold(5, 3) == 5, "Test 3"
assert sum_digits_to_threshold(100, 99) == 1, "Test 4"
