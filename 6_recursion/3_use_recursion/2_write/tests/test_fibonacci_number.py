#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..fibonacci_number import fibonacci_number


class TestFibonacciNumber(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci_number(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci_number(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci_number(2), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci_number(3), 2)

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci_number(6), 8)
