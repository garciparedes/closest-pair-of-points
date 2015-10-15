#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''


from Point import Point
from random import randint
import math



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

    @staticmethod
    def menor(pair1, pair2):
        if (pair1[0].distance(pair1[1]) < pair2[0].distance(pair2[1])):
            return pair1
        else:
            return pair2


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



    def getClosestBrutePlus(self, p):
        closestPair = [p[0], p[1]]

        for i in xrange(0,len(p)):
            for j in xrange(0, i):
                if ((i != j)
                    and (p[i].distance(p[j])
                    < closestPair[0].distance(closestPair[1]))):

                    closestPair[0] = p[i]
                    closestPair[1] = p[j]

        return closestPair



    def getClosestDivideConquer(self):

        closestPair = self.divide(self.points, 0)

        return closestPair



    def divide(self, p, i):
        i = i%self.getDimension()

        if (len(p) > 5):
            p.sort(key=lambda point: point.vector[i])
            #print self.printPoints(p)
            closestPairL = self.divide(p[len(p)/2:],i+1)
            closestPairR = self.divide(p[:len(p)/2],i+1)

            closestPair = self.menor(closestPairL, closestPairR)


            closestPairM = self.conquer(p,closestPair, i+1)

            if(closestPairM != None):
                closestPair = self.menor(closestPair, closestPairM)

        else:
            closestPair = self.getClosestBrutePlus(p)

        return closestPair


    def conquer(self, p, closestPair, i):
        i = i%self.getDimension()


        distance = math.ceil(closestPair[0].distance(closestPair[1]))

        listaFinal = list()

        izquierda = p[:len(p)/2]
        derecha = p[len(p)/2:]

        centro = p[len(p)/2]


        for j in derecha:
            #print distance
            #print ( p[len(p)/2:][-1].vector[i]- j.vector[i])
            if (distance > abs(centro.vector[i] - j.vector[i])):
                listaFinal.append(j)
            else:
                break

        for j in reversed(izquierda):
            #print distance
            #print (j.vector[i] - p[:len(p)/2][0].vector[i])
            if (distance > abs(centro.vector[i] - j.vector[i])):
                listaFinal.append(j)
            else:
                break

        if (len(listaFinal) >= 2):
            return  self.divide(listaFinal, i+1)
            #return None
        else:
            return None
