import unittest

from ..mystery_8 import mystery_8

class TestMystery8(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_8([], ''), [])
