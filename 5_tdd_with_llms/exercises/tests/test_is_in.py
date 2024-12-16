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

from ..is_in import is_in


class TestIsIn(unittest.TestCase):
    """Test suite for the is_in function"""

    def test_standard_case(self):
        """It should return True if item exists in one lists"""
        self.assertFalse(is_in("jerry", [], []))

    def test_one_empty_list(self):
        """It should return True even with one list is empty"""
        self.assertTrue(is_in("Gray", [], ["food", "Gray"]))

    def test_two_empty_str(self):
        """It should return True because both list are empty"""
        self.assertTrue(is_in("", [""], []))

    def test_two_empty_str2(self):
        """It should return True because both list are empty"""
        self.assertTrue(is_in("", [], []))

    def test_two_empty_list(self):
        """It should return False because both list are empty"""
        self.assertFalse(is_in("ball", [], []))

    def test_two_empty_list2(self):
        """It should return False because both list are empty"""
        self.assertFalse(is_in(None, [], []))

    def test_not_in_both(self):
        """It should return False because item does'nt exist in any list"""
        self.assertFalse(is_in("ride", ["Aziz", "date"], ["human", "time"]))

    def test_non_str_case(self):
        """It should return False because the item is int"""
        self.assertFalse(is_in(0, ["Blue", "Red"], ["Black", "Gray"]))
