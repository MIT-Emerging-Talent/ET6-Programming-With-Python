#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Reverse Input

This program reverses the user's input.

"""

user_text = ""
while user_text == "":
    user_text = input("Enter some text to reverse: ")
    if user_text == "":
        print("nope, you have to enter something")

backwards = ""
for character in user_text:
    backwards = character + backwards

print("here is your reversed input: " + backwards)
