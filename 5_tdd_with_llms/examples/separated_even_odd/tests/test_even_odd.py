#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole + Chat GPT
"""

import unittest

from ..even_odd import even_odd


class TestEvenOdd(unittest.TestCase):
    """
    This class contains unit tests for the even_odd function.
    The function takes a list of integers and separates them into a dictionary
    of two lists: one list contains all evens and the other list contains all odds.
    """

    def test_even_odd_with_mixed_numbers(self):
        """
        Tests the function with a list of mixed numbers.
        Expected result is a dictionary with two lists:
            one with even numbers and one with odd numbers.
        """
        self.assertEqual(even_odd([1, 2, 3]), {"even": [2], "odd": [1, 3]})

    def test_even_odd_with_all_odd_numbers(self):
        """
        Tests the function with a list of all odd numbers.
        Expected result is a dictionary with two lists:
            one empty and one with all the numbers.
        """
        self.assertEqual(even_odd([1, 3, 5]), {"even": [], "odd": [1, 3, 5]})

    def test_even_odd_with_empty_list(self):
        """
        Tests the function with an empty list.
        Expected result is a dictionary with two empty lists.
        """
        self.assertEqual(even_odd([]), {"even": [], "odd": []})

    def test_even_odd_with_negative_and_positive_numbers(self):
        """
        Tests the function with a list of negative numbers.
        Expected result is a dictionary with two lists:
            one with even numbers and one with odd numbers.
        """
        self.assertEqual(even_odd([-2, -4, 3, 0]), {"even": [-2, -4, 0], "odd": [3]})

    def test_even_odd_with_duplicate_numbers(self):
        """
        Tests the function with a list of duplicate numbers.
        Expected result is a dictionary with two lists:
            one with even numbers and one with odd numbers.
        """
        self.assertEqual(even_odd([1, 1, 4, 2, 5]), {"even": [4, 2], "odd": [1, 1, 5]})

    def test_even_odd_with_all_even_numbers(self):
        """
        Tests the function with a list of all even numbers.
        Expected result is a dictionary with two lists:
            one with all the numbers and one empty.
        """
        self.assertEqual(even_odd([2, 4, 8]), {"even": [2, 4, 8], "odd": []})

    def test_even_odd_with_all_negative_numbers(self):
        """
        Tests the function with a list of all negative numbers.
        Expected result is a dictionary with two lists:
            one empty and one with all the numbers.
        """
        self.assertEqual(even_odd([-1, -3, -5]), {"even": [], "odd": [-1, -3, -5]})

    def test_even_odd_with_non_list_argument(self):
        """
        Tests the function with a non-list argument.
        Expected result is an AssertionError.
        """
        with self.assertRaises(AssertionError):
            even_odd("not a list")

    def test_even_odd_with_non_integer_list_argument(self):
        """
        Tests the function with a list containing non-integer values.
        Expected result is an AssertionError.
        """
        with self.assertRaises(AssertionError):
            even_odd([1, "two", 3])


if __name__ == "__main__":
    unittest.main()
