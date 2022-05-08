#!/bin/python3

import math
import os
import random
import re
import sys


def power(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if (y & 1):
            res = (res * x) % p
        y >>= 1
        x = (x * x)  % p
    return res


def solve(a, m):
    if a == 0:
        return 'YES'
    if power(a, (m - 1) // 2, m) == 1:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(a, m)

        fptr.write(result + '\n')

    fptr.close()
