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

    for i in range(0,100):
        space = Space.generateSpace(10000,7,10**(-25))


        #print space

        fig = pylab.figure()
        ax = Axes3D(fig)


        for i in space.pointList:
            ax.scatter(i.vector[0], i.vector[1], i.vector[2])


        #pyplot.show()
        #closestPairBrute(space)
        #closestPairBrutePlus(space)
        closestPairBrutePlus(space)
        closestPairDivide(space)
        print "\n\n\n"


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
    lista = space.getClosestBrutePlus(space.pointList)
    time2 = time.time()

    print 'function took %0.3f s' % ( (time2-time1))
    print lista[0]
    print lista[1]
    print lista[0].distance(lista[1])

def closestPairDivide(space):
    time1 = time.time()
    lista = space.getClosestDivideConquer()
    time2 = time.time()

    print 'function took %0.3f s' % ( (time2-time1))
    print lista[0]
    print lista[1]
    print lista[0].distance(lista[1])


if __name__ == "__main__":
    main()
