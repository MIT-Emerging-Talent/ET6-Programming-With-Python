#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Comparing and Asserting

Comparing two values will tell you if they are the same or not.
The `assert` statement will throw an error if it's argument is false.
    If the argument is true, it does nothing.

Together, comparing and asserting are a good way to test your understanding.
    Some of the exercises in this workshop will use assertions.

"""

# --- Comparing ---

# Check if two values are the same using ==

equality = 1 == 1.0
equality = 1 == 1
equality = 1 == "1"
equality = True == "True"
equality = "dog" == "Dog"

# Check if two values are not the same using !=

difference = 1 != 1.0
difference = 1 != 1
difference = 1 != "1"
difference = True != "True"
difference = "dog" != "Dog"

# --- Asserting ---

# passing assertions
assert True
assert 1 == 1
assert 1 == 1.0

# asserting values stored in variables
assert equality is False
assert difference is True

assert isinstance(equality, bool)
assert isinstance(difference, bool)

# failing assertions
#   uncomment any of the following lines to throw an assertion error
#   a failed assertion will stop the program, no further lines will execute

# assert 1 != 1
# assert 1 != 1.0
# assert False
# assert difference == "difference"
# assert isinstance(equality, float)

print("end of script")
