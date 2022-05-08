#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    perms = {}
    for p in range(1, n+1):
        i = p - k
        if (abs(p-i) != k) or (i <= 0) or (i > n) or (i in perms):
            i = p + k
            if (abs(p-i) != k) or (i <= 0) or (i > n) or (i in perms):
                return [-1]
        perms[i] = p
    result = []
    # if len(perms.keys()) != n: return [-1]
    for i in range(1, n+1):
        if i in perms:
            result.append(perms[i])
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
