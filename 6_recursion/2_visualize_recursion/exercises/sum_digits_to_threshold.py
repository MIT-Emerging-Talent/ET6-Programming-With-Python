#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing sum_digit_to_threshold

To visualize implementation, 
- use your VSCode debugger
- copy-paste the code into PythonTutor

To visualize strategy:
- uncomment @trace_calls and run the script
or copy the code into one of these sites:
- https://www.recursionvisualizer.com
- (https://recursion.vercel.app
- https://recursion-visualizer.vercel.app
- https://visualgo.net/en/recursion

"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


# @trace_calls
def sum_digits_to_threshold(n, threshold):
    if n < 10:
        return n

    digit_sum = sum(int(digit) for digit in str(n))

    if digit_sum > threshold:
        return threshold

    return sum_digits_to_threshold(digit_sum, threshold)


# --- call the traced function ---

sum_digits_to_threshold(123456, 1000)
sum_digits_to_threshold(123456, 200)
sum_digits_to_threshold(555, 15)
sum_digits_to_threshold(100, 99)
sum_digits_to_threshold(9999999, 10)
