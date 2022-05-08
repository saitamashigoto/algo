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
#  1. INTEGER n
#  2. INTEGER k
#


def solve(n, k):
    x = 1
    y = 1
    p = n+k
    for i in range(1, k+1):
        x *= (p-i)
        y *= i
    return (x//y) % 1000000000

def binomialCoeff(n, r, m):
    
    if (r > n):
        return 0

    inv = [0 for i in range(r + 1)]
    inv[0] = 1
    if(r+1 >= 2):
        inv[1] = 1

    for i in range(2, r + 1):
        inv[i] = m - (m // i) * inv[m % i] % m

    ans = 1

    for i in range(2, r + 1):
        ans = ((ans % m) * (inv[i] % m)) % m

    for i in range(n, n - r, -1):
        ans = ((ans % m) * (i % m)) % m

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    result = ''
    for t_itr in range(t):
        n = int(input().strip())

        k = int(input().strip())

        result += (str(solve(n, k))) + '\n'
    fptr.write(result)

    fptr.close()
