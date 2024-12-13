#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Pausing on Errors

By default, the debugger will stop on errors and show what went wrong.
    
You can change this setting in the breakpoints pane down left.
        
"""

a = 1

b = "2"

# the error message will appear below this line
#   and the values in memory can help you understand what went wrong
# converting b into an integer
c = a + int(b)

print(c)
