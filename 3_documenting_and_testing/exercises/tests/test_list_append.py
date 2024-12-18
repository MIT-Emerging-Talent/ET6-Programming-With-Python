#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on 16 12 2024

@author: Evan Cole
@editor: Heba
"""

import unittest

from ..list_append import list_append


class Test(unittest.TestCase):
    """Test list append"""

    def test_empty(self):
        """It should evaluate []"""
        actual = list_append([])  # call function with test arguments
        expected = []  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_len1(self):
        """It should evaluate [0]"""
        actual = list_append([3])  # call function with test arguments
        expected = [0]  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_len2(self):
        """It should evaluate [0, 1]"""
        actual = list_append([3, 4])  # call function with test arguments
        expected = [0, 1]  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_len4(self):
        """It should evaluate [0, 1, 2, 3]"""
        actual = list_append([1, 2, 3, 4])  # call function with test arguments
        expected = [0, 1, 2, 3]  # hand-write the expected return value
        self.assertEqual(actual, expected)
