# Just Enough Python: Cheat Sheet

A reference for all the Python syntax and language features you need for Python
Self-Study 1.

- [Comments](#comments)
- [Data Types](#data-types)
- [Operators](#operators)
- [assertions](#assertions)
- [String Manipulation](#string-manipulation)
- [Printing](#printing)
- [Variables](#variables)
- [Lists](#lists)
- [Input](#input)
- [Conditionals](#conditionals)
- [While Loops](#while-loops)
- [For-In Loops](#for-in-loops)
- [Functions](#functions)
- [Pass](#pass)

---

## Comments

Notes written in your code for developers to read. The computer will ignore
these when executing your code.

```py
 # single-line comment

'''
  multiple line comment
  (actually a string, but don't worry about that just yet)
'''
```

[TOP](#just-enough-python-cheat-sheet)

---

## Data Types

The smallest pieces of data in a Python program. There are many data types but
you only need to know these for now:

```py
# Booleans
True
False

# Strings
''  # empty string
'hello'
'"hello"'  # quotes in a string (1)
"'hello'"  # quotes in a string (2)

# Integers
0
1
-100

# Floats
0.0
1.5
-3.14

# isinstance(): checks if a value is a certain type
isinstance("a string", str)  # True
isinstance(True, bool)  # True
isinstance(1, int)  # True
isinstance(1.0, float)  # True
```

[TOP](#just-enough-python-cheat-sheet)

---

## Operators

Ways to transform data. An operator takes in 1 or more values and _evaluates to_
a new value.

Operators in Python are a huge topic, for now this should be enough:

```py
# -- string concatenation --
"hello" + " " + "world"  # "hello world"

# -- logical (or boolean) operators --
True and False  # False
True or False  # True
not True  # False

# -- arithmetic: int int --
# addition
4 + 2  # 6
# subtraction
4 - 2  # 2

# -- arithmetic: float float --
# addition
4.0 + 2.0  # 6.0
# subtraction
4.0 - 2.0  # 2.0

# -- arithmetic: mixed --
# addition
4 + 2.0  # 6.0
# subtraction
4.0 - 2  # 2.0

# -- comparisons --
# equality
4 == "4"  # False
# inequality
4 != "4"  # True
# greater than
4 > 3  # True
4 > 4  # False
# less than
4 < 4  # False
4 < 5  # True
# greater than or equal to
4 >= 3  # True
4 >= 4  # True
4 >= 5  # False
# less than or equal to
4 <= 3  # False
4 <= 4  # True
4 <= 5  # True
```

[TOP](#just-enough-python-cheat-sheet)

---

## Assertions

You can test if something is True or False using `assert`. If the assertion If
the assertion fails, there will be an error and the program stops. If the
assertion passes, nothing happens and the program continues. This is a useful
tool for studying, you can use assertions like a small quiz to test your
understanding of the program.

Adding a description to your assertion will help you read the error messages in
your console.

```py
# a passing assertion without a description
assert 4 > 3

# a passing assertion with a description
assert 4 > 3, 'four is greater than 3'

# a failing assertion without a description
assert 4 == 3 # AssertionError

# a failing assertion with a description
assert 4 == 3, 'four is equal to three' # AssertionError: four is equal to three
```

[TOP](#just-enough-python-cheat-sheet)

---

## String Manipulation

The data type used for storing and manipulating text data. Strings will be the
main type of data used in the first Python workshops.

```py
# string length
len("")  # 0
len("a")  # 1
len("ab")  # 2

# indexed access
"abc"[-1]  # 'c'
"abc"[0]  # 'a'
"abc"[1]  # 'b'
"abc"[2]  # 'c'

# --- string methods ---

"HeLlO".lower()  # 'hello'
"HeLlO".upper()  # 'HELLO'

"b" in "abc"  # True

"+a+b+c+".replace("+", "")  # 'abc'

"  abc    ".strip()  # 'abc'

"abc".find("a")  # 0
"abc".find("")  # 0
"abc".find("b")  # 1
"abc".find("bc")  # 1
"abc".find("x")  # -1

# getting a substring by index
"abc"[0:]  # 'abc'
"abc"[1:]  # 'bc'
"abc"[2:]  # 'c'

"abc"[:0]  # ''
"abc"[:1]  # 'a'  no 'a'
"abc"[:2]  # 'ab'   no 'ab'

"abc"[0:0]  # ''
"abc"[0:1]  # 'a'
"abc"[0:2]  # 'ab'
"abc"[1:1]  # ''
"abc"[1:2]  # 'b'
"abc"[2:2]  # ''

"abc"[-2:-1]  # 'b'
```

[TOP](#just-enough-python-cheat-sheet)

---

## Printing

A simple way to print data to the console while the program is running. This is
helpful for knowing what data is stored in your program at different points in
execution.

```js
print("hello");
```

[TOP](#just-enough-python-cheat-sheet)

---

## Variables

Variables allow you to save values to use again later in your program.They're
kind of like a box that can only hold one thing at a time.

Variables are also an important tool for writing code that is clear for other
developers to read and understand. Using helpful names can make your code read
(sort of) like a story.

```py
# assign: name
name = "Python"

# read: name
print(name) # "Python"

# assign: exclaim
exclaim = "!"

# read: name, exclaim
# assign: name
name = name + exclaim

# read: name
print(name)  # "Python!"

# cannot read a variable before assigning it
print(noop) # NameError: name 'noop' is not defined
```

[TOP](#just-enough-python-cheat-sheet)

---

## Lists

Lists store multiple values in one data structure.

```py
letters = ['b', 'c']

# add an item to the end of the list
letters.append('d')
print(letters) # ['b', 'c', 'd']

# add an item to the beginning of the list
letters.insert('a') # => error
letters.insert(2,'c') # insert(element, index)
print(letters) # ['a', 'b', 'c', 'd']

# get the length of a list
len(letters) # 4

# get a specific letter by it's index
letters[0] # 'a'
letters[1] # 'b'
letters[2] # 'c'
letters[3] # 'a'

# slice a part of the list to a new list
letters[1:3] # ['b', 'c']
```

[TOP](#just-enough-python-cheat-sheet)

---

## Input

Programmers can pass string data into your programs using `input`.

```py
# --- input ---

# allows the user to enter a string value for the program to use
string_from_user = input("enter some text:\n")

# --- output ---

appreciation = 'thank you for this text: ' + string_from_user

# prints a message, but does not accept new input from the user
print(appreciation)
```

[TOP](#just-enough-python-cheat-sheet)

---

## Conditionals

Execute different blocks of code depending on whether an expression evaluates to
`True` or to `False`:

```py
# -- if statements conditionally execute one block of code based on one expression --
if an_expression:
    print('if') # executed if the expression is true

# -- if/else statements conditionally execute two blocks of based on one expression --
if an_expression
    print('if') # executed if the expression is true
else:
    print('else') # executed if the expression is false

# -- if/elif/else statements execute blocks of code based on multiple expressions --
#      the else block is executed by default if no expression if no condition is met
if expression_1:
    print('if') # executed if the first expression is true
elif expression_2:
    print('elif') # executed if the second expression is true
else:
    print('else') # executed if neither expression is true


# you can use if/elif without else when you do not want a default behavior
if expression_1:
    print('if') # executed if the first expression is true
elif expression_2:
    print('elif') # executed if the second expression is true
```

[TOP](#just-enough-python-cheat-sheet)

---

## While Loops

Repeat a block of code as long as an expression evaluates to `true`.

1. Evaluate the expression
2. Check if the expression is `True` or `False`
   1. if it is `True`, execute the block
   2. return to step 2
3. Move on to the next line after the loop

```py
while an_expression:
   print('still looping') # executed each time the expression is evaluated to True

# next line after the loop
```

[TOP](#just-enough-python-cheat-sheet)

---

## For-In Loops

Iterate over a string or list, executing the loop body once for each character
or item.

```py
text = 'bye'
for char in text:
  print (char) # 'b' -> 'y' -> 'e'

# next line after first loop

numbers = [1, 2, 3]
for number in numbers:
  print(number) # 1 -> 2 -> 3

# next line after second loop
```

[TOP](#just-enough-python-cheat-sheet)

---

## Functions

Wrap useful lines of code in a function so you can write them in one place and
reuse as many times as you want.

```py
# --- function declaration ---
def add(x, y):
    sum = x + y
    return sum


# --- call the function and save the result to a variable ---

seven = add(3, 4)
print(seven) # 7

eight = add(2, 6)
print(eight) # 8

# --- test the function with assertions ---

assert add(3, 4) == 7, '3 + 4 = 7'
assert add(2, 6) == 7, '2 + 6 = 8'

zero = add(-1, 1)
assert zero == 0, '-1 + 1 = 0'
```

[TOP](#just-enough-python-cheat-sheet)

---

## Pass

`pass` allows you to write the control flow structure of a program before
writing all of the logic. Without using `pass`, Python throws a syntax error if
a block is empty.

```py
if an_expression:
  pass

if expression_1:
  pass
elif expression_2:
  pass
else:
  pass

while an_expression:
  pass

for char in 'a string':
  pass

for item in []:
  pass

def funky():
  pass
```

[TOP](#just-enough-python-cheat-sheet)
