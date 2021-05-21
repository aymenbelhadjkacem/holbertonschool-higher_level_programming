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
    def area(self):
        area = self.__size*self.__size
        print("Area: "%d,area)
    pass
