#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Cat Detector: conditional

This program asks the user for "cat", 
then responds differently if they did provide a cat or not.

"""

user_text = input('Please enter "cat": ')

if user_text == "":
    response = "You entered nothing"
elif user_text == "cat":
    response = "Thank you for the cat"
else:
    response = '"' + user_text + '" is not "cat"'

print(response)
