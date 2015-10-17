#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''


from Point import Point
from PairPoint import PairPoint
from random import randint
import math



class Space(object):
    """ Clase Espacio.

    Esta clase modeliza el espacio donde estan contenidos los puntos en el sistema

    Attributes:
        dimension: dimension del espacio.
        pointList: conjunto de puntos del espacio.
    """



    def __init__(self, dimension, pointList = {}):
        '''
        Inicializa la clase.

        Descarta los puntos con dimension distinta a la fijada en self.dimension
        '''

        self.dimension = dimension

        for i in pointList:
            if (i.dimension() != self.dimension):
                pointList.remove(i)

        self.pointList = pointList



    @staticmethod
    def generateSpace(size, dimension, density):
        ''''
        Metodo estatico.

        Es el encargado de generar un espacio aleatoriamente
        a partir de los parametros introducidos.
        '''
        boxes = size**dimension
        points = int(boxes * density)
        listPoints = list()
        for i in range(points):
            vec = list()
            for j in range(dimension):
                vec.append(randint(0,size-1))
            listPoints.append( Point(vec))
        vec = list()
        for j in range(dimension+1):
            vec.append(randint(0,size-1))
        listPoints.append( Point(vec))
        return Space(dimension, listPoints)



    @staticmethod
    def min(pair1, pair2):
        '''
        Metodo Estatico.

        Devuelve el minimo de los dos
        parametros.
        '''
        if (pair1.distance() < pair2.distance()):
            return pair1
        else:
            return pair2



    def pointsToString(self, pointList = None):
        '''
        Metodo que devuelve el conjunto de puntos
        en formato string.

        Toma el atributo pointList como valor por defecto.
        '''

        if not pointList: pointList = self.pointList

        result = ''

        for i in pointList:
            result += str(i) + '\n'
        return result



    def pointListSize(self):
        '''
        Devuelve el numero de puntos
        que hay en el espacio.
        '''
        return len(self.pointList)



    def __str__(self):
        '''
        Convierte el objeto Espacio a String devolviendo
        el listado de puntos y el numero de ellos.
        '''
        result = self.pointsToString()

        result += "Hay %s puntos. \n" % (self.pointListSize())
        return result



    '''
    ******************************************************************************
            Algoritmos para encontrar la distancia minima entre dos puntos
    ******************************************************************************
    '''


    '''
                                Algoritmos Fuerza Bruta
    ******************************************************************************
    '''



    def getClosestBrute(self):
        '''
        Algoritmo de busqueda de los dos puntos mas cercanos.

        Solucion por fuerza bruta que compara todos los puntos
        con todos y asi obtiene los dos mas cercanos
        '''
        closestPair = [self.pointList[0], self.pointList[1]]

        for i in self.pointList:
            for j in self.pointList:
                if ( (i != j) and
                    (i.distance(j) < closestPair[0].distance(closestPair[1])) ):

                    closestPair[0] = i
                    closestPair[1] = j

        return closestPair



    def getClosestBrutePlus(self, initPointList = None):
        '''
        Algoritmo de busqueda de los dos puntos mas cercanos.

        Solucion por fuerza bruta que compara todos los puntos
        con todos pero si ha comparado A con B no vuelve
        A comparar B con A.
        '''

        if not initPointList: initPointList = self.pointList

        closestPair = PairPoint(initPointList[0], initPointList[1])

        for i in range(0,len(initPointList)):
            for j in range(0, i):
                if (initPointList[i].distance(initPointList[j])
                    < closestPair.distance()):

                    closestPair.set(initPointList[i], initPointList[j])

        return closestPair



    '''
                            Algoritmos Divide y venceras
    ******************************************************************************
    '''



    def getClosestDivideConquer(self):
        '''
        Algoritmo de busqueda de los dos puntos mas cercanos.

        Solucion por divide y venceras.
        '''

        return self.divide(self.pointList, 0)



    def divide(self, initPointList, i):

        i = (i+1) % self.dimension

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

        distance = math.ceil(closestPair.distance())

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

        if (len(finalPointList) >= 2):
            if (len(finalPointList) >= len(initPointList)):
                return self.getClosestBrutePlus(initPointList)
            else:
                return  self.divide(finalPointList, i)

        else:
            return None
