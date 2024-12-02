#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Functions

Functions allow you to package blocks of code to reuse with different arguments.
Calling a function creates a new scope with your arguments and local variables.
Functions can return a value to the main scope for later use.

Passing a str, bool, int or float to a function does not modify the variable's value.

Python Tutor is very helpful for visualizing functions *

"""


# --- function declaration ---
def reverse(to_reverse: str) -> str:
    """Reverses a string."""

    # variables declared in the function are local variables
    #   they are only available inside the function call
    backwards = ""

    for char in to_reverse:
        backwards = char + backwards

    return backwards


# --- function calls and assertion tests ---
# try stepping over this function call
_1_arg = "Bori"
_1_return_value = reverse(_1_arg)
assert _1_return_value == "iroB", "reverse: Test 1"

# try stepping all the way through this function call
_2_arg = "<[+]>"
_2_return_value = reverse(_2_arg)
assert _2_return_value == ">]+[<", "reverse: Test 2"

# try stepping into this function call
#   then stepping out of it before the function returns
_3_arg = "racecar"
_3_return_value = reverse(_3_arg)
assert _3_return_value == "racecar", "reverse: Test 3"


print("end of script")

# * https://pythontutor.com/render.html#code=def%20reverse%28to_reverse%3A%20str%29%20-%3E%20str%3A%0A%20%20%20%20backwards%20%3D%20''%0A%0A%20%20%20%20for%20char%20in%20to_reverse%3A%0A%20%20%20%20%20%20%20%20backwards%20%3D%20char%20%2B%20backwards%0A%0A%20%20%20%20return%20backwards%0A%0A%0A_1_arg%20%3D%20%22Bori%22%0A_1_return_value%20%3D%20reverse%28_1_arg%29%0Aassert%20_1_return_value%20%3D%3D%20%22iroB%22,%20%22reverse%3A%20Test%201%22%0A%0A_2_arg%20%3D%20%22%3C%5B%2B%5D%3E%22%0A_2_return_value%20%3D%20reverse%28_2_arg%29%0Aassert%20_2_return_value%20%3D%3D%20%22%3E%5D%2B%5B%3C%22,%20%22reverse%3A%20Test%202%22%0A%0A_3_arg%20%3D%20%22racecar%22%0A_3_return_value%20%3D%20reverse%28_3_arg%29%0Aassert%20_3_return_value%20%3D%3D%20'racecar',%20%22reverse%3A%20Test%203%22&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
