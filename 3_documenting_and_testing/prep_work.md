# Prep Work

Familiarize yourself with these resources for understanding and discussing code quality:

- Read through [Behavior, Strategy, Implementation](./behavior_strategy_implementation.md)
- Read through the [Code Review Checklist](./code_review_checklist.md)

Study and run the [`/examples`](./examples/).  Practice using these _code quality automations_ with `fibonacci_list.py` and `tests/test_fibonacci.py`:

- print the docstring: `$ python -m pydoc path/to/file.py`
- run the doctests: `$ python -m doctest -v path/to/file.py`
- run the unit tests: `$ python -m unittest path/to/tests/test_file.py`
- stepping through unit tests following this process:
  - open `fibonacci_list.py` and `tests/test_fibonacci.py` side-by-side
  - place a breakpoint on the first line of the function
  - open the VSCode debugger pane
  - launch the `ET: Debug Python (unittest)` process

Familiarize yourself these built-in Python tools for documenting and testing:

- [Docstrings](https://peps.python.org/pep-0257/)
- [Doctest](https://docs.python.org/3/library/doctest.html)
- [The `uittest` module](https://docs.python.org/3/library/unittest.html)
