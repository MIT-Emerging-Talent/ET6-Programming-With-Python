#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the mystery_8.
"""

import unittest

# --- import & test class before documenting and testing ---
# from .mystery_8 import mystery_8
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---


from ..mystery_8 import mystery_8


class TestMystery8(unittest.TestCase):
    """Test the mystery_8 function"""

    def test_mystery_8(self):
        """It should return apple, banana"""
        self.assertEqual(
            mystery_8(["apple", "banana", "cherry"], "a"), ["apple", "banana"]
        )
