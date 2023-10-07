#!/usr/bin/python3
"""This module contains the Square class"""


class square():
    """ Represents a square """

    width = 0

    def __init__(self, *args, **kwargs):
        """Initialize a square"""

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 4)

    def __str__(self):
        """Return string representation of a square"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
