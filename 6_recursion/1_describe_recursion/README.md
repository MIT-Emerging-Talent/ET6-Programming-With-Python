# Describe Recursion

Practice using different terms and notation to describe recursive solutions.

## Parts of Recursion

Basic recursive solutions can be described using these parts:

- **base case**: The smallest version of the problem you are trying to solve.
- **turn-around**: What to return when you have reached a base case.
- **recursive case**: A version of the problem that can be broken down further
- **break-down**: How you break the problem into a smaller piece / smaller
  pieces.
- **recursion**: Calling your function with the smaller version(s) of the
  problem.
- **build-up**: Re-combining the recursive results to get closer to the full
  solution.

## (semi-)Formal Description

You can also summarize a recursive strategy in a few lines like so:

```py
"""
behavior description

base case :
    argument description  ->  turn-around description
recursive case:
    argument description  ->  ƒ(break-down description) build-up description 
"""
```

## Function Template

Let's put these pieces together into a template Python function that can help
you learn how to read and understand recursive solutions.

For this chapter instead of writing a complete docstring, you only need to write
the semi-formal recursive description. Learning reading a recursive function and
summarizing it with this notation will help you master recursion and (later on)
connect your programming knowledge to computer science principles.

```py
def _func_name_(__: __) -> __:
    """
    behavior description

    base case :
        argument description  ->  turn-around description
    recursive case:
        argument description  ->  ƒ(break-down description) build-up description
    """
    is_base_case = __ # must use argument(s)
    if is_base_case:
        turn_around = __
        return turn_around
    else:
        break_down = __ # must use argument(s)
        recursion = _func_name_(break_down)
        build_up = __ # must use recursion
        return build_up
```

## All Together

Let's look at an example, going from a completed template to a more conventional
recursive solution. Notice that the closer you get to a standard Python
solution, the more it resembles the semi-formal description.

```py
# 0. completed template

def reverse_string(to_reverse: str) -> str:
  """
  Reverses the characters in a string.

  base case :
      empty string    ->  empty string
  recursive case:
      non-empty str ->  ƒ(string without first char) + first char
  """
  is_base_case = len(to_reverse) == 0 # must use argument(s)
  if is_base_case:
      turn_around = ''
      return turn_around

  break_down = to_reverse[1:] # must use argument(s)
  recursion = reverse_string(break_down)
  build_up = recursion + to_reverse[0] # must use recursion
  return build_up
```

```py
# 1. labeled base case

def reverse_string(to_reverse: str) -> str:
  """
  Reverses the characters in a string.

  base case :
      empty string    ->  empty string
  recursive case:
      non-empty str ->  ƒ(string without first char) + first char
  """
  if len(to_reverse) == 0: # base case
      return '' # turn-around

  break_down = to_reverse[1:] # must use argument(s)
  recursion = reverse_string(break_down)
  build_up = recursion + to_reverse[0] # must use recursion
  return build_up
```

```py
# 2. labeled recursive case

def reverse_string(to_reverse: str) -> str:
  """
  Reverses the characters in a string.

  base case :
      empty string    ->  empty string
  recursive case:
      non-empty str ->  ƒ(string without first char) + first char
  """
  if len(to_reverse) == 0: # base case
      return '' # turn-around

  #          recursion, break-down, build-up
  return reverse_string(to_reverse[1:]) + to_reverse[0]
```

```py
# 3. standard recursive solution

def reverse_string(to_reverse: str) -> str:
  """
  Reverses the characters in a string.

  base case :
      empty string    ->  empty string
  recursive case:
      non-empty str ->  ƒ(string without first char) + first char
  """
  if len(to_reverse) == 0:
      return ''

  return reverse_string(to_reverse[1:]) + to_reverse[0]
```
