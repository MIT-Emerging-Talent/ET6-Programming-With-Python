#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""
import unittest

from ..mystery_2 import compare_num


class TestCompuer(unittest.TestCase):
    """Test and compuer two numbers"""

    def test_1(self):
        """It should evaluate None to []"""
        actual = compare_num(2, 5)  # call function with test arguments
        expected = 2  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate None to []"""
        actual = compare_num(4.1, 1.3)  # call function with test arguments
        expected = 1.3  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_3(self):
        """It should evaluate None to []"""
        actual = compare_num(6, 6)  # call function with test arguments
        expected = 12  # hand-write the expected return value
        self.assertEqual(actual, expected)
