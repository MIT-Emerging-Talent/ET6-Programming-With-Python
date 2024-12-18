#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on 16 12 2024

@author: Evan Cole
@editor: Heba
"""

import unittest

from ..addition_two import addition_two

# from exercises.Addition import Addition


class TestAddition(unittest.TestCase):
    """Test the Addition function"""

    def test_add1(self):
        """It should evaluate 2+2 = 4"""
        actual = addition_two(2, 2)  # call function with test arguments
        expected = 4  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_add2(self):
        """It should evaluate 2+3 = 5"""
        actual = addition_two(2, 3)  # call function with test arguments
        expected = 5  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_add3(self):
        """It should evaluate -4+7 = 3"""
        actual = addition_two(-4, 7)  # call function with test arguments
        expected = 3  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_minimal_input(self):
        """It should evaluate 0+0=0"""
        self.assertEqual(addition_two(0, 0), 0)
