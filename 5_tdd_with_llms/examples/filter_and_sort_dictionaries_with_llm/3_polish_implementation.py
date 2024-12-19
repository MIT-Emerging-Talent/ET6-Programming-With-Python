#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole + Chat GPT
"""

# ----- define function (normally in a separate file) -----


def filter_and_sort_dictionaries(
    list_to_sort: list[dict[str, str]], sort_key: str
) -> list[dict[str, str]]:
    """Filters a list of dicts by key, and alphabetizes the entries by value.

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

    >>> filter_and_sort_dictionaries([{'a':'z'},{'b':'y'},{'a':'x'}], 'a')
    [{'a': 'x'}, {'a': 'z'}]

    >>> filter_and_sort_dictionaries([{'a':'z','b':'j'},{'b':'y'},{'b':'i','a':'x'}], 'b')
    [{'b': 'i', 'a': 'x'}, {'a': 'z', 'b': 'j'}, {'b': 'y'}]

    >>> filter_and_sort_dictionaries([{'a':'z'},{'b':'y'},{'a':'x'}], 'x')
    []
    """
    assert isinstance(list_to_sort, list), "Input must be a list"
    for dictionary in list_to_sort:
        assert isinstance(dictionary, dict), "List elements must be dictionaries"
        for key, value in dictionary.items():
            assert isinstance(key, str), "All keys must be strings"
            assert isinstance(value, str), "All values must be strings"

    # create a new list with the filtered dicts, this will help avoid side effects
    filtered_list = []
    for dictionary in list_to_sort:
        if sort_key in dictionary:
            filtered_list.append(dictionary)

    # sort the filtered dictionaries based on the value stored in the provided key
    sorted_list = sorted(filtered_list, key=lambda dictionary: dictionary[sort_key])

    return sorted_list


# ----- test function (normally in a separate file) -----

import unittest


class TestFilterAndSortDictionaries(unittest.TestCase):
    """A test suite for filtering and sorting a list of dicts"""

    def test_emtpy_list(self):
        """Test case 1: Empty list"""
        list_to_sort = []
        result = filter_and_sort_dictionaries(list_to_sort, "a")
        expected = []
        self.assertEqual(result, expected)

    def test_list_with_one_dictionary(self):
        """Test case 2: List with one dictionary"""
        list_to_sort = [{"a": "z"}]
        result = filter_and_sort_dictionaries(list_to_sort, "a")
        expected = [{"a": "z"}]
        self.assertEqual(result, expected)

    def test_many_dicts_same_key(self):
        """Test case 3: List with multiple dictionaries, all having the same key"""
        list_to_sort = [{"a": "z"}, {"a": "y"}, {"a": "x"}]
        result = filter_and_sort_dictionaries(list_to_sort, "a")
        expected = [{"a": "x"}, {"a": "y"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_many_dicts_some_shared_keys(self):
        """Test case 4: List with multiple dictionaries, some missing the key"""
        list_to_sort = [{"a": "z"}, {"b": "y"}, {"a": "x"}]
        result = filter_and_sort_dictionaries(list_to_sort, "a")
        expected = [{"a": "x"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_many_dicts_no_shared_keys(self):
        """Test case 5: List with dictionaries having different keys"""
        list_to_sort = [{"a": "z"}, {"b": "y"}, {"c": "x"}]
        result = filter_and_sort_dictionaries(list_to_sort, "a")
        expected = [{"a": "z"}]
        self.assertEqual(result, expected)

    def test_dicts_with_non_string_keys(self):
        """Test case 6: List with dictionaries having non-string values for the key"""
        list_to_sort = [{"a": 1}, {"a": True}, {"a": "x"}]
        with self.assertRaises(AssertionError):
            filter_and_sort_dictionaries(list_to_sort, "a")

    def test_dicts_with_other_non_string_keys(self):
        """Test case 7: List of dictionaries with non-string values for other keys"""
        list_to_sort = [{"a": "z"}, {"b": 1}, {"c": True}]
        with self.assertRaises(AssertionError):
            filter_and_sort_dictionaries(list_to_sort, "a")

    def test_list_with_non_dict_elements(self):
        """Test case 8: List with dictionaries having non-dict elements"""
        list_to_sort = [{"a": "z"}, "b", {"a": "x"}]
        with self.assertRaises(AssertionError):
            filter_and_sort_dictionaries(list_to_sort, "a")

    def test_dicts_with_all_different_keys(self):
        """Test case 9: List with dictionaries having different keys and values"""
        list_to_sort = [
            {"a": "z"},
            {"b": "y"},
            {"c": "x"},
            {"a": "w"},
            {"b": "v"},
            {"c": "u"},
        ]
        result = filter_and_sort_dictionaries(list_to_sort, "b")
        expected = [{"b": "v"}, {"b": "y"}]
        self.assertEqual(result, expected)

    def test_dicts_with_same_keys(self):
        """Test case 10: List with dictionaries having duplicate values for the key"""
        list_to_sort = [{"a": "z"}, {"a": "y"}, {"a": "y"}, {"a": "x"}]
        result = filter_and_sort_dictionaries(list_to_sort, "a")
        expected = [{"a": "x"}, {"a": "y"}, {"a": "y"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_dicts_with_many_keys(self):
        """Test case 11: List with dictionaries having duplicate values for the key"""
        list_to_sort = [
            {"a": "z", "b": "hi"},
            {"a": "y", "c": "bonjour"},
            {"a": "y"},
            {"a": "x", "b": "hallo"},
        ]
        result = filter_and_sort_dictionaries(list_to_sort, "b")
        expected = [
            {"a": "x", "b": "hallo"},
            {"a": "z", "b": "hi"},
        ]
        self.assertEqual(result, expected)

    def test_dicts_with_many_long_keys(self):
        """Test case 12: List with dictionaries having duplicate values for the key"""
        list_to_sort = [
            {"alphabet": "z", "bodega": "hi"},
            {"alphabet": "y", "Calliope": "bonjour"},
            {"alphabet": "y", "Calliope": "goede dag"},
            {"alphabet": "x", "bodega": "hallo"},
        ]
        result = filter_and_sort_dictionaries(list_to_sort, "Calliope")
        expected = [
            {"alphabet": "y", "Calliope": "bonjour"},
            {"alphabet": "y", "Calliope": "goede dag"},
        ]
        self.assertEqual(result, expected)

    def test_empty_dictionaries(self):
        """Test case 13: A list with some empty dictionaries"""
        list_to_sort = [
            {"a": "z"},
            {},
            {"a": "y"},
            {"a": "x"},
            {},
        ]
        result = filter_and_sort_dictionaries(list_to_sort, "a")
        expected = [{"a": "x"}, {"a": "y"}, {"a": "z"}]
        self.assertEqual(result, expected)

    def test_does_not_modify_argument_list(self):
        """Test case 14: Function does not modify the list argument"""
        lst = [{"a": "x"}, {"a": "y"}, {"a": "z"}]
        filter_and_sort_dictionaries(lst, "a")
        self.assertEqual(lst, [{"a": "x"}, {"a": "y"}, {"a": "z"}])


if __name__ == "__main__":
    unittest.main()
