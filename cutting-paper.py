#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n, m):
    return (m-1) + m*(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
