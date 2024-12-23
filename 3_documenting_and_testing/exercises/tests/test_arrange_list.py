import unittest

from ..arrange_list import arrange_list


class TestList(unittest.TestCase):
    """test aranging  a list"""

    def test_numbers(self):
        """Should give [1, 3, 6, 9]"""
        self.assertEqual(arrange_list([6, 3, 1, 9]), [1, 3, 6, 9])

    def test_letters(self):
        """Should give ["a", "b", "e", "y"]"""
        self.assertEqual(arrange_list(["e", "a", "y", "b"]), ["a", "b", "e", "y"])

    def test_empty(self):
        """Should give []"""
        self.assertEqual(arrange_list([]), [])

    def test_diffrent(self):
        """Should give ["1", "22", "5", "e", "r"]"""
        self.assertEqual(
            arrange_list(["r", "1", "e", "5", "22"]), ["1", "22", "5", "e", "r"]
        )
