#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

import math

class Point2d():


    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (math.sqrt(dx**2 + dy**2))


    def printP(self):
        return "(%s,%s)" % (self.x, self.y)
