#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the mystery_5.
"""

import unittest

# --- import & test class before documenting and testing ---
# from .mystery_5 import mystery_5
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from .mystery_5 import mystery_5


class TestMystery5(unittest.TestCase):
    """Test the mystery_5 function"""

    def test_mystery_5(self):
        """It should  returns 5"""
        self.assertEqual(mystery_5(5), [0, 1, 2, 3, 4])
