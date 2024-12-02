#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables

All the examples so far have not written to or read from program memory.
    They have used values and comparisons directly without saving the results for later.

Variables are how you save and access values in program memory.
Variables are useful, but they also add some complexity to your program,
    this is when the debugger becomes most useful!

You will know you have understood this file when you can:
    1. Predict which line will execute next and how it will change program state
    2. Step forward in the program in the debugger
    3. Check your prediction, correcting your understanding when you make a mistake
    4. repeat from step 1

"""

# you create a new variable by assign a value to it
name = "D'athaniel"

# you can assign a new value to a variable with the same syntax
name = "Mittens"


# variables can also be assigned the value stored in another variable
# notice!  Variables only store one value at a time, the most recent one
hand_thing = name

# reassigning the new variable does not change the value stored in the other
hand_thing = "glove"
# and vice-versa
name = "Poalia"

# using a variable without first assigning a value will throw an error
toadstool

print("end of script")
