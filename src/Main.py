#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''

from Point import Point
from Space import Space


def main():

    space = Space.generateSpace(35,2,0.01)

    print space.getPoint(1)
    print space.getPoint(0)

    print (space.getPoint(1).distance(space.getPoint(0)))

    print space

    # my code here

if __name__ == "__main__":
    main()
