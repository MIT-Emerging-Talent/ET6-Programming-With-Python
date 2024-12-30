"""This function filters a list of dicts by key, and alphabetizes the entries by value.

This function does not modify the argument list.

Parameters:
  list[dict[str, str]]: an list of dicts with string keys and string values
  str: the function will remove all dicts that don't have this key

Returns: a list of dicts where each dict contains the given key,
  and the dicts are sorted alphabetically by the value stored in the given key

Raises: AssertionError
  if the argument is not a list
  if each item is not a dict
  if any key in any dict is not a string
  if any value in any dict is not a string

>>> f([{'a':'z'},{'b':'y'},{'a':'x'}], 'a')
[{'a':'x'},{'a','z'}]


>>> f([{'a':'z','b':'j'},{'b':'y'},{'b':'i',a':'x'}], 'b')
[{'b':'i',a':'x'},{'a':'z','b':'j'},{'b':'y'}]

"""
