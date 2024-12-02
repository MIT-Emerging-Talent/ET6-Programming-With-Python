#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Cat Detector: while

This program continually prompts until it gets a cat.

"""

user_text = ""
while user_text.lower() != "cat":
    user_text = input("Please enter a cat: ")

    if user_text == "":
        print("You entered nothing, try again.")
    elif user_text.lower() != "cat":
        print('"' + user_text + '" is not  a cat, try again.')

print("thank you for the cat")
