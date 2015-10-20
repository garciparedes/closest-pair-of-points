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

    closestPairDivide(space)
    closestPairBrutePlus(space)
    print "\n\n\n"




    fig = pylab.figure()
    ax = Axes3D(fig)


    for i in space.pointList:
        ax.scatter(i.vector[0], i.vector[1], i.vector[2], s= 30)

    print "\n\n\n"


    closestPair = space.getClosestDivideConquer()
    closestPairBrutePlus(space)

    print closestPair
    ax.scatter(closestPair.pointA.vector[0], closestPair.pointA.vector[1], closestPair.pointA.vector[2], c= 'r', s= 30)
    ax.scatter(closestPair.pointB.vector[0], closestPair.pointB.vector[1], closestPair.pointB.vector[2], c= 'r', s= 30)
    pyplot.show()



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
