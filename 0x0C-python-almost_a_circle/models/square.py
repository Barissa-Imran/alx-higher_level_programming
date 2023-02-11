#!/usr/bin/python3
"""Defines square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square
        Args:
            size (int): The size of the new square.
            x (int): The X coordinate of the new square.
            y (int): The y coordinate of the new square.
            id (int): The identity of the new square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get/set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
