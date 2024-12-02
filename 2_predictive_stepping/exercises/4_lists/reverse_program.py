#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Reverse Program: List

A program that uses the function to reverse a user's list.

"""

# --- declare the helper function ---


def reverse_list(items: list) -> list:
    """Creates a reversed copy of a list"""
    backwards = []
    for item in items:
        backwards.insert(0, item)
    return backwards


# --- use the helper function in a program ---

print("This program prints your saved items in reverse order.\n")

items = []

next_item = None
while next_item != "":
    print("\nSaved items: ", items)
    next_item = input(
        "Enter some text to add to the list, or enter nothing to finish: "
    )
    if next_item != "":
        items.append(next_item)

reversed_items = reverse_list(items)

print("\nHere are your items in reverse order: ", reversed_items)
