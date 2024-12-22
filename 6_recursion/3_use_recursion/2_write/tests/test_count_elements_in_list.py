#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..count_items_in_list import count_items_in_list


class TestCountItemsInList(unittest.TestCase):
    """it is a class that inherits from unittest.TestCase"""

    def test_empty_list(self):
        """It should return 0 for an empty list"""
        self.assertEqual(count_items_in_list([]), 0)

    def test_single_element_list(self):
        """It should return 1 for a list with a single element"""
        self.assertEqual(count_items_in_list([1]), 1)

    def test_multiple_elements_list(self):
        """It should return the number of elements in the list"""
        self.assertEqual(count_items_in_list([1, 2, 3]), 3)
