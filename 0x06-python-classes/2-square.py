#!/usr/bin/python3
"""Module square empty"""


class Square:

    """Square class def"""
    def __init__(self, size=0):
        """if size not integer test raise expectation"""
        if type(size) != int:
            raise TypeError("must be int")
            """second test if size is negative it must be positive"""
        elif size < 0:
            raise ValueError("Value Error must be positive")
            """if size is positive init it"""
        else:
            self.__size = size
    pass
