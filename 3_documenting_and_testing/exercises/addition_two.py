#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on 16 12 2024

@author: Evan Cole
@editor: Heba
"""

# --- before documenting and testing ---

# def mystery_1(a, b):
#    return a + b

# --- after documenting and testing ---


def addition_two(first_number, second_number):
    """Add two numbers

    Parameters:
        first_number:Any number
        second_number:Any number

    Returns -> A number that is the Sum of the two numbers
    >>> addition_two(1,1)
    2

    >>> addition_two(3,9)
    12

    >>> addition_two(6.3,2.1)
    8.4

    """

    return first_number + second_number
