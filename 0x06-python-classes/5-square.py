#!/usr/bin/python3
"""Module square empty"""


class Square:

    """Square class def"""
    def __init__(self, size=0):
        """if size not integer test raise expectation"""
        """ attribute size (int): Size of square"""
        self.__size = size
    """are function defintion"""
    def area(self):
        """return the area of square"""
        return self.__size**2
    """getter of size"""
    @property
    def size(self):
        return self.__size
    """setter of size"""
    @size.setter
    def size(self, newsize):
        """if size not integer test raise expectation"""
        """ attribute size (int): Size of square"""
        if type(newsize) != int:
            raise TypeError("size must be an integer")
            """second test if size is negative it must be positive"""
        elif newsize < 0:
            raise ValueError("size must be >= 0")
            """if size is positive init it"""
        else:
            self.__size = newsize
    """definition print"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            """parcour"""
            for x in range(self.__size):
                print("#"*self.__size)
