#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

def primeFactors(n):
    primes = primeNumbers(math.floor(math.sqrt(n)))
    c = 2
    res = []
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            res.append(p)
            n = n // p
    
    if (n > 1):
        res.append(n)

    return res


def primeNumbers(n):
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1):
        if isPrime[i] and (i*i) <= n:
            for j in range(i*i, n+1, i):
                isPrime[j] = False
    result = []
    if n >=2:
        result.append(2)
    if n >=3:
        result.append(3)
    for i in range(5, n+1):
        if isPrime[i]:
            result.append(i)
    return result
    
def solve(n):
    str_n = str(n)
    sum_n = sum(map(int, list(str_n)))
    primeFactorsN = primeFactors(n)
    sum_p = sum(primeFactorsN)
    while len(str(sum_p)) != 1:
        sum_p = sum(map(int, list(str(sum_p))))
    
    while len(str(sum_n)) != 1:
        sum_n = sum(map(int, list(str(sum_n))))

    return 1 if sum_p == sum_n else 0

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
