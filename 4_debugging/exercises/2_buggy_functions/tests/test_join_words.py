#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for join_words function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical word lists with different separators
    - Edge cases: empty lists, single words
    - Defensive tests: invalid inputs, non-string items

Created on 2024-12-06
Author: Claude AI
"""

import unittest

from ..join_words import join_words

class TestJoinWords(unittest.TestCase):
    """Test suite for the join_words function"""

    # Standard test cases
    def test_two_words_space(self):
        """It should join two words with space"""
        self.assertEqual(join_words(['hello', 'world'], ' '), 'hello world')
    
    def test_three_words_comma(self):
        """It should join three words with comma"""
        self.assertEqual(join_words(['a', 'b', 'c'], ','), 'a,b,c')
    
    def test_words_with_dash(self):
        """It should join words with dash"""
        self.assertEqual(
            join_words(['one', 'two', 'three'], '-'),
            'one-two-three'
        )
    
    # Edge cases
    def test_empty_list(self):
        """It should return empty string for empty list"""
        self.assertEqual(join_words([], ','), '')
    
    def test_single_word(self):
        """It should return the word itself for single-item list"""
        self.assertEqual(join_words(['hello'], ','), 'hello')
    
    def test_empty_separator(self):
        """It should join directly when separator is empty string"""
        self.assertEqual(join_words(['a', 'b', 'c'], ''), 'abc')
    
    def test_multi_char_separator(self):
        """It should work with multi-character separators"""
        self.assertEqual(
            join_words(['hello', 'world'], ' :: '),
            'hello :: world'
        )
    
    # Defensive tests
    def test_non_list_input(self):
        """It should raise AssertionError for non-list input"""
        with self.assertRaises(AssertionError):
            join_words("hello", ',')
    
    def test_non_string_separator(self):
        """It should raise AssertionError for non-string separator"""
        with self.assertRaises(AssertionError):
            join_words(['a', 'b'], 123)
    
    def test_non_string_items(self):
        """It should raise AssertionError if list contains non-strings"""
        with self.assertRaises(AssertionError):
            join_words(['hello', 42, 'world'], ' ')

if __name__ == '__main__':
    unittest.main()
