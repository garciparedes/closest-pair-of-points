#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

from Point2d import Point2d
from random import randint


class Space2d():


    def __init__(self, points):
        self.points = points

    def getPoint(self, n):
        return self.points[n]

    @staticmethod
    def generateSpace(columns, rounds, density):
        boxes = columns * rounds
        points = int(boxes * density)
        listPoints = list()
        for i in range(points):
            listPoints.append( Point2d(randint(0,rounds), randint(0, columns)))
        return Space2d(listPoints)
