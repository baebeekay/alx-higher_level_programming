#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_maxatend(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_maxatmiddle(self):
         self.assertEqual(max_integer([1, 2, 8, 6, 4]), 8)


    def test_maxatbeginning(self):
         self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_onenegative(self):
         self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_allnegetive(self):
         self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_oneitem(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
