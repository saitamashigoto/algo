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
#  1. INTEGER d
#  2. INTEGER p
#


def solve(d, p):
    if d < 0:
        return 0
    a = 1
    b1 = d
    b2 = -d
    c = -p
    D = int(d**2 - 4*a*c)
    if D < 0:
        return 0
    if not isPerfectSquare(D):
        return 0
    root_D = int(math.sqrt(D))
    pairs =[(-b1+root_D) // 2]+\
    [(-b1-root_D) // 2]+\
    [(-b2+root_D) // 2]+\
    [(-b2-root_D) // 2]
    res_pairs = []
    for i in range(len(pairs)):
        if pairs[i] == 0 and p != 0:
            continue
        elif pairs[i] == 0 and p == 0:
            res_pairs.append((pairs[i], b1))
            res_pairs.append((pairs[i], b2))
            continue
        if pairs[i] != 0:
            res_pairs.append((pairs[i], p//pairs[i]))
    
    dict_pairs = {}
    res = 0
    for e_p in res_pairs:
        dict_pairs[e_p] = True
    pairs = list(dict_pairs.keys())
    for e_p in pairs:
        if abs(e_p[0] - e_p[1]) == d and e_p[0]*e_p[1] == p:         
            res += 1
    return res


def isPerfectSquare(n):
    if n == 0:
        return True
    r = int(math.sqrt(n))
    if r == 0:
        return False
    return n % r == 0


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        p = int(first_multiple_input[1])

        result = solve(d, p)

        fptr.write(str(result) + '\n')

    fptr.close()
