#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""

import unittest

# --- imports & test class before documenting and testing ---

# from ..mystery_0 import mystery_0

# class TestMystery0(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..fibonacci_list import fibonacci_list


class TestFibonacciList(unittest.TestCase):
    """Test the fibonacci_list function"""

    def test_0(self):
        """It should evaluate 0 to []"""
        actual = fibonacci_list(0)  # call function with test arguments
        expected = []  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate 1 to [0]"""
        actual = fibonacci_list(1)
        expected = [0]
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate 2 to [0, 1]"""
        actual = fibonacci_list(2)
        self.assertEqual(actual, [0, 1])

    def test_3(self):
        """It should evaluate 3 to [0, 1, 1]"""
        expected = [0, 1, 1]
        self.assertEqual(fibonacci_list(3), expected)

    def test_4(self):
        """It should evaluate 4 to [0, 1, 1, 2]"""
        actual = fibonacci_list(4)
        expected = [0, 1, 1, 2]
        self.assertEqual(actual, expected)

    def test_5(self):
        """It should evaluate 5 to [0, 1, 1, 2, 3]"""
        self.assertEqual(fibonacci_list(5), [0, 1, 1, 2, 3])

    def test_9(self):
        """It should evaluate 9 to [0, 1, 1, 2, 3, 5, 8, 13, 21]"""
        self.assertEqual(fibonacci_list(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_a_big_number(self):
        """It should evaluate 123 to [0, 1, 1, 2, 3, ...]"""
        self.assertEqual(
            fibonacci_list(123),
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
                10946,
                17711,
                28657,
                46368,
                75025,
                121393,
                196418,
                317811,
                514229,
                832040,
                1346269,
                2178309,
                3524578,
                5702887,
                9227465,
                14930352,
                24157817,
                39088169,
                63245986,
                102334155,
                165580141,
                267914296,
                433494437,
                701408733,
                1134903170,
                1836311903,
                2971215073,
                4807526976,
                7778742049,
                12586269025,
                20365011074,
                32951280099,
                53316291173,
                86267571272,
                139583862445,
                225851433717,
                365435296162,
                591286729879,
                956722026041,
                1548008755920,
                2504730781961,
                4052739537881,
                6557470319842,
                10610209857723,
                17167680177565,
                27777890035288,
                44945570212853,
                72723460248141,
                117669030460994,
                190392490709135,
                308061521170129,
                498454011879264,
                806515533049393,
                1304969544928657,
                2111485077978050,
                3416454622906707,
                5527939700884757,
                8944394323791464,
                14472334024676221,
                23416728348467685,
                37889062373143906,
                61305790721611591,
                99194853094755497,
                160500643816367088,
                259695496911122585,
                420196140727489673,
                679891637638612258,
                1100087778366101931,
                1779979416004714189,
                2880067194370816120,
                4660046610375530309,
                7540113804746346429,
                12200160415121876738,
                19740274219868223167,
                31940434634990099905,
                51680708854858323072,
                83621143489848422977,
                135301852344706746049,
                218922995834555169026,
                354224848179261915075,
                573147844013817084101,
                927372692193078999176,
                1500520536206896083277,
                2427893228399975082453,
                3928413764606871165730,
                6356306993006846248183,
                10284720757613717413913,
                16641027750620563662096,
                26925748508234281076009,
                43566776258854844738105,
                70492524767089125814114,
                114059301025943970552219,
                184551825793033096366333,
                298611126818977066918552,
                483162952612010163284885,
                781774079430987230203437,
                1264937032042997393488322,
                2046711111473984623691759,
                3311648143516982017180081,
                5358359254990966640871840,
                8670007398507948658051921,
                14028366653498915298923761,
            ],
        )  # noqa

    def test_less_than_0(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            fibonacci_list(-1)

    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            fibonacci_list(1.0)
