#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class BaseModel:
    """Base model.

    This serves as the foundation for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated BaseModel objects.
    """

    __nb_objects = 0

    def __init__(self, identity=None):
        """Initialize a new BaseModel.

        Args:
            identity (int): The identity of the new BaseModel instance.
        """
        if identity is not None:
            self.id = identity
        else:
            BaseModel.__nb_objects += 1
            self.id = BaseModel.__nb_objects

    @staticmethod
    def to_json_str(list_dicts):
        """Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dicts (list): A list of dictionaries to be serialized.
        """
        if not list_dicts:
            return "[]"
        return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of BaseModel instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(BaseModel.to_json_str(list_dicts))

    @staticmethod
    def from_json_str(json_str):
        """Deserialize a JSON-formatted string to a list of dictionaries.

        Args:
            json_str (str): A JSON-formatted string.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - the Python list represented by json_str.
        """
        if not json_str or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **attributes):
        """Instantiate a class using attributes from a dictionary.

        Args:
            **attributes (dict): Key/value pairs of attributes to initialize.
        """
        if attributes and attributes != {}:
            new_instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new_instance.update(**attributes)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Instantiate classes from a file containing JSON strings.

        Reads from a file named `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = BaseModel.from_json_str(jsonfile.read())
                return [cls.create(**attrs) for attrs in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of BaseModel instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                fieldnames = cls.get_csv_fieldnames()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Instantiate classes from a CSV file.

        Reads from a file named `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = cls.get_csv_fieldnames()
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [cls.convert_csv_dict(d) for d in list_dicts]
                return [cls.create(**attrs) for attrs in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Use the turtle module to draw Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
