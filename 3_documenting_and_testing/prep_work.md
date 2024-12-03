# Prep Work

Familiarize yourself these built-in Python tools for documenting and testing:

- [Docstrings](https://peps.python.org/pep-0257/)
- [Doctest](https://docs.python.org/3/library/doctest.html)
- [The `uittest` module](https://docs.python.org/3/library/unittest.html)

Familiarize yourself with these resources for understanding and discussing code quality:

- Read through [Behavior, Strategy, Implementation](./behavior_strategy_implementation.md)
- Read through the [Code Review Checklist](./code_review_checklist.md)
- Study and run the [`/examples`](./examples/).  Practice using these commands with `fibonacci_list.py` and `tests/test_fibonacci.py`:
  - print the docstring: `$ python -m pydoc path/to/file.py`
  - run the doctests: `$ python -m doctest -v path/to/file.py`
  - run the tests using `$ python -m unittest path/to/tests/test_file.py`
