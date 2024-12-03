#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole + Chat GPT
"""


from typing import Union


def add_two_numbers(
    num1: Union[int, float], num2: Union[int, float]
) -> Union[int, float]:
    """add_two_numbers will return the sum of two numbers.

    Parameters:
      num1: int or float. The first number to add.
      num2: int or float. The second number to add.

    Returns: int or float.
      the sum of both numbers.

    >>> add_two_numbers(1, 1)
    2

    >>> add_two_numbers(1.0, 3)
    4.0

    >>> add_two_numbers(1.0, 3.0)
    4.0


    >>> add_two_numbers(1, 3.0)
    4.0
    """
    assert isinstance(num1, (int, float)), "first argument must be an int or a float"
    assert isinstance(num2, (int, float)), "second argument must be an int or a float"

    return num1 + num2
