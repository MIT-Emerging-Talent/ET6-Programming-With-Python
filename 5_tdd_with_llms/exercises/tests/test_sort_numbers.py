#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_one function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2024-12-06
Author: Aziz & phind AI
"""

import unittest

from ..sort_numbers import sort_numbers


class TestRepeatCharacter(unittest.TestCase):
    """Test suite for the sort_numbers function"""

    # Standard test cases
    def test_sort_numbers(self):
        """It should sort the numbers in ascending order"""
        self.assertEqual(sort_numbers([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sort_numbers2(self):
        """It should sort the numbers in ascending order"""
        self.assertEqual(
            sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
            [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
        )

    # Edge test cases
    def test_float_negative_numbers(self):
        """It should sort the numbers in ascending order"""
        self.assertEqual(sort_numbers([10, -1, 2.5, 3, 0]), [-1, 0, 2.5, 3, 10])

    # Defensive test cases
    def test_sort_numbers4(self):
        """It should sort the numbers in ascending order"""
        self.assertEqual(sort_numbers([]), [])

    def test_sort_non_numeric_values(self):
        """It should raise a TypeError when the list contains strings"""
        with self.assertRaises(TypeError):
            sort_numbers([1, "a", 3])
