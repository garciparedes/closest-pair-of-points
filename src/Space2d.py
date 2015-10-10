#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

from Point2d import Point2d
from random import randint


class Space2d():


    def __init__(self,columns, rounds, points):
        self.columns = columns
        self.rounds = rounds
        self.points = points


    def getPoint(self, n):
        return self.points[n]


    def __str__(self):
        integerList = [[0 for x in range(self.rounds)] for x in range(self.columns)]

        for i in self.points:
            integerList[i.x][i.y] = 1

        linea = ''
        for i in range(len(integerList)):
            for j in range(len(integerList[i])):
                if (integerList[i][j] == 1):
                    linea += "* "
                else:
                    linea += "  "
            linea += '\n'

        return linea


    @staticmethod
    def generateSpace(columns, rounds, density):
        boxes = columns * rounds
        points = int(boxes * density)
        listPoints = list()
        for i in range(points):
            listPoints.append( Point2d(randint(0,rounds-1), randint(0, columns-1)))
        return Space2d( columns, rounds, listPoints)
