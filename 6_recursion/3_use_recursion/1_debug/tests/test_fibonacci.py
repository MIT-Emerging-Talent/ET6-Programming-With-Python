#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0, "fibonacci(0) should be 0")

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1, "fibonacci(1) should be 1")

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1, "fibonacci(2) should be 1")

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci(3), 2, "fibonacci(3) should be 2")

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 3, "fibonacci(4) should be 3")

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci(5), 5, "fibonacci(5) should be 5")

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci(6), 8, "fibonacci(6) should be 8")

    def test_fibonacci_7(self):
        self.assertEqual(fibonacci(7), 13, "fibonacci(7) should be 13")
