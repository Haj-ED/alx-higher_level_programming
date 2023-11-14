#!/usr/bin/python3
"""Base module."""


class Base:
    """Base class for managing id attribute."""

    # Class attribute to keep track of the number of instances
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method to initialize the Base instance.

        Args:
            id (int): If id is not None, assign it to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# Test the Base class
if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

