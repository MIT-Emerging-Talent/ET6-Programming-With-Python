import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_1(0, 0), 0)
