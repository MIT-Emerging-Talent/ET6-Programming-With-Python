#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for remove_spaces function.
Contains intentionally buggy tests for debugging practice.

Test categories:
    - Standard cases: typical inputs with spaces
    - Edge cases: empty strings, only spaces, special characters
    - Defensive tests: wrong input types, assertions

Created on 2024-12-06
Author: Claude AI
"""

import unittest
from ..remove_spaces import remove_spaces


class TestRemoveSpaces(unittest.TestCase):
    """Test suite for the remove_spaces function - contains buggy tests!"""

    # Standard test cases
    def test_single_word(self):
        """It should return the same string if no spaces present"""
        self.assertEqual(remove_spaces("hello"), "hello")

    def test_two_words(self):
        """It should remove a single space between words"""
        self.assertEqual(remove_spaces("hello world"), "helloworld")

    def test_multiple_words(self):
        """It should remove all spaces between multiple words"""
        self.assertEqual(remove_spaces("the quick brown fox"), "thequickbrownfox")

    # Edge cases
    def test_empty_string(self):
        """It should handle empty strings"""
        self.assertEqual(remove_spaces(""), "")  # Fixing test to use empty string

    def test_only_spaces(self):
        """It should handle strings containing only spaces"""
        self.assertEqual(remove_spaces("   "), "")  # Correct behavior for spaces only

    def test_spaces_at_ends(self):
        """It should remove spaces at start and end of string"""
        self.assertEqual(remove_spaces("  hello  "), "hello")

    def test_special_characters(self):
        """It should preserve all non-space characters"""
        self.assertEqual(remove_spaces("hello, world!"), "hello,world!")

    def test_numbers_and_symbols(self):
        """It should handle strings with numbers and symbols"""
        self.assertEqual(remove_spaces("123 + 456"), "123+456")

    # Defensive tests
    def test_non_string_input(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            remove_spaces(123)

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            remove_spaces(None)

    def test_list_input(self):
        """It should raise AssertionError for list input"""
        with self.assertRaises(AssertionError):
            remove_spaces(["hello", "world"])  # Correct test behavior


if __name__ == "__main__":
    unittest.main()
