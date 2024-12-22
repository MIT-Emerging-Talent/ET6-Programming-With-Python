#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..fibonacci_number import fibonacci_number


class TestFibonacciNumber(unittest.TestCase):
    """test the fibonacci_number function"""

    def test_fibonacci_0(self):
        """It should return 0 for the 0th Fibonacci number"""
        self.assertEqual(fibonacci_number(0), 0)

    def test_fibonacci_1(self):
        """It should return 1 for the 1st Fibonacci number"""
        self.assertEqual(fibonacci_number(1), 1)

    def test_fibonacci_2(self):
        """It should return 1 for the 2nd Fibonacci number"""
        self.assertEqual(fibonacci_number(2), 1)

    def test_fibonacci_3(self):
        """It should return 2 for the 3rd Fibonacci number"""
        self.assertEqual(fibonacci_number(3), 2)

    def test_fibonacci_6(self):
        """It should return 8 for the 6th Fibonacci number"""
        self.assertEqual(fibonacci_number(6), 8)
