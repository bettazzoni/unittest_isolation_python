#!/usr/bin/env python3

def echo(a):
    return a 

class MultipleEcho(object):


    def __init__(self, number_of_repetition=1):
        self.number_of_repetition = number_of_repetition
        self._x = None    

    def getList(self, a):
        return [ a for _ in range(self.number_of_repetition)]
    
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
