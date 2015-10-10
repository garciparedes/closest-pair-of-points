#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

from Point2d import Point2d
from Space2d import Space2d


def main():

    space = Space2d.generateSpace(10,10,0.5)

    print space.getPoint(1).printP()
    print space.getPoint(0).printP()

    print (space.getPoint(1).distance(space.getPoint(0)))


    # my code here

if __name__ == "__main__":
    main()
