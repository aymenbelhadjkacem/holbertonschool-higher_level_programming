#!/usr/bin/python3
"""Module square empty"""


class Square:

    """Square class def"""
    def __init__(self, size=0):
        """if size not integer test raise expectation"""
        """ attribute size (int): Size of square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
            """second test if size is negative it must be positive"""
        elif size < 0:
            raise ValueError("size must be >= 0")
            """if size is positive init it"""
        else:
            self.__size = size
    pass
    """are function defintion"""
    def area(self):
        """return the area of square"""
        return self.__size**2
    """getter of size"""
    def size(self):
        return self.__size
    """setter of size"""
    def size(self, size):
        """if size not integer test raise expectation"""
        """ attribute size (int): Size of square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
            """second test if size is negative it must be positive"""
        elif size < 0:
            raise ValueError("size must be >= 0")
            """if size is positive init it"""
        else:
            self.__size = size
