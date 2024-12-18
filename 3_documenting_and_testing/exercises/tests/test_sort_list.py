import unittest

from ..sort_list import sort_list


class TestMystery5(unittest.TestCase):
    """Test the sort_list function"""

    def test_two_lists(self):
        """it should give [1, 9, 0, 1, 4, 5] sort the first list and append it to the other"""
        self.assertEqual(sort_list([4, 5, 1, 0], [1, 9]), [1, 9, 0, 1, 4, 5])

    def test_two_empty(self):
        """it should give []"""
        self.assertEqual(sort_list([], []), [])

    def test_list_None(self):
        """it should give []"""
        self.assertEqual(sort_list([], None), [])

    def test_list_None_default(self):
        """it should give []"""
        self.assertEqual(sort_list([]), [])
