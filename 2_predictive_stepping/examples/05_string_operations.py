#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" String Operations

Python has features to help with lots of common string manipulations.
None of these operations modify the string they use as input!

"""

text = "Python"

# slicing single characters
sliced = text[0]
sliced = text[5]

# slicing substrings
sliced = text[0:5]
sliced = text[0:4]
sliced = text[0:3]
sliced = text[1:4]
sliced = text[2:4]

# getting the length of a string
length = len(text)

# replacing substrings
replaced = text.replace("P", "Z")
replaced = text.replace("p", "z")
replaced = text.replace("on", "agoras")

# setting strings to lower or opper case
upper = text.upper()
lower = text.lower()

# remove whitespace from the ends of a string
stripped = "  Python  ".strip()

print("end of script")
