#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#


def solve(coordinates):
    
    minX = coordinates[0][0]
    for i in range(1, len(coordinates)):
        p = coordinates[i]
        if minX > p[0]:
            minX = p[0]
    
    maxX = coordinates[0][0]
    for i in range(1, len(coordinates)):
        p = coordinates[i]
        if maxX < p[0]:
            maxX = p[0]
    
    maxY = coordinates[0][1]
    for i in range(1, len(coordinates)):
        p = coordinates[i]
        if maxY < p[1]:
            maxY = p[1]
    
    
    minY = coordinates[0][1]
    for i in range(1, len(coordinates)):
        p = coordinates[i]
        if minY > p[1]:
            minY = p[1]
    
    if (minX, minY) in coordinates:
        coordinates.remove((minX, minY))
    if (maxX, minY) in coordinates:
        coordinates.remove((maxX, minY))
    if (minX, maxY) in coordinates:
        coordinates.remove((minX, maxY))
    if (maxX, maxY) in coordinates:
        coordinates.remove((maxX, maxY))
    
    for c in coordinates:
        if c[1] > minY and c[1] < maxY and (c[0] < maxX and c[0] > minX):
            return 'NO'
        if c[0] > minX and c[0] < maxX and (c[1] > minY and c[1] < maxY):
            return 'NO'
    
    return 'YES'        

    


if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        coordinates = []

        for _ in range(n):
            coordinates.append(tuple(map(int, input().rstrip().split())))

        result = solve(coordinates)

        fptr.write(result + '\n')

    fptr.close()
