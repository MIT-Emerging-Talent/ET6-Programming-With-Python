import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_5([], []), [])
        
