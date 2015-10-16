#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''


from Point import Point
from random import randint
import math



class Space():



    def __init__(self, dimension, pointList):
        self.dimension = dimension
        self.pointList = pointList



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
    def printPoints(pointList):
        result = ''

        for i in pointList:
            result += str(i) + '\n'
        return result

    @staticmethod
    def min(pair1, pair2):
        if (pair1[0].distance(pair1[1]) < pair2[0].distance(pair2[1])):
            return pair1
        else:
            return pair2


    def getDimension(self):
        return self.dimension



    def getPoint(self, n):
        return self.pointList[n]



    def getNumPoints(self):
        return len(self.pointList)



    def __str__(self):
        result = ''

        for i in self.pointList:
            result += str(i) + '\n'

        result += "Hay %s puntos. \n" % (self.getNumPoints())
        return result



    def getClosestBrute(self):
        closestPair = [self.getPoint(0), self.getPoint(1)]

        for i in self.pointList:
            for j in self.pointList:
                if ((i != j)
                    and (i.distance(j) < closestPair[0].distance(closestPair[1]))):

                    closestPair[0] = i
                    closestPair[1] = j

        return closestPair



    def getClosestBrutePlus(self):
        closestPair = [self.getPoint(0), self.getPoint(1)]

        for i in xrange(0,len(self.pointList)):
            for j in xrange(0, i):
                if ((i != j)
                    and (self.getPoint(i).distance(self.getPoint(j))
                    < closestPair[0].distance(closestPair[1]))):

                    closestPair[0] = self.getPoint(i)
                    closestPair[1] = self.getPoint(j)

        return closestPair



    def getClosestBrutePlus(self, initPointList):
        closestPair = [initPointList[0], initPointList[1]]

        for i in xrange(0,len(initPointList)):
            for j in xrange(0, i):
                if ((i != j)
                    and (initPointList[i].distance(initPointList[j])
                    < closestPair[0].distance(closestPair[1]))):

                    closestPair[0] = initPointList[i]
                    closestPair[1] = initPointList[j]

        return closestPair



    def getClosestDivideConquer(self):

        closestPair = self.divide(self.pointList, 0)

        return closestPair



    def divide(self, initPointList, i):

        i = (i+1) % self.getDimension()

        if (len(initPointList) > 10):
            initPointList.sort(key=lambda point: point.vector[i])

            leftClosestPair = self.divide(initPointList[len(initPointList)/2:],i)
            rightClosestPair = self.divide(initPointList[:len(initPointList)/2],i)

            closestPair = self.min(leftClosestPair, rightClosestPair)

            closestPairM = self.conquer(initPointList,closestPair, i)

            if(closestPairM != None):
                closestPair = self.min(closestPair, closestPairM)

        else:
            closestPair = self.getClosestBrutePlus(initPointList)

        return closestPair



    def conquer(self, initPointList, closestPair, i):
        distance = math.ceil(closestPair[0].distance(closestPair[1]))

        finalPointList = list()
        leftPointList = initPointList[:len(initPointList)/2]
        rightPointList = initPointList[len(initPointList)/2:]

        leftBorderPoint = leftPointList[-1]
        rightBorderPoint = rightPointList[0]

        for j in rightPointList:
            if (distance > abs(leftBorderPoint.vector[i] - j.vector[i])):
                finalPointList.append(j)
            else:
                break

        for j in reversed(leftPointList):
            if (distance > abs(rightBorderPoint.vector[i] - j.vector[i])):
                finalPointList.append(j)
            else:
                break

        if (len(finalPointList) > 2):
            if (len(finalPointList) >= len(initPointList)):
                return self.getClosestBrutePlus(initPointList)
            else:
                return  self.divide(finalPointList, i)
        elif(len(finalPointList) == 2):
            return finalPointList
        else:
            return None
