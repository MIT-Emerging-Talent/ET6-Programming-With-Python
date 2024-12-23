import unittest

from ..list_intersection import list_intersection


class TestListIntersection(unittest.TestCase):
    """Test intersection between two lists"""

    def test_numbers(self):
        """Should give [2, 5]"""
        self.assertEqual(list_intersection([2, 3, 5, 6, 8], [4, 5, 2]), [2, 5])

    def test_letters(self):
        """Should give ["e"]"""
        self.assertEqual(list_intersection(["a", "q", "e", "r"], ["w", "e"]), ["e"])

    def test_empty(self):
        """Should give []"""
        self.assertEqual(list_intersection([], []), [])

    def test_letters_and_nums(self):
        """Should give ["a", "s",3]"""
        self.assertEqual(
            list_intersection(["a", 1, "2", "s", 3, 9, "v"], [3, 5, "s", "a", 8]),
            ["a", "s", 3],
        )
