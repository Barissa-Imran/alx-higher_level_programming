#!/usr/bin/python3
"""Defines a base model class"""
import json
import csv
import turtle

class Base:
    """
    Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base.
        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string of a list of dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of objects to a file
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = str(cls.__name__) + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None or list_objs == []:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of JSON string representation.
        Args:
            json_string (str): A JSON string representing a list of dictionaries.
        Return:
            If json_string is None or empty - return an empty list
            Otherwise  - return the list represented by json_string
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantiated from a dictionary of attributes.
        Args:
            **dictionary (dict): key/value pairs of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            else:
                instance = cls(1)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file of JSON strings
        Reads from `<Class name>.json`.
        Returns:
            If file does not exist - return an empty list
            Otherwise  - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string of a list of objects to a file
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a csv file.
        Reads from `<Class name>.csv`.
        Returns:
            If file does not exist - return an empty list
            Otherwise  - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                     fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                                for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor('#171C21')
        turt.pensize(3)
        turt.shape('turtle')

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#ffffff")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
