#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lists

Lists are stored by reference.
This means that two variables will actually point to the same list in memory.
So when you update one variable, the other variable is also updated!
-> this is called a "side-effect"

Python Tutor visualizes this more clearly than the VSCode debugger *

"""


letters = ["a", "b"]

letters.append("c")

letters_reference = letters

letters_reference.append("d")

letters_copy = letters.copy()

letters_copy.append("e")

print("end of script")

# * https://pythontutor.com/render.html#code=%0Aletters%20%3D%20%5B1,%202,%203,%204%5D%0A%0Aletters.append%285%29%0A%0Aother_letters%20%3D%20letters%0A%0Aother_letters.append%286%29%0A%0Aletters_copy%20%3D%20letters.copy%28%29%0A%0Aletters_copy.append%287%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
