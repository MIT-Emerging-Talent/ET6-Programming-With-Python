#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import unittest

from ..is_in import is_in


class TestIsIn(unittest.TestCase):
    """Test for the is_in function"""

    # Standard test cases
    def test_string_in_two_list(self):
        """It should give True if the string is in at least one list"""
        thestring = "Heba"
        list1 = ["Noor", "Omer", "Heba"]
        list2 = ["Ahmed", "Heba", "Sondos", "Haya"]
        self.assertEqual(is_in(thestring, list1, list2), True)

    def test_string_in_one_list(self):
        """It should give true if the string is in at least one list"""
        thestring = "Hala"
        list1 = ["Noor", "Hala", "Heba"]
        list2 = ["Ahmed", "Heba", "Sondos", "Haya"]
        self.assertEqual(is_in(thestring, list1, list2), True)

    def test_string_in_one_list_2(self):
        """It should give true if the string is in at least one list"""
        thestring = "Haya"
        list1 = ["Noor", "Hala", "Heba"]
        list2 = ["Ahmed", "Heba", "Sondos", "Haya"]
        self.assertEqual(is_in(thestring, list1, list2), True)

    def test_string_not_in(self):
        """It should give False if the string is not in"""
        thestring = "Mayar"
        list1 = ["Noor", "Omer", "Heba"]
        list2 = ["Ahmed", "Heba", "Sondos", "Haya"]
        self.assertEqual(is_in(thestring, list1, list2), False)

    def test_impty_list(self):
        """It should raise AssertionError if a list is empty"""
        thestring = "Heba"
        list1 = []
        list2 = ["Ahmed", "Heba", "Sondos", "Haya"]
        with self.assertRaises(AssertionError):
            is_in(thestring, list1, list2)

    def test_impty_list_2(self):
        """It should raise AssertionError if a list is empty"""
        thestring = "Heba"
        list1 = []
        list2 = []
        with self.assertRaises(AssertionError):
            is_in(thestring, list1, list2)

    def test_impty_string(self):
        """It should raise AssertionError if the string is empty"""
        thestring = ""
        list1 = ["samy", "omnia"]
        list2 = ["Ahmed", "Heba", "Sondos", "Haya"]
        with self.assertRaises(AssertionError):
            is_in(thestring, list1, list2)

    def test_Non_list(self):
        """It should raise AssertionError"""
        thestring = "Heba"
        list1 = "Noor and Heba"
        list2 = ["Ahmed", "Heba", "Sondos", "Haya"]
        with self.assertRaises(AssertionError):
            is_in(thestring, list1, list2)
