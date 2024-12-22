#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci_number(n):
    """
    Calculates the nth Fibonacci number.

    Base case1: if n == 0, return 0 (0th Fibonacci number)
    base case2: if n == 1, return 1 (1st Fibonacci number)
    base case3: if n == 2, return 1 (2nd Fibonacci number)

    Recursive case: if n > 2, return fibonacci_number(n - 1) + fibonacci_number(n - 2)
    """
    if n == 0:  # base case1
        return 0  # return case
    elif n == 1 or n == 2:  # base case2, base case3
        return 1  # return case
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)  # recursive case


# --- test cases ---

print(f"fibonacci 0 {fibonacci_number(0), "should be", 0}")
print(f"fibonacci 2{fibonacci_number(2), "should be", 1}")
print(f"fibonacci 3{fibonacci_number(3), "should be", 2}")
print(f"fibonacci 6{fibonacci_number(6), "should be", 8}")
print(f"fibonacci 9{fibonacci_number(9), "should be", 34}")
