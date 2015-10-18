#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''
from Point import Point


class PairPoint():
    '''
    Clase PairPoint.

    Sirve para modelar un par de puntos en
    el sistema.

    Attributes:
        pointA: Punto A del par.
        pointB: Punto B del par.
    '''


    def __init__(self, pointA, pointB):
        '''
        Constructor de la clase.
        '''
        self.pointA = pointA
        self.pointB = pointB


    def set(self, pointA, pointB):
        '''
        Procedimiento que modifica
        el valor de los atributos.
        '''
        self.pointA = pointA
        self.pointB = pointB

    def distance(self):
        '''
        Funcion que devuelve la distancia del
        punto A al punto B del par.
        '''
        return self.pointA.distance(self.pointB)


    def __str__(self):
        '''
        Funcion que devuelve el PairPoint
        como cadena de caracteres.
        '''
        return ("Punto A: %s \n"
                "Punto B: %s \n"
                "Distancia: %s") % (self.pointA, self.pointB, self.distance())
