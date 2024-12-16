#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_both function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2024-12-06
Author: Aziz & phind AI
"""

import unittest

from ..is_in_both import is_in_both


class TestIsInBoth(unittest.TestCase):
    """Test suite for the is_in_both function"""

    def test_standard_case(self):
        """It should return True if item exists in both lists"""
        self.assertTrue(is_in_both("date", ["Aziz", "date"], ["cool", "date"]))

    def test_standard2_case(self):
        """It should return True if item exists in both lists"""
        self.assertTrue(
            is_in_both(
                "MIT", ["MIT", "best", "University"], ["study", "MIT", "student"]
            )
        )

    def test_single_case(self):
        """It should return false because item exist in one list"""
        self.assertFalse(is_in_both("Aziz", ["Aziz", "date"], ["human", "time"]))

    def test_non_str_case(self):
        """It should return False because the item is int"""
        self.assertFalse(is_in_both(4, ["Blue", "Red"], ["Black", "Gray"]))

    def test_one_empty_list(self):
        """It should return False because one list is empty"""
        self.assertFalse(is_in_both("cool", [], ["cool", "date"]))

    def test_two_empty_list(self):
        """It should return False because one list is empty"""
        self.assertFalse(is_in_both("cool", [], []))

    def test_item_not_in_list(self):
        """It should return False because item is not in both list list"""
        self.assertFalse(is_in_both("cool", ["batman", "flash"], ["x-men", "hulk"]))
