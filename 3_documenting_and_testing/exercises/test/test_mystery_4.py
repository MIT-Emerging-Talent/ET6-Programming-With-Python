#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the mystery_4.
"""

import unittest

# --- import & test class before documenting and testing ---
# from .mystery_4 import mystery_4
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from ..mystery_4 import mystery_4


class TestMystery4(unittest.TestCase):
    """Test the mystery_4 function"""

    def test_mystery_4(self):
        """It should returns 3"""
        self.assertEqual(mystery_4(3), [0, 1, 2])
