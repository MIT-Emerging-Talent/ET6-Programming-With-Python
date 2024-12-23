#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on 23 12 2024

@author: Evan Cole
@editor: Heba
"""
import unittest

from ..sort_list import sort_list


class TestMystery5(unittest.TestCase):
    """Test the sort_list function"""

    def test_two_lists(self):
        """it should give [1, 9, 0, 1, 4, 5] sort the first list and append it to the other"""
        self.assertEqual(sort_list([4, 5, 1, 0], [1, 9]), [1, 9, 0, 1, 4, 5])

    def test_minimal_input(self):
        """it should give []"""
        self.assertEqual(sort_list([], []), [])

    def test_minimal_input_none(self):
        """it should give []"""
        self.assertEqual(sort_list([], None), [])

    def test_minimal_input_default_arguments(self):
        """it should give []"""
        self.assertEqual(sort_list([]), [])

    def test_letters(self):
        """it should give []"""
        self.assertEqual(sort_list(["n", "a", "m", "e"]), ["a", "e", "m", "n"])

    def test_sort_alphabetically(self):
        """it should give []"""
        self.assertEqual(
            sort_list(["one", "apple", "", "123", "heba"]),
            ["", "123", "apple", "heba", "one"],
        )

    def test_special_characters(self):
        """it should give []"""
        actual = sort_list([" ", "", "a", "1", "!", "/", "_", "...etc", "aa", "bb"], [])
        expexted = ["", " ", "!", "...etc", "/", "1", "_", "a", "aa", "bb"]
        self.assertEqual(actual, expexted)

    def test_mixed_nums_letters(self):
        """it should give []"""
        actual = sort_list(["1a", "b2", "a1", "2b"], [])
        expexted = ["1a", "2b", "a1", "b2"]
        self.assertEqual(actual, expexted)

    def test_upper_and_lower(self):
        """it should give []"""
        actual = sort_list(["B", "a", "b", "A", "ba", "BA"], [])
        expexted = ["A", "B", "BA", "a", "b", "ba"]
        self.assertEqual(actual, expexted)
