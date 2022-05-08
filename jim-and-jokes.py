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
# The function accepts 2D_INTEGER_ARRAY dates as parameter.
#


def solve(dates):
    events = {}
    for m, d in dates:
        try:
            base10 = int(str(d), m)
            events.setdefault(base10, []).append((m, d))
        except:
            pass
    ans = 0
    for key, eve in events.items():
        if len(eve) >=2:
            ans += binomialCoefficient(len(eve), 2)
    return ans
            

def binomialCoefficient(n, k):
    if(k > n - k):
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
        


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    dates = []

    for _ in range(n):
        dates.append(list(map(int, input().rstrip().split())))

    result = solve(dates)

    fptr.write(str(result) + '\n')

    fptr.close()
