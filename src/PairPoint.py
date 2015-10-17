#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''
from Point import Point


class PairPoint():


    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB


    def set(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def distance(self):
        return self.pointA.distance(self.pointB)


    def __str__(self):
        return ("Punto A: %s \n"
                "Punto B: %s \n"
                "Distancia: %s") % (self.pointA, self.pointB, self.distance())
