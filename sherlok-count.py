#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n, k):
    nk = n*k
    if (n//2)*(n-(n//2)) <= nk:
        return n-1
    if n-1 > nk:
        return 0
    start = 1
    end = n//2 if n % 2 == 0 else n//2 + 1
    while start <= end:
        nt = end-start + 1
        middle = nt//2 if nt%2 == 0 else nt//2 + 1
        mt = start + middle-1
        if mt*(n-mt) == nk:
            return 2* (n-mt if mt > n//2 else mt)
        if mt*(n-mt) < nk and (mt+1)*(n-mt-1) > nk:
            return 2* (n-mt if mt > n//2 else mt)
        if mt*(n-mt) > nk and (mt-1)*(n-mt+1) < nk:
            return 2 * (n-mt+1 if mt-1 > n//2 else mt-1)
        if mt*(n-mt) < nk:
            start = mt
        elif mt*(n-mt) > nk:
            end = mt
        
        

if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()
