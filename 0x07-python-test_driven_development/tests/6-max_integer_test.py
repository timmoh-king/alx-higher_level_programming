#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """define unittests for the max_integer(list[])"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test unordered list of integers"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with a beginning max value"""
        max_at_begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_begin), 4)

    def test_empty_list(self):
        """Test if the list is empty"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element_list(self):
        """Test a list if it has one element"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test if the list contains floats values"""
        floats = [1.53, 6.33, -9.132, 15.2, 6.08]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test if the list values are ints or float"""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_strings(self):
        """Test string values"""
        strings = ["I", "know", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an  empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
