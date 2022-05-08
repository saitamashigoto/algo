#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pythagoreanTriple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER a as parameter.
#

def pythagoreanTriple(a):
    if a%2 == 0:
        l  = a
        mul = 1
        while l%2 == 0:
            l //= 2
            mul *= 2
        triple = calulateFromOdd(l)
        if l == 1:
            mul = mul//4
        triple = (triple[0]*mul, triple[1]*mul, triple[2]*mul)
    else:
        triple = calulateFromOdd(a)
    t = triple
    # print((t[0]**2 + t[1]**2) == t[2]**2)
    return t
    
    
def calulateFromOdd(a):
    if a == 1:
        return 3,4,5
    else:
        k = (a-1) // 2    
        m = k+1
        n = k
    b = 2*m*n
    c = m**2 + n**2
    return (a, b, c)
    

if __name__ == '__main__':
    fptr = sys.stdout

    a = int(input().strip())

    triple = pythagoreanTriple(a)

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()
