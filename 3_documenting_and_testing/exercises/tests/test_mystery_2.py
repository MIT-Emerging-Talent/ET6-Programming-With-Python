import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """ """

    def test_minimal_list_input(self):
        """"""
        self.assertEqual(mystery_2([]), None)

    def test_minimal_string_input(self):
        """"""
        self.assertEqual(mystery_2(''), None)
