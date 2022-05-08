#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lights' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#


def lights(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    i_p = c_n_f = 1
    counter = 1
    res_sum = 0
    i = n   
    if n % 2 == 0:  
        limit = n // 2 - 1
    else:
        limit = (n - 1) // 2
    
    while counter <= limit:
        i_p *= i
        c_n_f *= counter
        counter += 1
        i -= 1
        res_sum += (i_p // c_n_f)
    res_sum *= 2
    res_sum += 1
    
    if n % 2 == 0:    
        res_sum += (i_p * (n//2 +1)) // (c_n_f * n // 2)

    return res_sum % (10**5)

def diwali2(n):
    return (2**n - 1) % (10**5)   

def print_fact_series(n):
    result = 0
    if n % 2 == 0:
        limit = n//2 - 1
    else:
        limit = (n-1) // 2
    limit -= 1
    counter = 1
    for i in range(n-1, limit, -1):
        result += 1/(counter*i)
        counter += 1
    print('%.6f' % result)

if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = diwali2(n)

        fptr.write(str(result) + '\n')
    
    fptr.close()
