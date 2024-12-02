#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..fibonacci_memo import fibonacci_memo


class TestFibonacciMemo(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci_memo(0), 0, "fibonacci_memo(0) should be 0")

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci_memo(1), 1, "fibonacci_memo(1) should be 1")

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci_memo(2), 1, "fibonacci_memo(2) should be 1")

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci_memo(3), 2, "fibonacci_memo(3) should be 2")

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci_memo(4), 3, "fibonacci_memo(4) should be 3")

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci_memo(5), 5, "fibonacci_memo(5) should be 5")

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci_memo(6), 8, "fibonacci_memo(6) should be 8")

    def test_fibonacci_7(self):
        self.assertEqual(fibonacci_memo(7), 13, "fibonacci_memo(7) should be 13")
