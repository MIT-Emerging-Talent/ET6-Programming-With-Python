#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 19/12/2024

@author: Evan Cole
@editor: Heba Shaheen
"""
import unittest

from ..make_list import make_list


class TestMakinglist(unittest.TestCase):
    """ """

    def test_add1(self):
        """It should evaluate 2+2 = 4"""
        actual = make_list(2, 2)  # call function with test arguments
        expected = [2, 3]  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_0(self):
        """It should evaluate 2+2 = 4"""
        actual = make_list(0, 2)  # call function with test arguments
        expected = []  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_float(self):
        """It should evaluate 2+2 = 4"""
        actual = make_list(5, 3.4)  # call function with test arguments
        expected = [3.4, 4.4, 5.4, 6.4, 7.4]  # hand-write the expected return value
        self.assertEqual(actual, expected)
