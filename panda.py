#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER x
#


def solve(a, b, x):
    if b > 0:
        return power(a, b, x)
    _, inver, inver2 = gcdExtended(a, x)
    inver = inver%x
    return power(inver, -b, x)

def gcdExtended(a, b):
    if a == 0 : 
        return b, 0, 1  
    gcd, x1, y1 = gcdExtended(b%a, a)
    
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        x = int(first_multiple_input[2])

        result = solve(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()
