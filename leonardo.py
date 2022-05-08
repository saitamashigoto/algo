#!/bin/python3

import math
import os
import random
import re
import sys

def getLimit(n):
    if n <= 100:
        return n
    else:
        return min(n, 30)

def primeCount(n):
    if n == 1:
        return 0
    split_limit = getLimit(n)
    res = 0
    pro = 1
    i = 0
    low = 1
    high = split_limit
    primes = []
    while True:
        while (len(primes) == 0 or i >= len(primes)) and high <= n and low <= high:
            
            primes = segmentedSieve(low, high)
            low = high + 1
            high += split_limit
            i = 0
            
        if (i == len(primes)):
            break
        if pro * primes[i] > n:
            break
        pro *= primes[i]
        res += 1
        i += 1
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


def fillPrimes(chprime, high):
    ck = [True]*(high+1)
    l = int(math.sqrt(high))
    for i in range(2, l+1):
        if ck[i]:
            for j in range(i*i, l+1, i):
                ck[j] = False
    for k in range(2, l+1):
        if ck[k]:
            chprime.append(k)



def segmentedSieve(low, high):

    chprime = list()
    fillPrimes(chprime, high)
    prime = [True] * (high-low + 1)
    for i in chprime:
        lower = (low//i)
        if lower <= 1:
            lower = i+i
        elif (low % i) != 0:
            lower = (lower * i) + i
        else:
            lower = lower*i
        for j in range(lower, high+1, i):
            prime[j-low] = False
    
    res = []
    for k in range(low, high + 1):
        if prime[k-low]:
            res.append(k)
    if 1 in res:
        res.remove(1)
    return res


if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
