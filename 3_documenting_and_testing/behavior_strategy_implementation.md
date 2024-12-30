# Behavior, Strategy, Implementation

3 different ways to understand the same function.

## Behavior

What does the function do? What are it’s arguments and it’s return value? How
could you use it in a program? Behavior is all about what your function looks
like "from the outside", without caring about what is written inside the body.

Functions behavior is generally described using **documentation**, **unit
tests** and **use cases**, here are examples describing the behavior of a
`fibonnaci_list` function:

<details>
<summary><strong>Documentation (docstring comment)</strong></summary>

```python
"""generates a list containing the first n numbers of the fibonacci sequence

Parameters:
  n: int, greater than or equal to zero

Returns -> list[int] with the first n numbers of the fibonacci sequence

>>> fib_list(0)
[]

>>> fib_list(4)
[0, 1, 1, 2]

>>> fib_list(8)
[0, 1, 1, 2, 3, 5, 8, 13]
"""
```

</details>

<details>
<summary><strong>Black Box Unit Tests (pass/fail assertions)</strong></summary>

```python
import unittest

from ..fib_list import fib_list


class TestFibLib(unittest.TestCase):
    """Test the fib_lib function"""

    def test_0(self):
        """It should evaluate 0 to []"""
        self.assertEqual(fib_list(0), [])

    def test_1(self):
        """It should evaluate 1 to [0]"""
        self.assertEqual(fib_list(1), [0])

    def test_2(self):
        """It should evaluate 2 to [0, 1]"""
        self.assertEqual(fib_list(2), [0, 1])

    def test_3(self):
        """It should evaluate 3 to [0, 1, 1]"""
        self.assertEqual(fib_list(3), [0, 1, 1])

    def test_4(self):
        """It should evaluate 4 to [0, 1, 1, 2]"""
        self.assertEqual(fib_list(4), [0, 1, 1, 2])

    def test_5(self):
        """It should evaluate 5 to [0, 1, 1, 2, 3]"""
        self.assertEqual(fib_list(5), [0, 1, 1, 2, 3])

    def test_9(self):
        """It should evaluate 9 to [0, 1, 1, 2, 3, 5, 8, 13, 21]"""
        self.assertEqual(fib_list(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])

```

</details>

<details>
<summary><strong>Use Cases ("real-world" examples)</strong></summary>
<br>

It can be difficult to come up with use cases for mathematical functions like
Fibonacci lists, so it's ok for these exercises to just play around with some
examples and explore the output. Use cases will be more intuitive later when you
are writing code for a larger project.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A file for experimenting with different fibonacci_list use cases
"""

from fibonacci_list import fibonacci_list

# %% what about big numbers?

print(fibonacci_list(150))

# %% is it really a Fibonacci sequence?

huge_list = fibonacci_list(500)

for index in range(2, 500):
    two_back = huge_list[index - 2]
    one_back = huge_list[index - 1]
    current = huge_list[index]

    assert two_back + one_back == current, f"entry {index} is not correct"

# %% does the function return the same or different lists?

list_1 = fibonacci_list(4)
list_2 = fibonacci_list(6)

# the function returned two different lists with the same values
assert list_1 == list_2, "the lists store the same values"
assert list_1 is not list_2, "the variables do not reference the same list"
```

</details>

---

## Strategy

How do you approach solving the problem? There are many strategies to solve the
same problem! A way to practice strategy is to think of transforming the
arguments to the return value in small steps, _focusing on the data not the
code_. This is the realm of flow charts, diagrams, and pseudo-code.

One way to approach strategy is to solve the problem a few different ways by
hand, writing what you expect to change in memory at each step. Like if you were
the debugger and you couldn't see the source code. Using a pencil and paper is a
the best way to go, pick a few test cases and see how you'd solve them manually.

There are many strategies for solving the same problem, the best strategy will
depend on your situation. Sometimes you should think about things like speed or
memory usage, but almost always the most important considerations are
_simplicity_ and _readability_. You should try to find the most obvious and
simple strategy so other people can more easily understand your code.

Below are some discussion questions and a few example strategies for creating a
list of Fibonacci numbers:

- Is one strategy easier to understand?
- How would you make a flowchart for each strategy?
- Which strategy do you prefer and why?
- Can you think of a strategy that is not listed below?

<details>
<summary><strong>Recursively calculate the previous list, then calculate the new last value.</strong></summary>

```txt
fibonnaci_list(int) -> list of ints
    if int is 0
        return []
    if int is 1
        return [0]
    if int is 2
        return [0, 1]

    recursively calculate the list for (int - 1)
    sum the two last values in the list
    append the sum to the list
    return the list
```

</details>

<details>
<summary><strong>Recursively calculate the previous list, then calculate the new last value. Memoize the solution for reuse.</strong></summary>

```txt
fibonnaci_list(int, dict of solutions) -> list of ints
    if int is in the dict of solutions
      return the solution

    if int is 0
        return []
    if int is 1
        return [0]
    if int is 2
        return [0, 1]

    recursively calculate the list for (int - 1)
    sum the two last values in the list
    append the sum to the list

    add the solution to your dict for reuse
    return the list
```

</details>

<details>
<summary><strong>Iterate until the list is long enough.</strong></summary>

```txt
fibonnaci_list(int) -> list of ints
    if int is zero
        return an empty list
    if int is one
        return [0]

    list = [0,1]
    while list is shorter than int
        add the last two numbers in the list
        append the sum to the end of the list

    return the list
```

</details>

<details>
<summary><strong>Iterate from 0 to the number, calculating the Fibonacci value from previous values</strong></summary>
<br>

```txt
fibonnaci_list(int) -> list of ints
    if int is 0
      return []
    if int is 1
      return [0]

    list = [0, 1]
    for number in range 2 ... int
      sum the previous two values
      append the new value to the list

    return the list
```

</details>

<details>
<summary><strong>Iterate from 0 to the number, calculating each Fibonacci value using a helper function</strong></summary>
<br>

This is one strategy where you should consider speed. Why is this strategy
incredibly slow?

```txt
fibonnaci_list(int) -> list of ints
    list = []
    for number in range 0 ... int
      use a helper function to calculate the next number
      append the next number to the list

    return the list
```

</details>

---

## Implementation

Which language features and which lines of code did you use to program your
strategy? There are many ways to implement the same strategy, and no single
right answer! A good implementation should be simple and clear, and help readers
understand your strategy by using helpful white space, variable names and
comments (when necessary).

Below are 2-3 different implementations of each strategy described above, and
some discussion questions:

- Which implementation(s) do you think are the easiest to understand?
- Do you think more comments are helpful or distracting?
- Do you think long variables names are more helpful or distracting?
- Which implementation do you think is better, and why?
- When is `else` used, and when is it not used? Which way do you prefer?
- How would you change the code to it more understandable?

<details>
<summary><strong>Recursively calculate the previous list, then calculate the new last value.</strong></summary>

```python
def fibonnaci_list(n: int) -> list[int]:
    # return a hard-coded value if n is too small
    if n is 0:
        return []
    if n is 1:
        return [0]
    if n is 2:
        return [0, 1]
    else:
      # make the right answer and return it
      list = fibonnaci_list(n - 1)
      list.append(list[-1] + list[-2])
      return list
```

---

```python
def fibonnaci_list(length: int) -> list[int]:
    # these are all too short for recursion
    if length == 0:
        return []

    if length == 1:
        return [0]

    if length == 2:
        return [0, 1]

    # calculate the previous list
    sequence = fibonnaci_list(length - 1)
    # calculate and append the next value
    new_value = sequence[-1] + sequence[-2]
    sequence.append(new_value)

    return sequence
```

---

</details>

<details>
<summary><strong>Recursively calculate the previous list, then calculate the new last value. Memoize the solution for reuse.</strong></summary>

```python
def fibonnaci_list(n: int, memo: dict = {}) -> list[int]:
    if n in memo:
        return memo[n]

    list = []

    # return a hard-coded value if n is too small
    if n is 0:
        pass
    elif n is 1:
        list = [0]
    elif n is 2:
        list = [0,1]
    else:
        # make the right answer
        list = fibonnaci_list(n - 1)
        list.append(list[-1] + list[-2])

    # save the answer for later and return it
    memo[n] = list
    return list
```

---

```python
def fibonnaci_list(length: int, previous_answers: dict = {}) -> list[int]:
    # these are all too short for recursion
    if length == 0:
        return []

    elif length == 1:
        return [0]

    elif length == 2:
        return [0, 1]

    # because the same argument will always have the same answer
    elif length in previous_answers:
        return previous_answers[length]

    # calculate the previous list
    sequence = fibonnaci_list(length - 1)
    # calculate and append the next value
    new_value = sequence[-1] + sequence[-2]

    sequence.append(new_value)
    previous_answers[length] = sequence

    return sequence
```

---

</details>

<details>
<summary><strong>Iterate until the list is long enough.</strong></summary>

```python
def fibonnaci_list(n: int) -> list[int]:
    # too short for iteration
    if n == 0:
        return []
    if n == 1:
        return [0]

    list = [0,1]
    while n > len(list) :
        # f(n) = f(n-1) + f(n-2)
        next = list[-1] + list[-2]
        list.append(next)

    return list
```

---

```python
def fibonnaci_list(max: int) -> list[int]:
    if max == 0:
        return []
    if max == 1:
        return [0]

    # you need at least 2 values to add together
    fib_list = [0,1]

    # stop when your list is as long as the `max` argument
    while len(fib_list) < max:
        # add the previous two values to calculate the next
        next_number = fib_list[-1] + fib_list[-2]
        fib_list.append(next_number)

    return fib_list
```

---

</details>

<details>
<summary><strong>Iterate from 0 to the number, calculating the Fibonacci value from previous values</strong></summary>
<br>

```python
def fibonacci_list(how_many: int) -> list[int]:
    # two base cases
    if how_many == 0:
        return []
    if how_many == 1:
        return [0]

    all_of_them = [0, 1]
    # use iterator to count, ignore its value
    # the loop body will not execute if how_many is 2
    for _ in range(2, how_many):
        # add previous two values from the list
        next_one = all_of_them[-1] + all_of_them[-2]
        # append the new value to the list
        all_of_them.append(next_one)

    return all_of_them
```

---

```python
def fibonacci_list(n: int) -> list[int]:
    if n is 1:
        return [0]
    elif n is 0:
        return []
    else:
        f_l = [0, 1]
        for i in range(2, n):
            f_l.append(f_l[i - 1] + f_l[i - 2])
        return f_l
```

</details>

<details>
<summary><strong>Iterate from 0 to the number, calculating the Fibonacci value using a helper function</strong></summary>
<br>

Which solution do you think is easier to read?

Which solution will be faster if you use it many times?

```python
def fibonacci(n: int) -> int:
    """fib(n) =
    if n is 0 -> 0
    if n is 1 -> 1
    else -> fib(n-1) + fib(n - 2)
    """
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_list(max: int) -> list[int]:
    all = []

    for _ in range(0, max):
        all.append(fibonacci(len(all)))

    return all
```

---

```python
def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci_list(length: int) -> list[int]:
    fib_sequence = []

    for index in range(0, length):
        next_value = fib(index)
        fib_sequence.append(next_value)

    return fib_sequence
```

---

```python
def fibonacci(num: int, cache: dict = {}) -> int:
    if num in cache:
        return cache[num]

    fib_num = num
    if num >= 2:
        fib_num = fibonacci(num - 1) + fibonacci(num - 2)

    cache[num] = fib_num
    return fib_num


def fibonacci_list(number_of_numbers: int) -> list[int]:
    sequence = []

    for i in range(0, number_of_numbers):
        sequence.append(fibonacci(i))

    return sequence

```

---

</details>
