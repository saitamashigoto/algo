#!/bin/python3

import os
import sys
import math

# Complete the solve function below.
def solve(a, queries):
    
    result = []
    copyA = list(a)
    pairs = []
    while len(copyA) >= 2:
        min1, min2 = getTwoDiffElems(copyA)
        if min1 == min2:
            continue    
        pairs.append((min1, min2))
    maxA = max(a)
    for k in queries:
        diff = maxA
        for p in pairs:
            newDiff = getDifference(p[0] + k, p[1] + k)
            if newDiff < diff:
                diff = newDiff
        result.append(diff)
    return result

# Complete the solve function below.
def solve2(a, queries):
    result = []
    diff = a[0]
    for i in range(1, len(a)):
        diff = math.gcd(diff, a[i])
    for k in queries:
        if diff == a[0]:
            ans = (diff + k)
        else:
            ans = math.gcd(diff, k)
        result.append(ans)
    return result


def getTwoDiffElems(a):
    ele1 = ele2 = -1
    while len(a) >= 2:
        ele1 = a[0]
        a.remove(ele1)
        if len(a) == 0:
            ele2 = ele1
        else:
            ele2 = a[0]
            a.remove(ele2)
        if ele1 != ele2:
            return (ele1, ele2)
    return (ele1,ele2)


def getDifference(min1, min2):
    while min1 != min2 and min1 > 0 and min2 > 0:
        if min1 > min2:
            min1 %= min2
        else:
            min2 %= min1
    return max(min1, min2)


if __name__ == '__main__':
    fptr = sys.stdout

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve2(a, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
