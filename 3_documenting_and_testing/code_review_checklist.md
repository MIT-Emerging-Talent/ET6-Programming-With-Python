# Code Review Checklist

Writing a good function involves a lot of detail, way too much to remember right
away! This checklist can help you review your own or your classmates' code until
the details become a habit.

## Behavior

### Files

- [ ] The file name describes the function's behavior
- [ ] There is a module docstring in the function file
- [ ] The test file's name matches the function file name -
  `/tests/test_file_name.py`
- [ ] There is a module docstring in the tests file

### Unit Tests

- [ ] The test class has a helpful name in PascalCase
- [ ] The test class has a docstring
- Every unit test has
  - [ ] A helpful name
  - [ ] A clear docstring
  - [ ] Only one assertion
  - [ ] There is no logic in the unit test
- [ ] All tests pass
- [ ] There are tests for defensive assertions
- [ ] There are tests for boundary cases

### Function Docstring

- [ ] The function's behavior is described
- The function's arguments are described:
  - [ ] Type
  - [ ] Purpose
  - [ ] Other assumptions (eg. if it's a number, what's the expected range?)
- The return value is described
  - [ ] Type
  - [ ] Other assumptions are documented
- The defensive assertions are documented using `Raises:`
  - [ ] Each assumption about an argument is checked with an assertion
  - [ ] Each assertion checks for _only one_ assumption about the argument
- [ ] Include 3 or more (passing!) doctests

### The Function

- [ ] The function's name describes it's behavior
- [ ] The function's name matches the file name
  - _It's ok to have extra helper functions if necessary, like with mergesort_
- [ ] The function has correct type annotations
- [ ] The function is not called at the top level of the function file
  - _Recursive solutions **can** call the function from **inside** the function body_

## Strategy

### Do's

- [ ] Variable names help to understand the strategy
- [ ] Any comments are clear and describe the strategy
- [ ] Lines of code are spaced to help show different stages of the strategy

### Don'ts

- [ ] The function's strategy _is not_ described in any docstrings or tests
- [ ] Comments explain the _strategy_, **not** the _implementation_
- [ ] The function _does not_ have more comments than code
  - If it does, consider finding a new strategy or a simpler implementation

## Implementation

- [ ] The code passes the formatting checks
- [ ] The code passes all Ruff linting checks
- [ ] The code has no (reasonable) Pylint errors
  - In code review, you can decide when fixing a Pylint error is helpful and
    when it's too restricting.
- [ ] Variables are named with snake_case
- [ ] Variable names are clear and helpful
- [ ] The code follows the strategy as simply as possible
- [ ] The implementation is as simple as possible given the strategy
- [ ] There are no commented lines of code
- [ ] There are no `print` statements anywhere
- [ ] The code includes defensive assertions
- [ ] Defensive assertions include as little logic as possible
