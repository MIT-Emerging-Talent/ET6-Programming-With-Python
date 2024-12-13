#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for count_between function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical number lists and ranges
    - Edge cases: empty lists, equal bounds, non-integer numbers
    - Defensive tests: invalid inputs, assertions

Created on 2024-12-06
Author: Claude AI
"""

import unittest

from ..count_between import count_between


class TestCountBetween(unittest.TestCase):
    """Test suite for the count_between function - contains buggy tests!"""

    # Standard test cases
    def test_simple_range(self):
        """It should count numbers in a simple range"""
        self.assertEqual(count_between([1, 2, 3, 4, 5], 2, 4), 3)

    def test_no_matches(self):
        """It should return 0 when no numbers in range"""
        self.assertEqual(count_between([1, 2, 3], 4, 6), 0)

    def test_all_match(self):
        """It should count all numbers when all in range"""
        self.assertEqual(count_between([2, 3, 4], 1, 3), 2)

    # Edge cases
    def test_empty_list(self):
        """It should return 0 for empty list"""
        self.assertEqual(count_between([], 1, 10), 0)

    def test_equal_bounds(self):
        """It should work when lower and upper bounds are equal"""
        self.assertEqual(count_between([1, 2, 3, 2, 1], 2, 2), 2)

    def test_float_numbers(self):
        """It should work with float numbers in list"""
        self.assertEqual(count_between([1.5, 2.0, 2.5, 3.0], 2, 3), 3)

    # Defensive tests
    def test_invalid_bounds(self):
        """It should raise AssertionError if bounds aren't integers"""
        with self.assertRaises(AssertionError):
            count_between([1, 2, 3], 1.5, 3)

    def test_reversed_bounds(self):
        """It should work with reversed bounds"""
        self.assertEqual(count_between([1, 2, 3, 4, 5], 4, 2), 0)


if __name__ == "__main__":
    unittest.main()
