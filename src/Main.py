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

    space = Space.generateSpace(100,3,0.0001)


    print space
    space.getClosestDivideConquer()

    fig = pylab.figure()
    ax = Axes3D(fig)


    for i in space.points:
        ax.scatter(i.vector[0], i.vector[1], i.vector[2])


    pyplot.show()
    #closestPairBrute(space)
    #closestPairBrutePlus(space)    plot([1,2,3])



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
    print lista[0]
    print lista[1]
    print lista[0].distance(lista[1])



if __name__ == "__main__":
    main()
