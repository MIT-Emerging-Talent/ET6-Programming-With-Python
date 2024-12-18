#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""
import unittest

from ..list_number import list_number


class TestListNumber(unittest.TestCase):
    """Test the length for a list"""

    def test_list1(self):
        """It should evaluate None to []"""
        actual = list_number([])  # call function with test arguments
        expected = None  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_list2(self):
        """It should evaluate None to []"""
        actual = list_number([4, 8, 3])  # call function with test arguments
        expected = 3  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_list3(self):
        """It should evaluate None to []"""
        actual = list_number([1, 1, 2, 3, 4, 5, 6])  # call function with test arguments
        expected = 7  # hand-write the expected return value
        self.assertEqual(actual, expected)
