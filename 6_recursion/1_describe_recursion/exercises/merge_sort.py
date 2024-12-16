#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Use test cases, the docstring, and labels to describe this solution. """


def merge_sort(numbers: list) -> list:
    """


    base case:

    recursive case:

    """
    if len(numbers) <= 1:  #
        return numbers  #

    mid = len(numbers) // 2
    # 
    left_half = merge_sort(numbers[:mid])
    # 
    right_half = merge_sort(numbers[mid:])

    return merge(left_half, right_half)


# you do not need to label this helper function
def merge(left, right):
    sorted_numbersay = []
    while left and right:
        if left[0] < right[0]:
            sorted_numbersay.append(left.pop(0))
        else:
            sorted_numbersay.append(right.pop(0))
    sorted_numbersay.extend(left or right)
    return sorted_numbersay


# --- --- --- test cases --- --- ---
