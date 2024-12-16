#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contains unittest for the functions implemented in the add.
"""

import unittest
# --- import & test class before documenting and testing ---
# from .add import add
# class TestFunctions(unittest.TestCase):
# --- import & test class before documenting and testing ---

from ..add import add


class TestFunctions(unittest.TestCase):
    """Test the add function"""

    def test_add(self):
        """It should return 4"""
        self.assertEqual(add(2, 2), 4)
