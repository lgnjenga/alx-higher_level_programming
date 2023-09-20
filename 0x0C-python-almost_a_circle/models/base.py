#!/usr/bin/python3

"""A base model for managing objects."""

import json
import csv
import turtle


class Base:
    """Base model for managing objects.

    This serves as the foundation for other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): The count of instantiated Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        """Return the JSON representation of a list of dictionaries.

        Args:
            list_dict (list): A list of dictionaries to be serialized.
        """
        if not list_dict:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances to be saved.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Deserialize a JSON string and return the corresponding Python list.

        Args:
            json_str (str): A JSON string to be deserialized.
        Returns:
            If json_str is None or empty - an empty list.
            Otherwise - a Python list represented by json_str.
        """
        if not json_str or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **kwargs):
        """Create an instance of a class from a dictionary of attributes.

        Args:
            **kwargs (dict): Key/value pairs of attributes for initialization.
        """
        if kwargs:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**kwargs)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Load objects from a file and return a list of instantiated classes.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances to be saved.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file and
           return a list of instantiated classes.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                        dict(
                            [k, int(v)] for k, v in d.items(
                                )) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

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
