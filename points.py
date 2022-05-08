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
#  1. INTEGER p
#  2. INTEGER q
#  3. INTEGER n
#


def solve(p):
    m, n = p[1][1]-p[0][1], p[1][0]-p[0][0]
    for i in range(1, len(p)-1):
        q, r = p[i+1][1]-p[i][1], p[i+1][0]-p[i][0]
        if not areSlopesEqual(m,n,q,r):
            return 'NO'
    if m == 0 or n == 0:
        return 'YES'
    return 'NO'


def areSlopesEqual(a,b, c,d):
    if a < 0 and b < 0:
        a = -a
        b = -b
    elif a < 0 and b > 0:
        b = -b
    elif a > 0 and b < 0:
        a = -a
    
    if c < 0 and d < 0:
        c = -c
        d = -d
    elif c < 0 and d > 0:
        d = -d
    elif c > 0 and d < 0:
        c = -c
    if d == 0 and b == 0:
        return True
    if a == 0 and c == 0:
        return True
    gcd_b = math.gcd(a, b)
    gcd_d = math.gcd(c, d)
    a //= gcd_b
    b //= gcd_b
    c //= gcd_d
    d //= gcd_d
    return a==c and b==d

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())
    p  = []
    for t_itr in range(n):
        first_multiple_input = input().rstrip().split()
        p.append((int(first_multiple_input[0]), int(first_multiple_input[1])))

    result = solve(p)
    fptr.write(str(result) + '\n')
    fptr.close()
