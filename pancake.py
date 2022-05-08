#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY operations as parameter.
#

def solve(n, operations):
    currentType = 1
    angle = 0
    angle_b_a = 360//2*n
    for (type, op) in operations:
        if type == 1:
            angle += (360*op//n)
            angle = angle%360
        if type == 2:
            angle -= (360*4//n)
            angle = angle%360
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
