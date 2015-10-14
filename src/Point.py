#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

import math

class Point():


    def __init__(self, vector):
        self.vector = vector

    def distance(self, other):
        sume = 0
        for i in xrange(0, len(self.vector)):
            sume += (self.vector[i] - other.vector[i])**2
        return (math.sqrt(sume))


    def __str__(self):
        return str(self.vector)
