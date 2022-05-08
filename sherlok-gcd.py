#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    ans = a[0]
    for i in range(1, len(a)):
        ans = math.gcd(ans, a[i])
    if ans == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(result + '\n')

    fptr.close()
