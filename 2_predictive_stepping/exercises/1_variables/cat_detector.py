#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables: Cat Detector

Asks the use for the input "cat", throws an assertion error if the input is wrong

"""

maybe_cat = input('Enter "cat": ')

is_cat = maybe_cat == "cat"

assert is_cat, 'you should have entered "cat"'

print("thank you for the cat")
