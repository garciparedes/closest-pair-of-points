#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

from Point import Point
from random import randint


class Space():


    def __init__(self, points):
        self.points = points


    def getPoint(self, n):
        return self.points[n]

    def __str__(self):
        result = ''

        for i in self.points:
            result += str(i) + '\n'
        return result

    @staticmethod
    def generateSpace(size, dimension, density):
        boxes = size**dimension
        points = int(boxes * density)
        listPoints = list()
        for i in range(points):
            vec = list()
            for j in range(dimension):
                vec.append(randint(0,size-1))
            listPoints.append( Point(vec))
        return Space(listPoints)
