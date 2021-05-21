#!/usr/bin/python3
""" Module Sqaure """
class Square:
    """Empty Square class"""
    def __init__(self,size=0):
        if type(size) !=  int:
            print ("must be int")
            raise TypeError
        if size < 0:
            print("Must be positive")
            raise ValueError
    self.__size=size
    pass
