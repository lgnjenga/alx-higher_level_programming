#!/usr/bin/python3
# test_rectangle.py
"""
    Defines unittests for models/rectangle.py
"""


class TestRectangleInstantiation(unittest.TestCase):
    """Unit tests for Rectangle class instantiation."""

    def test_rectangle_is_base(self):
        """Verifies if Rectangle is an instance of Base class."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Tests instantiation of Rectangle with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Tests instantiation of Rectangle with only one argument."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Tests if different rectangles have consecutive IDs."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    # ... (remaining test methods)

    def test_y_setter(self):
        """Tests the setter method for y."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangleWidth(unittest.TestCase):
    """Unit tests for validating Rectangle's width attribute initialization."""

    def test_invalid_width_values(self):
        """Tests various invalid width values."""
        invalid_values = [
            (None, TypeError, "width must be an integer"),
            ("invalid", TypeError, "width must be an integer"),
            (5.5, TypeError, "width must be an integer"),
            (complex(5), TypeError, "width must be an integer"),
            ({"a": 1, "b": 2}, TypeError, "width must be an integer"),
            (True, TypeError, "width must be an integer"),
            ([1, 2, 3], TypeError, "width must be an integer"),
            ({1, 2, 3}, TypeError, "width must be an integer"),
            ((1, 2, 3), TypeError, "width must be an integer"),
            (frozenset({1, 2, 3, 1}), TypeError, "width must be an integer"),
            (range(5), TypeError, "width must be an integer"),
            (b'Python', TypeError, "width must be an integer"),
            (bytearray(b'abcdefg'), TypeError, "width must be an integer"),
            (memoryview(b'abcedfg'), TypeError, "width must be an integer"),
            (float('inf'), TypeError, "width must be an integer"),
            (float('nan'), TypeError, "width must be an integer"),
            (-1, ValueError, "width must be > 0"),
            (0, ValueError, "width must be > 0"),
        ]

        for value, error_type, error_msg in invalid_values:
            with self.assertRaisesRegex(error_type, error_msg):
                Rectangle(value, 2)


class TestRectangleHeight(unittest.TestCase):
    """
       Unit tests for validating Rectangle's
       height attribute initialization.
    """

    def test_invalid_height_values(self):
        """Tests various invalid height values."""
        invalid_values = [
            (None, TypeError, "height must be an integer"),
            ("invalid", TypeError, "height must be an integer"),
            (5.5, TypeError, "height must be an integer"),
            (complex(5), TypeError, "height must be an integer"),
            ({"a": 1, "b": 2}, TypeError, "height must be an integer"),
            (True, TypeError, "height must be an integer"),
            ([1, 2, 3], TypeError, "height must be an integer"),
            ({1, 2, 3}, TypeError, "height must be an integer"),
            ((1, 2, 3), TypeError, "height must be an integer"),
            (frozenset({1, 2, 3, 1}), TypeError, "height must be an integer"),
            (range(5), TypeError, "height must be an integer"),
            (b'Python', TypeError, "height must be an integer"),
            (bytearray(b'abcdefg'), TypeError, "height must be an integer"),
            (memoryview(b'abcedfg'), TypeError, "height must be an integer"),
            (float('inf'), TypeError, "height must be an integer"),
            (float('nan'), TypeError, "height must be an integer"),
            (-1, ValueError, "height must be > 0"),
            (0, ValueError, "height must be > 0"),
        ]

        for value, error_type, error_msg in invalid_values:
            with self.assertRaisesRegex(error_type, error_msg):
                Rectangle(1, value)


class TestRectangleX(unittest.TestCase):
    """Unit tests for validating Rectangle's x attribute initialization."""

    def test_invalid_x_values(self):
        """Tests various invalid x values."""
        invalid_values = [
            (None, TypeError, "x must be an integer"),
            ("invalid", TypeError, "x must be an integer"),
            (5.5, TypeError, "x must be an integer"),
            (complex(5), TypeError, "x must be an integer"),
            ({"a": 1, "b": 2}, TypeError, "x must be an integer"),
            (True, TypeError, "x must be an integer"),
            ([1, 2, 3], TypeError, "x must be an integer"),
            ({1, 2, 3}, TypeError, "x must be an integer"),
            ((1, 2, 3), TypeError, "x must be an integer"),
            (frozenset({1, 2, 3, 1}), TypeError, "x must be an integer"),
            (range(5), TypeError, "x must be an integer"),
            (b'Python', TypeError, "x must be an integer"),
            (bytearray(b'abcdefg'), TypeError, "x must be an integer"),
            (memoryview(b'abcedfg'), TypeError, "x must be an integer"),
            (float('inf'), TypeError, "x must be an integer"),
            (float('nan'), TypeError, "x must be an integer"),
            (-1, ValueError, "x must be >= 0"),
        ]

        for value, error_type, error_msg in invalid_values:
            with self.assertRaisesRegex(error_type, error_msg):
                Rectangle(1, 2, value)


class TestRectangleOrderOfInitialization(unittest.TestCase):
    """
       Unit tests for verifying the order of
       Rectangle's attribute initialization.
    """

    def test_invalid_width_before_height(self):
        """Ensure width is checked before height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_invalid_width_before_x(self):
        """Ensure width is checked before x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_invalid_width_before_y(self):
        """Ensure width is checked before y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_invalid_height_before_x(self):
        """Ensure height is checked before x."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_invalid_height_before_y(self):
        """Ensure height is checked before y."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_invalid_x_before_y(self):
        """Ensure x is checked before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangleArea(unittest.TestCase):
    """Unit tests for verifying the area method of the Rectangle class."""

    def test_calculate_area_small(self):
        """Calculate area for a small rectangle."""
        rect = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rect.area())

    def test_calculate_area_large(self):
        """Calculate area for a large rectangle."""
        rect = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        expected_area = 999999999999998999000000000000001
        self.assertEqual(expected_area, rect.area())

    def test_calculate_area_with_changed_attributes(self):
        """Calculate area after changing rectangle attributes."""
        rect = Rectangle(2, 10, 1, 1, 1)
        rect.width = 7
        rect.height = 14
        self.assertEqual(98, rect.area())

    def test_area_method_with_additional_arg(self):
        """Ensure area method does not accept additional arguments."""
        rect = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect.area(1)


class TestRectangleStdout(unittest.TestCase):
    """
       Unit tests for verifying the __str__ and
       display methods of Rectangle class.
    """

    @staticmethod
    def capture_stdout(rect, method):
        """Capture and return text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Tests for __str__ method
    def test_str_method_print_width_height(self):
        """Test printing width and height."""
        rectangle = Rectangle(4, 6)
        captured_output = TestRectangleStdout.capture_stdout(
                            rectangle, "print")
        correct_output = "[Rectangle] ({}) 0/0 - 4/6\n".format(rectangle.id)
        self.assertEqual(correct_output, captured_output.getvalue())

    def test_str_method_width_height_x(self):
        """Test width, height, and x."""
        rectangle = Rectangle(5, 5, 1)
        correct_output = "[Rectangle] ({}) 1/0 - 5/5".format(rectangle.id)
        self.assertEqual(correct_output, rectangle.__str__())

    def test_str_method_width_height_x_y(self):
        """Test width, height, x, and y."""
        rectangle = Rectangle(1, 8, 2, 4)
        correct_output = "[Rectangle] ({}) 2/4 - 1/8".format(rectangle.id)
        self.assertEqual(correct_output, str(rectangle))

    def test_str_method_width_height_x_y_id(self):
        """Test width, height, x, y, and ID."""
        rectangle = Rectangle(13, 21, 2, 4, 7)
        correct_output = "[Rectangle] (7) 2/4 - 13/21"
        self.assertEqual(correct_output, str(rectangle))

    def test_str_method_changed_attributes(self):
        """Test with changed attributes."""
        rectangle = Rectangle(7, 7, 0, 0, [4])
        rectangle.width = 15
        rectangle.height = 1
        rectangle.x = 8
        rectangle.y = 10
        correct_output = "[Rectangle] ([4]) 8/10 - 15/1"
        self.assertEqual(correct_output, str(rectangle))

    def test_str_method_one_arg(self):
        """Test with one argument."""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rectangle.__str__(1)

    # Tests for display method
    def test_display_width_height(self):
        """Test display with width and height."""
        rectangle = Rectangle(2, 3, 0, 0, 0)
        captured_output = TestRectangleStdout.capture_stdout(
                            rectangle, "display")
        self.assertEqual("##\n##\n##\n", captured_output.getvalue())

    def test_display_width_height_x_y(self):
        """Test display with width, height, x, and y."""
        rectangle = Rectangle(2, 4, 3, 2, 0)
        captured_output = TestRectangleStdout.capture_stdout(
                            rectangle, "display")
        display_output = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display_output, captured_output.getvalue())

    def test_display_width_height_x(self):
        """Test display with width, height, and x."""
        rectangle = Rectangle(3, 2, 1, 0, 1)
        captured_output = TestRectangleStdout.capture_stdout(
                            rectangle, "display")
        self.assertEqual(" ###\n ###\n", captured_output.getvalue())

    def test_display_width_height_y(self):
        """Test display with width, height, and y."""
        rectangle = Rectangle(4, 5, 0, 1, 0)
        captured_output = TestRectangleStdout.capture_stdout(
                                        rectangle, "display")
        display_output = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display_output, captured_output.getvalue())

    def test_display_one_arg(self):
        """Test display with one argument."""
        rectangle = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rectangle.display(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect))

    def test_update_args_one(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_update_args_two(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_update_args_three(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

    def test_update_args_four(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rect))

    def test_update_args_five(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect))

    def test_update_args_more_than_five(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect))

    def test_update_args_None_id(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_args_None_id_and_more(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_args_twice(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5, 6)
        rect.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rect))

    def test_update_args_invalid_width_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid")

    def test_update_args_width_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(89, 0)

    def test_update_args_width_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(89, -5)

    def test_update_args_invalid_height_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(89, 1, 0)

    def test_update_args_height_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(89, 1, 2, "invalid", "invalid")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(rect))

    def test_update_kwargs_two(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(rect))

    def test_update_kwargs_three(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

    def test_update_kwargs_four(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(rect))

    def test_update_kwargs_five(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(rect))

    def test_update_kwargs_None_id(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_kwargs_None_id_and_more(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(rect.id)
        self.assertEqual(correct, str(rect))

    def test_update_kwargs_twice(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(id=89, x=1, height=2)
        rect.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(rect))

    def test_update_kwargs_invalid_width_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(width=0)

    def test_update_kwargs_width_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(height=0)

    def test_update_kwargs_height_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.update(height=-5)

    def test_update_kwargs_invalid_x_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(y=-5)

    def test_update_args_and_kwargs(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_update_kwargs_wrong_keys(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rect))

    def test_update_kwargs_some_wrong_keys(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(rect))


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        rect = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, rect.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rect1 = Rectangle(10, 2, 1, 9, 5)
        rect2 = Rectangle(5, 9, 1, 2, 10)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)

    def test_to_dictionary_arg(self):
        rect = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rect.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
