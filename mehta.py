#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#


def solve(n):
    if n%2 != 0:
        return '0'
    return printDivisors(n)
    
    
def printDivisors(n):
    numPF = 0
    numF = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if (n % i == 0):
            
            sqr = int(math.sqrt(i))
            if i % 2 == 0 and (sqr*sqr) == i:
                numPF += 1
                  
            if (n / i == i):
                numF += 1
            else:
                numF += 2
                fac1 = n//i
                sqr1 = int(math.sqrt(fac1))
                if fac1 % 2 == 0 and (sqr1*sqr1) == fac1:
                    numPF += 1
    numF += 1
    gc = math.gcd(numPF, numF)
    numPF //= gc
    numF //= gc
    if numPF == 0:
        return '0'
    if numPF == numF:
        return '1'
    else:
        return ('%d/%d' % (numPF, numF))

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
