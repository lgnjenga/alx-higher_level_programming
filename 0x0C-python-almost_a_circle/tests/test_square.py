#!/usr/bin/python3
# test_square.py
"""
   Defines unittests for models/square.py
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unit tests for verifying instantiation of the Square class."""

    def test_is_base_instance(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_square_instance(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_single_argument(self):
        square1 = Square(10)
        square2 = Square(11)
        self.assertEqual(square1.id, square2.id - 1)

    def test_two_arguments(self):
        square1 = Square(10, 2)
        square2 = Square(2, 10)
        self.assertEqual(square1.id, square2.id - 1)

    def test_three_arguments(self):
        square1 = Square(10, 2, 2)
        square2 = Square(2, 2, 10)
        self.assertEqual(square1.id, square2.id - 1)

    def test_four_arguments(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_arguments(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_private_size_attribute(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4)._Square__size)

    def test_size_getter_method(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter_method(self):
        square = Square(4, 1, 9, 2)
        square.size = 8
        self.assertEqual(8, square.size)

    def test_width_getter_method(self):
        square = Square(4, 1, 9, 2)
        square.size = 8
        self.assertEqual(8, square.width)

    def test_height_getter_method(self):
        square = Square(4, 1, 9, 2)
        square.size = 8
        self.assertEqual(8, square.height)

    def test_x_getter_method(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter_method(self):
        self.assertEqual(0, Square(10).y)


class TestSquareSize(unittest.TestCase):
    """Unit tests for verifying size initialization of the Square class."""

    # Test invalid size types
    def test_invalid_size_types(self):
        invalid_sizes = [None, "invalid", 5.5,
                         complex(5), {"a": 1, "b": 2},
                         True, [1, 2, 3], {1, 2, 3}, (1, 2, 3),
                         frozenset({1, 2, 3, 1}),
                         range(5), b'Python',
                         bytearray(b'abcdefg'),
                         memoryview(b'abcdefg'),
                         float('inf'), float('nan')]

        for size in invalid_sizes:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(size)

    # Test negative and zero size values
    def test_negative_and_zero_sizes(self):
        negative_sizes = [-1, 0]

        for size in negative_sizes:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Square(size, 2)


class TestSquareX(unittest.TestCase):
    """Unit tests for verifying initialization of Square x attribute."""

    # Test invalid x types
    def test_invalid_x_types(self):
        invalid_x_values = [None, "invalid", 5.5,
                            complex(5), {"a": 1, "b": 2},
                            True, [1, 2, 3], {1, 2, 3}, (1, 2, 3),
                            frozenset({1, 2, 3, 1}),
                            range(5), b'Python',
                            bytearray(b'abcdefg'), memoryview(b'abcdefg'),
                            float('inf'), float('nan')]

        for x_value in invalid_x_values:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Square(1, x_value)

    # Test negative x value
    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquareY(unittest.TestCase):
    """Unit tests for verifying initialization of Square y attribute."""

    # Test invalid y types
    def test_invalid_y_types(self):
        invalid_y_values = [None, "invalid", 5.5,
                            complex(5), {"a": 1, "b": 2},
                            True, [1, 2, 3], {1, 2, 3}, (1, 2, 3),
                            frozenset({1, 2, 3, 1}),
                            range(5), b'Python',
                            bytearray(b'abcdefg'),
                            memoryview(b'abcdefg'),
                            float('inf'), float('nan')]

        for y_value in invalid_y_values:
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Square(1, 3, y_value)

    # Test negative y value
    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquareOrderOfInitialization(unittest.TestCase):
    """
       Unit tests for verifying the
       order of Square attribute initialization.
    """

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquareArea(unittest.TestCase):
    """Unit tests for testing the area method of the Square class."""

    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        square = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, square.area())

    def test_area_changed_attributes(self):
        square = Square(2, 0, 0, 1)
        square.size = 7
        self.assertEqual(49, square.area())

    def test_area_one_arg(self):
        square = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            square.area(1)


class TestSquareStdout(unittest.TestCase):
    """
       Unit tests for testing __str__ and
       display methods of the Square class.
    """

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        square = Square(4)
        captured_output = TestSquareStdout.capture_stdout(square, "print")
        correct_output = "[Square] ({}) 0/0 - 4\n".format(square.id)
        self.assertEqual(correct_output, captured_output.getvalue())

    def test_str_method_size_x(self):
        square = Square(5, 5)
        correct_output = "[Square] ({}) 5/0 - 5".format(square.id)
        self.assertEqual(correct_output, square.__str__())

    def test_str_method_size_x_y(self):
        square = Square(7, 4, 22)
        correct_output = "[Square] ({}) 4/22 - 7".format(square.id)
        self.assertEqual(correct_output, str(square))

    def test_str_method_size_x_y_id(self):
        square = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(square))

    def test_str_method_changed_attributes(self):
        square = Square(7, 0, 0, [4])
        square.size = 15
        square.x = 8
        square.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(square))

    def test_str_method_one_arg(self):
        square = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            square.__str__(1)

    # Test display method
    def test_display_size(self):
        square = Square(2, 0, 0, 9)
        captured_output = TestSquareStdout.capture_stdout(square, "display")
        self.assertEqual("##\n##\n", captured_output.getvalue())

    def test_display_size_x(self):
        square = Square(3, 1, 0, 18)
        captured_output = TestSquareStdout.capture_stdout(square, "display")
        self.assertEqual(" ###\n ###\n ###\n", captured_output.getvalue())

    def test_display_size_y(self):
        square = Square(4, 0, 1, 9)
        captured_output = TestSquareStdout.capture_stdout(square, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, captured_output.getvalue())

    def test_display_size_x_y(self):
        square = Square(2, 3, 2, 1)
        captured_output = TestSquareStdout.capture_stdout(square, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, captured_output.getvalue())

    def test_display_one_arg(self):
        square = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            square.display(1)


class TestSquareUpdateArgs(unittest.TestCase):
    """Unit tests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        square = Square(10, 10, 10, 10)
        square.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(square))

    def test_update_args_one(self):
        square = Square(10, 10, 10, 10)
        square.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(square))

    # Test cases for various update scenarios...

    def test_update_args_invalid_size_type(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid")

    def test_update_args_size_zero(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, 0)

    def test_update_args_size_negative(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(89, -4)

    def test_update_args_invalid_x(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square.update(89, 1, "invalid", "invalid")

    # Other test cases based on the update args method...

    def test_update_args_twice(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, 3, 4)
        square.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(square))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Unit tests for testing update kwargs method of Square class."""

    # Test cases for updating with different keyword arguments

    def test_update_kwargs_one(self):
        square = Square(10, 10, 10, 10)
        square.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(square))

    def test_update_kwargs_two(self):
        square = Square(10, 10, 10, 10)
        square.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(square))

    # Add more test cases for updating with kwargs...

    def test_update_kwargs_invalid_size(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="invalid")

    # Additional test cases for updating kwargs with different keys...

    def test_update_args_and_kwargs(self):
        square = Square(10, 10, 10, 10)
        square.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(square))


class TestSquareToDictionary(unittest.TestCase):
    """Unit tests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        square = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, square.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        square1 = Square(10, 2, 1, 2)
        square2 = Square(1, 2, 10)
        square2.update(**square1.to_dictionary())
        self.assertNotEqual(square1, square2)

    # Add more test cases for to_dictionary method...

    def test_to_dictionary_arg(self):
        square = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            square.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
