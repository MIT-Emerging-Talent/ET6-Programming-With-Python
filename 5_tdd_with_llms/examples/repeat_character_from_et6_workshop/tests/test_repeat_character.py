#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import unittest
from ..repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    """"""

    def test_empty_string(self):
        """it should return an empty if you pass an empty string"""
        self.assertEqual(repeat_character('', '!',  100000000000), "")

    def test_zero_repetitions(self):
        """it should return the same string without the repeated char"""
        self.assertEqual(repeat_character('agabani', 'a',  0), "gbni")

    def test_repeat_character_seven_times(self):
        """It should repeat 'm' 7 times in Omnia"""
        self.assertEqual(repeat_character('Omnia', 'm', 7), "Ommmmmmmnia")
    
    def test_character_with_more_than_one(self):
        """It should repeat 's' 2 times in Jola-Moses"""
        self.assertEqual(repeat_character('Jola-Moses', 's', 2), 'Jola-Mossess')
    
    def test_character_doesnt_exist(self):
        """It should repeat nothing in Hasan because there is no 'e'"""
        self.assertEqual(repeat_character('Hasan', 'e', 999999999999), 'Hasan')
    
    def test_characters_that_are_next_to_each_other(self):
        """It should repeat characters even if they're already repeated"""
        self.assertEqual(repeat_character('Rafaa', 'a', 3), 'Raaafaaaaaa')

    def test_case_insensitive_upper_text(self):
        """it should be case insensitive when the text is upper and the char is lower"""
        self.assertEqual(repeat_character('Agabani', 'a',  0), "gbni")

    def test_case_insensitive_upper_char(self):
        """it should be case insensitive when the text is lower and the char is upper"""
        self.assertEqual(repeat_character('Agabani', 'A',  0), "gbni")
    
    def test_case_insensitive_with_non_zero_repetition(self):
        """it should be case insensitive and repeat characters"""
        self.assertEqual(repeat_character('Agabani', 'A',  2), "AAgaabaani")

    # test defensive assertions
    def test_defensive_check_repetitions_is_not_int(self):
        """it should raise an error if the reptitions is not an integer"""
        with self.assertRaises(AssertionError):
            repeat_character('Agabani', 'A', '3' )

    def test_defensive_check_for_negative_repetitions(self):
        """it should raise an error if the reptitions is less than 0"""
        with self.assertRaises(AssertionError):
            repeat_character('Agabani', 'A',  -2)
