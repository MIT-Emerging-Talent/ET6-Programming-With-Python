# Code Review Checklist

Writing a good function involves a lot of detail, way too much to remember right
away! This checklist can help you review your own or your classmates' code until
the details become a habit.

## File Names

- [ ] The file names match the function
- [ ] Test file is named `/tests/test_file_name.py`

## Files

- [ ] The file names match the function
- [ ] Module header in each file
- [ ] Module docstring in each file

## Unit Tests

- [ ] The test class has a helpful name in PascalCase
- [ ] The test class has a docstring
- Each unit test has
  - [ ] A helpful name
  - [ ] A clear docstring
  - [ ] Only one assertion
  - [ ] There is no logic in the unit test
- [ ] All tests pass
- [ ] (challenge) Tests for defensive assertions
- [ ] (challenge) Tests for many boundary cases

## Function Docstring

- [ ] behavior description
- [ ] parameter description
- [ ] return value description
- [ ] include any assumptions
- [ ] include 3 or more (passing!) doctests
- [ ] assertions are documented (if there are any)
- [ ] include 1-2 use cases (if necessary)

## Function Implementation

- [ ] The code is auto-formatted
- [ ] The code has no (reasonable) linting mistakes
- [ ] Variables are named with snake_case
- [ ] The function has a clear and helpful name
- [ ] The file's name matches the function name
- [ ] The code follows the strategy as simply as possible
- [ ] Variable names are clear and helpful
- [ ] Comments explain the strategy (if necessary)
- [ ] There are type annotations
- [ ] (challenge) The code includes defensive assertions
