

#!/usr/bin/python3
""" Module Sqaure """
class Square:
    """Empty Square class"""
    def __init__(self,size=0):
        try
            self.size = int(self.size)
            self.size >= 0 
        expect 	TypeError
           print ('TypeError')
        expect ValueError
           print('ValueError')
    pass
