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

    def test_ascending_ordered_list(self):
        """Test with ascending ordered list"""
        list = [1, 2, 3]
        self.assertEqual(max_integer(list), list[-1])

    def test_descending_ordered_list(self):
        """Test with ascending ordered list"""
        list = [3, 2, 1]
        self.assertEqual(max_integer(list), list[0])

    def test_unordered_list(self):
        """Test with unordered list"""
        list = [2, 1, 3]
        self.assertEqual(max_integer(list), 3)

    def test_negative_ints(self):
        """Test with negative ints"""
        list = [-2, -1, -3]
        self.assertEqual(max_integer(list), -1)

    def test_negative_and_positive_ints(self):
        """Test with negative and positive ints"""
        list = [-2, 1, 3]
        self.assertEqual(max_integer(list), 3)

    def test_max_at_beginning(self):
        """Test with max at beginning"""
        list = [3, 1, 2]
        self.assertEqual(max_integer(list), 3)

    def test_max_at_middle(self):
        """Test with max at middle"""
        list = [1, 3, 2]
        self.assertEqual(max_integer(list), 3)

    def test_max_at_end(self):
        """Test with max at end"""
        list = [1, 2, 3]
        self.assertEqual(max_integer(list), 3)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)


if __name__ == '__main__':
    unittest.main()
