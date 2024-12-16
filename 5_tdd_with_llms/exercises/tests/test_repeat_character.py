#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in_one function.

Test categories:
    - Standard cases: typical lists with different lengths
    - Edge cases: empty lists, single elements
    - Defensive tests: wrong input types, assertions

Created on 2024-12-06
Author: Aziz & phind AI
"""

import unittest

from ..repeat_character import repeat_character


class TestRepeatCharacter(unittest.TestCase):
    """Test suite for the repeat_character function"""

    # Standard test cases
    def test_Aziz_z(self):
        """It should repeat z 3 times in Aziz"""
        self.assertEqual(repeat_character("Aziz", "z", 3), "Azzzizzz")

    def test_gray_r(self):
        """It should repeat r 5 times in Gray"""
        self.assertEqual(repeat_character("Gray", "r", 5), "Grrrrray")

    def test_time_e(self):
        """It should repeat e 7 times in Time"""
        self.assertEqual(repeat_character("Time", "e", 7), "Timeeeeeee")

    # Edge test cases
    def test_hand_D(self):
        """It should repeat D 3 times in Hand and lower the D"""
        self.assertEqual(repeat_character("Hand", "D", 3), "Handdd")

    # Defensive test cases
    def test_goat_d(self):
        """It should not repeat d in Goat"""
        self.assertEqual(repeat_character("Goat", "d", 20), "Goat")

    def test_invalid_input_type(self):
        """It should handle invalid input types gracefully"""
        with self.assertRaises(TypeError):
            repeat_character(123, "a", 3)

    def test_invalid_input_type2(self):
        """It should handle invalid input types gracefully"""
        with self.assertRaises(TypeError):
            repeat_character("text", 4, 6)

    def test_invalid_input_type3(self):
        """It should handle invalid input types gracefully"""
        with self.assertRaises(TypeError):
            repeat_character("Earth", "t", "g")
