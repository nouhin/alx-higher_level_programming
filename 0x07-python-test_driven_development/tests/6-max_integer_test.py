#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class to test the max_integer function """

    def test_empty_list(self):
        """ Test with empty list """
        self.assertEqual(max_integer([]), None)

    def test_sigle_element_list(self):
        """Test with single element list"""
        list = [1]
        self.assertEqual(max_integer(list), list[0])


if __name__ == '__main__':
    unittest.main()
