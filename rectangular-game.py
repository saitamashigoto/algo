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
# The function accepts 2D_INTEGER_ARRAY steps as parameter.
#


def solve(steps):
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    steps = []

    for _ in range(n):
        steps.append(list(map(int, input().rstrip().split())))

    result = solve(steps)

    fptr.write(str(result) + '\n')

    fptr.close()
