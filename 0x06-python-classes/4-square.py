#!/usr/bin/python3
"""This defines a class Square"""


class Square:
    """ A class that defines a square by its size
    """

    def __init__(self, size=0):
        """ Initialises the square object"""

        self.size = size

    def area(self):
        """calculates the square's area"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
