# Code Review Checklist

Writing a good function involves a lot of detail, way too much to remember right
away! This checklist can help you review your own or your classmates' code until
the details become a habit.

## File Names

- [x] The file names match the function
- [x] Test file is named `/tests/test_file_name.py`

## Files

- [x] The file names match the function
- [x] Module header in each file
- [x] Module docstring in each file

## Unit Tests

- [x] The test class has a helpful name in PascalCase
- [x] The test class has a docstring
- Each unit test has
  - [x] A helpful name
  - [x] A clear docstring
  - [x] Only one assertion
  - [x] There is no logic in the unit test
- [x] All tests pass
- [x] (challenge) Tests for defensive assertions
- [x] (challenge) Tests for many boundary cases

## Function Docstring

- [x] behavior description
- [x] parameter description
- [x] return value description
- [x] include any assumptions
- [x] include 3 or more (passing!) doctests
- [x] include 1-2 use cases (if necessary)
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
