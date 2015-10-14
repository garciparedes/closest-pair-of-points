#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''


from Point import Point
from random import randint



class Space():



    def __init__(self, dimension, points):
        self.dimension = dimension
        self.points = points



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
        return Space(dimension, listPoints)



    @staticmethod
    def printPoints(points):
        result = ''

        for i in points:
            result += str(i) + '\n'
        return result



    def getDimension(self):
        return self.dimension



    def getPoint(self, n):
        return self.points[n]



    def getNumPoints(self):
        return len(self.points)



    def __str__(self):
        result = ''

        for i in self.points:
            result += str(i) + '\n'

        result += "Hay %s puntos. \n" % (self.getNumPoints())
        return result



    def getClosestPair(self):
        return self.getClosestBrutePlus()



    def getClosestBrute(self):
        closestPair = [self.getPoint(0), self.getPoint(1)]

        for i in self.points:
            for j in self.points:
                if ((i != j)
                    and (i.distance(j) < closestPair[0].distance(closestPair[1]))):

                    closestPair[0] = i
                    closestPair[1] = j

        return closestPair



    def getClosestBrutePlus(self):
        closestPair = [self.getPoint(0), self.getPoint(1)]

        for i in xrange(0,len(self.points)):
            for j in xrange(0, i):
                if ((i != j)
                    and (self.getPoint(i).distance(self.getPoint(j))
                    < closestPair[0].distance(closestPair[1]))):

                    closestPair[0] = self.getPoint(i)
                    closestPair[1] = self.getPoint(j)

        return closestPair



    def getClosestDivideConquer(self):

        self.divide(self.points, 0)

        return None

    def divide(self, p, i):
        if (len(p) > 2):
            p.sort(key=lambda point: point.vector[i%self.getDimension()])
            print self.printPoints(p)
            self.divide(p[:len(p)/2],i+1)
            self.divide(p[len(p)/2:],i+1)
