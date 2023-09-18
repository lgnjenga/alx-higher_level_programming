# models/base.py

class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with an optional id."""
        if id is not None:
            # If id is provided,
            # assign it to the public instance attribute 'id'
            self.id = id
        else:
            # If id is not provided, increment __nb_objects and assign it as id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
