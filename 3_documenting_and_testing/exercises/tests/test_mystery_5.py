import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_5([], []), [])

    def test_minimal_input_none(self):
        """"""
        self.assertEqual(mystery_5([], None), [])

    def test_minimal_input_default_argument(self):
        """"""
        self.assertEqual(mystery_5([]), [])
