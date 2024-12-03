#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole + Chat GPT
"""


import unittest


from ..add_two_numbers import add_two_numbers


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers_int_int(self):
        self.assertEqual(add_two_numbers(1, 1), 2)

    def test_add_two_numbers_float_int(self):
        self.assertEqual(add_two_numbers(1.0, 3), 4.0)

    def test_add_two_numbers_float_float(self):
        self.assertEqual(add_two_numbers(1.0, 3.0), 4.0)

    def test_add_two_numbers_int_float(self):
        self.assertEqual(add_two_numbers(1, 3.0), 4.0)

    def test_add_two_numbers_zero_zero(self):
        self.assertEqual(add_two_numbers(0, 0), 0)

    def test_add_two_numbers_large_numbers(self):
        self.assertEqual(add_two_numbers(1e100, 1e100), 2e100)

    def test_add_two_numbers_small_numbers(self):
        self.assertEqual(add_two_numbers(1e-100, 1e-100), 2e-100)

    def test_add_two_numbers_negative_negative(self):
        self.assertEqual(add_two_numbers(-1, -1), -2)

    def test_add_two_numbers_positive_negative(self):
        self.assertEqual(add_two_numbers(1, -2), -1)

    def test_add_two_numbers_negative_positive(self):
        self.assertEqual(add_two_numbers(-1, 3), 2)

    def test_add_two_numbers_non_numeric_first(self):
        with self.assertRaises(AssertionError):
            add_two_numbers("1", 1)

    def test_add_two_numbers_non_numeric_second(self):
        with self.assertRaises(AssertionError):
            add_two_numbers(1, "1")

    def test_add_two_numbers_non_numeric_both(self):
        with self.assertRaises(AssertionError):
            add_two_numbers("1", "1")


if __name__ == "__main__":
    unittest.main()
