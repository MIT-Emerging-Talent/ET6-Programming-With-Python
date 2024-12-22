#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome using recursion.

    base case:
        if the len(s) <= 1 (string is empty or has one character)  ->
            return True

    recursive case:
        if s[0](first letter) == s[-1](last letter)  ->
            return check_palindrome(s[1:-1])

    """

    if len(s) <= 1:  # base case
        return True  # return case

    if s[0] == s[-1]:  # recursive case
        return check_palindrome(s[1:-1])  # must use recursion
    else:
        return False


# --- test cases ---

print(check_palindrome("racecar"), "should be", True)
print(check_palindrome("madam"), "should be", True)
print(check_palindrome("hello"), "should be", False)
