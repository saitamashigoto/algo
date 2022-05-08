#!/bin/python3

import math
import os
import random
import re
import sys


def gameWithCells(n, m):
    p = n // 2
    q = m // 2
    res = p*q
    s = (n*m - res*4) // 2
    r = (n*m - res*4) % 2
    return res + s + r   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
