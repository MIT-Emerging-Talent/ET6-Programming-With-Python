#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the mystery_7.
"""

import unittest

# --- import & test class before documenting and testing ---
# from .mystery_7 import mystery_7
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from .mystery_7 import mystery_7


class TestMystery7(unittest.TestCase):
    """Test the mystery_7 function"""

    def test_mystery_7(self):
        """It should apple, banana"""
        self.assertEqual(
            mystery_7(["apple", "banana", "cherry"], "a"), ["apple", "banana"]
        )
