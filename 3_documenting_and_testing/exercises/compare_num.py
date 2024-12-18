#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on 16 12 2024

@author: Evan Cole
@editor: Heba
"""

# --- before documenting and testing ---

# def mystery_3(a, b):
#    if a < b:
#        return a
#    elif a > b:
#        return b
#    else:
#        return a + b

# --- after documenting and testing ---


def compare_num(number_1, number_2):
    """Function that compers two numbers
    then returns the lowest and if they equal it returns sum

    Args:
        number_1 : just a number
        number_2 : just a number

    Returns -> the lowest number or the sum of the twon numbers

    >>> compare_num(4,5)
    4

    >>> compare_num(2,6)
    2

    >>> compare_num(2.1,2.1)
    4.2

    """

    if number_1 < number_2:
        return number_1
    elif number_1 > number_2:
        return number_2
    else:
        return number_1 + number_2


# print(compare_num(2.1, 2.1))
