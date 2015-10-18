#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

import math

class Point():
    '''
    Clase punto.
    Modeliza el objeto punto en el sistema.
    Esta clase modeliza puntos de dimension
    arbitraria.

    Attributes:
        vector: coordenadas del punto.
    '''


    def __init__(self, vector):
        '''
        Constructor del punto.
        '''
        self.vector = vector



    def distance(self, other):
        '''
        Funcion que devuelve la distancia
        euclidea del punto invocante a otro
        pasado por parametro.
        '''
        sume = 0
        for i in range(0, len(self.vector)):
            sume += (self.vector[i] - other.vector[i])**2
        return (math.sqrt(sume))



    def dimension(self):
        '''
        Funcion que devuelve la
        dimension del punto.
        '''
        return len(self.vector)



    def __str__(self):
        '''
        Funcion que devuelve el
        punto como cadena de caracteres.
        '''
        return str(self.vector)
