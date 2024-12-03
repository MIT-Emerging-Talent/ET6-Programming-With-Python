#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..fibonacci_sequence import fibonacci_sequence


class TestFibonacciSequence(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci_sequence(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci_sequence(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci_sequence(2), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci_sequence(3), 2)

    def test_fibonacci_6(self):
        self.assertEqual(fibonacci_sequence(6), 8)
