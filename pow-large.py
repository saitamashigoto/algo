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
#  1. STRING a
#  2. STRING b
#

def solve(a, b):
    MODULO = (10**9 + 7)
    cb = int(b) % (MODULO - 1)
    xm = int(a) % MODULO
    result = 1
    am = xm
    while cb > 0:
        if (cb & 1) != 0:
            result *= am
            result %= MODULO
        am *= am
        am %= MODULO
        cb >>= 1
    
    return result

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = first_multiple_input[0]

        b = first_multiple_input[1]

        result = solve(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
