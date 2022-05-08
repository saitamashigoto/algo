#!/bin/python3

import math
import os
import random
import re
import sys

def solve(p1, p2, p3, p4):
    
    if p1 and p2 and p3 and p4:
        d1 = distance(p1, p2)
        d2 = distance(p3, p4)
        d3 = distance(p2, p4)
        d4 = distance(p2, p3)
        d5 = distance(p1, p3)
        d6 = distance(p1, p4)
        return max(d1, d2, d3, d4, d5, d6)
    
    if p1 and not p2 and p3 and not p4:
        return distance(p1, p3)
    
    if not p1 and not p2 and p3 and p4:
        return distance(p3, p4)
    
    if p1 and not p2 and p3 and p4:
        d1 = distance(p3, p4)
        d2 = distance(p1, p3)
        d3 = distance(p1, p4)
        return max(d1, d2, d3)
    
    if not p1 and p2 and p3 and p4:
        d1= distance(p3, p4)
        d1 = distance(p2, p4)
        d1 = distance(p2, p3)
        return max(d1, d2, d3)
    
    if p1 and p2 and not p3 and not p4:
        d1 = distance(p1, p2)
        return d1
    
    if p1 and p2 and not p3 and p4:
        d1 = distance(p1, p2)
        d2 = distance(p2, p4)
        d3 = distance(p1, p4)
        return max(d1, d2, d3)
    
    if p1 and p2 and p3 and not p4:
        d1 = distance(p1, p2)
        d2 = distance(p2, p3)
        d3 = distance(p1, p3)
        return max(d1, d2, d3)
    
    
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
 

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    xCoordinates = []
    yCoordinates = []

    p1 = [0,0]
    p2 = [0,0]
    p3 = [0,0]
    p4 = [0,0]
    
    for _ in range(n):
        coord = list(map(int, input().rstrip().split()))
        if coord[0] < p1[0]:
            p1 = coord
        elif coord[0] > p2[0]:
            p2 = coord
        elif coord[1] > p4[1]:
            p4 = coord
        elif coord[1] < p3[1]:
            p3 = coord

    result = solve(p1, p2, p3, p4)

    fptr.write(str(result) + '\n')

    fptr.close()
