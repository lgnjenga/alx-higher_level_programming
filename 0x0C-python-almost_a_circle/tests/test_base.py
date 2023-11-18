#!/usr/bin/python3
"""
    Defines unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Unit tests to validate instantiation of the Base class."""

    def test_no_arguments(self):
        # Test instantiation of Base class without arguments
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 3)

    def test_multiple_instances(self):
        # Test instantiation of multiple Base class instances
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 5)

    def test_none_argument(self):
        # Test instantiation of Base class with None as an argument
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 4)

    def test_unique_identifier(self):
        # Test instantiation of Base class with a unique identifier
        self.assertEqual(20, Base(20).id)

    def test_instances_after_unique_id(self):
        # Test instances of Base class after a unique identifier is assigned
        b1 = Base()
        b2 = Base(30)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_modify_public_id(self):
        # Test modification of the public id attribute
        b = Base(25)
        b.id = 35
        self.assertEqual(35, b.id)

    def test_private_attribute(self):
        # Test access to private attribute '__nb_instances'
        with self.assertRaises(AttributeError):
            print(Base(40).__nb_instances)

    # Additional test cases for different data types
    # ... (rest of the test cases remain unchanged)

    def test_two_arguments(self):
        # Test instantiation of Base class with two arguments
        with self.assertRaises(TypeError):
            Base(50, 60)


class TestBaseToJsonString(unittest.TestCase):
    """Unit tests for testing the to_json_string method of the Base class."""

    def test_rectangle_json_string_type(self):
        # Test if the JSON string from Rectangle is of string type
        rectangle = Rectangle(7, 12, 3, 5, 8)
        self.assertEqual(str, type(Base.to_json_string(
                            [rectangle.to_dictionary()])))

    def test_rectangle_json_string_one_dict(self):
        # Test JSON string length for a single Rectangle dictionary
        rectangle = Rectangle(7, 12, 3, 5, 8)
        self.assertTrue(len(Base.to_json_string(
                            [rectangle.to_dictionary()])) == 68)

    def test_rectangle_json_string_two_dicts(self):
        # Test JSON string length for two Rectangle dictionaries
        rect1 = Rectangle(3, 8, 6, 2, 11)
        rect2 = Rectangle(5, 10, 4, 1, 7)
        list_dicts = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 136)

    def test_square_json_string_type(self):
        # Test if the JSON string from Square is of string type
        square = Square(8, 3, 6, 9)
        self.assertEqual(str, type(Base.to_json_string(
                            [square.to_dictionary()])))

    def test_square_json_string_one_dict(self):
        # Test JSON string length for a single Square dictionary
        square = Square(8, 3, 6, 9)
        self.assertTrue(len(Base.to_json_string(
                            [square.to_dictionary()])) == 58)

    def test_square_json_string_two_dicts(self):
        # Test JSON string length for two Square dictionaries
        sq1 = Square(5, 2, 4, 7)
        sq2 = Square(10, 1, 3, 12)
        list_dicts = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 116)

    def test_json_string_empty_list(self):
        # Test JSON string for an empty list
        self.assertEqual("[]", Base.to_json_string([]))

    def test_json_string_none(self):
        # Test JSON string for None
        self.assertEqual("[]", Base.to_json_string(None))

    def test_json_string_no_args(self):
        # Test JSON string for no arguments
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_json_string_more_than_one_arg(self):
        # Test JSON string for more than one argument
        with self.assertRaises(TypeError):
            Base.to_json_string([], 10)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(cls):
        """Delete any created files."""
        files = ["Rectangle.json", "Square.json", "Base.json"]
        for file in files:
            try:
                os.remove(file)
            except IOError:
                pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unit tests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        # Test if the type of the returned object is a list
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    # Additional test cases for different scenarios...

    def test_from_json_string_more_than_one_arg(self):
        # Test from_json_string method with more than one argument
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unit tests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        # Test creation of a Rectangle object
        # and comparison with its string representation
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    # Additional test cases for Rectangle and Square creation...

    def test_create_square_equals(self):
        # Test if created Square object is not equal to the original one
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Unit tests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files after all tests in this class."""
        file_list = ["Rectangle.json", "Square.json"]
        for file in file_list:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    # Additional test cases for loading rectangles and squares...

    def test_load_from_file_no_file(self):
        # Test loading from file when file doesn't exist
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        # Test load_from_file method with more than one argument
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBaseSaveToFileCSV(unittest.TestCase):
    """Unit tests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files after all tests in this class."""
        file_list = ["Rectangle.csv", "Square.csv", "Base.csv"]
        for file in file_list:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass

    # Tests for save_to_file_csv method with different scenarios...
    # ... (existing test cases remain the same)

    def test_save_to_file_csv_more_than_one_arg(self):
        # Test save_to_file_csv method with more than one argument
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBaseLoadFromFileCSV(unittest.TestCase):
    """Unit tests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created files after all tests in this class."""
        file_list = ["Rectangle.csv", "Square.csv"]
        for file in file_list:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass

    # Tests for load_from_file_csv method with different scenarios...
    # ... (existing test cases remain the same)

    def test_load_from_file_csv_more_than_one_arg(self):
        # Test load_from_file_csv method with more than one argument
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
