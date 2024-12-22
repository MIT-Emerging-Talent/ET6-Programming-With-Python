#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_items_in_list(to_count):
    """
    Counts the number of items in a list.

    base case:
        if the len(to_count) == 0, return 0
            empty list (if the len(to_count) == 0)    ->  0 (return 0)

    recursive case:
        if the len(to_count) > 0, return count_items(to_count[1:]) + 1
            non-empty list ->  ƒ(list without first item) + 1

    """
    if len(to_count) == 0:  # empty list    ->  0
        return 0  # return case
    else:
        return count_items_in_list(to_count[1:]) + 1  # recursive case


# --- test cases ---
print(f"empty list should be, {count_items_in_list([])} ")  # should be 0
print(f"3 items in list should be, {count_items_in_list([1, 2, 3])}")  # should be 3
print(f"4 items in list should be, {count_items_in_list([10, 9, 8, 7])}")  # should be 4
print(
    f"5 items in list should be, {count_items_in_list(["zizi", False, 7, None, ""])}"
)  # should be 4
