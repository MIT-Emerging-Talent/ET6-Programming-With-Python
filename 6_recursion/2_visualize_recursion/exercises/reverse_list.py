#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Visualizing reverse_list

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
def reverse_list(to_reverse: list) -> list:
    if len(to_reverse) == 0:
        return []

    return reverse_list(to_reverse[1:]) + [to_reverse[0]]


# --- call the traced function ---

reverse_list([])
reverse_list([1, 2, 3])
reverse_list([1, 2, 1])
reverse_list(["", False, None, 0])
