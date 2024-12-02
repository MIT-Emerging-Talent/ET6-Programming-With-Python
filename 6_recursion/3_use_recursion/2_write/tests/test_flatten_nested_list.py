#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..flatten_nested_list import flatten_nested_list


class TestFlattenNestedList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(flatten_nested_list([]), [])

    def test_flatten_single_nested_list(self):
        self.assertEqual(flatten_nested_list([1, [2, 3]]), [1, 2, 3])

    def test_flatten_deeply_nested_list(self):
        self.assertEqual(flatten_nested_list([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])

    def test_flatten_already_flat_list(self):
        self.assertEqual(flatten_nested_list([1, 2, 3]), [1, 2, 3])
