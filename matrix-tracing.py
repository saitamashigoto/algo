#!/bin/python3

import math
import os
import random
import re
import sys


def moduloMultiplication(a, b, p):
    res = 0
    a %= p
    while b:
        if b & 1:
            res = (res + a) % p
        a = (a<<1) % p
        b >>= 1
    return res

def nCr(n, r, p):
    if r > n:
        return 0
    if r > n-r:
        r = n-r
    x = 1
    y = 1
    for i in range(0, r):
        x = moduloMultiplication(x, n-i, p)
        y = moduloMultiplication(y, i+1, p)
    return (x * power(y, p-2, p)) % p


def power(x, y, p):
    res = 1     
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p

    return res


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


def solve(n, m):
    x = n-1
    y = m-1
    r = min(x, y)
    p = 1000000007
    return binomialCoeff(x+y, r, p)


def binomialCoeff(n, r, m):

    if (r > n):
        return 0

    inv = [0 for i in range(r + 1)]
    inv[0] = 1
    if(r+1 >= 2):
        inv[1] = 1

    for i in range(2, r + 1):
        inv[i] = m - (m // i) * inv[m % i] % m

    ans = 1

    for i in range(2, r + 1):
        ans = ((ans % m) * (inv[i] % m)) % m

    for i in range(n, n - r, -1):
        ans = ((ans % m) * (i % m)) % m

    return ans



if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
