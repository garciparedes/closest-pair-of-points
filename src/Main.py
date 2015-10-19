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

    space = Space.generateSpace(10000,3,10**(-10))


    print space

    fig = pylab.figure()
    ax = Axes3D(fig)


    for i in space.pointList:
        ax.scatter(i.vector[0], i.vector[1], i.vector[2], s= 30)


    #closestPairBrute(space)
    closestPairBrutePlus(space)
    closestPairDivide(space)
    print "\n\n\n"

    closestPairBrute = space.getClosestDivideConquer()
    ax.scatter(closestPairBrute.pointA.vector[0], closestPairBrute.pointA.vector[1], closestPairBrute.pointA.vector[2], c= 'g', s= 30)
    ax.scatter(closestPairBrute.pointB.vector[0], closestPairBrute.pointB.vector[1], closestPairBrute.pointB.vector[2], c= 'g', s= 30)
    pyplot.show()



def closestPairBrute(space):
    time1 = time.time()
    lista = space.getClosestBrute()
    time2 = time.time()

    print 'function took %0.3f s' % ( (time2-time1))
    print lista[0]
    print lista[1]
    print lista[0].distance(lista[1])



def closestPairBrutePlus(space):
    time1 = time.time()
    lista = space.getClosestBrutePlus()
    time2 = time.time()

    print 'function took %0.3f s' % ( (time2-time1))
    print lista

def closestPairDivide(space):
    time1 = time.time()
    lista = space.getClosestDivideConquer()
    time2 = time.time()

    print 'function took %0.3f s' % ( (time2-time1))
    print lista


if __name__ == "__main__":
    main()
