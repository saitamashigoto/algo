#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n, m):
    primes = segmentedPrime(n, m)
    ans = 0
    if n == 1:
        primes = primes[1:]
    for i in range(0, len(primes) - 1):
        for j in range(i+1, len(primes)):
            if abs(primes[i] - primes[j]) == 2:
                ans += 1
                break
            if abs(primes[i] - primes[j]) > 2:
                break
    return ans


def sieveOfAtkins(left, limit):
    result = []
    if limit > 2 and left <= 2:
        result.append(2)
    if limit > 3 and left <= 3:
        result.append(3)
    sieve = {2:False, 3:False}
    # print('x  y  4x2+y2  n%12(1, 5)  3x2+y2  n%12(7)  3x2-y2  n%12(11, x > y)')
    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                sieve[n] = sieve.setdefault(n, False) ^ True
            # print('%d  %d  %6d  %10d ' % (x, y, n, n%12), end='')
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] = sieve.setdefault(n, False) ^ True
            # print('%6d %7d ' % (n, n%12), end='')
            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and n % 12 == 11):
                sieve[n] = sieve.setdefault(n, False) ^ True
            # print('%6d  %15d' % (n, n%12))
            y += 1
        x += 1
    # print('r')
    print(sieve)
    r = left    
    while r * r <= limit:
        # print(r, end=' ')
        if r in sieve and sieve[r]:
            for i in range(r * r, limit+1, r * r):
                sieve[i] = False
                # print(i, end=' ')
        # print()      
        r += 1
    
    for a in range(left, limit+1):
        if a in sieve and sieve[a]:
            result.append(a)
    return result


def segmentedPrime(low, high):
    chprime = list()
    fillPrimes(chprime, high)

    prime = [True] * (high - low + 1)
    result = []
    for i in chprime:
        lower = (low // i)

        if lower <= 1:
            lower = i + i
        elif (low % i) != 0:
            lower = (lower * i) + i
        else:
            lower = lower * i
        for j in range(lower, high + 1, i):
            prime[j - low] = False

    for k in range(low, high + 1):
        if prime[k-low]:
            result.append(k)
    return result


def fillPrimes(chprime, high):
    l = int(math.sqrt(high))
    ck = [True] * (l + 1)

    for i in range(2, l + 1):
        if ck[i]:
            for j in range(i * i, l + 1, i):
                ck[j] = False
    
    for k in range(2, l + 1):
        if ck[k]:
            chprime.append(k)


if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
