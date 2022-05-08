#!/bin/python3

import math
import os
import random
import re
import sys


def gcdExtended(a, b):
    if a == 0 : 
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


def solve(n, r, m):
    primeFactorsM = primeFactors(m)
    res = 0
    for k in primeFactorsM:
        mi = m // k
        ai = nCrModpLucas(n, r, k)
        _, _, s = gcdExtended(k, mi)
        res += (mi * ai * s ) % m
    return res % m


def nCrModpDP(n, r, p):
    if n < r:
        return 0
    c = [0] * (n+1)
    c[0] = 1
    for i in range(1, (n+1)):
        j = min(i, r)
        while j > 0:
            c[j] = (c[j] + c[j-1]) % p
            j -= 1
    return c[r]

def nCrModpLucas(n, r, p):
    if (r == 0):
        return 1
    ni = n % p
    ri = r % p
    return (nCrModpLucas(n//p, r//p, p) *\
        nCrModpDP(ni, ri, p))  % p


def primeFactors(n):
    res = []
    primes = sieveOfEratosthenes(math.floor(math.sqrt(n)))
    for p in primes:
        if p*p > n:
            break
        while (n % p == 0):
            res.append(p)
            n = n // p
    if n > 1:
        res.append(n)
    return res


def sieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    res = []
    for p in range(2, n+1):
        if prime[p]:
            res.append(p)
    return res


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = solve(n, r, m)

        fptr.write(str(result) + '\n')

    fptr.close()
