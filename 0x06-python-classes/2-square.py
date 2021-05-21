#!/usr/bin/python3
""" Module Sqaure """
class Square:
    """Empty Square class"""
    def __init__(self,size=0):
        self.__size=size
        if type(size) !=  int:
            print ("must be int")
            raise TypeError
        if size < 0:
            raise ValueError("self must be positive")
    self.__size=size
    pass
