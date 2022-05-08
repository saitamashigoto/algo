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
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

def solve(x1, y1, x2, y2):
    if x2-x1 == 0:
        return abs(y2-y1)-1
    
    slope_num = y2-y1
    slope_deno = x2-x1
    gcd = math.gcd(slope_deno, slope_num)
    slope_num //= gcd
    slope_deno //= gcd
    avg = abs(x2-x1)
    res = avg // abs(slope_deno)
    return res - 1

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])

        y1 = int(first_multiple_input[1])

        x2 = int(first_multiple_input[2])

        y2 = int(first_multiple_input[3])

        result = solve(x1, y1, x2, y2)

        fptr.write(str(result) + '\n')

    fptr.close()
