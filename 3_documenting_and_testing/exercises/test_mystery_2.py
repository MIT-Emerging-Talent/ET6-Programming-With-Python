#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the mystery_2.
"""

import unittest
# --- import & test class before documenting and testing ---
# from .mystery_2 import mystery_2
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from .mystery_2 import mystery_2


class TestMystery2(unittest.TestCase):
    """Test the mystery_2 function"""

    def test_mystery_2(self):
        """It should return 5"""
        self.assertEqual(mystery_2([1, 2, 3, 4, 5]), 5)
