#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the mystery_3.
"""

import unittest

# --- import & test class before documenting and testing ---
# from .mystery_3 import mystery_3
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from ..mystery_3 import mystery_3


class TestMystery3(unittest.TestCase):
    """Test the mystery_3 function"""

    def test_mystery_3(self):
        """It should returns 5"""
        self.assertEqual(mystery_3(10, 5), 5)
