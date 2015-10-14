#!/usr/bin/env python

'''
Author: Sergio Garcia Prado
        www.garciparedes.me
'''


from Point import Point
from Space import Space



def main():

    space = Space.generateSpace(500,3,0.00001)


    print space
    lista = space.getClosestBrute()

    print lista[0]
    print lista[1]
    print lista[0].distance(lista[1])

    lista = space.getClosestBrutePlus()

    print lista[0]
    print lista[1]
    print lista[0].distance(lista[1])



if __name__ == "__main__":
    main()
