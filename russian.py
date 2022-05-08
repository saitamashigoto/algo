#!/bin/python3

import math
import os
import random
import re
import sys


def solve(a, b, k, m):
    return power(a, b, k, m)

def power(a, b, k, m) :
    X,Y = 1, 0
    a = a % m
    b = b % m
    while (k > 0) :
        if ((k & 1) == 1) :
            p = ((X*a) - (Y*b)) % m
            q = ((X*b) + (Y*a)) % m
            X,Y = p,q
        k = k >> 1
        x = ((a*a) - (b*b)) % m
        y = (2*a*b) % m
        a,b = x,y
    return X,Y

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        k = int(first_multiple_input[2])

        m = int(first_multiple_input[3])

        result = solve(a, b, k, m)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
