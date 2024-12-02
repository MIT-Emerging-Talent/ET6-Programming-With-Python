#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Contains Cat

This program continually prompts until their input contains "cat".

"""

user_text = ""
while "cat" not in user_text.lower():
    user_text = input('Please enter something containing "cat": ')

    if user_text == "":
        print("You entered nothing, try again.")
    elif "cat" not in user_text.lower():
        print('"' + user_text + '" does not contain cat, try again.')

print("thank you for the cat")
