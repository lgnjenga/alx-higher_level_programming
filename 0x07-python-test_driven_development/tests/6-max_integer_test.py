#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from unittest.mock import patch

# Import the max_integer function from the module
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Test cases for the max_integer function."""

    def test_max_integer(self):
        """Test the max_integer function."""
        # Test when the list is empty
        self.assertIsNone(max_integer([]))

        # Test when the list contains positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

        # Test when the list contains negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

        # Test when the list contains both positive and negative integers
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([1, -3, 4, -2]), 4)
        self.assertEqual(max_integer([-4, 3, -2, 1]), 3)

        # Test when the list contains repeated values
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([-3, -3, -3, -3]), -3)

        # Test when the list contains a single value
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

        # Test when the list contains large numbers
        self.assertEqual(max_integer(
            [1000000, 100000, 10000, 1000]), 1000000)
        self.assertEqual(max_integer(
            [-1000000, -100000, -10000, -1000]), -1000)

        # Test when the list is very large
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            long_list = list(range(10**6, 0, -1))
            self.assertEqual(max_integer(long_list), 10**6)


if __name__ == '__main__':
    unittest.main()
