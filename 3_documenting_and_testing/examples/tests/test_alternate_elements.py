#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for alternate_elements function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2024-12-06
Author: Claude AI
"""

import unittest
from ..alternate_elements import alternate_elements

class TestAlternateElements(unittest.TestCase):
    """Test suite for the alternate_elements function - contains buggy tests!"""

    # Standard test cases
    def test_five_numbers(self):
        """It should return every other number from a list of five"""
        self.assertEqual(alternate_elements([1, 2, 3, 4, 5]), [1, 3, 5])
    
    def test_four_numbers(self):
        """It should return every other number from a list of four"""
        self.assertEqual(alternate_elements([1, 2, 3, 4]), [1, 3])
    
    def test_strings(self):
        """It should work with strings"""
        self.assertEqual(alternate_elements(['a', 'b', 'c', 'd']), ['a', 'c'])
    
    # Edge cases
    def test_empty_list(self):
        """It should return empty list for empty input"""
        self.assertEqual(alternate_elements([]), [])
    
    def test_single_element(self):
        """It should return single element list for single element input"""
        self.assertEqual(alternate_elements([1]), [1])
    
    def test_two_elements(self):
        """It should return first element for two element input"""
        self.assertEqual(alternate_elements([1, 2]), [1])
    
    # Defensive tests
    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            alternate_elements(None)

if __name__ == '__main__':
    unittest.main()
