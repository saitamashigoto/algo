#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n, k):
    a = []
    for i in range(0, n):
        a.append(i)
    print(rotate(a, 0).index(k))


def rotate(a, start):
    if start == len(a) - 1:
        return a
    a = a[0:start] + (a[start:])[::-1]
    return rotate(a, start+1)


if __name__ == '__main__':
    t = int(input().strip())
    for i in range(t):

        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])
        solve(n, k)
