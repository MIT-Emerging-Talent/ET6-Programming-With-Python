import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_3(0, 0), 0)
