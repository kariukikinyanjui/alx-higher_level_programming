#!/usr/bin/python3
import json
"""Define a class Base"""


class Base:
    """Base class for managing id attributes in future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
           id (int): If provided, set the instance's id attribute to the
           given value.
           Otherwise, increment __nb_objects and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries to convert.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of a list of objects to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """

        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"

        list_dict = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dict)

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string represenation to a list of dictionaries.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: A list of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            **dictionary: Dictionary containing attribute-value pairs.

        Returns:
            Base: An instance with attributes set from the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)

        return dummy_instance

    def update(self, *args, **kwargs):
        """
        Update the attributes of the instance based on the provided arguments.

        Args:
            *args: No-keyword arguments in the order (id, width, height, x, y).
            **kwargs: Keyword arguments representing attribute-value pairs.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
