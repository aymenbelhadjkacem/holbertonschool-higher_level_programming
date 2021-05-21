#!/usr/bin/python3
""" Module Sqaure """
class Square:
    """Empty Square class"""
    def __init__(self,size=0):
        self.__size=size
        if not type(self.__size) is int:
            raise TypeError("only integers are allowed")
        if self.raise < 0:
            raise ValueError("self must be positive")
    pass
