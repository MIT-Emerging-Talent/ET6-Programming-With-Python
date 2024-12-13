#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Data Types

"Types" are different ways to represent data in a program.
Different types are useful for modeling different aspects of the world in your program.

We will start with only 4 types: string, integer, float, boolean.
You can use type() to print the type of a value.

"""

# Strings: store and work with text data
a_string = "Pine trees make pinecones."
a_string = ""  # an empty string is still a string

# Integer: represent whole numbers
an_integer = 1
an_integer = 0
an_integer = -12

# Float: represents decimal numbers
a_float = 1.0
a_float = 0.1
a_float = -1.2

# Boolean: useful for "yes"/"no" situations
a_boolean = True
a_boolean = False

# --- isinstance() : test the type of a value ---

# passing
pass_check_string = isinstance(a_string, str)
pass_check_integer = isinstance(an_integer, int)
pass_check_float = isinstance(a_float, float)
pass_check_boolean_as_bool = isinstance(a_boolean, bool)
pass_check_boolean_as_int = isinstance(a_boolean, int) # Booleans can be integers: True = 1, False = 0

# failing
fail_check_string = isinstance(a_string, bool)
fail_check_integer = isinstance(an_integer, float)
fail_check_float = isinstance(a_float, int)
fail_check_boolean = isinstance(a_boolean, str)

print("end of script")
