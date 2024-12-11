#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module containing string manipulation functions for removing spaces.
This is part of the debugging exercise series focusing on buggy tests.

Module contents:
    - remove_spaces: Removes all spaces from a string

Created on 2024-12-06
Author: Claude AI
"""

def remove_spaces(text: str) -> str:
    """Removes all spaces from a string.
    
    This function takes any string input and returns a new string with all
    space characters removed. It preserves all other characters including
    numbers, punctuation, and special characters.
    
    Parameters:
        text: str, the input string to process
        
    Returns -> str: the input string with all spaces removed
    
    Raises:
        AssertionError: if input is not a string
    
    Examples:
        >>> remove_spaces("hello world")
        'helloworld'
        >>> remove_spaces("   spaces   ")
        'spaces'
        >>> remove_spaces("no spaces")
        'nospaces'
        >>> remove_spaces("")
        ''
    """
    assert isinstance(text, str), "input must be a string"
    return text.replace(" ", "")
