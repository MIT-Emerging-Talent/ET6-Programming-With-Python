#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..reverse_list import reverse_list


class TestReverseList(unittest.TestCase):
    def test_reverse_list_empty(self):
        self.assertEqual(reverse_list([]), [], "reverse_list([]) should return []")

    def test_reverse_list_integers(self):
        self.assertEqual(
            reverse_list([1, 2, 3]),
            [3, 2, 1],
            "reverse_list([1, 2, 3]) should return [3, 2, 1]",
        )

    def test_reverse_list_palindrome(self):
        self.assertEqual(
            reverse_list([1, 2, 1]),
            [1, 2, 1],
            "reverse_list([1, 2, 1]) should return [1, 2, 1]",
        )

    def test_reverse_list_mixed(self):
        self.assertEqual(
            reverse_list(["", False, None, 0]),
            [0, None, False, ""],
            "reverse_list(['', False, None, 0]) should return [0, None, False, '']",
        )
