#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..check_palindrome import check_palindrome


class TestCheckPalindrome(unittest.TestCase):
    """it is a palindrome if it reads the same forwards and backwards"""

    def test_empty_string(self):
        """It should return an empty string."""
        self.assertTrue(check_palindrome(""), "")

    def test_single_character(self):
        """It should return a single character."""
        self.assertTrue(check_palindrome("a"), "a")

    def test_palindrome_even_length(self):
        """It should return a palindrome with an even length."""
        self.assertTrue(check_palindrome("abba"), "abba")

    def test_palindrome_odd_length(self):
        """It should return a palindrome with an odd length."""
        self.assertTrue(check_palindrome("madam"), "madam")

    def test_not_a_palindrome(self):
        """It should return a string that is not a palindrome."""
        self.assertFalse(check_palindrome("hello"), "olleh")
