#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Use test cases, the docstring, and labels to describe this solution."""


def merge_sort(numbers: list) -> list:
    """


    base case: if the len(numbers(list))<= 1, return the numbers(list)

    recursive case: if the len(numbers(list)) > 1, return merge(left_half, right_half)

    """
    if len(numbers) <= 1:  # base case
        return numbers  # return case

    mid = len(numbers) // 2
    # Recursive call to sort the left half of the list
    left_half = merge_sort(numbers[:mid])
    # Recursive call to sort the right half of the list
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

print(merge_sort([10, -1, 2, 5, 0, 6, 4, -5]), "should be", [-5, -1, 0, 2, 4, 5, 6, 10])
print(merge_sort([]), "should be", [])
print(merge_sort([1]), "should be", [1])
print(merge_sort([2, 1]), "should be", [1, 2])
print(
    merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
    "should be",
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
)
