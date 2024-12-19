class: middle, center

<!-- this file is written for remark: https://github.com/gnab/remark/wiki -->

# Recursion

<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---

class: middle, center

## Knowledge Sharing: _Slido_

---

class: middle

## Agenda

- **Learning Objectives**

- **Recursion: _Implementation_ vs. _Strategy_**

- **Describing Recursive Strategies: _the 5 parts_**

- **Describing Recursive Strategies: _semi-formally_**

- **Visualizing Recursion: _Implementation_ vs. _Strategy_**

- **Code-Along: _understanding recursion_**

- **Code-Along: _using recursion_**

- **Discussion + Q&A**

---

class: middle

## Learning Objectives

- You can distinguish  _recursive calls_ from _recursive strategies_

- You are familiar with the 5 parts of a basic recursive strategy

- You can describe recursion semi-formally in a docstring

- You can use the debugger to visualize a recursive solution's _implementation_

- You can use `@trace_recursion` to visualize a recursive solution's _strategy_

- You can use the 5 parts of recursion to scaffold your own recursive solutions

- For self-study: _[objectives in the README](./README.md#learning-objectives)_

---

class: middle

## Recursion: _Implementation_ vs. _Strategy_

- **Implementing Recursion in Python**

  - A function calls itself from inside the function body

  - Unchecked, this will cause a `RecursioaError`

- **Recursive Problem-Solving Strategy**

  - Breaking a problem into smaller pieces

  - Solving the smallest version of the problem (avoids `RecursionError`)

  - Building the full solution from smaller solutions

---

class: middle, center

## Recursive Implementation

**A function calling itself;  Let's trace this.**

```py
# declare a recursive function
def bottomless():
    
    print('bottomless calling itself')
    bottomless()

    print('this line will never execute!')

# call the recursive function
bottomless()
```

---

class: middle, center

## Recursive Strategy

**Recursively counting items in a list;  Let's trace this.**

_(We'll study this solution in depth today)_

```py
# a recursive strategy for counting the items in a list
def count_items(list_of_things: list) -> int:
    # don't call count_items again (avoid RecursionError)
    if len(list_of_things) == 0: # the smallest problem
      return 0 # counting 0 items in the empty list

    # create a smaller version of the problem (1 item fewer)
    list_without_last_item = list_of_things[:-1]
    # use count_items to solve the smaller problem
    previously_counted = count_items(list_without_last_item)
    # add 1 to the smaller solution because of line 8
    return previously_counted + 1

# use the recursive solution to count items in this list
count_items(['a', 'b', 'c', 'd'])
```

---

class: middle

## Describing Recursive Strategies

Recursion doesn't need to be mysterious or metaphorical!

All basic recursive strategies have these 5 parts.

- **Base Case**: The smallest version of the problem you are solving.

- **Turn-Around**: How you solve the base case.

- **Break-Down**: Create a smaller version of the problem from a bigger version.

- **Recursion**: Calling the function recursively with the smaller problem.

- **Build-Up**: Combining the smaller solution(s) to create a larger solution.

---

class: middle, center

## Describing Recursion: _the 5 parts_

**Labeling the 5 parts will help demystify and understand recursion.**

```py
# a recursive strategy for counting the items in a list
def count_items(list_of_things: list) -> int:
    # base case:  an empty list
    if len(list_of_things) == 0:
      return 0 # turn-around:  an empty list has 0 items

    # break-down:  create an list with 1 fewer items
    list_without_last_item = list_of_things[:-1]
    # recursion:  recursively count items in the smaller list
    previously_counted = count_items(list_without_last_item)
    # build-up:  count the item you removed from the list
    return previously_counted + 1

# use the recursive solution to count items in this list
count_items(['a', 'b', 'c', 'd'])
```

---

class: middle, center

## Describing Recursion: _variables_

**You can even name variables after the 5 parts.**

**This can help you understand solutions in the debugger.**

```py
# a recursive strategy for counting the items in a list
def count_items(list_of_things: list) -> int:
    base_case = len(list_of_things) == 0  # smallest problem
    if base_case:
      turn_around = 0 # solve the smallest problem
      return turn_around

    break_down = list_of_things[:-1] # create a smaller problem
    recursion = count_items(break_down) # solve smaller problem
    build_up = recursion + 1 # build the larger solution 
    return build_up

# use the recursive solution to count items in this list
count_items(['a', 'b', 'c', 'd'])
```

---

class: middle, center

## Describing Recursion: _semi-formally_

_Somewhere between documentation and mathematics:_

```py
# a recursive strategy for counting the items in a list
def count_items(list_of_things: list) -> int:
  """
  Counts the items in a list.

  base case:
    an empty list    ->  0
  recursive case:
    a non-empty list ->  ƒ(the list one item removed) + 1
  """
  if len(list_of_things) == 0: # base case
    return 0 # turn-around
  #         recursion,  break-down, build-up
  return count_items(list_of_things[:-1]) + 1

# use the recursive solution to count items in this list
count_items(['a', 'b', 'c', 'd'])
```

---

class: middle

## Visualizing Recursion

**Visualize Recursive Implementation**

- Step through the solution, visualizing memory and the callstack

- Python Tutor, VSCode Debugger, ...

**Visualizing Recursive Strategies**

- Study an image of how the problem is broken down, solved, then built up
  
- There are web pages and Python packages that generate these images
  - _demo_: [recursionvisualizer.com](https://www.recursionvisualizer.com/?function_definition=%23%20a%20recursive%20strategy%20for%20counting%20the%20items%20in%20a%20list%0Adef%20count_items%28list_of_things%3A%20list%29%20-%3E%20int%3A%0A%20%20%20%20base_case%20%3D%20len%28list_of_things%29%20%3D%3D%200%20%20%23%20smallest%20problem%0A%20%20%20%20if%20base_case%3A%0A%20%20%20%20%20%20turn_around%20%3D%200%20%23%20solve%20the%20smallest%20problem%0A%20%20%20%20%20%20return%20turn_around%0A%0A%20%20%20%20break_down%20%3D%20list_of_things%5B%3A-1%5D%20%23%20create%20a%20smaller%20problem%0A%20%20%20%20recursion%20%3D%20count_items%28break_down%29%20%23%20solve%20smaller%20problem%0A%20%20%20%20build_up%20%3D%20recursion%20%2B%201%20%23%20build%20the%20larger%20solution%20%0A%20%20%20%20return%20build_up%0A&function_call=count_items%28%5B'a'%2C%20'b'%2C%20'c'%2C%20'd'%5D%29)
  - more listed in the README for self-study
  
- We'll use `@trace_recursion` to print recursive strategies to the console

---

class: middle, center

## Visualizing Recursive Strategies (_bonus_)

**Manual replacement - solve it in your head!**

```py
# breaking down & recursing
count_items(['a', 'b', 'c', 'd'])
count_items(['a', 'b', 'c']) + 1
(count_items(['a', 'b']) + 1) + 1
((count_items(['a']) + 1) + 1) + 1
# base case
(((count_items([]) + 1) + 1) + 1) + 1
# turning around
(((0 + 1) + 1) + 1) + 1
# building up
((1 + 1) + 1) + 1
(2 + 1) + 1
3 + 1
4
```

_Can you describe how the 5 parts of recursion are represented here?_

---

class: middle, center

## Code-Along: _understanding recursion_

**`2_visualize_recursion/examples/count_items.py`**

---

class: middle, center

## Code-Along: _using recursion_

### Reversing a list using this template

```py
def reverse_list(to_reverse: list) -> list:
    base_case = _ # must use to_reverse
    if base_case:
        turn_around = _
        return turn_around

    break_down = _ # must use to_reverse
    recursion = reverse_list(break_down)
    build_up = _ # must use recursion
    
    return build_up
```

---

class: middle, center

## Discussion + Q & A

---

class: middle, center

# Thank You

<br />

<img alt="Emerging Talent Logo" src="../.assets/emerging_talent_logo.png" height="50%"  width="50%">

---
