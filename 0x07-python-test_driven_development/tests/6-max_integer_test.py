#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_positive_numbers(self):
        """Test a list of positive integers."""
        numbers = [1, 10, 5, 100, 25]
        self.assertEqual(max_integer(numbers), 100)

    def test_negative_numbers(self):
        """Test a list of negative integers."""
        numbers = [-1, -10, -5, -100, -25]
        self.assertEqual(max_integer(numbers), -1)

    def test_mixed_numbers(self):
        """Test a list of mixed integers."""
        numbers = [1, -10, 5, -100, 25]
        self.assertEqual(max_integer(numbers), 25)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_strings(self):
        """Test a list of strings."""
        strings = ["apple", "banana", "cherry", "date"]
        self.assertEqual(max_integer(strings), 'date')

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
