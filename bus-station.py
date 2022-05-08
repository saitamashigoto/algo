#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def solve(a):
    s = a[0]
    data = []
    for i in range(1, len(a)):
        data.append(s)
        s += a[i]
    m = max(a)
    data.append(s)
    data_dict = {data[i]: True for i in range(len(data))}
    factors = printDivisors(s, m)
    res = []
    
    for f in factors:
        flag = True
        for l in range(s//f, 0, -1):
           if l*f not in data_dict:
               flag = False
               break
        if flag:
            res.append(f) 
        
    return res


def printDivisors(n, m):
    res2 = []
    res1 = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            if (n // i == i):
                if i >=m:
                    res1.append(i)
            else:
                if i >= m:
                    res1.append(i)
                if n//i >= m:
                    res2.append(n // i)

    return res1 + res2[::-1]
        



if __name__ == '__main__':
    fptr = sys.stdout

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
