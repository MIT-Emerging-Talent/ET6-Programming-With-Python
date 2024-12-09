#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the mystery_6.
"""

import unittest

# --- import & test class before documenting and testing ---
# from .mystery_6 import mystery_6
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from .mystery_6 import mystery_6


class TestMystery6(unittest.TestCase):
    """Test the mystery_6 function"""

    def test_mystery_6(self):
        """It should returns 3"""
        self.assertEqual(mystery_6(3, 10), [10, 11, 12])
