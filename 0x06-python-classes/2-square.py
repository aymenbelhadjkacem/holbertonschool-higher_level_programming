#!/usr/bin/python3
"""Module square empty"""


class Square:

    """Square class def"""
    def __init__(self, size=0):
        """if size not integer test raise expectation"""
        if type(size) != int:
            print("must be int")
            raise TypeError
        """second test if size is negative it must be positive"""
        if size < 0:
            print("Must be positive")
            raise ValueErro
        """if size is positive init it"""
        if size >= 0:
            self.__size = size
    pass
