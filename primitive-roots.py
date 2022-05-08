#!/bin/python3

import math
import os
import random
import re
import sys



def solve(p):
    s = p - 1
    pF = getFactorization(s)
    powers = []
    for pN in pF:
        powers.append(s//pN)
    lowestPrimeRoot = 0
    for n in range(2, p):
        isPrimeRoot = True
        for pn in powers:
            if (power(n, pn, p)) % p == 1:
                isPrimeRoot = False
                break
        if isPrimeRoot:
            lowestPrimeRoot = n
            break

    print('%d %d\n' % (lowestPrimeRoot, phi(p-1)))


def phi(n):
    result = n
    p = 2
    while(p * p <= n):
        if (n % p == 0):
            while (n % p == 0):
                n = int(n / p)
            result -= int(result / p)
        p += 1
    if (n > 1):
        result -= int(result / n)
    return result


def numPrimeRoots(p):
    phi = p - 1
    primeFactors = getFactorization(phi)
    res = phi
    d = 1
    for pf in primeFactors:
        d *=pf
        res *= (pf-1)
    return res//d      

def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    res = []
    for p in range(2, n+1):
        if prime[p]:
            res.append(p)
    return res

def getFactorization(x):
    primes = sieve(int(math.sqrt(x)))
    res = []
    i = 0
    copyX = x
    while i < len(primes) and primes[i]*primes[i] <= x:
        if x % primes[i] == 0:
            res.append(primes[i])
            while x%primes[i] == 0:
                x //= primes[i]
        i += 1
    if x > 1 and x != copyX:
        res.append(x)
    return res



def power(x, y, p):
    res = 1
    x = x % p 
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res



if __name__ == '__main__':
    p = int(input().strip())
    solve(p)
