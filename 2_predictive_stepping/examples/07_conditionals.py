#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Conditionals

Conditional statements execute different lines depending on an expression's value

"""

prompt_1 = '-> Do you want to save your input? \n \
    Enter "Y" for yes, anything else for no: '
prompt_2 = '-> Do you want to save your input? \n \
    Enter "Y" for yes, enter "N" for no: '


# -- if statements conditionally execute one block of code based on one expression --

response = input(prompt_1)
if response == "Y":
    saved_1 = response


# -- if/else statements conditionally execute two blocks of based on one expression --

response = input(prompt_1)
if response == "Y":
    saved_2 = response
else:
    saved_2 = "[[ redacted ]]"


# -- if/elif/else statements execute blocks of code based on multiple expressions --
#      the else block is executed by default if no expression if no condition is met

response = input(prompt_2)
if response == "Y":
    saved_3 = response
elif response == "N":
    saved_3 = "[[ redacted ]]"
else:
    saved_3 = "received an unrecognized command"


# you can use if/elif without else when you do not want a default behavior

response = input(prompt_2)
if response == "Y":
    saved_4 = response
elif response == "N":
    saved_4 = "[[ redacted ]]"


print("end of script")
