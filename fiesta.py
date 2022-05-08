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
# The function accepts INTEGER_ARRAY a as parameter.
#


def solve(a):
    odd = []
    even = []
    p = 10**9 + 7
    for i in a:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    res = 0
    odd_len = len(odd)
    even_len = len(even)
    X = 0 if even_len == 0 else (2**even_len) - 1
    Y =  0 if odd_len==0 else 2**(odd_len-1) - 1

    res = (X + Y + X*Y) % p
    return res

if __name__ == '__main__':
    fptr = sys.stdout

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
