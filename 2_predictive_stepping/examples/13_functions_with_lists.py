#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Functions with Lists

Passing a list to a function passes a reference to the list, not a copy of it.
    This can cause side-effects if you are not careful.
Side-effects can cause tricky bugs if you don't understand how to find and fix them.

It's best practice to write "pure functions", functions without side-effects.
An easy way to avoid side-effects is to copy the argument list before modifying it.

Python Tutor is very helpful for visualizing side-effects *

"""

# this function modifies the argument list - side-effects!


def append__side_effect(items: list, new_value: str) -> list:
    items.append(new_value)
    return items


_1_list_before = ["a", "b"]
_1_list_after = append__side_effect(_1_list_before, "c")


# this function modifies a copy of the argument list - no side-effects!


def append__pure(items: list, new_value: str) -> list:
    updated_list = items.copy()
    updated_list.append(new_value)
    return updated_list


_2_list_before = ["x", "y"]
_2_list_after = append__pure(_2_list_before, "z")

print("end of script")

# * https://pythontutor.com/render.html#code=def%20append__side_effect%28items%3A%20list,%20new_value%3A%20str%29%20-%3E%20list%3A%0A%20%20%20%20items.append%28new_value%29%0A%20%20%20%20return%20items%0A%0A_1_list_before%20%3D%20%5B'a',%20'b'%5D%0A_1_list_after%20%3D%20append__side_effect%28_1_list_before,%20'c'%29%0A%0A%0Adef%20append__pure%28items%3A%20list,%20new_value%3A%20str%29%20-%3E%20list%3A%0A%20%20%20%20updated_list%20%3D%20items.copy%28%29%0A%20%20%20%20updated_list.append%28new_value%29%0A%20%20%20%20return%20updated_list%0A%0A_2_list_before%20%3D%20%5B'x',%20'y'%5D%0A_2_list_after%20%3D%20append__pure%28_2_list_before,%20'z'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
