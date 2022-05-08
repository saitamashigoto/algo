#!/bin/python3

import math
import os
import random
import re
import sys


def solve(a, b, c):
    if a < c and b < c:
        return 'NO'
    if a ==c or b == c:
        return 'YES'
    if a < b:
        return solve(b, a, c)
    ja = a
    jb = 0
    while (ja != c and jb != c):
        c_t_b = min(b-jb, ja)
        jb += c_t_b
        ja -= c_t_b
        if ja == 0:
            ja = a
        if jb == b:
            jb = 0
        if ja == b:
            break

    if ja == c or jb == c:
        return  'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()
