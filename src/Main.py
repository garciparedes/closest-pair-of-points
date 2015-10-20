#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''


from Point import Point
from Space import Space

import time

from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D



def main():
    multidim()


    space = Space.generateSpace(10000,3,10**(-10))
    print space

    fig = pylab.figure()
    ax = Axes3D(fig)


    for i in space.pointList:
        ax.scatter(i.vector[0], i.vector[1], i.vector[2], s= 30)

    closestPair = closestPairBrutePlus(space)

    print "\n\n\n"

    closestPair = closestPairDivide(space)

    ax.scatter(closestPair.pointA.vector[0], closestPair.pointA.vector[1], closestPair.pointA.vector[2], c= 'r', s= 30)
    ax.scatter(closestPair.pointB.vector[0], closestPair.pointB.vector[1], closestPair.pointB.vector[2], c= 'r', s= 30)
    pyplot.show()





def multidim():
    space2 = Space.generateSpace(10000,7,10**(-25))
    print space2


    closestPair = closestPairBrutePlus(space2)
    closestPair = closestPairDivide(space2)


def closestPairBrutePlus(space):
    time1 = time.time()
    lista = space.getClosestBrutePlus()
    time2 = time.time()

    print "Fuerza Bruta: "
    print 'function took %0.3f s' % ( (time2-time1))
    print lista
    return lista

def closestPairDivide(space):
    time1 = time.time()
    lista = space.getClosestDivideConquer()
    time2 = time.time()

    print "Divide y venceras: "
    print 'function took %0.3f s' % ( (time2-time1))
    print lista
    return lista


if __name__ == "__main__":
    main()
