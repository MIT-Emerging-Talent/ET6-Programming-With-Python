#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..find_biggest_number import find_biggest_number


class TestFindBiggestNumber(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(find_biggest_number([42]), 42)

    def test_sorted_list(self):
        self.assertEqual(find_biggest_number([5, 1, 2, 3, 4]), 5)

    def test_unsorted_list(self):
        self.assertEqual(find_biggest_number([3, 1, 4, 9, 1, 5]), 9)
