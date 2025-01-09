#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for list manipulation focusing on alternating elements.

Module contents:
    - alternate_elements: Creates a new list with every other element

Created on 2024-12-06
Author: Claude AI
"""

def alternate_elements(items: list) -> list:
    """Returns a new list containing every other element from the input list.
    
    Takes any list and returns a new list with elements at even indices
    (0, 2, 4, etc.). The original list is not modified.
    
    Parameters:
        items: list, the input list to process
        
    Returns -> list: new list containing every other element
    
    Raises:
        AssertionError: if input is not a list
    
    Examples:
        >>> alternate_elements([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> alternate_elements(['a', 'b', 'c'])
        ['a', 'c']
        >>> alternate_elements([])
        []
    """
    assert isinstance(items, list), "input must be a list"

    return items[::2]
