#!/bin/python3

import math
import os
import random
import re
import sys


def mult(a, b, m):
    mul = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mul[i][j] = (mul[i][j]) + (a[i][k] * b[k][j])
            mul[i][j] %= m
    for i in range(2):
        for j in range(2):
            a[i][j] = mul[i][j]
    return a


def power(x, y, m):
    res = [[1, 0], [0, 1]]
    while y > 0:
        if y & 1:
            res = mult(res, x, m)
        y >>= 1
        x = mult(x, x, m)
    return res
    

def solve(a, b, n):
    MODULO = (10**9 + 7)
    if n == 1:
        return b % MODULO
    A = [[1, 1], [1, 0]]
    A = power(A, n-1, MODULO)
    return ((b*A[0][0]) + (A[0][1]*a)) % MODULO


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(a, b, n)

        fptr.write(str(result) + '\n')

    fptr.close()
