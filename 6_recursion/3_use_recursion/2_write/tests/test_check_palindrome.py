#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..check_palindrome import check_palindrome


class TestCheckPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(check_palindrome(""))

    def test_single_character(self):
        self.assertTrue(check_palindrome("a"))

    def test_palindrome_even_length(self):
        self.assertTrue(check_palindrome("abba"))

    def test_palindrome_odd_length(self):
        self.assertTrue(check_palindrome("madam"))

    def test_not_a_palindrome(self):
        self.assertFalse(check_palindrome("hello"))
