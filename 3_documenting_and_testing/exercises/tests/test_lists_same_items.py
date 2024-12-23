#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on 23 12 2024

@author: Evan Cole
@editor: Heba
"""
import unittest

from ..lists_same_items import lists_same_items


class TestLists(unittest.TestCase):
    """Test two list to git the same items"""

    def test_numbers(self):
        """Should give [1,2]"""
        self.assertEqual(lists_same_items([1, 4, 6, 8, 2], [3, 5, 2, 1]), [1, 2])

    def test_empty(self):
        """Should give []"""
        self.assertEqual(lists_same_items([], []), [])

    def test_letters(self):
        """Should give ["b"]"""
        self.assertEqual(lists_same_items(["a", "b", "c"], ["v", "b", "t"]), ["b"])

    def test_words(self):
        """Should give ["Heba"]"""
        self.assertEqual(
            lists_same_items(["Heba", "Shaheen", "Engineer"], ["Coding", "Heba"]),
            ["Heba"],
        )
