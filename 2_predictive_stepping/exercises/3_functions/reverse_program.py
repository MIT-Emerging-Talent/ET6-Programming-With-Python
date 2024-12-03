#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Reverse Program: String

A program that uses the function to reverse a user's input.

"""

# --- declare the helper function ---


def reverse_string(text: str) -> str:
    """Creates a reversed copy of a string"""
    backwards = ""
    for char in text:
        backwards = char + backwards
    return backwards


# --- use the helper function in a program ---

print("This program prints your input in reverse.\n")

user_text = ""
while user_text == "":
    user_text = input("\nEnter some something to reverse: ")
    if user_text == "":
        print("Nope, gotta enter something.  Try again.")

reversed_text = reverse_string(user_text)

print(user_text, " -> ", reversed_text)
