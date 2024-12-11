#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for find_longest function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical string lists
    - Edge cases: empty strings, equal lengths
    - Defensive tests: invalid inputs

Created on 2024-12-06
Author: Claude AI
"""

import unittest

from ..find_longest import find_longest

class TestFindLongest(unittest.TestCase):
    """Test suite for the find_longest function"""

    # Standard test cases
    def test_increasing_lengths(self):
        """It should find longest in increasing lengths"""
        self.assertEqual(find_longest(['a', 'bb', 'ccc']), 'ccc')
    
    def test_decreasing_lengths(self):
        """It should find longest in decreasing lengths"""
        self.assertEqual(find_longest(['ccc', 'bb', 'a']), 'ccc')
    
    def test_mixed_lengths(self):
        """It should find longest in mixed lengths"""
        self.assertEqual(
            find_longest(['hi', 'hello', 'hey', 'howdy']),
            'hello'
        )
    
    # Edge cases
    def test_empty_string_first(self):
        """It should handle empty string at start"""
        self.assertEqual(find_longest(['', 'a', 'bb']), 'bb')
    
    def test_empty_string_middle(self):
        """It should handle empty string in middle"""
        self.assertEqual(find_longest(['a', '', 'bb']), 'bb')
    
    def test_all_empty(self):
        """It should handle all empty strings"""
        self.assertEqual(find_longest(['', '', '']), '')
    
    def test_equal_lengths(self):
        """It should return first string when multiple are longest"""
        self.assertEqual(find_longest(['abc', 'def', 'ghi']), 'abc')
    
    # Defensive tests
    def test_empty_list(self):
        """It should raise ValueError for empty list"""
        with self.assertRaises(ValueError):
            find_longest([])
    
    def test_non_list_input(self):
        """It should raise AssertionError for non-list input"""
        with self.assertRaises(AssertionError):
            find_longest("hello")
    
    def test_non_string_items(self):
        """It should raise AssertionError if list contains non-strings"""
        with self.assertRaises(AssertionError):
            find_longest(['hello', 42, 'world'])

if __name__ == '__main__':
    unittest.main()
