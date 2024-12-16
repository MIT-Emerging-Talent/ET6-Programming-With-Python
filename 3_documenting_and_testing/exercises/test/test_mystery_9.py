#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented isn the mystery_9.
"""

import unittest

# --- import & test class before documenting and testing ---
# from .mystery_9 import mystery_9
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from ..mystery_9 import mystery_9


class TestMystery9(unittest.TestCase):
    """Test the mystery_9 function"""

    def test_mystery_9(self):
        """It should return [1, 2, 3, 4, 5]"""
        self.assertEqual(mystery_9([4, 3, 1, 5, 2]), [1, 2, 3, 4, 5])
