#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for count_words function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: typical string lists
    - Edge cases: empty strings, equal lengths
    - Defensive tests: invalid inputs

Created on 2024-12-06
Author: Claude AI
"""

import unittest

from ..count_words import count_words

class TestCountWords(unittest.TestCase):
    """Test the count_words function"""
    
    def test_empty_string(self):
        """It should return 0 for empty string"""
        self.assertEqual(count_words(""), 0)
    
    def test_one_word(self):
        """It should count a single word"""
        self.assertEqual(count_words("hello"), 1)
    
    def test_two_words(self):
        """It should count two words"""
        self.assertEqual(count_words("hello world"), 2)
    
    def test_multiple_spaces(self):
        """It should handle multiple spaces between words"""
        self.assertEqual(count_words("hello   world"), 2)
    
    def test_only_spaces(self):
        """It should return 0 for string with only spaces"""
        self.assertEqual(count_words("   "), 0)
