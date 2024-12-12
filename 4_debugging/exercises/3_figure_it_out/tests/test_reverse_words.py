#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for reverse_words function.
Contains correct tests to help identify bugs in the implementation.
    careful! these tests may have bugs too.

Test categories:
    - Standard cases: typical string lists
    - Edge cases: empty strings, equal lengths
    - Defensive tests: invalid inputs

Created on 2024-12-06
Author: Claude AI
"""

import unittest

from ..reverse_words import reverse_words

class TestReverseWords(unittest.TestCase):
    """Test the reverse_words function"""
    
    def test_empty_string(self):
        """It should return empty string for empty input"""
        self.assertEqual(reverse_words(""), "") # probably ok
    
    def test_one_word(self):
        """It should return the same string for one word"""
        self.assertEqual(reverse_words("hello"), "hello") # probably ok
    
    def test_two_words(self):
        """It should reverse two words"""
        self.assertEqual(reverse_words("hello world"), "world hello") # probably ok
    
    def test_two_spaces(self):
        """It should handle two spaces"""
        self.assertEqual(reverse_words("hello  world"), "world  hello") # probably ok

    def test_three_spaces(self):
        """It should handle three spaces"""
        self.assertEqual(reverse_words("hello   world"), "world   hello") # probably ok
    
    # write more tests!
