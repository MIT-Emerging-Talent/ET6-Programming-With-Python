#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Use test cases, the docstring, and labels to describe this solution.
> I did it in 29/12/2024
"""


def merge_sort(numbers: list) -> list:
    """
    A function that call itself recursivly to sort a list

    base case: n <= 1   -> return numbers

    recursive case: f(numbers[:mid])
                    f(numbers[mid:])

    """
    if len(numbers) <= 1:  # base case 1
        return numbers  # turn-around 1

    mid = len(numbers) // 2
    #            rec. 1     | bd 1
    left_half = merge_sort(numbers[:mid])
    #            rec. 2     | bd 2 |
    right_half = merge_sort(numbers[mid:])
    #      | build-up |
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
assert merge_sort([8, 2, 9, 5, 1, 0]) == [0, 1, 2, 5, 8, 9]
assert merge_sort(["Heba", "yas", "Rose", "Sara", "Jasmeen"]) == [
    "Heba",
    "Jasmeen",
    "Rose",
    "Sara",
    "yas",
]
assert merge_sort(["c", "2", "1", "a"]) == ["1", "2", "a", "c"]
assert merge_sort([22, 0, 3, 2, 78]) == [0, 2, 3, 22, 78]
assert merge_sort(["s", "@", "13", "!"]) == ["!", "13", "@", "s"]
