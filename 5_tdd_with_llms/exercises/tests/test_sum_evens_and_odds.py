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

from ..sum_evens_and_odds import sum_even_and_odds


class TestSumEvensAndOdds(unittest.TestCase):
    """Test suite for the sum_even_and_odd_numbers function"""

    # Standard test cases
    def test_mix_1(self):
        """It should sum the evens and odds in [1, 2, 3, 4, 5, 6]"""
        self.assertEqual(
            sum_even_and_odds([1, 2, 3, 4, 5, 6]), {"evens": 12, "odds": 9}
        )

    def test_mix_2(self):
        """It should sum the evens and odds in [7, 6, 5, 4, 3, 2, 1]"""
        self.assertEqual(
            sum_even_and_odds([7, 6, 5, 4, 3, 2, 1]), {"evens": 12, "odds": 16}
        )

    def test_only_odds(self):
        """It should sum the evens and odds in [1, 3, 5, 7, 9]"""
        self.assertEqual(sum_even_and_odds([1, 3, 5, 7, 9]), {"evens": 0, "odds": 25})

    def test_only_evens(self):
        """It should sum the evens and odds in [2, 4, 6, 8, 10]"""
        self.assertEqual(sum_even_and_odds([2, 4, 6, 8, 10]), {"evens": 30, "odds": 0})

    def test_duplicate(self):
        """It should sum the evens and odds in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]"""
        self.assertEqual(
            sum_even_and_odds([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
            {"evens": 12, "odds": 32},
        )

    # Edge test cases
    def test_floats(self):
        """It should sum the evens and odds in [10, -1, 2.5, 3, 0]"""
        self.assertEqual(
            sum_even_and_odds([10, -1, 2.5, 3, 0]), {"evens": 12.5, "odds": 2}
        )

    def test_floats_2(self):
        """It should sum the evens and odds in [12.6, 1, 2.4, 3, 0, 1.5]"""
        self.assertEqual(
            sum_even_and_odds([12.6, 1, 2.4, 3, 0, 1.5]), {"evens": 15.0, "odds": 5.5}
        )

    # Defensive test cases
    def empty_list(self):
        """It should sum the evens and odds in []"""
        self.assertEqual(sum_even_and_odds([]), {"evens": 0, "odds": 0})

    def str_list(self):
        """It should raise a TypeError for [1, 'a', 2, 3]"""
        with self.assertRaises(TypeError):
            sum_even_and_odds([1, "a", 2, 3])
