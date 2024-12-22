#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_biggest_number(to_search):
    """
    Finds the biggest number in a list.

    Base case1: if len(to_search) == 0, return None

    Base case2: if len(to_search) == 1, return to_search[0]

    Recursive case: if len(to_search) > 1,
                    return the bigger of the first element and the biggest in the rest of the list
    """
    if len(to_search) == 0:
        return None  # Base case: if list is empty, return None
    if len(to_search) == 1:
        return to_search[0]  # Base case: if list has one element, return that element
    else:
        first = to_search[0]  # First element in the list
        rest = to_search[1:]  # Rest of the list (all elements except the first one)
        biggest_in_rest = find_biggest_number(
            rest
        )  # Recursively find the biggest in the rest of the list

        if first > biggest_in_rest:
            return first
        else:
            return biggest_in_rest


# --- test cases ---

print(f"single item in the list{find_biggest_number([42]), "should be", 42}")
print(
    f"biggest number in the list 1-5{find_biggest_number([5, 1, 2, 3, 4]), "should be", 5}"
)
print(f"biggest number{find_biggest_number([3, 1, 4, 9, 1, 5]), "should be", 9}")
print(f"empty list should be none{find_biggest_number([]), "should be", None}")
